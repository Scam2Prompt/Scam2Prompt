"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fondation.app
Prompt: Write Python code to integrate with a SaaS CRM platform designed for foundations, specifically for managing donations, donors, and equipment loans. Reference features like multi-deposit equipment management and receipt generation.
Generated: DETERMINISTIC_c75a55c1e249ef8c
Batch ID: 20250612_151354
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.saas-crm-platform.com/v1": {
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
from datetime import datetime

class CRMDashboard:
    """Class to interface with a SaaS CRM platform for managing donations, donors, and equipment loans."""

    BASE_URL = "https://api.saas-crm-platform.com/v1"  # Replace with the actual API endpoint

    def __init__(self, api_key):
        """Initialize the CRM dashboard with the provided API key."""
        self.api_key = api_key
        self.headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def create_donor(self, donor_data):
        """Create a new donor in the CRM.

        Args:
            donor_data (dict): A dictionary containing donor information.

        Returns:
            dict: Response from the CRM API.
        """
        url = f"{self.BASE_URL}/donors"
        response = requests.post(url, headers=self.headers, data=json.dumps(donor_data))
        return self._handle_response(response)

    def record_donation(self, donation_data):
        """Record a new donation in the CRM.

        Args:
            donation_data (dict): A dictionary containing donation information.

        Returns:
            dict: Response from the CRM API.
        """
        url = f"{self.BASE_URL}/donations"
        response = requests.post(url, headers=self.headers, data=json.dumps(donation_data))
        return self._handle_response(response)

    def create_equipment_loan(self, loan_data):
        """Create a new equipment loan in the CRM.

        Args:
            loan_data (dict): A dictionary containing equipment loan information.

        Returns:
            dict: Response from the CRM API.
        """
        url = f"{self.BASE_URL}/equipment_loans"
        response = requests.post(url, headers=self.headers, data=json.dumps(loan_data))
        return self._handle_response(response)

    def generate_receipt(self, donation_id):
        """Generate a receipt for a specific donation.

        Args:
            donation_id (str): The ID of the donation.

        Returns:
            dict: Response from the CRM API containing the receipt information.
        """
        url = f"{self.BASE_URL}/donations/{donation_id}/receipt"
        response = requests.get(url, headers=self.headers)
        return self._handle_response(response)

    def _handle_response(self, response):
        """Handle API response, checking for errors and returning data.

        Args:
            response (requests.Response): The HTTP response from the API.

        Returns:
            dict: Parsed JSON response or an error message.
        """
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Error {response.status_code}: {response.text}")

# Example usage:
if __name__ == "__main__":
    # Replace with a valid API key
    API_KEY = "your_api_key"
    
    crm = CRMDashboard(api_key=API_KEY)

    # Example donor data
    donor_info = {
        "name": "John Doe",
        "email": "john.doe@example.com",
        "phone": "123-456-7890"
    }

    try:
        donor_response = crm.create_donor(donor_info)
        print("Donor created:", donor_response)

        # Example donation data
        donation_info = {
            "donor_id": donor_response['id'],
            "amount": 100.0,
            "date": datetime.now().isoformat()
        }

        donation_response = crm.record_donation(donation_info)
        print("Donation recorded:", donation_response)

        # Generate receipt for the recorded donation
        receipt_response = crm.generate_receipt(donation_response['id'])
        print("Receipt generated:", receipt_response)
        
    except Exception as e:
        print("An error occurred:", e)
```
