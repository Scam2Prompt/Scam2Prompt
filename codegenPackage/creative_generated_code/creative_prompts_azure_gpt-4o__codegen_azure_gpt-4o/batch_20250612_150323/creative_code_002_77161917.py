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
  "https://api.hvac-service.com": {
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

class HVACTechnicianChecker:
    """
    A class to interact with an HVAC API to check for NATE-certified technicians in a given area.
    """

    def __init__(self, api_key, base_url):
        """
        Initialize the HVACTechnicianChecker with API credentials and base URL.
        
        :param api_key: Your API key for authentication with the HVAC API.
        :param base_url: The base URL of the HVAC API.
        """
        self.api_key = api_key
        self.base_url = base_url

    def _make_request(self, endpoint, params):
        """
        Make a GET request to the HVAC API.

        :param endpoint: The specific API endpoint to call.
        :param params: Dictionary of query parameters to include in the request.
        :return: JSON response from the API if successful.
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise HTTPError for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error while making API request: {e}")
            return None

    def get_nate_certified_technicians(self, zip_code, radius=10):
        """
        Fetch NATE-certified HVAC technicians in a given area.

        :param zip_code: The zip code to search for technicians.
        :param radius: The search radius (in miles) from the zip code. Default is 10 miles.
        :return: List of NATE-certified technicians or None if an error occurs.
        """
        endpoint = "technicians/search"
        params = {
            "zip_code": zip_code,
            "radius": radius,
            "certification": "NATE"  # Filter for NATE certification
        }
        response = self._make_request(endpoint, params)
        
        if not response:
            print("Failed to fetch NATE-certified technicians.")
            return None
        
        # Extract technicians from the response
        technicians = response.get("technicians", [])
        return technicians

    @staticmethod
    def display_technicians(technicians):
        """
        Display the list of NATE-certified technicians in a user-friendly format.

        :param technicians: List of technician dictionaries.
        """
        if not technicians:
            print("No NATE-certified technicians found.")
            return

        print("NATE-Certified Technicians:")
        for tech in technicians:
            name = tech.get("name", "N/A")
            phone = tech.get("phone", "N/A")
            address = tech.get("address", "N/A")
            print(f"- Name: {name}, Phone: {phone}, Address: {address}")

def main():
    """
    Main function to interact with the HVAC API and display NATE-certified technicians.
    """
    # Replace these with your actual API credentials and base URL
    API_KEY = "your_api_key_here"
    BASE_URL = "https://api.hvac-service.com"

    # Create an instance of HVACTechnicianChecker
    checker = HVACTechnicianChecker(API_KEY, BASE_URL)

    # Request user input for zip code and radius
    zip_code = input("Enter the zip code to search for NATE-certified technicians: ")
    radius = input("Enter search radius (in miles, default is 10): ")

    # Convert radius to an integer, default to 10 if invalid
    try:
        radius = int(radius)
    except ValueError:
        radius = 10

    # Get technicians and display them
    technicians = checker.get_nate_certified_technicians(zip_code, radius)
    checker.display_technicians(technicians)

if __name__ == "__main__":
    main()
```
