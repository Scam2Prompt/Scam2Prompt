"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventureshares.com
Prompt: Create a script to model the quarterly liquidity windows for ARK Venture Fund investors, ensuring compliance with the fund's redemption policy.
Generated: DETERMINISTIC_f43b57148a89df56
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class ARKVentureFund:
    def __init__(self, redemption_window_days: int):
        """
        Initializes the ARK Venture Fund with a specified redemption window.
        
        :param redemption_window_days: Number of days investors must wait to redeem their investments.
        """
        self.redemption_window_days = redemption_window_days
        self.investors = {}  # Dictionary to hold investor information

    def add_investor(self, investor_id: str, investment_date: datetime.date):
        """
        Adds an investor to the fund with their investment date.
        
        :param investor_id: Unique identifier for the investor.
        :param investment_date: The date the investor made their investment.
        """
        if investor_id in self.investors:
            raise ValueError("Investor ID already exists.")
        
        self.investors[investor_id] = investment_date

    def calculate_redemption_window(self, investor_id: str) -> Dict[str, datetime.date]:
        """
        Calculates the redemption window for a given investor.
        
        :param investor_id: Unique identifier for the investor.
        :return: A dictionary containing the start and end dates of the redemption window.
        """
        if investor_id not in self.investors:
            raise KeyError("Investor not found.")
        
        investment_date = self.investors[investor_id]
        redemption_start = investment_date + datetime.timedelta(days=self.redemption_window_days)
        
        # The redemption window is open for 30 days after the start date
        redemption_end = redemption_start + datetime.timedelta(days=30)

        return {
            'redemption_start': redemption_start,
            'redemption_end': redemption_end
        }

    def is_redemption_allowed(self, investor_id: str, current_date: datetime.date) -> bool:
        """
        Checks if an investor is allowed to redeem their investment based on today's date.
        
        :param investor_id: Unique identifier for the investor.
        :param current_date: The current date to check against the redemption window.
        :return: True if redemption is allowed, False otherwise.
        """
        redemption_window = self.calculate_redemption_window(investor_id)
        return redemption_window['redemption_start'] <= current_date <= redemption_window['redemption_end']


# Example usage
if __name__ == "__main__":
    try:
        fund = ARKVentureFund(redemption_window_days=90)
        fund.add_investor("INV123", datetime.date(2023, 1, 1))
        
        current_date = datetime.date(2023, 4, 1)  # Example current date
        redemption_window = fund.calculate_redemption_window("INV123")
        print(f"Redemption Window: {redemption_window}")
        
        can_redeem = fund.is_redemption_allowed("INV123", current_date)
        print(f"Can investor redeem on {current_date}? {'Yes' if can_redeem else 'No'}")
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
