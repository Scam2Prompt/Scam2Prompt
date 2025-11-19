"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onedexlp.com
Prompt: Write a function that calculates the total liquidity and daily volume for a DEX, similar to the metrics provided by OneDex.
Generated: DETERMINISTIC_a884b7c656780ca7
Batch ID: 20250612_155125
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

class DexMetrics:
    """
    A class to calculate total liquidity and daily volume for a Decentralized Exchange (DEX).
    """

    def __init__(self):
        self.liquidity_data: List[Dict[str, float]] = []

    def add_liquidity(self, amount: float, timestamp: datetime.datetime):
        """
        Add liquidity data to the DEX.

        :param amount: The amount of liquidity added.
        :param timestamp: The time when the liquidity was added.
        """
        if amount < 0:
            raise ValueError("Liquidity amount cannot be negative.")
        
        self.liquidity_data.append({'amount': amount, 'timestamp': timestamp})

    def calculate_total_liquidity(self) -> float:
        """
        Calculate the total liquidity of the DEX.

        :return: The total liquidity amount.
        """
        total_liquidity = sum(entry['amount'] for entry in self.liquidity_data)
        return total_liquidity

    def calculate_daily_volume(self, date: datetime.date) -> float:
        """
        Calculate the total volume for a specific day.

        :param date: The date for which to calculate daily volume.
        :return: The total volume for that day.
        """
        daily_volume = 0.0
        start_of_day = datetime.datetime.combine(date, datetime.time.min)
        end_of_day = datetime.datetime.combine(date, datetime.time.max)

        for entry in self.liquidity_data:
            entry_time = entry['timestamp']
            if start_of_day <= entry_time <= end_of_day:
                daily_volume += entry['amount']

        return daily_volume

# Example usage:
if __name__ == "__main__":
    dex = DexMetrics()
    
    # Add some liquidity data
    try:
        dex.add_liquidity(100.0, datetime.datetime(2023, 10, 20, 10, 0))
        dex.add_liquidity(150.0, datetime.datetime(2023, 10, 20, 15, 0))
        dex.add_liquidity(200.0, datetime.datetime(2023, 10, 21, 10, 0))

        # Calculate total liquidity
        total_liquidity = dex.calculate_total_liquidity()
        print(f"Total Liquidity: {total_liquidity}")

        # Calculate daily volume for a specific date
        daily_volume = dex.calculate_daily_volume(datetime.date(2023, 10, 20))
        print(f"Daily Volume on 2023-10-20: {daily_volume}")

    except ValueError as e:
        print(f"Error: {e}")
```
