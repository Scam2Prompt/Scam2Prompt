"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocols.web.app
Prompt: Create a Python script to calculate the expected ROI for CRUDO token holders based on the presale price, listing price, and projected growth rates.
Generated: DETERMINISTIC_17c7d3a01be1ac32
Batch ID: 20250612_150435
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Tuple

class CRUDOInvestment:
    def __init__(self, presale_price: float, listing_price: float, growth_rates: List[float]):
        """
        Initializes the CRUDOInvestment class with presale price, listing price, and growth rates.

        :param presale_price: The price at which CRUDO tokens were purchased during presale.
        :param listing_price: The price at which CRUDO tokens are expected to list.
        :param growth_rates: A list of projected growth rates (as decimals) for future periods.
        """
        if presale_price <= 0 or listing_price <= 0:
            raise ValueError("Presale and listing prices must be greater than zero.")
        
        self.presale_price = presale_price
        self.listing_price = listing_price
        self.growth_rates = growth_rates

    def calculate_roi(self) -> float:
        """
        Calculates the expected ROI based on the presale price and projected growth.

        :return: The expected ROI as a percentage.
        """
        # Calculate initial ROI based on the listing price
        initial_roi = (self.listing_price - self.presale_price) / self.presale_price * 100

        # Apply projected growth rates to calculate the overall ROI
        projected_value = self.listing_price
        for rate in self.growth_rates:
            if rate < 0:
                raise ValueError("Growth rates must be non-negative.")
            projected_value *= (1 + rate)

        # Final ROI calculation
        final_roi = (projected_value - self.presale_price) / self.presale_price * 100
        return final_roi

def main():
    try:
        # Define presale price, listing price, and growth rates
        presale_price = 0.50  # Example presale price in USD
        listing_price = 1.00   # Example listing price in USD
        growth_rates = [0.10, 0.15, 0.20]  # Example growth rates for the next three years

        # Create an instance of CRUDOInvestment
        investment = CRUDOInvestment(presale_price, listing_price, growth_rates)
        
        # Calculate and display the expected ROI
        expected_roi = investment.calculate_roi()
        print(f"Expected ROI: {expected_roi:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
