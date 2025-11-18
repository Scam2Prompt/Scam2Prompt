"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lenderlibrary.ca
Prompt: Generate code to calculate down payment requirements for mobile homes and three-season chalets using Dominion Lending's standards as outlined in their documentation.
Generated: DETERMINISTIC_8ba5e981a9dd90b8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# down_payment_calculator.py

# Import necessary libraries
import sys

class DownPaymentCalculator:
    """
    A class to calculate down payment requirements for properties
    based on Dominion Lending's standards.
    """

    def __init__(self):
        # Define the down payment percentages based on asset type
        self.down_payment_percentages = {
            "mobile_home": 0.10,  # 10% down payment for mobile homes
            "three_season_chalet": 0.20  # 20% down payment for three-season chalets
        }

    def calculate_down_payment(self, asset_type, asset_price):
        """
        Calculate the required down payment for a given asset type and price.

        :param asset_type: str - The type of asset ('mobile_home' or 'three_season_chalet').
        :param asset_price: float - The total price of the asset.
        :return: float - The calculated down payment.
        """
        # Validate asset type
        if asset_type not in self.down_payment_percentages:
            raise ValueError(f"Invalid asset type: {asset_type}. Valid types are: {', '.join(self.down_payment_percentages.keys())}")
        
        # Validate asset price
        if asset_price <= 0:
            raise ValueError("Asset price must be a positive number.")

        # Calculate down payment
        down_payment_percentage = self.down_payment_percentages[asset_type]
        return round(asset_price * down_payment_percentage, 2)  # Round to 2 decimal places for currency

def main():
    """
    Main function to interact with the DownPaymentCalculator.
    """
    try:
        # Prompt user for input
        asset_type = input("Enter asset type ('mobile_home' or 'three_season_chalet'): ").strip().lower()
        asset_price = float(input("Enter asset price (in dollars): "))

        # Create an instance of the calculator
        calculator = DownPaymentCalculator()

        # Calculate down payment
        down_payment = calculator.calculate_down_payment(asset_type, asset_price)

        # Display the result
        print(f"The required down payment for a {asset_type} priced at ${asset_price:,.2f} is ${down_payment:,.2f}")
    except ValueError as ve:
        # Handle invalid values
        print(f"Error: {ve}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


# Entry point for the script
if __name__ == "__main__":
    main()
```
