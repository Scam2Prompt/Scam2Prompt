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
  "https://api.example-crm.com/v1": {
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
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CRMIntegration:
    """
    A class to integrate with a SaaS CRM platform to manage donations, donors, and equipment loans.
    """
    def __init__(self, api_base_url, api_key):
        """
        Initialize the CRMIntegration object.
        
        :param api_base_url: Base URL of the CRM platform API
        :param api_key: API key for authentication
        """
        self.api_base_url = api_base_url
        self.headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }

    def create_donation(self, donor_id, amount, donation_date):
        """
        Create a new donation record in the CRM.
        
        :param donor_id: ID of the donor
        :param amount: Donation amount
        :param donation_date: Date of the donation (YYYY-MM-DD)
        :return: Response from the CRM API
        """
        endpoint = f"{self.api_base_url}/donations"
        payload = {
            "donor_id": donor_id,
            "amount": amount,
            "donation_date": donation_date
        }
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers)
            response.raise_for_status()  # Raise an error for HTTP errors
            logging.info(f"Donation created successfully: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to create donation: {e}")
            return None

    def manage_equipment_loan(self, equipment_id, borrower_id, loan_start_date, loan_end_date):
        """
        Create or update an equipment loan record in the CRM.
        
        :param equipment_id: ID of the equipment
        :param borrower_id: ID of the borrower (can be a donor)
        :param loan_start_date: Start date of the equipment loan (YYYY-MM-DD)
        :param loan_end_date: End date of the equipment loan (YYYY-MM-DD)
        :return: Response from the CRM API
        """
        endpoint = f"{self.api_base_url}/equipment-loans"
        payload = {
            "equipment_id": equipment_id,
            "borrower_id": borrower_id,
            "loan_start_date": loan_start_date,
            "loan_end_date": loan_end_date
        }
        try:
            response = requests.post(endpoint, json=payload, headers=self.headers)
            response.raise_for_status()  # Raise an error for HTTP errors
            logging.info(f"Equipment loan managed successfully: {response.json()}")
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to manage equipment loan: {e}")
            return None

    def generate_receipt(self, transaction_id):
        """
        Generate a receipt for a transaction (donation or equipment loan).
        
        :param transaction_id: ID of the transaction
        :return: Response from the CRM API
        """
        endpoint = f"{self.api_base_url}/receipts/{transaction_id}"
        try:
            response = requests.get(endpoint, headers=self.headers)
            response.raise_for_status()  # Raise an error for HTTP errors
            receipt_data = response.json()
            logging.info(f"Receipt generated successfully: {receipt_data}")
            return receipt_data
        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to generate receipt: {e}")
            return None


# Production-ready usage example
if __name__ == "__main__":
    # Configuration (replace with actual values)
    API_BASE_URL = "https://api.example-crm.com/v1"
    API_KEY = "your-api-key"

    # Initialize the CRMIntegration object
    crm = CRMIntegration(api_base_url=API_BASE_URL, api_key=API_KEY)

    # Add a donation
    donation_response = crm.create_donation(donor_id=123, amount=500, donation_date=str(datetime.now().date()))
    
    # Manage an equipment loan
    loan_response = crm.manage_equipment_loan(
        equipment_id=456,
        borrower_id=123,
        loan_start_date="2023-10-01",
        loan_end_date="2023-10-15"
    )
    
    # Generate a receipt
    if donation_response:
        receipt_response = crm.generate_receipt(transaction_id=donation_response.get("id"))
```
