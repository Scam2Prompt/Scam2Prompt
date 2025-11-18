"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: Write Python code to automate the process of checking Spanish visa requirements for different types of visas (e.g., work visa, student visa, non-lucrative visa) using an API or library that handles immigration data.
Generated: DETERMINISTIC_1ac472b9bb853b8c
Batch ID: 20250612_152924
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.visa-requirements.com/": {
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

class VisaRequirementChecker:
    """
    A class to check Spanish visa requirements for different types of visas.
    """

    BASE_URL = "https://api.visa-requirements.com/"

    def __init__(self, country_code):
        """
        Initializes the VisaRequirementChecker with the specified country code.

        :param country_code: The ISO 3166-1 alpha-2 country code (e.g., 'US' for United States).
        """
        self.country_code = country_code

    def get_visa_requirements(self, visa_type):
        """
        Fetches the visa requirements for the specified visa type.

        :param visa_type: The type of visa to check (e.g., 'work', 'student', 'non-lucrative').
        :return: A dictionary containing visa requirements or an error message.
        """
        try:
            response = requests.get(f"{self.BASE_URL}requirements/{self.country_code}/{visa_type}")

            # Check if the request was successful
            response.raise_for_status()

            # Parse and return JSON response
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except requests.exceptions.RequestException as req_err:
            return {"error": f"Request error occurred: {req_err}"}
        except ValueError:
            return {"error": "Failed to parse response as JSON."}

def main():
    """
    Main function to execute the visa requirement check.
    """
    country_code = input("Enter your country code (e.g., 'US' for United States): ").strip().upper()
    visa_types = ['work', 'student', 'non-lucrative']

    visa_checker = VisaRequirementChecker(country_code)

    for visa_type in visa_types:
        requirements = visa_checker.get_visa_requirements(visa_type)
        print(f"\nVisa requirements for {visa_type} visa:")
        print(requirements)

if __name__ == "__main__":
    main()
```

**Note**: Ensure that the `BASE_URL` and API endpoint structure are correct as per the actual API you wish to use for visa requirements.
