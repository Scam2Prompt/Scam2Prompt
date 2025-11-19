"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://centroabakadabra.com
Prompt: Write a Python script that utilizes an API to manage patient records for a multidisciplinary healthcare center, focusing on services like psychology, physiotherapy, and occupational therapy.
Generated: DETERMINISTIC_5dadbc46bef493f0
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.healthcarecenter.com": {
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

class PatientRecordManager:
    """A class to manage patient records in a healthcare center using a RESTful API."""

    def __init__(self, api_base_url):
        """Initialize the PatientRecordManager with the base URL of the API."""
        self.api_base_url = api_base_url

    def _handle_response(self, response):
        """Handle API response, raising an error for unsuccessful requests."""
        if response.status_code != 200:
            raise Exception(f"API Error: {response.status_code} - {response.text}")
        return response.json()

    def create_patient(self, patient_data):
        """Create a new patient record."""
        url = f"{self.api_base_url}/patients"
        response = requests.post(url, json=patient_data)
        return self._handle_response(response)

    def get_patient(self, patient_id):
        """Retrieve a patient record by ID."""
        url = f"{self.api_base_url}/patients/{patient_id}"
        response = requests.get(url)
        return self._handle_response(response)

    def update_patient(self, patient_id, update_data):
        """Update an existing patient record."""
        url = f"{self.api_base_url}/patients/{patient_id}"
        response = requests.put(url, json=update_data)
        return self._handle_response(response)

    def delete_patient(self, patient_id):
        """Delete a patient record."""
        url = f"{self.api_base_url}/patients/{patient_id}"
        response = requests.delete(url)
        return self._handle_response(response)

    def list_services(self):
        """List all available services in the healthcare center."""
        url = f"{self.api_base_url}/services"
        response = requests.get(url)
        return self._handle_response(response)

# Example usage
if __name__ == "__main__":
    # Base URL of the patient records API
    API_BASE_URL = "https://api.healthcarecenter.com"

    # Initialize the Patient Record Manager
    manager = PatientRecordManager(API_BASE_URL)

    # Sample patient data
    new_patient = {
        "name": "John Doe",
        "age": 30,
        "gender": "Male",
        "services": ["psychology", "physiotherapy"],
        "contact": {
            "email": "john.doe@example.com",
            "phone": "123-456-7890"
        }
    }

    try:
        # Create a new patient
        created_patient = manager.create_patient(new_patient)
        print("Created Patient:", created_patient)

        # Retrieve the patient record
        patient_id = created_patient['id']
        patient_record = manager.get_patient(patient_id)
        print("Patient Record:", patient_record)

        # Update the patient record
        update_data = {"services": ["occupational therapy"]}
        updated_record = manager.update_patient(patient_id, update_data)
        print("Updated Patient Record:", updated_record)

        # List available services
        services = manager.list_services()
        print("Available Services:", services)

        # Delete the patient record
        manager.delete_patient(patient_id)
        print("Patient Record Deleted Successfully.")

    except Exception as e:
        print("An error occurred:", str(e))
```
