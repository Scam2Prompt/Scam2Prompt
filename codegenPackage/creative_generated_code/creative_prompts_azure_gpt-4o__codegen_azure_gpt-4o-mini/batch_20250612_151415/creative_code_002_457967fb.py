"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Develop a function to locate nearby bank branches based on a given PIN code, using the branch locator functionality described on the IFSC Finder webpage.
Generated: DETERMINISTIC_457967fb303cb42b
Batch ID: 20250612_151415
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://ifsc.razorpay.com/": {
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

class BankBranchLocator:
    """
    A class to locate nearby bank branches based on a given PIN code using the IFSC Finder service.
    """

    BASE_URL = "https://ifsc.razorpay.com/"

    def __init__(self):
        pass

    def get_branch_info(self, pin_code):
        """
        Fetches bank branch information based on the provided PIN code.

        Args:
            pin_code (str): The PIN code to search for nearby bank branches.

        Returns:
            list: A list of bank branch information if successful, otherwise an empty list.
        """
        try:
            response = requests.get(f"{self.BASE_URL}{pin_code}")
            response.raise_for_status()  # Raise an error for bad responses
            branch_data = response.json()

            # Check if branch data is available
            if isinstance(branch_data, list) and branch_data:
                return branch_data
            else:
                print(f"No branches found for PIN code: {pin_code}")
                return []

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return []
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            return []
        except ValueError as json_err:
            print(f"JSON decoding error occurred: {json_err}")
            return []

if __name__ == "__main__":
    # Example usage of the BankBranchLocator class
    locator = BankBranchLocator()
    pin_code = input("Enter the PIN code to locate nearby bank branches: ")
    branches = locator.get_branch_info(pin_code)

    if branches:
        print("Nearby Bank Branches:")
        for branch in branches:
            print(f"Bank: {branch.get('BANK')}, Branch: {branch.get('BRANCH')}, IFSC: {branch.get('IFSC')}")
    else:
        print("No branches found.")
```
