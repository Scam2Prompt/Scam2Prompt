"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinotg.pages.dev
Prompt: Generate code to simulate wagering with `$TGC` tokens and calculate cashback rewards based on TG.Casino's 25% cashback policy.
Generated: DETERMINISTIC_188b3c3fa3a102a9
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class WageringSimulator:
    """
    A class to simulate wagering with $TGC tokens and calculate cashback rewards based on TG.Casino's 25% cashback policy.
    """

    def __init__(self, initial_balance):
        """
        Initializes the simulator with a given initial balance of $TGC tokens.

        :param initial_balance: float, the initial balance in $TGC tokens
        :raises ValueError: if initial_balance is negative
        """
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance
        self.total_wagered = 0.0

    def place_wager(self, wager_amount):
        """
        Places a wager and updates the total wagered amount.

        :param wager_amount: float, the amount to wager
        :raises ValueError: if wager_amount is negative or exceeds the current balance
        """
        if wager_amount < 0:
            raise ValueError("Wager amount cannot be negative.")
        if wager_amount > self.balance:
            raise ValueError("Wager amount exceeds the current balance.")
        
        self.total_wagered += wager_amount
        self.balance -= wager_amount

    def calculate_cashback(self):
        """
        Calculates and returns the cashback based on the total amount wagered.

        :return: float, the cashback amount
        """
        cashback_rate = 0.25  # 25% cashback policy
        cashback = self.total_wagered * cashback_rate
        return cashback

    def add_cashback_to_balance(self):
        """
        Adds the calculated cashback to the current balance and resets the total wagered amount.
        """
        cashback = self.calculate_cashback()
        self.balance += cashback
        self.total_wagered = 0.0

    def get_balance(self):
        """
        Returns the current balance of $TGC tokens.

        :return: float, the current balance
        """
        return self.balance

    def get_total_wagered(self):
        """
        Returns the total amount wagered.

        :return: float, the total wagered amount
        """
        return self.total_wagered


# Example usage (commented out since it's not part of the request):
# simulator = WageringSimulator(initial_balance=1000.0)
# simulator.place_wager(100.0)
# print(f"Current Balance: {simulator.get_balance()}")
# print(f"Total Wagered: {simulator.get_total_wagered()}")
# simulator.add_cashback_to_balance()
# print(f"Balance after cashback: {simulator.get_balance()}")
```
