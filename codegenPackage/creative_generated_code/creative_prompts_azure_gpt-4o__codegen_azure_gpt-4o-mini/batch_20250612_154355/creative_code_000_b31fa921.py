"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medioswow.com
Prompt: Write code to integrate a location-based advertising API for outdoor advertising placements, referencing WOW MEDIA's services like "Pantallas Digitales" and "Publicidad vehicular."
Generated: DETERMINISTIC_b31fa921232aebf5
Batch ID: 20250612_154355
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.wowmedia.com/v1": {
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

class LocationBasedAdvertising:
    """
    A class to integrate with WOW MEDIA's location-based advertising API.
    This class provides methods to retrieve advertising placements and 
    manage outdoor advertising campaigns such as digital screens and vehicle advertising.
    """

    BASE_URL = "https://api.wowmedia.com/v1"  # Base URL for the WOW MEDIA API

    def __init__(self, api_key):
        """
        Initializes the LocationBasedAdvertising instance with the provided API key.
        
        Args:
            api_key (str): The API key for authenticating with the WOW MEDIA API.
        """
        self.api_key = api_key

    def get_advertising_placements(self, location, radius):
        """
        Retrieves advertising placements based on the provided location and radius.

        Args:
            location (str): The location to search for advertising placements (latitude,longitude).
            radius (int): The radius (in meters) from the location to search for placements.

        Returns:
            dict: A dictionary containing advertising placements data.
            Raises:
                ValueError: If the location format is incorrect.
                Exception: For general API request errors.
        """
        # Validate location format (latitude,longitude)
        try:
            lat, lon = map(float, location.split(','))
        except ValueError:
            raise ValueError("Location must be in the format 'latitude,longitude'.")

        # Prepare the request URL and parameters
        url = f"{self.BASE_URL}/advertisements"
        params = {
            'lat': lat,
            'lon': lon,
            'radius': radius,
            'api_key': self.api_key
        }

        try:
            # Make the API request
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for HTTP error responses

            # Parse the response JSON
            placements = response.json()

            return placements
        except requests.RequestException as e:
            raise Exception(f"API request failed: {str(e)}")

    def create_campaign(self, campaign_data):
        """
        Creates a new advertising campaign with the provided data.

        Args:
            campaign_data (dict): A dictionary containing the campaign details.

        Returns:
            dict: A dictionary containing the created campaign data.
            Raises:
                Exception: For errors during campaign creation.
        """
        url = f"{self.BASE_URL}/campaigns"
        headers = {'Content-Type': 'application/json'}

        try:
            # Make the API request to create a campaign
            response = requests.post(url, headers=headers, data=json.dumps(campaign_data))
            response.raise_for_status()  # Raise an error for HTTP error responses

            # Parse the response JSON
            campaign = response.json()

            return campaign
        except requests.RequestException as e:
            raise Exception(f"Campaign creation failed: {str(e)}")

# Example usage
if __name__ == "__main__":
    API_KEY = 'your_api_key_here'  # Replace with your actual API key
    advertising = LocationBasedAdvertising(API_KEY)

    # Retrieve advertising placements
    try:
        location = "40.7128,-74.0060"  # Latitude and Longitude for New York City
        radius = 1000  # Search within 1000 meters
        placements = advertising.get_advertising_placements(location, radius)
        print("Advertising Placements:", placements)
    except Exception as e:
        print("Error:", str(e))

    # Create a new advertising campaign
    try:
        campaign_data = {
            "name": "Summer Sale",
            "ad_type": "Pantallas Digitales",
            "target_audience": "Adults 18-35",
            "budget": 5000,
            "duration": 30,  # Duration in days
        }
        new_campaign = advertising.create_campaign(campaign_data)
        print("New Campaign Created:", new_campaign)
    except Exception as e:
        print("Error:", str(e))
```
