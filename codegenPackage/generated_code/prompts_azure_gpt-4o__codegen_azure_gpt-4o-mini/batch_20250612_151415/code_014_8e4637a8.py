"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Generate a Python script to search for Indian postal codes by location or district, inspired by the India PIN Code Finder tool on the IFSC Finder website.
Generated: DETERMINISTIC_8e4637a8debff047
Batch ID: 20250612_151415
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.postalpincode.in": {
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

class PinCodeFinder:
    """
    A class to find Indian postal codes (PIN codes) based on location or district.
    """

    BASE_URL = "https://api.postalpincode.in"

    def __init__(self):
        """
        Initializes the PinCodeFinder class.
        """
        pass

    def get_pincode_by_district(self, district: str) -> dict:
        """
        Fetches the PIN codes for a given district.

        Args:
            district (str): The name of the district to search for.

        Returns:
            dict: A dictionary containing the district's PIN codes and status.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/postoffice/{district}")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            if data[0]['Status'] == 'Success':
                return {
                    'status': 'Success',
                    'pincodes': [post['PinCode'] for post in data[0]['PostOffice']]
                }
            else:
                return {'status': 'Error', 'message': 'District not found.'}

        except requests.exceptions.RequestException as e:
            return {'status': 'Error', 'message': str(e)}

    def get_pincode_by_location(self, location: str) -> dict:
        """
        Fetches the PIN codes for a given location.

        Args:
            location (str): The name of the location to search for.

        Returns:
            dict: A dictionary containing the location's PIN codes and status.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/pincode/{location}")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            if data[0]['Status'] == 'Success':
                return {
                    'status': 'Success',
                    'pincodes': [post['PinCode'] for post in data[0]['PostOffice']]
                }
            else:
                return {'status': 'Error', 'message': 'Location not found.'}

        except requests.exceptions.RequestException as e:
            return {'status': 'Error', 'message': str(e)}

def main():
    """
    Main function to demonstrate the usage of the PinCodeFinder class.
    """
    finder = PinCodeFinder()

    # Example usage
    district = input("Enter the district name: ")
    district_result = finder.get_pincode_by_district(district)
    print(district_result)

    location = input("Enter the location name: ")
    location_result = finder.get_pincode_by_location(location)
    print(location_result)

if __name__ == "__main__":
    main()
```
