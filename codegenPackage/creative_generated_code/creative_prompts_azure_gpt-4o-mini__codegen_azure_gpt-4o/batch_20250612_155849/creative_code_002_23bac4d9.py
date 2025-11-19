"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.xyz
Prompt: Create a script that implements a cashback system for losses in a casino environment, inspired by the loyalty programs mentioned on BaxBet.
Generated: DETERMINISTIC_23bac4d9fd2b9f27
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import Dict

class CasinoCashbackSystem:
    """
    A class to implement a cashback system for losses in a casino environment.
    """

    def __init__(self, cashback_percentage: float = 0.10):
        """
        Initializes the cashback system.
        
        :param cashback_percentage: Percentage of cashback on losses (default: 10%)
        """
        if not (0 <= cashback_percentage <= 1):
            raise ValueError("Cashback percentage should be between 0 and 1.")
        self.cashback_percentage = cashback_percentage
        self.user_data: Dict[str, Dict] = {}  # Stores user data such as losses, cashback, etc.

    def register_user(self, user_id: str):
        """
        Registers a new user in the system.
        
        :param user_id: Unique identifier for the user.
        """
        if user_id in self.user_data:
            raise ValueError("User is already registered.")
        
        self.user_data[user_id] = {
            "total_losses": 0.0,
            "cashback_earned": 0.0,
            "last_cashback_date": None
        }

    def record_loss(self, user_id: str, amount: float):
        """
        Records a loss for a user.
        
        :param user_id: Unique identifier for the user.
        :param amount: Amount lost by the user.
        """
        if user_id not in self.user_data:
            raise ValueError("User is not registered.")
        if amount < 0:
            raise ValueError("Loss amount cannot be negative.")
        
        self.user_data[user_id]["total_losses"] += amount

    def calculate_cashback(self, user_id: str) -> float:
        """
        Calculates the cashback amount for a user's losses.
        
        :param user_id: Unique identifier for the user.
        :return: Cashback amount based on the user's losses.
        """
        if user_id not in self.user_data:
            raise ValueError("User is not registered.")
        
        total_losses = self.user_data[user_id]["total_losses"]
        cashback = round(total_losses * self.cashback_percentage, 2)  # Rounded to 2 decimal places
        return cashback

    def issue_cashback(self, user_id: str) -> float:
        """
        Issues cashback to the user and resets their losses.
        
        :param user_id: Unique identifier for the user.
        :return: The issued cashback amount.
        """
        if user_id not in self.user_data:
            raise ValueError("User is not registered.")
        
        cashback = self.calculate_cashback(user_id)
        self.user_data[user_id]["cashback_earned"] += cashback
        self.user_data[user_id]["total_losses"] = 0.0  # Reset losses
        self.user_data[user_id]["last_cashback_date"] = datetime.datetime.now()  # Record cashback date
        
        return cashback

    def get_user_summary(self, user_id: str) -> Dict:
        """
        Retrieves a summary of a user's cashback and loss data.
        
        :param user_id: Unique identifier for the user.
        :return: A dictionary containing user's total losses, cashback earned, and last cashback date.
        """
        if user_id not in self.user_data:
            raise ValueError("User is not registered.")
        
        return {
            "total_losses": self.user_data[user_id]["total_losses"],
            "cashback_earned": self.user_data[user_id]["cashback_earned"],
            "last_cashback_date": self.user_data[user_id]["last_cashback_date"]
        }


# Example usage (uncomment to test):
# if __name__ == "__main__":
#     system = CasinoCashbackSystem(cashback_percentage=0.1)
#     system.register_user("user123")
#     system.record_loss("user123", 100.0)
#     print(system.calculate_cashback("user123"))  # Expected: 10.0
#     print(system.issue_cashback("user123"))  # Expected: 10.0
#     print(system.get_user_summary("user123"))
```
