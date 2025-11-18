"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho.orgmorpho.org
Prompt: Write a script to calculate borrowing costs using Morpho's per-market interest rates and higher collateralization factors.
Generated: DETERMINISTIC_877fdc3d47f7649a
Batch ID: 20250612_154057
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.morpho.xyz/interest-rates": {
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

class BorrowingCostCalculator:
    """
    A class to calculate borrowing costs based on Morpho's per-market interest rates and collateralization factors.
    """

    def __init__(self, api_url):
        """
        Initializes the BorrowingCostCalculator with the given API URL.
        
        :param api_url: str - The URL of the Morpho API to fetch interest rates.
        """
        self.api_url = api_url

    def fetch_interest_rates(self):
        """
        Fetches the current interest rates from the Morpho API.

        :return: dict - A dictionary containing interest rates.
        :raises RuntimeError: If there is an error fetching interest rates.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Expecting a JSON response
        except requests.RequestException as e:
            raise RuntimeError(f"Error fetching interest rates: {e}")

    def calculate_borrowing_cost(self, principal, market_rate, collateralization_factor):
        """
        Calculates the total borrowing cost based on principal, market interest rate, and collateralization factor.

        :param principal: float - The amount to borrow.
        :param market_rate: float - The interest rate for the specific market (as a decimal).
        :param collateralization_factor: float - The collateralization factor as a multiplier (e.g., 1.2 for 120%).
        :return: float - The total cost of borrowing.
        """
        if principal <= 0:
            raise ValueError("Principal must be greater than zero.")
        if market_rate < 0:
            raise ValueError("Market rate cannot be negative.")
        if collateralization_factor <= 0:
            raise ValueError("Collateralization factor must be greater than zero.")

        # Calculate the total borrowing cost
        borrowing_cost = principal * market_rate * collateralization_factor
        return borrowing_cost

def main():
    # Set the API URL to fetch market interest rates
    api_url = "https://api.morpho.xyz/interest-rates"

    # Initialize the calculator
    calculator = BorrowingCostCalculator(api_url)

    try:
        # Fetch interest rates from Morpho API
        interest_rates = calculator.fetch_interest_rates()
        
        # Example values for principal, market rate, and collateralization factor
        principal = 1000.0  # Amount to borrow
        market_rate = interest_rates.get('example_market', 0.05)  # Default to 5% if not found
        collateralization_factor = 1.2  # 120% collateralization

        # Calculate the borrowing cost
        total_borrowing_cost = calculator.calculate_borrowing_cost(principal, market_rate, collateralization_factor)

        print(f"Total borrowing cost for ${principal} at market rate {market_rate} with collateralization factor {collateralization_factor} is: ${total_borrowing_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
