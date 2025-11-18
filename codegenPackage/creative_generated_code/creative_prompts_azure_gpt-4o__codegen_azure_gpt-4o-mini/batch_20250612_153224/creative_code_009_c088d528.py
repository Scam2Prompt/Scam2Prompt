"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vigilanciadomotica.es
Prompt: Provide a step-by-step guide to implement a smart lighting system using APIs, as outlined in the articles on vigilanciadomotica.es.
Generated: DETERMINISTIC_c088d52800d6daca
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.your-smart-lighting-system.com": {
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

class SmartLightingSystem:
    def __init__(self, api_url, api_key):
        """
        Initialize the SmartLightingSystem with API URL and API Key.
        
        :param api_url: The base URL of the smart lighting API.
        :param api_key: The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key

    def get_light_status(self, light_id):
        """
        Retrieve the current status of a specific light.
        
        :param light_id: The ID of the light to check.
        :return: The status of the light as a JSON object.
        """
        try:
            response = requests.get(f"{self.api_url}/lights/{light_id}", headers={"Authorization": f"Bearer {self.api_key}"})
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching light status: {e}")
            return None

    def turn_on_light(self, light_id):
        """
        Turn on a specific light.
        
        :param light_id: The ID of the light to be turned on.
        :return: Response from the API as a JSON object.
        """
        return self.control_light(light_id, 'on')

    def turn_off_light(self, light_id):
        """
        Turn off a specific light.
        
        :param light_id: The ID of the light to be turned off.
        :return: Response from the API as a JSON object.
        """
        return self.control_light(light_id, 'off')

    def control_light(self, light_id, action):
        """
        Control the state of a specific light.

        :param light_id: The ID of the light to control.
        :param action: The action to perform ('on' or 'off').
        :return: Response from the API as a JSON object.
        """
        try:
            data = {"action": action}
            response = requests.post(f"{self.api_url}/lights/{light_id}/control", 
                                     headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}, 
                                     data=json.dumps(data))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            print(f"Error controlling light {light_id}: {e}")
            return None

    def schedule_light(self, light_id, action, time_to_execute):
        """
        Schedule a light to turn on or off at a specified time.

        :param light_id: The ID of the light to schedule.
        :param action: The action to perform ('on' or 'off').
        :param time_to_execute: The time to execute the action in 'HH:MM' format.
        :return: None
        """
        while True:
            current_time = time.strftime("%H:%M")
            if current_time == time_to_execute:
                if action == 'on':
                    self.turn_on_light(light_id)
                elif action == 'off':
                    self.turn_off_light(light_id)
                break
            time.sleep(30)  # Check every 30 seconds

if __name__ == "__main__":
    # Example usage of SmartLightingSystem
    API_URL = "https://api.your-smart-lighting-system.com"
    API_KEY = "your_api_key_here"
    
    smart_lighting = SmartLightingSystem(API_URL, API_KEY)
    
    # Replace 'light1' with the actual light ID
    light_id = 'light1'
    
    # Turn on the light
    print(smart_lighting.turn_on_light(light_id))
    
    # Check the status of the light
    print(smart_lighting.get_light_status(light_id))
    
    # Schedule the light to turn off at 22:00
    smart_lighting.schedule_light(light_id, 'off', '22:00')
```
