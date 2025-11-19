"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cliniquerobinpaul.com
Prompt: Write a Python function that integrates with a health clinic's API to retrieve patient information and appointment history, focusing on chiropractic and osteopathic treatments.
Generated: DETERMINISTIC_c218fad32b4c33b9
Batch ID: 20250612_162311
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.healthclinic.com": {
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
from typing import Dict, Any

def fetch_patient_data(api_url: str, api_key: str, patient_id: str) -> Dict[str, Any]:
    """
    Fetch patient information and appointment history from the health clinic's API.

    Args:
        api_url (str): Base URL of the health clinic's API.
        api_key (str): API key for authentication.
        patient_id (str): Unique identifier for the patient.

    Returns:
        Dict[str, Any]: Dictionary containing patient information and filtered appointment history.

    Raises:
        ValueError: If the patient_id is invalid.
        requests.exceptions.RequestException: If an error occurs during API communication.
    """
    # Validate the patient_id
    if not patient_id or not patient_id.isalnum():
        raise ValueError("Invalid patient ID. Please provide a valid alphanumeric ID.")

    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    try:
        # Retrieve patient info
        patient_info_response = requests.get(f"{api_url}/patients/{patient_id}", headers=headers)
        patient_info_response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        patient_info = patient_info_response.json()
        
        # Retrieve appointment history
        appointments_response = requests.get(f"{api_url}/appointments/{patient_id}", headers=headers)
        appointments_response.raise_for_status()
        appointments = appointments_response.json()

        # Filter appointments for chiropractic and osteopathic treatments
        filtered_appointments = [
            appointment for appointment in appointments
            if appointment.get("type") in {"chiropractic", "osteopathic"}
        ]

        # Combine and return the data as a structured dictionary
        return {
            "patient_info": patient_info,
            "filtered_appointments": filtered_appointments
        }

    except requests.exceptions.RequestException as e:
        # Log or handle API communication errors
        raise requests.exceptions.RequestException(f"Error communicating with the API: {e}")

# Example usage:
# api_url = "https://api.healthclinic.com"
# api_key = "your_api_key_here"
# patient_id = "12345"
# try:
#     data = fetch_patient_data(api_url, api_key, patient_id)
#     print(data)
# except Exception as e:
#     print(f"An error occurred: {e}")
```
