"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Develop a sample application that utilizes a revolving credit facility API to manage cash flow by drawing funds and calculating interest on used amounts.
Generated: DETERMINISTIC_95f596d5680d3a8c
Batch ID: 20250612_160158
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/revolving-credit": {
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
"""
Revolving Credit Facility Application
This application simulates managing cash flow using a Revolving Credit Facility API.
It allows drawing funds, calculating interest on the drawn amount, and displaying the current balance.
"""

import requests
import datetime

# Constants (Replace with actual values for production)
API_BASE_URL = "https://api.example.com/revolving-credit"
API_KEY = "your_api_key_here"
INTEREST_RATE = 0.05  # Annual interest rate (5%)
DAYS_IN_YEAR = 365  # Used for interest calculations

class RevolvingCreditFacility:
    def __init__(self, api_key, base_url):
        self.api_key = api_key
        self.base_url = base_url
        self.balance = 0  # Total drawn amount

    def _send_request(self, endpoint, payload=None):
        """
        Sends a request to the API and handles errors.
        :param endpoint: API endpoint to hit.
        :param payload: Payload for POST requests (optional).
        :return: API response in JSON format.
        """
        try:
            headers = {"Authorization": f"Bearer {self.api_key}"}
            if payload:
                response = requests.post(f"{self.base_url}/{endpoint}", json=payload, headers=headers)
            else:
                response = requests.get(f"{self.base_url}/{endpoint}", headers=headers)
            
            response.raise_for_status()  # Raise HTTPError for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            return None

    def draw_funds(self, amount):
        """
        Draw funds from the revolving credit facility.
        :param amount: Amount to draw (positive integer).
        """
        if amount <= 0:
            print("Amount must be a positive value.")
            return
        
        payload = {"amount": amount}
        response = self._send_request("draw-funds", payload)

        if response and response.get("success"):
            self.balance += amount
            print(f"Successfully drew ${amount}. Current balance: ${self.balance:.2f}")
        else:
            print(f"Failed to draw funds: {response.get('message', 'Unknown error')}")

    def calculate_interest(self, days_used):
        """
        Calculate interest on the drawn amount based on the number of days used.
        :param days_used: Number of days the funds have been used.
        :return: Interest amount.
        """
        if self.balance <= 0:
            print("No balance to calculate interest on.")
            return 0

        if days_used <= 0:
            print("Days used must be a positive value.")
            return 0

        interest = (self.balance * INTEREST_RATE * days_used) / DAYS_IN_YEAR
        print(f"Interest for {days_used} days: ${interest:.2f}")
        return interest

    def get_balance(self):
        """
        Fetch the current balance from the API.
        """
        response = self._send_request("get-balance")
        if response and response.get("success"):
            self.balance = response.get("balance", 0)
            print(f"Current balance: ${self.balance:.2f}")
        else:
            print(f"Failed to fetch balance: {response.get('message', 'Unknown error')}")

# Example usage of the RevolvingCreditFacility class
if __name__ == "__main__":
    facility = RevolvingCreditFacility(api_key=API_KEY, base_url=API_BASE_URL)

    # Draw funds
    facility.draw_funds(1000)

    # Calculate interest on used funds for 30 days
    facility.calculate_interest(days_used=30)

    # Get the current balance
    facility.get_balance()
```
