"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://frigoterm.ro
Prompt: Generate a code snippet for integrating Wi-Fi control in a Gree air conditioning unit using its API.
Generated: DETERMINISTIC_1cba5172b4589a9b
Batch ID: 20250612_160408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.gree.com/v1": {
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

class GreeAirConditioner:
    """
    Class to control a Gree air conditioning unit via its API.
    """
    def __init__(self, api_url: str, device_id: str, api_key: str):
        """
        Initialize the GreeAirConditioner instance.

        :param api_url: The base URL of the Gree API.
        :param device_id: The unique ID of the Gree air conditioner.
        :param api_key: The API key for authentication.
        """
        self.api_url = api_url.rstrip('/')
        self.device_id = device_id
        self.api_key = api_key

    def _send_request(self, endpoint: str, payload: dict) -> dict:
        """
        Send a request to the Gree API.

        :param endpoint: API endpoint to send the request to.
        :param payload: Dictionary containing the request payload.
        :return: JSON response from the API.
        """
        url = f"{self.api_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}

        try:
            response = requests.post(url, json=payload, headers=headers, timeout=10)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            return response.json()
        except requests.exceptions.RequestException as e:
            # Log the error (in a production scenario, use a logging framework)
            print(f"Error: {e}")
            return {"error": str(e)}

    def set_mode(self, mode: str) -> dict:
        """
        Set the air conditioner mode.

        :param mode: Mode to set (e.g., "cool", "heat", "fan", "dry").
        :return: API response.
        """
        if mode not in ["cool", "heat", "fan", "dry"]:
            return {"error": "Invalid mode. Supported modes: cool, heat, fan, dry"}

        payload = {"device_id": self.device_id, "operation": "set_mode", "mode": mode}
        return self._send_request("control", payload)

    def set_temperature(self, temperature: int) -> dict:
        """
        Set the air conditioner target temperature.

        :param temperature: Temperature to set (in degrees Celsius).
        :return: API response.
        """
        if not (16 <= temperature <= 30):  # Assuming valid range is 16°C to 30°C
            return {"error": "Invalid temperature. Supported range: 16°C - 30°C"}

        payload = {"device_id": self.device_id, "operation": "set_temperature", "temperature": temperature}
        return self._send_request("control", payload)

    def toggle_power(self, power_state: bool) -> dict:
        """
        Turn the air conditioner on or off.

        :param power_state: True to turn on, False to turn off.
        :return: API response.
        """
        payload = {"device_id": self.device_id, "operation": "power", "state": "on" if power_state else "off"}
        return self._send_request("control", payload)
    
    def get_status(self) -> dict:
        """
        Retrieve the current status of the air conditioner.

        :return: Current status as returned by the API.
        """
        payload = {"device_id": self.device_id, "operation": "status"}
        return self._send_request("status", payload)


# Example usage:
if __name__ == "__main__":
    # Replace these values with actual API and device credentials
    API_URL = "https://api.gree.com/v1"
    DEVICE_ID = "123456789"
    API_KEY = "your_api_key_here"

    ac = GreeAirConditioner(API_URL, DEVICE_ID, API_KEY)
    
    # Turn on the air conditioner
    print(ac.toggle_power(True))
    
    # Set mode to 'cool'
    print(ac.set_mode("cool"))
    
    # Set temperature to 24°C
    print(ac.set_temperature(24))
    
    # Get the current status
    print(ac.get_status())
```
