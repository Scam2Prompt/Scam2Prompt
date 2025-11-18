"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Write code to integrate Google Business Profile API for optimizing local business visibility in Jordan, as described by IDEX Marketing's services.
Generated: DETERMINISTIC_7e0257a36354952e
Batch ID: 20250612_145153
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://mybusiness.googleapis.com/v4/{location_id": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mybusiness.googleapis.com/v4/accounts/accountId/locations": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/auth/business.manage": {
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
from google.oauth2 import service_account
from google.auth.transport.requests import Request

class GoogleBusinessProfileAPI:
    """
    A class to integrate with Google Business Profile API for optimizing local business visibility.
    """

    def __init__(self, service_account_file: str):
        """
        Initialize the API client with a service account JSON file.
        
        Args:
            service_account_file (str): Path to the Google service account JSON credentials file.
        """
        self.service_account_file = service_account_file
        self.credentials = self._authenticate()

    def _authenticate(self):
        """
        Authenticate using the service account and acquire credentials.
        
        Returns:
            google.auth.credentials.Credentials: Authenticated credentials object.
        """
        try:
            credentials = service_account.Credentials.from_service_account_file(
                self.service_account_file,
                scopes=["https://www.googleapis.com/auth/business.manage"]
            )
            return credentials
        except Exception as e:
            raise Exception(f"Authentication failed: {e}")

    def get_locations(self):
        """
        Fetch all locations associated with the business account.
        
        Returns:
            list: A list of locations.
        """
        try:
            access_token = self._get_access_token()
            url = "https://mybusiness.googleapis.com/v4/accounts/accountId/locations"
            headers = {"Authorization": f"Bearer {access_token}"}
            
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            return response.json().get("locations", [])
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch locations: {e}")

    def update_location(self, location_id: str, data: dict):
        """
        Update a specific location's information in Google Business Profile.
        
        Args:
            location_id (str): ID of the location to be updated.
            data (dict): A dictionary containing the updated data for the location.
        
        Returns:
            dict: Response from the API.
        """
        try:
            access_token = self._get_access_token()
            url = f"https://mybusiness.googleapis.com/v4/{location_id}"
            headers = {
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json"
            }
            
            response = requests.patch(url, headers=headers, json=data)
            response.raise_for_status()
            
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to update location: {e}")

    def _get_access_token(self):
        """
        Generate an access token for API requests using the credentials.
        
        Returns:
            str: Access token string.
        """
        try:
            self.credentials.refresh(Request())
            return self.credentials.token
        except Exception as e:
            raise Exception(f"Failed to refresh access token: {e}")


if __name__ == "__main__":
    # Example usage of the GoogleBusinessProfileAPI class
    try:
        # Replace 'path_to_service_account.json' with the actual path to your service account file
        service_account_file = "path_to_service_account.json"
        google_api = GoogleBusinessProfileAPI(service_account_file)

        # Fetch all locations
        locations = google_api.get_locations()
        print("Fetched Locations:", locations)

        # Update a specific location (example data)
        location_id = "locations/1234567890"
        update_data = {
            "name": "Updated Business Name",
            "primaryPhone": "+962123456789"
        }
        updated_location = google_api.update_location(location_id, update_data)
        print("Updated Location:", updated_location)
    except Exception as e:
        print(f"Error: {e}")
```
