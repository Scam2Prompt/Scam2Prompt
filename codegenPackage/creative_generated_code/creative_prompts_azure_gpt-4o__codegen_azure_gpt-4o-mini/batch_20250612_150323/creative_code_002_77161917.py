"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Develop a Python program that integrates with an HVAC API to check for NATE-certified technicians in a given area, referencing the certification details mentioned on the Quality Sheet Metal, Inc. site.
Generated: DETERMINISTIC_7716191798a8c389
Batch ID: 20250612_150323
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.hvac_service.com": {
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

class HVACService:
    """
    A class to interface with the HVAC API for checking NATE-certified technicians.
    """

    BASE_URL = "https://api.hvac_service.com"  # Replace with actual HVAC API base URL

    def __init__(self, api_key):
        """
        Initializes the HVACService with the provided API key.

        Args:
            api_key (str): The API key for authenticating with the HVAC API.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, params):
        """
        Makes a GET request to the specified endpoint with the given parameters.

        Args:
            endpoint (str): The API endpoint to call.
            params (dict): The parameters to include in the request.

        Returns:
            dict: The JSON response from the API.

        Raises:
            Exception: Raises an exception for any HTTP errors or API issues.
        """
        headers = {'Authorization': f'Bearer {self.api_key}'}
        response = requests.get(f"{self.BASE_URL}/{endpoint}", headers=headers, params=params)

        # Check for HTTP errors
        if response.status_code != 200:
            raise Exception(f"Error fetching data from API: {response.status_code} {response.text}")

        return response.json()

    def find_nate_certified_technicians(self, location):
        """
        Finds NATE-certified technicians in the specified location.

        Args:
            location (str): The location to search for technicians.

        Returns:
            list: A list of NATE-certified technicians in the area.

        Raises:
            Exception: Raises an exception if the API call fails.
        """
        params = {'location': location, 'certification': 'NATE'}
        try:
            response = self._make_request("technicians", params)
            return response.get('technicians', [])
        except Exception as e:
            print(f"Failed to retrieve NATE-certified technicians: {e}")
            return []

def main():
    """
    Main function to execute the HVAC service program.
    """
    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    hvac_service = HVACService(api_key)

    location = input("Enter your location (city, state): ")
    
    technicians = hvac_service.find_nate_certified_technicians(location)

    if technicians:
        print(f"NATE-certified technicians in {location}:")
        for tech in technicians:
            print(f"- {tech['name']}, Phone: {tech['phone']}, Company: {tech['company']}")
    else:
        print("No NATE-certified technicians found in that area.")

if __name__ == "__main__":
    main()
```
