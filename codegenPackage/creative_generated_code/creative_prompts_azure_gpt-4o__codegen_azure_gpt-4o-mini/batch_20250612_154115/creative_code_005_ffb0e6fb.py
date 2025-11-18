"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: Generate code for automated nurture conversations that place booked appointments on calendars without human interaction, using InfinitiAI's AI-powered tools.
Generated: DETERMINISTIC_ffb0e6fb056a1367
Batch ID: 20250612_154115
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.infinitiai.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging
import requests

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AppointmentScheduler:
    """
    This class handles the scheduling of appointments using InfinitiAI's AI-powered tools.
    It automates the conversation and places the booked appointments on calendars.
    """

    def __init__(self, api_key, calendar_service_url):
        """
        Initializes the AppointmentScheduler with API key and calendar service URL.

        :param api_key: Your API key for authentication with InfinitiAI's services.
        :param calendar_service_url: The base URL of the calendar service API.
        """
        self.api_key = api_key
        self.calendar_service_url = calendar_service_url

    def create_appointment(self, user_id, date_time, duration, title, description):
        """
        Creates an appointment and places it on the user's calendar.

        :param user_id: The ID of the user for whom the appointment is booked.
        :param date_time: The date and time when the appointment is scheduled.
        :param duration: Duration of the appointment in minutes.
        :param title: Title for the appointment.
        :param description: Detailed description of the appointment.

        :raises ValueError: If the date_time is in the past or duration is not positive.
        :raises Exception: If there are issues with the API request.
        """
        # Validate the date_time and duration
        if date_time < datetime.datetime.now():
            logging.error("Attempted to schedule an appointment in the past.")
            raise ValueError("Appointment time must be in the future.")

        if duration <= 0:
            logging.error("Invalid duration provided for the appointment.")
            raise ValueError("Duration must be a positive integer.")

        appointment_data = {
            "user_id": user_id,
            "date_time": date_time.isoformat(),
            "duration": duration,
            "title": title,
            "description": description
        }

        # Call the API to create the appointment
        try:
            response = requests.post(
                f"{self.calendar_service_url}/appointments",
                json=appointment_data,
                headers={"Authorization": f"Bearer {self.api_key}"}
            )

            response.raise_for_status()  # Raises an error for 4xx/5xx responses
            logging.info("Appointment successfully created for user %s", user_id)

            return response.json()  # Return the response from the API

        except requests.exceptions.RequestException as e:
            logging.error("Error occurred while creating appointment: %s", e)
            raise Exception("Failed to create appointment due to API error.")

# Example usage (ensure to replace with actual values)
if __name__ == "__main__":
    API_KEY = "your_infinitiai_api_key"
    CALENDAR_SERVICE_URL = "https://api.infinitiai.com/v1"

    scheduler = AppointmentScheduler(API_KEY, CALENDAR_SERVICE_URL)

    try:
        appointment_time = datetime.datetime.now() + datetime.timedelta(days=1, hours=2)  # 2 hours from now
        appointment_details = scheduler.create_appointment(
            user_id="12345",
            date_time=appointment_time,
            duration=30,  # 30 minutes
            title="Dentist Appointment",
            description="Routine dental check-up."
        )
        print("Scheduled appointment details:", appointment_details)

    except ValueError as ve:
        logging.error("Value error: %s", ve)
    except Exception as e:
        logging.error("An error occurred: %s", e)
```
