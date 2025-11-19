"""
Generated Code Metadata:
========================
Original URL: https://betpandaofficial.com
Prompt: Provide a code example for implementing a cashback system for losses in a casino application, reflecting the promotions offered by Betpanda.
Generated: DETERMINISTIC_498a697579dccc53
Batch ID: 20250612_161301
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cashback_system.py

from datetime import datetime, timedelta
from typing import Dict

class CashbackSystem:
    """
    A class representing a cashback system for losses in a casino application.

    Attributes:
    ----------
    promotions (Dict[str, float]): A dictionary of promotions offered by Betpanda.
    """

    def __init__(self, promotions: Dict[str, float]):
        """
        Initializes the CashbackSystem class.

        Args:
        ----
        promotions (Dict[str, float]): A dictionary of promotions offered by Betpanda.
        """
        self.promotions = promotions

    def calculate_cashback(self, user_id: int, loss_amount: float, promotion_name: str) -> float:
        """
        Calculates the cashback amount for a user's loss.

        Args:
        ----
        user_id (int): The ID of the user.
        loss_amount (float): The amount of loss.
        promotion_name (str): The name of the promotion.

        Returns:
        -------
        float: The cashback amount.

        Raises:
        ------
        ValueError: If the promotion name is not found.
        """
        if promotion_name not in self.promotions:
            raise ValueError("Promotion not found")

        cashback_percentage = self.promotions[promotion_name]
        cashback_amount = loss_amount * (cashback_percentage / 100)
        return cashback_amount

    def is_eligible_for_cashback(self, user_id: int, promotion_name: str, last_cashback_date: datetime) -> bool:
        """
        Checks if a user is eligible for cashback.

        Args:
        ----
        user_id (int): The ID of the user.
        promotion_name (str): The name of the promotion.
        last_cashback_date (datetime): The date of the last cashback.

        Returns:
        -------
        bool: True if the user is eligible, False otherwise.
        """
        # Assuming a 24-hour cooldown period for cashback
        cooldown_period = timedelta(hours=24)
        return (datetime.now() - last_cashback_date) > cooldown_period

    def process_cashback(self, user_id: int, loss_amount: float, promotion_name: str, last_cashback_date: datetime) -> Dict[str, float]:
        """
        Processes a cashback request.

        Args:
        ----
        user_id (int): The ID of the user.
        loss_amount (float): The amount of loss.
        promotion_name (str): The name of the promotion.
        last_cashback_date (datetime): The date of the last cashback.

        Returns:
        -------
        Dict[str, float]: A dictionary containing the cashback amount and a success flag.

        Raises:
        ------
        ValueError: If the promotion name is not found.
        """
        if not self.is_eligible_for_cashback(user_id, promotion_name, last_cashback_date):
            raise ValueError("User is not eligible for cashback")

        try:
            cashback_amount = self.calculate_cashback(user_id, loss_amount, promotion_name)
            return {"cashback_amount": cashback_amount, "success": True}
        except ValueError as e:
            return {"error": str(e), "success": False}


def main():
    # Example usage
    promotions = {
        "Betpanda Bronze": 5.0,
        "Betpanda Silver": 10.0,
        "Betpanda Gold": 15.0
    }

    cashback_system = CashbackSystem(promotions)

    user_id = 12345
    loss_amount = 100.0
    promotion_name = "Betpanda Silver"
    last_cashback_date = datetime.now() - timedelta(hours=48)

    try:
        result = cashback_system.process_cashback(user_id, loss_amount, promotion_name, last_cashback_date)
        print(result)
    except ValueError as e:
        print({"error": str(e)})


if __name__ == "__main__":
    main()
```
