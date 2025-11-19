"""
Generated Code Metadata:
========================
Original URL: https://rapidcointrades.org
Prompt: Create a script to validate the investment amounts and profit percentages for each plan on RapidCoinTrades Market, ensuring that they comply with the company's rules and regulations.
Generated: DETERMINISTIC_e49efb7372cc325d
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rapid_coin_trades_validator.py

import logging

# Define company rules and regulations
class RapidCoinTradesRules:
    def __init__(self):
        self.min_investment_amount = 100.0  # Minimum investment amount in USD
        self.max_investment_amount = 10000.0  # Maximum investment amount in USD
        self.min_profit_percentage = 0.01  # Minimum profit percentage
        self.max_profit_percentage = 0.50  # Maximum profit percentage

# Define a class to validate investment plans
class InvestmentPlanValidator:
    def __init__(self, rules):
        self.rules = rules

    def validate_investment_amount(self, amount):
        """Validate investment amount"""
        if amount < self.rules.min_investment_amount:
            raise ValueError(f"Investment amount must be greater than or equal to ${self.rules.min_investment_amount:.2f}")
        if amount > self.rules.max_investment_amount:
            raise ValueError(f"Investment amount must be less than or equal to ${self.rules.max_investment_amount:.2f}")
        return True

    def validate_profit_percentage(self, percentage):
        """Validate profit percentage"""
        if percentage < self.rules.min_profit_percentage:
            raise ValueError(f"Profit percentage must be greater than or equal to {self.rules.min_profit_percentage*100:.2f}%")
        if percentage > self.rules.max_profit_percentage:
            raise ValueError(f"Profit percentage must be less than or equal to {self.rules.max_profit_percentage*100:.2f}%")
        return True

    def validate_investment_plan(self, plan):
        """Validate investment plan"""
        try:
            self.validate_investment_amount(plan['investment_amount'])
            self.validate_profit_percentage(plan['profit_percentage'])
            logging.info(f"Investment plan is valid: {plan}")
            return True
        except ValueError as e:
            logging.error(f"Invalid investment plan: {plan}. Error: {str(e)}")
            return False

# Define a function to validate multiple investment plans
def validate_investment_plans(rules, plans):
    """Validate multiple investment plans"""
    validator = InvestmentPlanValidator(rules)
    valid_plans = []
    for plan in plans:
        if validator.validate_investment_plan(plan):
            valid_plans.append(plan)
    return valid_plans

# Main function
def main():
    logging.basicConfig(level=logging.INFO)

    # Define company rules and regulations
    rules = RapidCoinTradesRules()

    # Define investment plans to validate
    plans = [
        {'investment_amount': 500.0, 'profit_percentage': 0.10},
        {'investment_amount': 50000.0, 'profit_percentage': 0.20},  # Invalid investment amount
        {'investment_amount': 2000.0, 'profit_percentage': 0.005},  # Invalid profit percentage
        {'investment_amount': 2000.0, 'profit_percentage': 0.20}
    ]

    # Validate investment plans
    valid_plans = validate_investment_plans(rules, plans)

    # Print valid plans
    print("Valid Investment Plans:")
    for plan in valid_plans:
        print(plan)

if __name__ == "__main__":
    main()
```
