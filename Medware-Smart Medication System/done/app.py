from flask import Flask, redirect, url_for, render_template, request, session, flash
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
import os
import datetime
import json 

from flask import Flask, jsonify, request, send_file, send_from_directory
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI


app = Flask(__name__)
app.secret_key = "your_secret_key"
os.environ["GOOGLE_API_KEY"] = "enteryourapikey"; 


# Google OAuth Configuration
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # Enable HTTP for local testing
CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ['https://www.googleapis.com/auth/calendar']
API_SERVICE_NAME = 'calendar'
API_VERSION = 'v3'

# Flask routes
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login')
def login():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=url_for('callback', _external=True)
    )
    authorization_url, state = flow.authorization_url()
    session['state'] = state
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    state = session['state']
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        state=state,
        redirect_uri=url_for('callback', _external=True)
    )
    flow.fetch_token(authorization_response=request.url)

    session['credentials'] = {
        'token': flow.credentials.token,
        'refresh_token': flow.credentials.refresh_token,
        'token_uri': flow.credentials.token_uri,
        'client_id': flow.credentials.client_id,
        'client_secret': flow.credentials.client_secret,
        'scopes': flow.credentials.scopes
    }
    return redirect(url_for('main_page'))

@app.route('/main')
def main_page():
    if 'credentials' not in session:
        return redirect(url_for('login'))
    return render_template("main.html")

@app.route('/view_reminders')
def view_reminders():
    if 'credentials' not in session:
        return redirect(url_for('login'))

    credentials = Credentials(**session['credentials'])
    service = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

    # Get events from the calendar
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    return render_template("reminders.html", events=events)

@app.route('/set_reminder', methods=['GET', 'POST'])
def set_reminder():
    if 'credentials' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        # Get reminder details
        title = request.form['title']
        date = request.form['date']
        time = request.form['time']
        datetime_str = f"{date}T{time}:00"

        credentials = Credentials(**session['credentials'])
        service = build(API_SERVICE_NAME, API_VERSION, credentials=credentials)

        # Create an event
        event = {
            'summary': title,
            'start': {'dateTime': datetime_str, 'timeZone': 'UTC'},
            'end': {'dateTime': datetime_str, 'timeZone': 'UTC'},
        }
        service.events().insert(calendarId='primary', body=event).execute()
        flash("Reminder set successfully!")
        return redirect(url_for('main_page'))

    return render_template("set_reminder.html")

@app.route('/chat')
def home1():
    return render_template("index.html")

@app.route("/api/generate", methods=["POST"])
def generate_api():
    if request.method == "POST":
        try:
            req_body = request.get_json()
            content = req_body.get("contents")
            model = ChatGoogleGenerativeAI(model=req_body.get("model"))
            message = HumanMessage(
                content=content
            )
            response = model.stream([message])
            def stream():
                for chunk in response:
                    yield 'data: %s\n\n' % json.dumps({ "text": chunk.content })

            return stream(), {'Content-Type': 'text/event-stream'}

        except Exception as e:
            return jsonify({ "error": str(e) })
        return redirect(url_for('main_page'))


# Defines a route to serve static files from the web directory for any given path.
# When a request matches the path, it sends the requested file from the web directory.
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('templates', path)

# If the script is run directly, it starts the Flask app in debug mode.

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
