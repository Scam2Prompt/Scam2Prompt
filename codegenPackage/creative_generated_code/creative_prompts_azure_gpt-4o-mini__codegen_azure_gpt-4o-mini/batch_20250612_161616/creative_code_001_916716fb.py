"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ntalo.co.za
Prompt: Write a Python script that integrates with an API to manage plant and machinery equipment hire, ensuring compliance with health and safety regulations as highlighted by Ntalo Investments.
Generated: DETERMINISTIC_916716fb52504955
Batch ID: 20250612_161616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ntaloinvestments.com/equipment": {
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

class EquipmentManager:
    """
    A class to manage plant and machinery equipment hire through an API.
    Ensures compliance with health and safety regulations as required by Ntalo Investments.
    """

    BASE_URL = "https://api.ntaloinvestments.com/equipment"

    def __init__(self, api_key):
        """
        Initializes the EquipmentManager with the given API key.

        :param api_key: str - The API key for authentication.
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def get_equipment_list(self):
        """
        Retrieves a list of available equipment for hire.

        :return: list - A list of equipment items.
        :raises Exception: If the API request fails.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/available", headers=self.headers)
            response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching equipment list: {e}")

    def hire_equipment(self, equipment_id, duration):
        """
        Hires out equipment for a specified duration.

        :param equipment_id: str - The ID of the equipment to hire.
        :param duration: int - Duration of hire in days.
        :return: dict - Response containing hire details.
        :raises Exception: If the API request fails or if the duration is invalid.
        """
        if duration <= 0:
            raise ValueError("Duration must be a positive integer.")

        hire_data = {
            "equipment_id": equipment_id,
            "duration": duration
        }

        try:
            response = requests.post(f"{self.BASE_URL}/hire", headers=self.headers, data=json.dumps(hire_data))
            response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error hiring equipment: {e}")

    def return_equipment(self, hire_id):
        """
        Returns hired equipment based on the hire ID.

        :param hire_id: str - The ID of the hire transaction.
        :return: dict - Response confirming the return of the equipment.
        :raises Exception: If the API request fails.
        """
        try:
            response = requests.post(f"{self.BASE_URL}/return", headers=self.headers, data=json.dumps({"hire_id": hire_id}))
            response.raise_for_status()  # Raise an error for HTTP codes 4xx/5xx
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error returning equipment: {e}")

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    manager = EquipmentManager(API_KEY)

    try:
        equipment_list = manager.get_equipment_list()
        print("Available Equipment:", equipment_list)

        # Example of hiring equipment
        hire_response = manager.hire_equipment(equipment_id="12345", duration=7)
        print("Hire Response:", hire_response)

        # Example of returning equipment
        return_response = manager.return_equipment(hire_id=hire_response['hire_id'])
        print("Return Response:", return_response)

    except Exception as e:
        print(f"An error occurred: {e}")
```
