"""
Generated Code Metadata:
========================
Original URL: https://lightningzaim.online
Prompt: "Generate a Python script to filter and compare loan offers from various MFOs in Kazakhstan based on user input for loan amount and duration."
Generated: DETERMINISTIC_aa981250504bd2bd
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class LoanOffer:
    """Class to represent a loan offer from an MFO."""
    
    def __init__(self, name: str, amount: float, duration: int, interest_rate: float):
        self.name = name
        self.amount = amount
        self.duration = duration
        self.interest_rate = interest_rate

    def monthly_payment(self) -> float:
        """Calculate the monthly payment using the formula for an amortizing loan."""
        if self.interest_rate == 0:
            return self.amount / self.duration
        monthly_rate = self.interest_rate / 12 / 100
        return (self.amount * monthly_rate) / (1 - (1 + monthly_rate) ** -self.duration)

    def __repr__(self):
        return f"{self.name}: Amount={self.amount}, Duration={self.duration}, Interest Rate={self.interest_rate}%"


def load_loan_offers(file_path: str) -> List[LoanOffer]:
    """Load loan offers from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [LoanOffer(**offer) for offer in data['offers']]
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def filter_loan_offers(offers: List[LoanOffer], amount: float, duration: int) -> List[LoanOffer]:
    """Filter loan offers based on user input for amount and duration."""
    return [offer for offer in offers if offer.amount >= amount and offer.duration >= duration]


def main():
    """Main function to execute the loan offer filtering."""
    # Load loan offers from a JSON file
    offers = load_loan_offers('loan_offers.json')

    if not offers:
        print("No loan offers available to compare.")
        return

    # User input for loan amount and duration
    try:
        loan_amount = float(input("Enter the desired loan amount: "))
        loan_duration = int(input("Enter the desired loan duration (in months): "))
    except ValueError:
        print("Invalid input. Please enter numeric values for loan amount and duration.")
        return

    # Filter offers based on user input
    filtered_offers = filter_loan_offers(offers, loan_amount, loan_duration)

    if not filtered_offers:
        print("No loan offers match your criteria.")
    else:
        print("Filtered Loan Offers:")
        for offer in filtered_offers:
            print(f"{offer} | Monthly Payment: {offer.monthly_payment():.2f}")


if __name__ == "__main__":
    main()
```

**Note:** Ensure that the `loan_offers.json` file exists in the same directory as this script and follows the expected structure:

```json
{
    "offers": [
        {
            "name": "MFO A",
            "amount": 100000,
            "duration": 12,
            "interest_rate": 15.0
        },
        {
            "name": "MFO B",
            "amount": 200000,
            "duration": 24,
            "interest_rate": 12.5
        }
        // Add more offers as needed
    ]
}
```
