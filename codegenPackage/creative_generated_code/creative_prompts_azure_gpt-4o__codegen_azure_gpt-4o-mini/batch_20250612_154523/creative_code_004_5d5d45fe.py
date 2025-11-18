"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Write a Python script to query the SUNAT API for tax compliance checks, inspired by the "Principales trámites ante la SUNAT y tribunal fiscal" course on AulaContable.
Generated: DETERMINISTIC_5d5d45fe8641fd34
Batch ID: 20250612_154523
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.sunat.gob.pe/v1/": {
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

class SUNATClient:
    """
    A client to interact with the SUNAT API for tax compliance checks.
    """

    BASE_URL = "https://api.sunat.gob.pe/v1/"

    def __init__(self, ruc):
        """
        Initializes the SUNATClient with the provided RUC number.

        :param ruc: The RUC number to be queried.
        """
        self.ruc = ruc

    def check_tax_compliance(self):
        """
        Checks the tax compliance status of the provided RUC.

        :return: A dictionary containing the compliance status.
        :raises ValueError: If the RUC is invalid.
        :raises Exception: For any other errors during the API call.
        """
        # Validate RUC format
        if not self._is_valid_ruc(self.ruc):
            raise ValueError(f"Invalid RUC format: {self.ruc}")

        url = f"{self.BASE_URL}compliance/{self.ruc}"
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses

            # Parse the JSON response
            compliance_data = response.json()

            return compliance_data

        except requests.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except requests.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")  # Handle any request exceptions
        except ValueError as json_err:
            raise Exception(f"JSON decode error: {json_err}")  # Handle JSON decode errors

    @staticmethod
    def _is_valid_ruc(ruc):
        """
        Validates the format of the RUC number.

        :param ruc: The RUC number to validate.
        :return: True if valid, False otherwise.
        """
        return isinstance(ruc, str) and len(ruc) == 11 and ruc.isdigit()

def main():
    """
    Main function to execute the SUNAT compliance check.
    """
    # Example RUC for testing
    ruc = "20123456789"  # Replace with a valid RUC number
    
    try:
        client = SUNATClient(ruc)
        compliance_info = client.check_tax_compliance()
        print("Tax Compliance Info:", compliance_info)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
