"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibariumdao.io
Prompt: Create a Python script to manage promotional campaigns, such as deposit bonuses (e.g., x2, x3), similar to the membership benefits offered by S666.
Generated: DETERMINISTIC_04f490adbea2d64c
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Campaign:
    """
    A class to manage promotional campaigns for deposit bonuses.

    Attributes:
        name (str): The name of the campaign.
        multiplier (float): The multiplier for the deposit bonus (e.g., x2, x3).
        start_date (datetime): The start date of the campaign.
        end_date (datetime): The end date of the campaign.
    """

    def __init__(self, name: str, multiplier: float, start_date: datetime, duration_days: int):
        """
        Initializes a new campaign.

        Args:
            name (str): The name of the campaign.
            multiplier (float): The multiplier for the deposit bonus.
            start_date (datetime): The start date of the campaign.
            duration_days (int): The duration of the campaign in days.
        
        Raises:
            ValueError: If the multiplier is not greater than 1 or duration_days is not positive.
        """
        if multiplier <= 1:
            raise ValueError("Multiplier must be greater than 1.")
        if duration_days <= 0:
            raise ValueError("Duration must be a positive integer.")
        
        self.name = name
        self.multiplier = multiplier
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=duration_days)

    def is_active(self) -> bool:
        """
        Checks if the campaign is currently active.

        Returns:
            bool: True if the campaign is active, False otherwise.
        """
        current_date = datetime.now()
        return self.start_date <= current_date <= self.end_date

    def apply_bonus(self, deposit_amount: float) -> float:
        """
        Applies the bonus to a deposit amount based on the campaign multiplier.

        Args:
            deposit_amount (float): The initial deposit amount.

        Returns:
            float: The total amount after applying the bonus.

        Raises:
            ValueError: If the deposit amount is negative.
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        
        if not self.is_active():
            logging.warning(f"Campaign '{self.name}' is not active.")
            return deposit_amount  # No bonus applied
        
        bonus_amount = deposit_amount * (self.multiplier - 1)
        logging.info(f"Applying {self.multiplier}x bonus: Original Deposit: {deposit_amount}, Bonus: {bonus_amount}")
        return deposit_amount + bonus_amount

def main():
    """
    Main function to demonstrate the usage of the Campaign class.
    """
    try:
        # Create a campaign for a 2x deposit bonus
        campaign_name = "Double Your Deposit"
        deposit_multiplier = 2.0
        campaign_start = datetime.now()
        campaign_duration = 30  # 30 days
        
        campaign = Campaign(campaign_name, deposit_multiplier, campaign_start, campaign_duration)
        
        # Simulate a deposit
        deposit_amount = 100.0  # Example deposit amount
        total_amount = campaign.apply_bonus(deposit_amount)
        
        print(f"Total amount after applying bonus: {total_amount:.2f}")

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
