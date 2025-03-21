# Medware - Medication Management System

## Overview
Medware is a Flask-based web application designed to simplify and enhance medication management through intelligent reminders and notifications. The platform leverages OAuth-based authentication for secure and seamless user login, integrating with the Google Cloud Console to utilize the Google Calendar API for scheduling medication reminders and sending timely notifications. This ensures users can effectively manage their medication routines while leveraging the familiar interface of Google Calendar.

Additionally, Medware incorporates the Gemini API to provide an AI-powered chatbot for personalized assistance. The chatbot can handle user queries related to medication schedules, provide health tips, and offer interactive support, thereby enriching the user experience.

## Features
- Secure user authentication using OAuth.
- Smart medication reminders integrated with Google Calendar API.
- AI-powered chatbot for personalized health assistance.
- User-friendly dashboard for managing medication schedules.


## Installation
### Prerequisites
Ensure you have the following dependencies installed:
- Python 3.x
- Flask
- NumPy
- Google Cloud SDK (for Calendar API integration)
- Gemini API key (for chatbot integration)

### Setup
1. Clone the repository
2. Install the required dependencies
3. Configure Google Calendar API credentials and place them in the project directory.
4. Run the application:
   ```bash
   python app.py
   ```
5. Access the application in your web browser at `http://127.0.0.1:5000/`.

## Usage
- **User Authentication:** Secure login via OAuth.
- ![image](https://github.com/user-attachments/assets/d16925ba-f4f0-4490-a03d-e00cc43af5a5)
- ![image](https://github.com/user-attachments/assets/c6ee8bac-5dea-4d92-80b2-24117cf92786)
![image](https://github.com/user-attachments/assets/3a10643b-4601-46ce-8293-3da62b39ad99)
- ![image](https://github.com/user-attachments/assets/9e819fb9-7d9a-49bc-85b5-66ac3709d3c3)

- **Medication Reminders:** Set up and manage reminders using Google Calendar.
- ![image](https://github.com/user-attachments/assets/aef85184-503e-49a8-8371-b67e972cbbf7)


- **AI Chatbot:** Get medication-related advice and support.
- ![image](https://github.com/user-attachments/assets/1acfbcb9-9d19-4544-b8eb-a81b6d7bdda7)
- ![image](https://github.com/user-attachments/assets/389d2239-fcb6-4ead-878d-0afd08fa825b)


- **Dashboard:** View and modify scheduled medications.
- ![image](https://github.com/user-attachments/assets/42319ba1-c6a9-486a-9b99-33449e25da08)


## System Architecture
- **User Authentication Module**: Secure login using OAuth.
- **Reminder Module**: Schedules and manages medication alerts.
- **Chatbot Module**: Provides AI-powered assistance.
- **Calendar Integration**: Syncs reminders with Google Calendar.

## Future Improvements
- Mobile app integration.
- Support for voice-based commands.


## Contributors
- Sonam Dobriyal
- Vanshika Garg


## Acknowledgments
- Google Cloud and Gemini API providers.
- Flask and Python open-source community.
- Our mentors and project guides at Dr. A.P.J. Abdul Kalam Technical University.

