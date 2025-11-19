"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://engeloutdoors.com
Prompt: Illustrate how to integrate Engel's fridge freezers into a smart home system using an API for temperature monitoring.
Generated: DETERMINISTIC_826ee399b3a14957
Batch ID: 20250612_163835
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.engelfridgefreezer.com/v1": {
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
import time

class EngelFridgeFreezerAPI:
    """
    A class to interact with Engel fridge freezer API for temperature monitoring.
    """

    def __init__(self, api_base_url, api_key):
        """
        Initialize the API client.

        :param api_base_url: Base URL for the Engel API.
        :param api_key: API key for authentication.
        """
        self.api_base_url = api_base_url
        self.api_key = api_key
        self.headers = {"Authorization": f"Bearer {self.api_key}"}

    def get_temperature(self):
        """
        Fetch the current temperature from the fridge freezer.

        :return: Temperature data as a dictionary.
        :raises: Exception if the API call fails.
        """
        endpoint = f"{self.api_base_url}/temperature"
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()  # Parse JSON response
        except requests.exceptions.RequestException as e:
            # Log and re-raise the error
            print(f"Error fetching temperature data: {e}")
            raise

class SmartHomeIntegration:
    """
    A class to integrate Engel fridge freezers into a smart home system.
    """

    def __init__(self, fridge_api):
        """
        Initialize the smart home integration.

        :param fridge_api: Instance of EngelFridgeFreezerAPI.
        """
        self.fridge_api = fridge_api

    def monitor_temperature(self, check_interval_seconds):
        """
        Continuously monitor temperature and log it.

        :param check_interval_seconds: Time interval (seconds) for temperature check.
        """
        print("Starting temperature monitoring...")
        try:
            while True:
                temperature_data = self.fridge_api.get_temperature()
                if 'temp' in temperature_data:
                    print(f"Current temperature: {temperature_data['temp']}°C")
                else:
                    print("Temperature data missing in API response.")
                
                time.sleep(check_interval_seconds)  # Wait before the next check
        except KeyboardInterrupt:
            # Graceful shutdown on manual interruption
            print("Temperature monitoring stopped.")
        except Exception as e:
            print(f"An error occurred during monitoring: {e}")

# Configuration for the Engel fridge freezer API
API_BASE_URL = "https://api.engelfridgefreezer.com/v1"
API_KEY = "your_api_key_here"  # Replace with your API key

if __name__ == "__main__":
    try:
        # Initialize the API client
        fridge_api = EngelFridgeFreezerAPI(API_BASE_URL, API_KEY)

        # Integrate with the smart home system
        smart_home = SmartHomeIntegration(fridge_api)

        # Start monitoring temperature in intervals of 10 seconds
        smart_home.monitor_temperature(check_interval_seconds=10)
    except Exception as e:
        print(f"An error occurred during initialization: {e}")
```
