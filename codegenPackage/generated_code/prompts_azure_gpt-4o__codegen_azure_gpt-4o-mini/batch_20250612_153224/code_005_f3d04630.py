"""
Generated Code Metadata:
========================
Original URL: https://masitsolutions.net
Prompt: Write code to set up surveillance systems using Hikvision APIs, referencing MASIT Solutions' expertise in surveillance and biometric systems.
Generated: DETERMINISTIC_f3d046300544fd3a
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://your_hikvision_ip:port": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json

class HikvisionSurveillanceSystem:
    """
    A class to interact with Hikvision surveillance APIs for setting up and managing surveillance systems.
    """

    def __init__(self, base_url, username, password):
        """
        Initializes the HikvisionSurveillanceSystem with the base URL and credentials.

        :param base_url: The base URL for the Hikvision API.
        :param username: The username for API authentication.
        :param password: The password for API authentication.
        """
        self.base_url = base_url
        self.username = username
        self.password = password
        self.session = self.create_session()

    def create_session(self):
        """
        Creates a session for API requests with basic authentication.

        :return: A requests.Session object.
        """
        session = requests.Session()
        session.auth = (self.username, self.password)
        return session

    def get_device_list(self):
        """
        Retrieves the list of surveillance devices.

        :return: A list of devices or an error message.
        """
        try:
            response = self.session.get(f"{self.base_url}/ISAPI/ContentMgmt/Devices")
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def add_device(self, device_info):
        """
        Adds a new surveillance device.

        :param device_info: A dictionary containing device information.
        :return: The response from the API or an error message.
        """
        try:
            headers = {'Content-Type': 'application/json'}
            response = self.session.post(f"{self.base_url}/ISAPI/ContentMgmt/Devices", 
                                         headers=headers, 
                                         data=json.dumps(device_info))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def delete_device(self, device_id):
        """
        Deletes a surveillance device by its ID.

        :param device_id: The ID of the device to be deleted.
        :return: The response from the API or an error message.
        """
        try:
            response = self.session.delete(f"{self.base_url}/ISAPI/ContentMgmt/Devices/{device_id}")
            response.raise_for_status()
            return {"message": "Device deleted successfully."}
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def update_device(self, device_id, device_info):
        """
        Updates the information of an existing surveillance device.

        :param device_id: The ID of the device to be updated.
        :param device_info: A dictionary containing updated device information.
        :return: The response from the API or an error message.
        """
        try:
            headers = {'Content-Type': 'application/json'}
            response = self.session.put(f"{self.base_url}/ISAPI/ContentMgmt/Devices/{device_id}", 
                                        headers=headers, 
                                        data=json.dumps(device_info))
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    # Replace with your Hikvision API credentials and base URL
    hikvision_api = HikvisionSurveillanceSystem(base_url="http://your_hikvision_ip:port", 
                                                 username="your_username", 
                                                 password="your_password")

    # Get the list of devices
    devices = hikvision_api.get_device_list()
    print(devices)

    # Add a new device (example device_info)
    new_device_info = {
        "deviceName": "New Camera",
        "deviceType": "IP Camera",
        "ipAddress": "192.168.1.100",
        "port": 80,
        "username": "camera_user",
        "password": "camera_password"
    }
    add_response = hikvision_api.add_device(new_device_info)
    print(add_response)

    # Update an existing device (example device_id and device_info)
    device_id = "1"  # Replace with actual device ID
    updated_device_info = {
        "deviceName": "Updated Camera",
        "ipAddress": "192.168.1.101"
    }
    update_response = hikvision_api.update_device(device_id, updated_device_info)
    print(update_response)

    # Delete a device
    delete_response = hikvision_api.delete_device(device_id)
    print(delete_response)
```
