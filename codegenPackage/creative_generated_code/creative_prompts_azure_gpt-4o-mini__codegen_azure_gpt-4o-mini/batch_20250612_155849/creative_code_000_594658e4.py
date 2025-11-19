"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackpanttthers.com
Prompt: Write a Python script that integrates with a smart home system to adjust the temperature and lighting based on real-time occupancy data.
Generated: DETERMINISTIC_594658e434540d75
Batch ID: 20250612_155849
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.smarthome.com/v1": {
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
import json
import requests
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SmartHomeController:
    def __init__(self, api_url, auth_token):
        """
        Initializes the SmartHomeController with the provided API URL and authentication token.

        :param api_url: The base URL for the smart home API
        :param auth_token: The authentication token for API access
        """
        self.api_url = api_url
        self.auth_token = auth_token
    
    def get_occupancy_data(self):
        """
        Retrieves the occupancy data from the smart home API.

        :return: A dictionary containing occupancy data if successful, None otherwise
        """
        try:
            response = requests.get(f"{self.api_url}/occupancy", headers={"Authorization": f"Bearer {self.auth_token}"})
            response.raise_for_status()  # Raise an error for bad responses
            logging.info("Occupancy data retrieved successfully.")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching occupancy data: {e}")
            return None

    def adjust_temperature(self, target_temperature):
        """
        Adjusts the temperature of the smart home system.

        :param target_temperature: The desired temperature to set
        """
        try:
            response = requests.post(f"{self.api_url}/temperature", json={"temperature": target_temperature},
                                     headers={"Authorization": f"Bearer {self.auth_token}"})
            response.raise_for_status()
            logging.info(f"Temperature adjusted to {target_temperature}°C successfully.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error adjusting temperature: {e}")

    def adjust_lighting(self, is_occupied):
        """
        Adjusts the lighting based on occupancy.

        :param is_occupied: Boolean indicating if the space is occupied
        """
        target_brightness = 100 if is_occupied else 0
        try:
            response = requests.post(f"{self.api_url}/lighting", json={"brightness": target_brightness},
                                     headers={"Authorization": f"Bearer {self.auth_token}"})
            response.raise_for_status()
            logging.info(f"Lighting adjusted to {'on' if is_occupied else 'off'}.")
        except requests.exceptions.RequestException as e:
            logging.error(f"Error adjusting lighting: {e}")

    def run(self):
        """
        Main method to run the smart home adjustments based on occupancy.
        """
        occupancy_data = self.get_occupancy_data()
        if occupancy_data is None:
            logging.error("Failed to retrieve occupancy data. Exiting.")
            return
        
        is_occupied = occupancy_data.get("is_occupied", False)
        logging.info(f"Current occupancy status: {'Occupied' if is_occupied else 'Unoccupied'}")

        # Temperature settings based on occupancy
        target_temperature = 22 if is_occupied else 18  # Example temperatures
        self.adjust_temperature(target_temperature)
        self.adjust_lighting(is_occupied)


if __name__ == "__main__":
    # Configuration
    API_URL = "https://api.smarthome.com/v1"
    AUTH_TOKEN = "your_auth_token_here"  # Replace with a valid token

    # Create an instance of the SmartHomeController and run it
    controller = SmartHomeController(API_URL, AUTH_TOKEN)
    controller.run()
```
