"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://events-borpatoken.com
Prompt: Develop a program to track and display the BorpaToken claim timeline, including investment details, token price, and TGE percentage.
Generated: DETERMINISTIC_3e09453e19687732
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class BorpaTokenClaim:
    def __init__(self):
        self.investments = []
        self.token_price = 0.0
        self.tge_percentage = 0.0
        self.claims_timeline = []

    def add_investment(self, amount, date):
        """Add an investment record."""
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        if not isinstance(date, datetime.date):
            raise TypeError("Date must be a datetime.date object.")
        
        investment_record = {
            'amount': amount,
            'date': date
        }
        self.investments.append(investment_record)

    def set_token_price(self, price):
        """Set the current token price."""
        if price < 0:
            raise ValueError("Token price must not be negative.")
        self.token_price = price

    def set_tge_percentage(self, percentage):
        """Set the Token Generation Event (TGE) percentage."""
        if not (0 <= percentage <= 100):
            raise ValueError("TGE percentage must be between 0 and 100.")
        self.tge_percentage = percentage

    def record_claim_timeline(self, date):
        """Record a token claim in the timeline."""
        if not isinstance(date, datetime.date):
            raise TypeError("Date must be a datetime.date object.")
        
        claim_record = {
            'date': date,
            'investment_details': self.investments,
            'token_price': self.token_price,
            'tge_percentage': self.tge_percentage
        }
        self.claims_timeline.append(claim_record)

    def display_claim_timeline(self):
        """Display the claims timeline in a readable format."""
        if not self.claims_timeline:
            print("No claims recorded yet.")
            return
        
        for claim in self.claims_timeline:
            print(f"Claim Date: {claim['date']}")
            print(f"Token Price: {claim['token_price']}")
            print(f"TGE Percentage: {claim['tge_percentage']}%")
            print("Investments:")
            for investment in claim['investment_details']:
                print(f"  - Amount: {investment['amount']}, Date: {investment['date']}")
            print("")

    def save_timeline_to_file(self, filename):
        """Save the claims timeline to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.claims_timeline, file, default=str, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

# Example Usage
if __name__ == "__main__":
    try:
        tracker = BorpaTokenClaim()
        tracker.set_token_price(1.5)
        tracker.set_tge_percentage(50)

        # Add sample investments
        tracker.add_investment(1000, datetime.date(2023, 9, 1))
        tracker.add_investment(2000, datetime.date(2023, 9, 15))

        # Record claims timeline
        tracker.record_claim_timeline(datetime.date(2023, 10, 1))

        # Display the timeline
        tracker.display_claim_timeline()

        # Save to file
        tracker.save_timeline_to_file("claims_timeline.json")
    except Exception as e:
        print(f"An error occurred: {e}")
```
