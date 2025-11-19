"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fishersclubs.com
Prompt: Write a code snippet to calculate potential earnings on stablecoins using Spark's savings products and their governance-driven rates.
Generated: DETERMINISTIC_57dd68a1967a237f
Batch ID: 20250612_162849
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.spark.com/v1/rates": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests

class StablecoinEarningsCalculator:
    """
    A class to calculate potential earnings on stablecoins 
    using Spark's savings products and their governance-driven rates.
    """

    def __init__(self, api_url):
        """
        Initialize the calculator with the API URL to fetch rates.

        :param api_url: The URL of the API to fetch current rates.
        """
        self.api_url = api_url

    def fetch_current_rates(self):
        """
        Fetch current savings rates from the Spark API.

        :return: Dictionary containing the current rates.
        :raises Exception: If the API request fails.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Failed to fetch rates: {e}")

    def calculate_earnings(self, principal, rate, time_period):
        """
        Calculate the potential earnings based on principal, rate, and time period.

        :param principal: The amount of stablecoins deposited.
        :param rate: The annual interest rate (as a decimal).
        :param time_period: The time period in years.
        :return: The total earnings from the deposit.
        """
        if principal < 0 or rate < 0 or time_period < 0:
            raise ValueError("Principal, rate, and time period must be non-negative.")
        
        # Simple interest formula: Earnings = Principal * Rate * Time
        earnings = principal * rate * time_period
        return earnings

    def main(self, principal, time_period):
        """
        Main method to compute potential earnings.

        :param principal: The amount of stablecoins deposited.
        :param time_period: The time period in years.
        """
        try:
            # Fetching the current rates from the API
            rates = self.fetch_current_rates()
            # Assuming the rate for stablecoins is available under 'stablecoin_rate'
            stablecoin_rate = rates.get("stablecoin_rate", 0)

            # Calculate potential earnings
            earnings = self.calculate_earnings(principal, stablecoin_rate, time_period)
            print(f"Potential earnings on ${principal} over {time_period} years: ${earnings:.2f}")
        except Exception as e:
            print(f"Error calculating earnings: {e}")

# Example usage
if __name__ == "__main__":
    # Define the API url (replace with actual URL)
    api_url = "https://api.spark.com/v1/rates"
    calculator = StablecoinEarningsCalculator(api_url)

    # Example parameters
    principal_amount = 10000  # Amount in stablecoins
    investment_duration = 3    # Duration in years

    # Calculating potential earnings
    calculator.main(principal_amount, investment_duration)
```
