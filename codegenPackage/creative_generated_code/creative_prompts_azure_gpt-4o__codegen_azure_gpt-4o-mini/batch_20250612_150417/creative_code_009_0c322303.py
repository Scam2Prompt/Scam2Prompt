"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passiveinvestincome.com
Prompt: Write a program to simulate the reinvestment process through an interest wallet, as mentioned in PassiveInvestIncome's referral program. Include functionality to track reinvestment amounts and calculate updated earnings.
Generated: DETERMINISTIC_0c322303de201aff
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InterestWallet:
    def __init__(self, initial_amount=0.0, interest_rate=0.05):
        """
        Initializes the InterestWallet with an initial amount and an interest rate.
        
        :param initial_amount: The starting balance in the wallet, defaults to 0.0
        :param interest_rate: The interest rate for reinvestment, defaults to 5%
        """
        self.balance = initial_amount
        self.interest_rate = interest_rate
        self.reinvestment_history = []

    def add_funds(self, amount):
        """
        Adds funds to the wallet.

        :param amount: The amount to be added to the wallet.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount to add must be non-negative.")
        self.balance += amount
        print(f"Added {amount:.2f} to the wallet. New balance: {self.balance:.2f}")

    def calculate_interest(self):
        """
        Calculates the interest based on the current balance and interest rate.
        
        :return: The calculated interest amount.
        """
        return self.balance * self.interest_rate

    def reinvest_interest(self):
        """
        Reinvests the calculated interest back into the wallet and records the transaction.
        """
        interest = self.calculate_interest()
        self.balance += interest
        self.reinvestment_history.append(interest)
        print(f"Reinvested interest: {interest:.2f}. New balance: {self.balance:.2f}")

    def get_balance(self):
        """
        Returns the current balance of the wallet.
        
        :return: The current balance.
        """
        return self.balance

    def get_reinvestment_history(self):
        """
        Returns the history of reinvestments made.

        :return: List of reinvested amounts.
        """
        return self.reinvestment_history

    def print_summary(self):
        """
        Prints the summary of the wallet, including current balance and reinvestment history.
        """
        print(f"Current Balance: {self.balance:.2f}")
        print("Reinvestment History:")
        for idx, amount in enumerate(self.reinvestment_history, start=1):
            print(f"  {idx}: {amount:.2f}")

if __name__ == "__main__":
    try:
        wallet = InterestWallet(initial_amount=100.0, interest_rate=0.05)
        wallet.add_funds(50.0)
        wallet.reinvest_interest()
        wallet.reinvest_interest()
        wallet.print_summary()
    except ValueError as e:
        print(f"Error: {e}")
```
