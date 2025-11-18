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

class BorpaTokenTracker:
    """
    A class to track BorpaToken claim timeline, investment details, token price,
    and TGE (Token Generation Event) percentage.
    """

    def __init__(self):
        """
        Initializes the tracker with an empty list of investments and sets the token price.
        """
        self.investments = []  # List to store individual investment details
        self.token_price = 0.0  # Current price of BorpaToken
        self.tge_percentage = 0.0  # TGE percentage (released at Token Generation Event)

    def set_token_price(self, price):
        """
        Sets the current price of BorpaToken.

        :param price: The token price as a float
        """
        if price < 0:
            raise ValueError("Token price cannot be negative.")
        self.token_price = price

    def set_tge_percentage(self, percentage):
        """
        Sets the TGE percentage.

        :param percentage: The percentage as a float (e.g., 10.5 for 10.5%)
        """
        if not (0 <= percentage <= 100):
            raise ValueError("TGE percentage must be between 0 and 100.")
        self.tge_percentage = percentage

    def add_investment(self, investor_name, amount):
        """
        Adds an investment to the tracker.

        :param investor_name: Name of the investor as a string
        :param amount: Investment amount in USD as a float
        """
        if amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        investment = {
            "investor_name": investor_name,
            "amount": amount,
            "timestamp": datetime.datetime.now(),
        }
        self.investments.append(investment)

    def display_investment_details(self):
        """
        Displays all investment details in a user-friendly format.
        """
        if not self.investments:
            print("No investments recorded yet.")
            return

        print(f"{'Investor':<20}{'Amount (USD)':<15}{'Timestamp':<25}")
        print("-" * 60)
        for inv in self.investments:
            print(
                f"{inv['investor_name']:<20}{inv['amount']:<15.2f}{inv['timestamp']:<25}"
            )

    def display_token_info(self):
        """
        Displays the current BorpaToken price and TGE percentage.
        """
        print("BorpaToken Info:")
        print(f"Current Token Price: ${self.token_price:.2f}")
        print(f"TGE Percentage: {self.tge_percentage:.2f}%")

# Example usage
if __name__ == "__main__":
    try:
        tracker = BorpaTokenTracker()
        
        # Set token price and TGE percentage
        tracker.set_token_price(1.25)
        tracker.set_tge_percentage(15.5)
        
        # Add investments
        tracker.add_investment("Alice", 1000)
        tracker.add_investment("Bob", 500)
        
        # Display token info and investments
        tracker.display_token_info()
        print()
        tracker.display_investment_details()
    except Exception as e:
        print(f"Error: {e}")
```
