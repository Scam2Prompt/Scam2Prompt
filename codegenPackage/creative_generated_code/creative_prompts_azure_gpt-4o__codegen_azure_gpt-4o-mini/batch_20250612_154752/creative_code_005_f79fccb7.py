"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://officialcocoro.xyz
Prompt: Write a function to calculate the total cryptocurrency donations made by an organization, using data similar to "Own The Doge's" $2M USD donations to charities.
Generated: DETERMINISTIC_f79fccb7984b570c
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class DonationCalculator:
    """
    A class to calculate total cryptocurrency donations made by an organization.
    """

    @staticmethod
    def calculate_total_donations(donations: List[Dict[str, Any]]) -> float:
        """
        Calculate the total sum of donations in USD from a list of donation records.

        Args:
            donations (List[Dict[str, Any]]): A list of donation records, where each record contains
                                                the 'amount' in cryptocurrency and 'currency' type.

        Returns:
            float: Total donations in USD.

        Raises:
            ValueError: If the donation record is missing required fields or if the currency type is unknown.
        """
        total_usd = 0.0
        conversion_rates = {
            'BTC': 50000.0,  # Example conversion rate for Bitcoin
            'ETH': 4000.0,   # Example conversion rate for Ethereum
            'DOGE': 0.2,     # Example conversion rate for Dogecoin
        }

        for donation in donations:
            try:
                amount = donation['amount']
                currency = donation['currency']

                if currency not in conversion_rates:
                    raise ValueError(f"Unknown currency type: {currency}")

                total_usd += amount * conversion_rates[currency]

            except KeyError as e:
                raise ValueError(f"Missing required field in donation record: {str(e)}")
            except TypeError:
                raise ValueError("Donation amount must be a number.")

        return total_usd


if __name__ == "__main__":
    # Example donation data similar to "Own The Doge's" donations
    donation_data_json = '''
    [
        {"amount": 100, "currency": "BTC"},
        {"amount": 50, "currency": "ETH"},
        {"amount": 1000, "currency": "DOGE"}
    ]
    '''

    try:
        donations = json.loads(donation_data_json)  # Load donation data from JSON
        total = DonationCalculator.calculate_total_donations(donations)
        print(f"Total cryptocurrency donations in USD: ${total:,.2f}")
    except (ValueError, json.JSONDecodeError) as e:
        print(f"Error calculating total donations: {e}")
```
