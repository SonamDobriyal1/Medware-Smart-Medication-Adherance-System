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
![Screenshot 2024-12-16 095817](https://github.com/user-attachments/assets/304d3524-8be0-48b4-8f0e-4b7a0d2625ea)
![Screenshot 2024-12-16 093159](https://github.com/user-attachments/assets/a544f66f-a41f-403f-bb2e-888947ec07d3)
![Screenshot 2024-12-16 093232](https://github.com/user-attachments/assets/e2f675a2-ca2c-459d-bc94-1b63650d6bd4)
![Screenshot 2024-12-16 093330](https://github.com/user-attachments/assets/1f201a0d-b899-4cee-8065-1d0b7aa952b9)


- **Medication Reminders and Scheduling:** Set up and manage reminders using Google Calendar.
 ![Screenshot 2024-12-16 093300](https://github.com/user-attachments/assets/928b1ca4-bc3d-44c1-98fc-a43f4f477785)
 


- **AI Chatbot:** Get medication-related advice and support.
![Screenshot 2024-12-16 093417](https://github.com/user-attachments/assets/d2bb0be1-fa44-40c2-bcd7-9c6d6b8067b4)
![Screenshot 2024-12-16 093455](https://github.com/user-attachments/assets/d03981b3-8c5e-4e32-b1e9-46e034542240)


  


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
- Snigdha Pratap



## Acknowledgments
- Google Cloud and Gemini API providers.
- Flask and Python open-source community.
- Our mentors and project guides at Dr. A.P.J. Abdul Kalam Technical University.

