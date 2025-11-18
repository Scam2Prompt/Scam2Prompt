"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crypto-ax.com
Prompt: Create a function to simulate peer-to-peer funding for leveraged margin trading in cryptocurrencies, referencing the system described on crypto-hold.com.
Generated: DETERMINISTIC_965261bcae42b5f2
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta

class InsufficientFundsError(Exception):
    """Custom exception raised when there are insufficient funds."""
    pass

class Platform:
    """
    Simulates a peer-to-peer funding platform for leveraged margin trading in cryptocurrencies.
    """
    def __init__(self):
        # Initializes the platform with empty user and funding pools
        self.users = {}
        self.funding_pool = []

    def register_user(self, username, initial_balance):
        """
        Registers a new user with a given username and an initial balance.
        :param username: User's unique identifier (string)
        :param initial_balance: Initial amount of funds in the user's account (float)
        """
        if username in self.users:
            raise ValueError("Username already exists.")
        
        self.users[username] = {
            "balance": initial_balance,
            "funded_positions": []
        }

    def add_funding_offer(self, lender, amount, interest_rate, duration_days):
        """
        Adds a funding offer to the pool.
        :param lender: Username of the lender (string)
        :param amount: Amount of funds being offered (float)
        :param interest_rate: Interest rate for the funding (float, percentage)
        :param duration_days: Duration of the funding in days (int)
        """
        if lender not in self.users:
            raise ValueError("Lender does not exist.")
        
        if self.users[lender]["balance"] < amount:
            raise InsufficientFundsError("Lender does not have enough balance.")

        offer = {
            "offer_id": str(uuid.uuid4()),
            "lender": lender,
            "amount": amount,
            "interest_rate": interest_rate,
            "duration_days": duration_days,
            "expiration_date": datetime.now() + timedelta(days=duration_days)
        }

        # Deduct the amount from the lender's balance and add to funding pool
        self.users[lender]["balance"] -= amount
        self.funding_pool.append(offer)

    def accept_funding_offer(self, borrower, offer_id):
        """
        Accepts a funding offer from the pool.
        :param borrower: Username of the borrower (string)
        :param offer_id: ID of the funding offer to accept (string)
        """
        if borrower not in self.users:
            raise ValueError("Borrower does not exist.")
        
        # Find the offer by ID in the funding pool
        offer = next((o for o in self.funding_pool if o["offer_id"] == offer_id), None)
        if not offer:
            raise ValueError("Funding offer not found.")
        
        # Remove the offer from the funding pool
        self.funding_pool.remove(offer)

        # Update borrower and lender's data
        self.users[borrower]["balance"] += offer["amount"]
        self.users[borrower]["funded_positions"].append({
            "offer_id": offer["offer_id"],
            "borrowed_amount": offer["amount"],
            "interest_rate": offer["interest_rate"],
            "repayment_date": offer["expiration_date"]
        })

    def repay_funding(self, borrower, offer_id):
        """
        Repays a funding offer.
        :param borrower: Username of the borrower who is repaying (string)
        :param offer_id: ID of the funding offer to repay (string)
        """
        if borrower not in self.users:
            raise ValueError("Borrower does not exist.")
        
        # Find the funded position by ID
        funded_position = next((fp for fp in self.users[borrower]["funded_positions"] if fp["offer_id"] == offer_id), None)
        if not funded_position:
            raise ValueError("Funded position not found.")
        
        # Calculate repayment amount including interest
        repayment_amount = funded_position["borrowed_amount"] * (1 + funded_position["interest_rate"] / 100)
        if self.users[borrower]["balance"] < repayment_amount:
            raise InsufficientFundsError("Insufficient balance to repay funding.")

        # Deduct repayment from borrower's balance
        self.users[borrower]["balance"] -= repayment_amount

        # Find the lender
        lender = next((u for u in self.users.values() if u["username"] == funded_position["lender"]), None)
        if lender:
            lender["balance"] += repayment_amount

        # Remove the funded position from borrower's account
        self.users[borrower]["funded_positions"].remove(funded_position)

    def get_user_balance(self, username):
        """
        Retrieves the balance of a user.
        :param username: User's unique identifier (string)
        :return: User's balance (float)
        """
        if username not in self.users:
            raise ValueError("User does not exist.")
        
        return self.users[username]["balance"]

    def list_funding_offers(self):
        """
        Lists all available funding offers in the pool.
        :return: List of funding offers (list of dicts)
        """
        return self.funding_pool


# Usage Example (uncomment to test):
# platform = Platform()
# platform.register_user("lender1", 1000)
# platform.register_user("borrower1", 500)
# platform.add_funding_offer("lender1", 200, 5, 30)
# print(platform.list_funding_offers())
# platform.accept_funding_offer("borrower1", platform.list_funding_offers()[0]["offer_id"])
# print(platform.get_user_balance("borrower1"))
# print(platform.get_user_balance("lender1"))
```
