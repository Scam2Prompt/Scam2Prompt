"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rexas-token.xyz
Prompt: Describe the process of investing in precious metals through Rexas Finance and the benefits of using their platform.
Generated: DETERMINISTIC_bd5bee27bd36dfd7
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Investment in Precious Metals through Rexas Finance

This script provides a simple simulation of the investment process in precious metals
using the Rexas Finance platform. It includes functionalities like adding funds, purchasing
precious metals, and checking the investment portfolio.

Assumptions:
- Rexas Finance allows users to invest in various precious metals.
- The user can check their balance and view their investment portfolio.
"""

class RexasFinance:
    def __init__(self):
        # Initialize a user account with a balance of 0 and an empty portfolio.
        self.balance = 0.0
        self.portfolio = {}

    def add_funds(self, amount):
        """
        Add funds to the user's account.

        :param amount: float - The amount of money to add.
        :raises ValueError: If the amount is non-positive.
        """
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        self.balance += amount
        print(f"Added ${amount:.2f} to your balance. New balance: ${self.balance:.2f}")

    def purchase_metal(self, metal, quantity, price_per_unit):
        """
        Purchase a specified quantity of a precious metal.

        :param metal: str - The type of precious metal (e.g., Gold, Silver).
        :param quantity: float - The quantity of metal to purchase.
        :param price_per_unit: float - The price per unit of the metal.
        :raises ValueError: If the quantity is non-positive or insufficient funds.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        
        total_cost = quantity * price_per_unit
        if total_cost > self.balance:
            raise ValueError("Insufficient funds to complete this purchase.")
        
        # Deduct the cost from balance and update the portfolio
        self.balance -= total_cost
        if metal in self.portfolio:
            self.portfolio[metal] += quantity
        else:
            self.portfolio[metal] = quantity

        print(f"Purchased {quantity} units of {metal} for ${total_cost:.2f}. New balance: ${self.balance:.2f}")

    def check_portfolio(self):
        """
        Display the current investment portfolio.
        """
        if not self.portfolio:
            print("Your portfolio is currently empty.")
        else:
            print("Current Portfolio:")
            for metal, quantity in self.portfolio.items():
                print(f"{metal}: {quantity} units")
            print(f"Remaining Balance: ${self.balance:.2f}")

# Example Usage
if __name__ == "__main__":
    try:
        rexas_investment = RexasFinance()
        rexas_investment.add_funds(1000)
        rexas_investment.purchase_metal("Gold", 2, 500)  # Assume Gold price is $500 per unit
        rexas_investment.check_portfolio()
        rexas_investment.purchase_metal("Silver", 5, 25)  # Assume Silver price is $25 per unit
        rexas_investment.check_portfolio()
    except ValueError as e:
        print(f"Error: {e}")
```
