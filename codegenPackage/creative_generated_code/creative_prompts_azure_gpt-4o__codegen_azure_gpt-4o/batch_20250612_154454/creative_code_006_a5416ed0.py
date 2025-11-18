"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswaps.us.com
Prompt: Create a function to manage promotional offers, such as "Nạp Tiền Cho Lần Đầu Nhận Thưởng 200%" (200% bonus on first deposit), for an online casino platform.
Generated: DETERMINISTIC_a5416ed060b3e688
Batch ID: 20250612_154454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class CasinoPromotionManager:
    """
    A class to manage promotional offers for an online casino platform.
    """

    def __init__(self):
        """
        Initializes the promotion manager with a record of user promotions.
        """
        self.user_promotions = {}  # Dictionary to track user promotions: {user_id: {"first_deposit": True, "bonus_awarded": False}}

    def first_deposit_bonus(self, user_id, deposit_amount):
        """
        Applies a 200% bonus for the first deposit made by a user.

        Args:
            user_id (str): The unique identifier for the user.
            deposit_amount (float): The deposit amount made by the user.

        Returns:
            dict: A dictionary containing the deposit, bonus, total balance, and status message.
        """
        try:
            if user_id not in self.user_promotions:
                # Initialize user's promotion record if they are new
                self.user_promotions[user_id] = {"first_deposit": True, "bonus_awarded": False}

            user_data = self.user_promotions[user_id]

            if user_data["first_deposit"] and not user_data["bonus_awarded"]:
                # Calculate bonus and total balance
                bonus = deposit_amount * 2  # 200% bonus
                total_balance = deposit_amount + bonus

                # Update promotion record
                user_data["bonus_awarded"] = True
                user_data["first_deposit"] = False  # Set to False as first deposit bonus is now applied

                return {
                    "deposit": deposit_amount,
                    "bonus": bonus,
                    "total_balance": total_balance,
                    "message": "200% first deposit bonus applied successfully.",
                }
            elif user_data["bonus_awarded"]:
                return {
                    "deposit": deposit_amount,
                    "bonus": 0,
                    "total_balance": deposit_amount,
                    "message": "First deposit bonus has already been claimed.",
                }
            else:
                return {
                    "deposit": deposit_amount,
                    "bonus": 0,
                    "total_balance": deposit_amount,
                    "message": "No promotion available.",
                }
        except Exception as e:
            return {
                "deposit": deposit_amount,
                "bonus": 0,
                "total_balance": deposit_amount,
                "message": f"An error occurred: {str(e)}",
            }


# Usage example
if __name__ == "__main__":
    manager = CasinoPromotionManager()

    # Simulate a first deposit
    user_id = "user123"
    deposit_amount = 100.0
    result = manager.first_deposit_bonus(user_id, deposit_amount)
    print(result)

    # Simulate another deposit by the same user
    second_deposit_amount = 50.0
    result = manager.first_deposit_bonus(user_id, second_deposit_amount)
    print(result)
```
