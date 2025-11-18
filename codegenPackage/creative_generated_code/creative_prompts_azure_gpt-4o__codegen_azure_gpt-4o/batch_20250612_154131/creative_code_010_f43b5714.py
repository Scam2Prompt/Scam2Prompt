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

class ArkVentureFund:
    """
    Class to model quarterly liquidity windows for ARK Venture Fund investors.
    Ensures compliance with the fund's redemption policy.
    """

    def __init__(self, redemption_policy: Dict[str, int]):
        """
        Initialize the fund with its redemption policy.

        :param redemption_policy: A dictionary containing redemption policy rules.
                                  Keys should be 'minimum_hold_period' (in months)
                                  and 'maximum_redemption_percentage'.
        """
        self.redemption_policy = redemption_policy
        self.investor_data = {}

    def add_investor(self, investor_id: str, investment_date: datetime.date, investment_amount: float):
        """
        Adds an investor to the fund.

        :param investor_id: Unique identifier for the investor.
        :param investment_date: Date of initial investment.
        :param investment_amount: Amount invested in the fund.
        """
        self.investor_data[investor_id] = {
            'investment_date': investment_date,
            'investment_amount': investment_amount,
            'redemption_requests': []
        }

    def request_redemption(self, investor_id: str, request_date: datetime.date, requested_amount: float) -> bool:
        """
        Handles a redemption request from an investor.

        :param investor_id: Unique identifier for the investor.
        :param request_date: Date of redemption request.
        :param requested_amount: Amount requested for redemption.
        :return: True if redemption is approved, False otherwise.
        """
        if investor_id not in self.investor_data:
            print(f"Error: Investor {investor_id} does not exist.")
            return False

        investor = self.investor_data[investor_id]
        investment_date = investor['investment_date']
        investment_amount = investor['investment_amount']

        # Calculate the holding period in months
        holding_period = (request_date.year - investment_date.year) * 12 + (request_date.month - investment_date.month)

        # Check compliance with the minimum hold period
        if holding_period < self.redemption_policy['minimum_hold_period']:
            print(f"Redemption denied: Investor {investor_id} has only held investment for {holding_period} months, "
                  f"which is less than the required {self.redemption_policy['minimum_hold_period']} months.")
            return False

        # Check compliance with the maximum redemption percentage
        max_redemption = investment_amount * (self.redemption_policy['maximum_redemption_percentage'] / 100)
        if requested_amount > max_redemption:
            print(f"Redemption denied: Requested amount ${requested_amount:.2f} exceeds maximum allowed redemption "
                  f"of ${max_redemption:.2f} for investor {investor_id}.")
            return False

        # Redemption approved
        investor['redemption_requests'].append({
            'request_date': request_date,
            'requested_amount': requested_amount
        })
        print(f"Redemption approved for investor {investor_id}: ${requested_amount:.2f}")
        return True

    def calculate_next_liquidity_window(self, current_date: datetime.date) -> datetime.date:
        """
        Calculates the next quarterly liquidity window based on the current date.

        :param current_date: The date from which the next liquidity window is calculated.
        :return: Date of the next quarterly liquidity window.
        """
        current_month = current_date.month
        next_quarter_month = ((current_month - 1) // 3 + 1) * 3 + 1
        next_quarter_year = current_date.year if next_quarter_month <= 12 else current_date.year + 1
        next_quarter_month = next_quarter_month if next_quarter_month <= 12 else next_quarter_month - 12

        return datetime.date(next_quarter_year, next_quarter_month, 1)

    def get_investor_redemption_summary(self, investor_id: str) -> Dict:
        """
        Provides a summary of redemption requests for a given investor.

        :param investor_id: Unique identifier for the investor.
        :return: Dictionary containing redemption history.
        """
        if investor_id not in self.investor_data:
            print(f"Error: Investor {investor_id} does not exist.")
            return {}

        return {
            'investment_date': self.investor_data[investor_id]['investment_date'],
            'investment_amount': self.investor_data[investor_id]['investment_amount'],
            'redemption_requests': self.investor_data[investor_id]['redemption_requests']
        }


# Usage example
if __name__ == "__main__":
    # Define redemption policy
    redemption_policy = {
        'minimum_hold_period': 12,  # Minimum hold period in months
        'maximum_redemption_percentage': 25  # Maximum redemption percentage
    }

    # Initialize fund
    ark_fund = ArkVentureFund(redemption_policy)

    # Add investor
    ark_fund.add_investor("INV123", datetime.date(2022, 1, 15), 100000)

    # Test redemption request
    ark_fund.request_redemption("INV123", datetime.date(2023, 1, 15), 20000)

    # Calculate next liquidity window
    next_window = ark_fund.calculate_next_liquidity_window(datetime.date(2023, 1, 15))
    print(f"Next liquidity window starts on: {next_window}")

    # Get investor redemption summary
    summary = ark_fund.get_investor_redemption_summary("INV123")
    print(f"Investor Redemption Summary: {summary}")
```
