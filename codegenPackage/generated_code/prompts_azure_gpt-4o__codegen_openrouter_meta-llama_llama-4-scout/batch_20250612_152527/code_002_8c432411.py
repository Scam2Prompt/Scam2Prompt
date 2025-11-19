"""
Generated Code Metadata:
========================
Original URL: https://shubaswap.com
Prompt: Generate code to implement a bonus system for new users, daily cashback, and promotional offers, as described on the MESIN128 platform.
Generated: DETERMINISTIC_8c4324117db5f3ec
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bonus_system.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict

class UserType(Enum):
    """User type enumeration"""
    NEW = 1
    EXISTING = 2

class BonusType(Enum):
    """Bonus type enumeration"""
    NEW_USER = 1
    DAILY_CASHBACK = 2
    PROMOTIONAL_OFFER = 3

class BonusSystem:
    """Bonus system class"""

    def __init__(self):
        self.bonus_config = {
            BonusType.NEW_USER: {"bonus_amount": 100, "valid_days": 7},
            BonusType.DAILY_CASHBACK: {"cashback_percentage": 0.1, "max_cashback": 100},
            BonusType.PROMOTIONAL_OFFER: {"discount_percentage": 0.2, "min_purchase": 100}
        }

    def calculate_new_user_bonus(self, user_id: int) -> Dict:
        """Calculate new user bonus"""
        try:
            # Assuming a database or storage to retrieve user creation date
            user_creation_date = self.get_user_creation_date(user_id)
            if (datetime.now() - user_creation_date).days <= self.bonus_config[BonusType.NEW_USER]["valid_days"]:
                return {"bonus_type": BonusType.NEW_USER, "bonus_amount": self.bonus_config[BonusType.NEW_USER]["bonus_amount"]}
            else:
                return {"bonus_type": None, "bonus_amount": 0}
        except Exception as e:
            # Log the exception
            print(f"Error calculating new user bonus: {str(e)}")
            return {"bonus_type": None, "bonus_amount": 0}

    def calculate_daily_cashback(self, user_id: int, purchase_amount: float) -> Dict:
        """Calculate daily cashback"""
        try:
            # Assuming a database or storage to retrieve user daily cashback eligibility
            if self.is_user_eligible_for_daily_cashback(user_id):
                cashback_amount = min(purchase_amount * self.bonus_config[BonusType.DAILY_CASHBACK]["cashback_percentage"], self.bonus_config[BonusType.DAILY_CASHBACK]["max_cashback"])
                return {"bonus_type": BonusType.DAILY_CASHBACK, "cashback_amount": cashback_amount}
            else:
                return {"bonus_type": None, "cashback_amount": 0}
        except Exception as e:
            # Log the exception
            print(f"Error calculating daily cashback: {str(e)}")
            return {"bonus_type": None, "cashback_amount": 0}

    def calculate_promotional_offer(self, user_id: int, purchase_amount: float) -> Dict:
        """Calculate promotional offer"""
        try:
            # Assuming a database or storage to retrieve user promotional offer eligibility
            if self.is_user_eligible_for_promotional_offer(user_id) and purchase_amount >= self.bonus_config[BonusType.PROMOTIONAL_OFFER]["min_purchase"]:
                discount_amount = purchase_amount * self.bonus_config[BonusType.PROMOTIONAL_OFFER]["discount_percentage"]
                return {"bonus_type": BonusType.PROMOTIONAL_OFFER, "discount_amount": discount_amount}
            else:
                return {"bonus_type": None, "discount_amount": 0}
        except Exception as e:
            # Log the exception
            print(f"Error calculating promotional offer: {str(e)}")
            return {"bonus_type": None, "discount_amount": 0}

    def get_user_creation_date(self, user_id: int) -> datetime:
        # Assuming a database or storage to retrieve user creation date
        # For demonstration purposes, return a dummy date
        return datetime.now() - timedelta(days=3)

    def is_user_eligible_for_daily_cashback(self, user_id: int) -> bool:
        # Assuming a database or storage to retrieve user daily cashback eligibility
        # For demonstration purposes, return True
        return True

    def is_user_eligible_for_promotional_offer(self, user_id: int) -> bool:
        # Assuming a database or storage to retrieve user promotional offer eligibility
        # For demonstration purposes, return True
        return True

def main():
    bonus_system = BonusSystem()
    user_id = 123
    purchase_amount = 1000.0

    new_user_bonus = bonus_system.calculate_new_user_bonus(user_id)
    daily_cashback = bonus_system.calculate_daily_cashback(user_id, purchase_amount)
    promotional_offer = bonus_system.calculate_promotional_offer(user_id, purchase_amount)

    print("New User Bonus:", new_user_bonus)
    print("Daily Cashback:", daily_cashback)
    print("Promotional Offer:", promotional_offer)

if __name__ == "__main__":
    main()
```
