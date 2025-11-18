"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: Generate code for automated appointment scheduling using InfinitiAI's built-in calendar application. Ensure the appointments flow seamlessly into the pipeline.
Generated: DETERMINISTIC_4d705091539969bb
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import requests

class InfinitiAIAppointmentScheduler:
    """
    Automated appointment scheduler using InfinitiAI's built-in calendar application.

    This class handles appointment creation, validation, and integration
    into InfinitiAI's scheduling pipeline.
    """

    def __init__(self, infiniti_api_key: str, base_url: str):
        """
        Initialize the scheduler with API credentials.

        :param infiniti_api_key: API key for authenticating with InfinitiAI's calendar service.
        :param base_url: Base URL for the InfinitiAI API.
        """
        self.api_key = infiniti_api_key
        self.base_url = base_url

    def create_appointment(self, title: str, start_time: datetime.datetime, end_time: datetime.datetime, description: str = "") -> dict:
        """
        Schedule a new appointment using the InfinitiAI API.

        :param title: Title of the appointment.
        :param start_time: Start time of the appointment (datetime object).
        :param end_time: End time of the appointment (datetime object).
        :param description: Optional description of the appointment.
        :return: Response from the InfinitiAI API as a dictionary.
        """
        # Validate input parameters
        if end_time <= start_time:
            raise ValueError("End time must be after start time.")
        if not title:
            raise ValueError("Appointment title cannot be empty.")

        # Prepare payload for the API request
        payload = {
            "title": title,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "description": description
        }

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            # Make API request to schedule the appointment
            response = requests.post(f"{self.base_url}/appointments", json=payload, headers=headers)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()
        except requests.RequestException as e:
            # Handle network or API errors
            print(f"Error scheduling appointment: {e}")
            return {"error": str(e)}

    def list_appointments(self) -> dict:
        """
        Retrieve all scheduled appointments from the InfinitiAI API.

        :return: Response from the InfinitiAI API as a dictionary.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            # Make API request to fetch appointments
            response = requests.get(f"{self.base_url}/appointments", headers=headers)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()
        except requests.RequestException as e:
            # Handle network or API errors
            print(f"Error retrieving appointments: {e}")
            return {"error": str(e)}

    def delete_appointment(self, appointment_id: str) -> dict:
        """
        Delete a specific appointment from InfinitiAI's calendar.

        :param appointment_id: ID of the appointment to delete.
        :return: Response from the InfinitiAI API as a dictionary.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            # Make API request to delete the appointment
            response = requests.delete(f"{self.base_url}/appointments/{appointment_id}", headers=headers)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()
        except requests.RequestException as e:
            # Handle network or API errors
            print(f"Error deleting appointment: {e}")
            return {"error": str(e)}


# Example usage (ensure to replace '<your_api_key>' and '<base_url>' with actual values):
if __name__ == "__main__":
    scheduler = InfinitiAIAppointmentScheduler("<your_api_key>", "<base_url>")
    
    # Create a new appointment
    new_appointment = scheduler.create_appointment(
        title="Team Meeting",
        start_time=datetime.datetime(2023, 10, 10, 14, 0),
        end_time=datetime.datetime(2023, 10, 10, 15, 0),
        description="Discuss project updates and milestones."
    )
    print("Created Appointment:", new_appointment)

    # List all appointments
    appointments = scheduler.list_appointments()
    print("Appointments List:", appointments)

    # Delete an appointment (replace '<appointment_id>' with actual ID)
    delete_response = scheduler.delete_appointment("<appointment_id>")
    print("Delete Response:", delete_response)
```
