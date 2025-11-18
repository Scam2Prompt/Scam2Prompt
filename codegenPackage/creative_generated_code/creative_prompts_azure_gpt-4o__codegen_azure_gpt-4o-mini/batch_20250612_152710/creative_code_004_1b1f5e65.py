"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lootbotxyz.pages.dev
Prompt: Write a script in Python to calculate the total revenue share ($ETH) distributed to $xLOOT holders during the last epoch based on the data provided.
Generated: DETERMINISTIC_1b1f5e65152c414a
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class RevenueShareCalculator:
    def __init__(self, data: List[Dict[str, float]], total_revenue: float):
        """
        Initializes the RevenueShareCalculator with the provided data and total revenue.

        :param data: A list of dictionaries containing the distribution data for each $xLOOT holder.
                     Each dictionary should have 'holder' and 'amount' keys.
        :param total_revenue: The total revenue ($ETH) to be distributed among $xLOOT holders.
        """
        self.data = data
        self.total_revenue = total_revenue

    def validate_data(self):
        """
        Validates the input data to ensure it meets the expected structure.

        :raises ValueError: If the data is not structured correctly.
        """
        if not isinstance(self.data, list) or not isinstance(self.total_revenue, (int, float)):
            raise ValueError("Invalid input: data must be a list and total_revenue must be a number.")

        for entry in self.data:
            if not isinstance(entry, dict) or 'holder' not in entry or 'amount' not in entry:
                raise ValueError("Invalid entry in data: each entry must be a dictionary with 'holder' and 'amount'.")

    def calculate_shares(self) -> Dict[str, float]:
        """
        Calculates the revenue share for each $xLOOT holder based on their respective shares.

        :returns: A dictionary mapping each holder to their respective revenue share.
        """
        self.validate_data()

        total_shares = sum(holder['amount'] for holder in self.data)
        revenue_distribution = {}

        if total_shares == 0:
            raise ValueError("Total shares cannot be zero to avoid division by zero error.")

        for holder in self.data:
            # Calculate revenue share for the holder
            holder_amount = holder['amount']
            share = (holder_amount / total_shares) * self.total_revenue
            revenue_distribution[holder['holder']] = share

        return revenue_distribution

def main():
    # Example data input
    data_input = [
        {"holder": "0x12345", "amount": 100},
        {"holder": "0x67890", "amount": 200},
        {"holder": "0xabcde", "amount": 300}
    ]
    
    total_revenue_input = 6000.0  # Total ETH to be distributed

    # Create a RevenueShareCalculator instance
    calculator = RevenueShareCalculator(data=data_input, total_revenue=total_revenue_input)

    try:
        # Calculate and print the revenue shares
        shares = calculator.calculate_shares()
        print("Revenue shares distributed to $xLOOT holders:")
        for holder, share in shares.items():
            print(f"{holder}: {share:.2f} $ETH")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
