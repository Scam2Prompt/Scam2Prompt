"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bepretty.hamburg
Prompt: Write a Python script that integrates with an API to manage appointments for makeup and styling services, inspired by the services provided by Lilianna Wysocki at bePretty Hamburg.
Generated: DETERMINISTIC_e9615eaf9ae42a9d
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api": {
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
import requests
import json
from datetime import datetime

# Constants for API endpoint and authentication
API_BASE_URL = "https://example.com/api"  # Replace with the actual API base URL
API_KEY = "your_api_key_here"  # Replace with your API key

# Utility function for API requests
def make_api_request(endpoint, method="GET", data=None):
    """
    Makes an API request and handles errors.

    Args:
        endpoint (str): API endpoint to hit.
        method (str): HTTP method (GET, POST, PUT, DELETE).
        data (dict, optional): Data payload for POST/PUT requests.

    Returns:
        dict: JSON response from the API.

    Raises:
        Exception: If the API request fails.
    """
    url = f"{API_BASE_URL}/{endpoint}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    try:
        if method == "GET":
            response = requests.get(url, headers=headers)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=data)
        elif method == "PUT":
            response = requests.put(url, headers=headers, json=data)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers)
        else:
            raise ValueError("Invalid HTTP method specified.")
        
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        raise

# Function to create a new appointment
def create_appointment(customer_name, service_type, appointment_date):
    """
    Creates a new makeup/styling appointment.

    Args:
        customer_name (str): Name of the customer.
        service_type (str): Type of service (e.g., 'makeup', 'styling').
        appointment_date (str): Appointment date in ISO format (YYYY-MM-DDTHH:MM:SS).

    Returns:
        dict: Response from the API.
    """
    payload = {
        "customer_name": customer_name,
        "service_type": service_type,
        "appointment_date": appointment_date
    }
    
    return make_api_request("appointments", method="POST", data=payload)

# Function to get all appointments
def get_appointments():
    """
    Retrieves all appointments.

    Returns:
        list: List of appointments retrieved from the API.
    """
    return make_api_request("appointments")

# Function to update an existing appointment
def update_appointment(appointment_id, updated_data):
    """
    Updates an existing appointment.

    Args:
        appointment_id (int): ID of the appointment to update.
        updated_data (dict): Dictionary containing updated fields.

    Returns:
        dict: Response from the API.
    """
    return make_api_request(f"appointments/{appointment_id}", method="PUT", data=updated_data)

# Function to delete an appointment
def delete_appointment(appointment_id):
    """
    Deletes an appointment.

    Args:
        appointment_id (int): ID of the appointment to delete.

    Returns:
        dict: Response from the API.
    """
    return make_api_request(f"appointments/{appointment_id}", method="DELETE)

# Example usage
if __name__ == "__main__":
    try:
        # Create a new appointment
        new_appointment = create_appointment(
            customer_name="Jane Doe",
            service_type="makeup",
            appointment_date=datetime.now().isoformat()
        )
        print("New Appointment Created:", new_appointment)
        
        # Get all appointments
        appointments = get_appointments()
        print("All Appointments:", appointments)
        
        # Update an appointment
        appointment_id = new_appointment.get("id")
        updated_data = {"service_type": "styling"}
        updated_appointment = update_appointment(appointment_id, updated_data)
        print("Updated Appointment:", updated_appointment)
        
        # Delete an appointment
        delete_response = delete_appointment(appointment_id)
        print("Appointment Deleted:", delete_response)
    except Exception as e:
        print(f"An error occurred: {e}")
```
