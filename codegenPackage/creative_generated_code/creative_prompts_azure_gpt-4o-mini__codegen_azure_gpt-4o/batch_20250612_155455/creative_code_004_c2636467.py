"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-dashboard.pages.dev
Prompt: How does the Crypto All-Stars presale work, and what advantages do early buyers have in terms of staking rewards?
Generated: DETERMINISTIC_c26364677e9d5186
Batch ID: 20250612_155455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python code example that simulates how a Crypto All-Stars presale might work, focusing on the advantages early buyers gain in terms of staking rewards. This code includes comments and error handling, and follows best practices for readability and maintainability.

```python
import datetime

class CryptoAllStarsPresale:
    """
    A class to represent the Crypto All-Stars presale.
    Early buyers receive higher staking rewards as incentives.
    """
    def __init__(self, presale_start, presale_end):
        """
        Initialize the presale with start and end dates.
        
        Args:
            presale_start (datetime): Start date of the presale.
            presale_end (datetime): End date of the presale.
        """
        if presale_start >= presale_end:
            raise ValueError("Presale start date must be earlier than presale end date.")
        self.presale_start = presale_start
        self.presale_end = presale_end
        self.buyers = {}  # Stores buyer addresses and purchase details
    
    def buy_tokens(self, buyer_address, amount):
        """
        Allows buyers to purchase tokens during the presale.
        
        Args:
            buyer_address (str): Wallet address of the buyer.
            amount (float): Amount of tokens purchased.
        
        Returns:
            str: Confirmation message.
        """
        current_time = datetime.datetime.now()
        if not self.presale_start <= current_time <= self.presale_end:
            return "The presale is not active. Please check the presale dates."
        
        if amount <= 0:
            return "Amount must be greater than zero."
        
        # Record the purchase along with the timestamp
        self.buyers[buyer_address] = {
            "amount": amount,
            "purchase_time": current_time
        }
        return f"Purchase successful! {amount} tokens bought by {buyer_address}."
    
    def calculate_staking_rewards(self, buyer_address):
        """
        Calculates staking rewards for a given buyer based on their purchase time.
        Early buyers receive higher rewards.
        
        Args:
            buyer_address (str): Wallet address of the buyer.
        
        Returns:
            float: Staking rewards multiplier.
        """
        buyer = self.buyers.get(buyer_address)
        if not buyer:
            raise ValueError("Buyer not found. Please check the wallet address.")
        
        purchase_time = buyer["purchase_time"]
        purchase_day = (purchase_time - self.presale_start).days + 1
        
        # Early buyers (e.g., Day 1) get the highest reward multiplier
        if purchase_day <= 5:
            return 2.0  # 2x rewards for purchases in the first 5 days
        elif purchase_day <= 10:
            return 1.5  # 1.5x rewards for purchases between Day 6 and Day 10
        else:
            return 1.0  # Regular rewards for purchases after Day 10
    
    def get_buyer_summary(self, buyer_address):
        """
        Provides a summary of the buyer's purchase and staking rewards.

        Args:
            buyer_address (str): Wallet address of the buyer.
        
        Returns:
            dict: Summary containing amount and staking rewards.
        """
        buyer = self.buyers.get(buyer_address)
        if not buyer:
            raise ValueError("Buyer not found. Please check the wallet address.")
        
        reward_multiplier = self.calculate_staking_rewards(buyer_address)
        return {
            "wallet_address": buyer_address,
            "amount_purchased": buyer["amount"],
            "staking_rewards_multiplier": reward_multiplier
        }

# Example usage:
if __name__ == "__main__":
    presale_start_date = datetime.datetime(2023, 10, 1, 0, 0, 0)  # Presale starts on October 1, 2023
    presale_end_date = datetime.datetime(2023, 10, 15, 23, 59, 59)  # Presale ends on October 15, 2023
    
    presale = CryptoAllStarsPresale(presale_start_date, presale_end_date)
    
    try:
        # Simulate some purchases
        print(presale.buy_tokens("0xABC123", 100))
        print(presale.buy_tokens("0xDEF456", 250))
        
        # Get buyer summary
        buyer_summary = presale.get_buyer_summary("0xABC123")
        print("Buyer Summary:", buyer_summary)
        
    except ValueError as e:
        print("Error:", e)
```

This code snippet is syntactically correct, runnable, and includes error handling to handle invalid inputs or situations where the presale is inactive. It also demonstrates the advantage early buyers get in terms of staking reward multipliers.
