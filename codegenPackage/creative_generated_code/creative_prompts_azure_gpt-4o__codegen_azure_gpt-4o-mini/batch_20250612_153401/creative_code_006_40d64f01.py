"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gemcaster.vercel.app
Prompt: Create a function to calculate the total Zora fees in ETH for collecting multiple casts on Gemcaster.
Generated: DETERMINISTIC_40d64f01c2444136
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any

class ZoraFeeCalculator:
    def __init__(self, fee_percentage: float):
        """
        Initialize the ZoraFeeCalculator with a specified fee percentage.
        
        :param fee_percentage: The fee percentage to be applied on the total value of casts.
        """
        if not (0 <= fee_percentage <= 100):
            raise ValueError("Fee percentage must be between 0 and 100.")
        self.fee_percentage = fee_percentage

    def calculate_total_fees(self, casts: List[Dict[str, Any]]) -> float:
        """
        Calculate the total Zora fees in ETH for the given list of casts.

        :param casts: A list of dictionaries, each containing the 'value' of the cast in ETH.
        :return: Total Zora fees in ETH.
        """
        if not casts:
            raise ValueError("The list of casts cannot be empty.")

        total_value = 0.0

        for cast in casts:
            if 'value' not in cast:
                raise KeyError("Each cast must have a 'value' key.")
            if not isinstance(cast['value'], (int, float)):
                raise TypeError("The 'value' must be a numeric type.")
            total_value += float(cast['value'])

        # Calculate the total fees based on the total value of casts
        total_fees = (self.fee_percentage / 100) * total_value
        return total_fees

# Example usage
if __name__ == "__main__":
    try:
        fee_calculator = ZoraFeeCalculator(fee_percentage=5.0)  # 5% fee
        casts_data = [
            {'value': 0.1},
            {'value': 0.2},
            {'value': 0.15}
        ]
        total_fees = fee_calculator.calculate_total_fees(casts_data)
        print(f"Total Zora fees in ETH: {total_fees}")
    except (ValueError, KeyError, TypeError) as e:
        print(f"Error: {e}")
```
