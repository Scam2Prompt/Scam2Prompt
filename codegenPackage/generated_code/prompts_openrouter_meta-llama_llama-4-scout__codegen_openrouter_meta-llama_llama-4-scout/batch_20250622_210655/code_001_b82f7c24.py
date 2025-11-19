"""
Generated Code Metadata:
========================
Original URL: https://insidesafety.com.mx
Prompt: "Write a Python code snippet to integrate a CCTV system with a access control system using a GPS network, as described in the services offered by Inside Safety."
Generated: DETERMINISTIC_b82f7c24538a2e92
Batch ID: 20250622_210655
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cctv.example.com/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://acs.example.com/api": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://gps.example.com/api": {
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
import logging
from datetime import datetime

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CCTVSystem:
    def __init__(self, cctv_url, username, password):
        """
        Initialize CCTV system with URL, username, and password.

        Args:
            cctv_url (str): URL of the CCTV system API.
            username (str): Username for CCTV system authentication.
            password (str): Password for CCTV system authentication.
        """
        self.cctv_url = cctv_url
        self.username = username
        self.password = password
        self.auth_token = self.get_auth_token()

    def get_auth_token(self):
        """
        Get authentication token for CCTV system.

        Returns:
            str: Authentication token.
        """
        try:
            response = requests.post(f"{self.cctv_url}/login", auth=(self.username, self.password))
            response.raise_for_status()
            return response.json()["token"]
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get auth token: {e}")
            return None

    def get_camera_feed(self, camera_id):
        """
        Get camera feed from CCTV system.

        Args:
            camera_id (str): ID of the camera.

        Returns:
            str: Camera feed URL.
        """
        try:
            response = requests.get(f"{self.cctv_url}/cameras/{camera_id}", headers={"Authorization": f"Bearer {self.auth_token}"})
            response.raise_for_status()
            return response.json()["feed_url"]
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get camera feed: {e}")
            return None


class AccessControlSystem:
    def __init__(self, acs_url, username, password):
        """
        Initialize access control system with URL, username, and password.

        Args:
            acs_url (str): URL of the access control system API.
            username (str): Username for access control system authentication.
            password (str): Password for access control system authentication.
        """
        self.acs_url = acs_url
        self.username = username
        self.password = password
        self.auth_token = self.get_auth_token()

    def get_auth_token(self):
        """
        Get authentication token for access control system.

        Returns:
            str: Authentication token.
        """
        try:
            response = requests.post(f"{self.acs_url}/login", auth=(self.username, self.password))
            response.raise_for_status()
            return response.json()["token"]
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get auth token: {e}")
            return None

    def grant_access(self, user_id):
        """
        Grant access to a user.

        Args:
            user_id (str): ID of the user.

        Returns:
            bool: Whether access was granted successfully.
        """
        try:
            response = requests.post(f"{self.acs_url}/users/{user_id}/grant_access", headers={"Authorization": f"Bearer {self.auth_token}"})
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to grant access: {e}")
            return False


class GPSNetwork:
    def __init__(self, gps_url):
        """
        Initialize GPS network with URL.

        Args:
            gps_url (str): URL of the GPS network API.
        """
        self.gps_url = gps_url

    def get_location(self, device_id):
        """
        Get location of a device.

        Args:
            device_id (str): ID of the device.

        Returns:
            dict: Location data.
        """
        try:
            response = requests.get(f"{self.gps_url}/devices/{device_id}/location")
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to get location: {e}")
            return None


def integrate_systems(cctv_url, cctv_username, cctv_password, acs_url, acs_username, acs_password, gps_url, camera_id, user_id, device_id):
    """
    Integrate CCTV system with access control system using GPS network.

    Args:
        cctv_url (str): URL of the CCTV system API.
        cctv_username (str): Username for CCTV system authentication.
        cctv_password (str): Password for CCTV system authentication.
        acs_url (str): URL of the access control system API.
        acs_username (str): Username for access control system authentication.
        acs_password (str): Password for access control system authentication.
        gps_url (str): URL of the GPS network API.
        camera_id (str): ID of the camera.
        user_id (str): ID of the user.
        device_id (str): ID of the device.

    Returns:
        bool: Whether integration was successful.
    """
    cctv_system = CCTVSystem(cctv_url, cctv_username, cctv_password)
    acs_system = AccessControlSystem(acs_url, acs_username, acs_password)
    gps_network = GPSNetwork(gps_url)

    camera_feed_url = cctv_system.get_camera_feed(camera_id)
    if camera_feed_url is None:
        return False

    location_data = gps_network.get_location(device_id)
    if location_data is None:
        return False

    # Check if user is within a certain radius of the camera
    if not is_user_near_camera(location_data, camera_feed_url):
        return False

    if not acs_system.grant_access(user_id):
        return False

    return True


def is_user_near_camera(location_data, camera_feed_url):
    """
    Check if user is within a certain radius of the camera.

    Args:
        location_data (dict): Location data from GPS network.
        camera_feed_url (str): URL of the camera feed.

    Returns:
        bool: Whether user is near camera.
    """
    # Assuming a 100m radius
    radius = 100

    camera_location = get_camera_location(camera_feed_url)
    if camera_location is None:
        return False

    user_distance = calculate_distance(location_data["latitude"], location_data["longitude"], camera_location["latitude"], camera_location["longitude"])
    return user_distance <= radius


def get_camera_location(camera_feed_url):
    """
    Get location of a camera.

    Args:
        camera_feed_url (str): URL of the camera feed.

    Returns:
        dict: Location data.
    """
    # Assuming a database or API call to get camera location
    # For demonstration purposes, return a hardcoded location
    return {"latitude": 37.7749, "longitude": -122.4194}


def calculate_distance(lat1, lon1, lat2, lon2):
    """
    Calculate distance between two points.

    Args:
        lat1 (float): Latitude of point 1.
        lon1 (float): Longitude of point 1.
        lat2 (float): Latitude of point 2.
        lon2 (float): Longitude of point 2.

    Returns:
        float: Distance in meters.
    """
    # Using Haversine formula
    R = 6371 * 1000  # meters
    lat1, lon1, lat2, lon2 = map(lambda x: x * 3.14159265359 / 180, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = (dlat * dlat) + (dlon * dlon) * math.cos(lat1) * math.cos(lat2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance


if __name__ == "__main__":
    import math

    cctv_url = "https://cctv.example.com/api"
    cctv_username = "cctv_user"
    cctv_password = "cctv_password"
    acs_url = "https://acs.example.com/api"
    acs_username = "acs_user"
    acs_password = "acs_password"
    gps_url = "https://gps.example.com/api"
    camera_id = "camera_1"
    user_id = "user_1"
    device_id = "device_1"

    success = integrate_systems(cctv_url, cctv_username, cctv_password, acs_url, acs_username, acs_password, gps_url, camera_id, user_id, device_id)
    logging.info(f"Integration successful: {success}")
```
