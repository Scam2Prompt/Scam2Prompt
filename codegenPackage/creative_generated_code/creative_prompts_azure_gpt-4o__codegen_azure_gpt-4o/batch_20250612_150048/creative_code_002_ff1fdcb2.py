"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://profittradeplatform.com.guaranteetrades247.com
Prompt: Create a script to calculate trading interest rates for crypto assets based on tiered loyalty plans (e.g., Starter Plan, Basic Plan, Premium Plan) as described on Profit Trade Platform.
Generated: DETERMINISTIC_ff1fdcb252c0f79f
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LoyaltyPlan:
    """
    A class to represent a loyalty plan with tiered interest rates for trading crypto assets.
    """
    def __init__(self, name, interest_rates):
        """
        Initialize a LoyaltyPlan.

        :param name: Name of the plan (e.g., Starter, Basic, Premium)
        :param interest_rates: Dictionary mapping asset names to their interest rates
        """
        self.name = name
        self.interest_rates = interest_rates

    def get_interest_rate(self, asset):
        """
        Retrieve the interest rate for a specific crypto asset.

        :param asset: The name of the crypto asset
        :return: Interest rate for the asset or None if not found
        """
        return self.interest_rates.get(asset, None)

class TradingInterestRateCalculator:
    """
    A class responsible for calculating trading interest rates based on loyalty plans.
    """
    def __init__(self):
        """
        Initialize the calculator with pre-defined loyalty plans.
        """
        self.loyalty_plans = {
            'Starter': LoyaltyPlan('Starter', {'BTC': 0.01, 'ETH': 0.015, 'ADA': 0.02}),
            'Basic': LoyaltyPlan('Basic', {'BTC': 0.02, 'ETH': 0.025, 'ADA': 0.03}),
            'Premium': LoyaltyPlan('Premium', {'BTC': 0.03, 'ETH': 0.035, 'ADA': 0.04})
        }

    def calculate_interest(self, plan_name, asset_name, trading_amount):
        """
        Calculate the interest for a given asset trading amount based on the loyalty plan.

        :param plan_name: Name of the loyalty plan (e.g., Starter, Basic, Premium)
        :param asset_name: Name of the crypto asset (e.g., BTC, ETH, ADA)
        :param trading_amount: The trading amount in numeric form
        :return: Calculated interest amount or None if input is invalid
        """
        try:
            loyalty_plan = self.loyalty_plans.get(plan_name)
            if not loyalty_plan:
                logging.error(f"Loyalty plan '{plan_name}' is not found.")
                return None

            interest_rate = loyalty_plan.get_interest_rate(asset_name)
            if interest_rate is None:
                logging.error(f"Asset '{asset_name}' is not available in the '{plan_name}' plan.")
                return None

            if trading_amount <= 0:
                logging.error("Trading amount must be greater than zero.")
                return None

            interest_amount = trading_amount * interest_rate
            logging.info(f"Interest calculated: {interest_amount} for {trading_amount} {asset_name} on {plan_name} plan.")
            return interest_amount
        except Exception as e:
            logging.error(f"An unexpected error occurred: {str(e)}")
            return None

# Example usage
if __name__ == '__main__':
    calculator = TradingInterestRateCalculator()

    # User input for demonstration
    plan_name = 'Premium'
    asset_name = 'BTC'
    trading_amount = 1000

    # Calculate interest
    interest = calculator.calculate_interest(plan_name, asset_name, trading_amount)
    if interest is not None:
        print(f"Interest for {trading_amount} {asset_name} on {plan_name} plan: {interest}")
    else:
        print("Failed to calculate interest.")
```
