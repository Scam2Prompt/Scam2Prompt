"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
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

# Creative Generated Code:
# ========================

```python
import requests

class PinCodeFinder:
    """
    A class to find Indian postal codes (PIN codes) based on location or district.
    """

    BASE_URL = "https://api.postalpincode.in"

    def __init__(self):
        """Initializes the PinCodeFinder class."""
        pass

    def search_by_district(self, district_name):
        """
        Search for postal codes by district name.

        Args:
            district_name (str): The name of the district to search for.

        Returns:
            list: A list of postal codes and associated details for the district.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/pincode/{district_name}")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            if data[0]['Status'] == 'Success':
                return data[0]['PostOffice']
            else:
                raise ValueError(f"No postal codes found for district: {district_name}")

        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            return []
        except ValueError as ve:
            print(ve)
            return []

    def display_postal_codes(self, district_name):
        """
        Display postal codes for a given district.

        Args:
            district_name (str): The name of the district to display postal codes for.
        """
        post_offices = self.search_by_district(district_name)

        if post_offices:
            print(f"Postal codes for district '{district_name}':")
            for office in post_offices:
                print(f"Office Name: {office['Name']}, PIN: {office['Pincode']}, State: {office['State']}")
        else:
            print(f"No postal codes found for district '{district_name}'.")

if __name__ == "__main__":
    finder = PinCodeFinder()
    district = input("Enter the district name to search for postal codes: ").strip()
    finder.display_postal_codes(district)
```
