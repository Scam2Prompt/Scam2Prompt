"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unitedsoftwareservices.com
Prompt: How can I develop an IoT solution using the custom integration software services mentioned on United Software Services' site?
Generated: DETERMINISTIC_32899cf7080a5e9a
Batch ID: 20250612_155332
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.unitedsoftware.com/iot": {
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

class IoTDeviceManager:
    """
    A class to manage IoT devices using custom integration software services.
    """

    def __init__(self, base_url, api_key):
        """
        Initializes the IoTDeviceManager with the base URL and API key.

        :param base_url: The base URL for the API services.
        :param api_key: The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _make_request(self, endpoint, method='GET', data=None):
        """
        Private method to make HTTP requests to the API.

        :param endpoint: The API endpoint to hit.
        :param method: The HTTP method to use (GET or POST).
        :param data: The data to send in the request body (for POST).
        :return: Response object from the API call.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}

        try:
            if method == 'GET':
                response = requests.get(url, headers=headers)
            elif method == 'POST':
                response = requests.post(url, headers=headers, data=json.dumps(data))
            else:
                raise ValueError("Invalid HTTP method. Use 'GET' or 'POST'.")

            # Raise an error for bad responses
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return None
        except Exception as err:
            print(f"An error occurred: {err}")
            return None

    def register_device(self, device_info):
        """
        Registers a new IoT device.

        :param device_info: A dictionary containing device information.
        :return: Response from the API.
        """
        return self._make_request('devices/register', method='POST', data=device_info)

    def get_device_status(self, device_id):
        """
        Retrieves the status of an IoT device.

        :param device_id: The ID of the device to query.
        :return: Response from the API.
        """
        return self._make_request(f'devices/{device_id}/status')

    def update_device_data(self, device_id, data):
        """
        Updates the data for an IoT device.

        :param device_id: The ID of the device to update.
        :param data: A dictionary containing the data to update.
        :return: Response from the API.
        """
        return self._make_request(f'devices/{device_id}/update', method='POST', data=data)


# Example usage
if __name__ == "__main__":
    BASE_URL = "https://api.unitedsoftware.com/iot"
    API_KEY = "your_api_key_here"

    device_manager = IoTDeviceManager(BASE_URL, API_KEY)

    # Register a new device
    new_device_info = {
        "name": "Temperature Sensor",
        "type": "sensor",
        "location": "Living Room"
    }
    registration_response = device_manager.register_device(new_device_info)
    print("Device Registration Response:", registration_response)

    # Get device status
    device_id = "12345"
    status_response = device_manager.get_device_status(device_id)
    print("Device Status Response:", status_response)

    # Update device data
    new_data = {
        "temperature": 22.5,
        "humidity": 60
    }
    update_response = device_manager.update_device_data(device_id, new_data)
    print("Device Update Response:", update_response)
```
