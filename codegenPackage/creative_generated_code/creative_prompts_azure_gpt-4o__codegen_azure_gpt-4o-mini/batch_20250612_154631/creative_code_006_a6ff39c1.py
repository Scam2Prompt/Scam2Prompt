"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rapidcointrades.org
Prompt: Write a Python script to validate user input for investment amounts based on the minimum and maximum limits for each plan (Starter, Basic, Golden, VIP) as described on RapidCoinTrades.
Generated: DETERMINISTIC_a6ff39c1788f79f4
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# investment_validator.py

class InvestmentPlan:
    """Class to represent an investment plan with its limits."""
    
    def __init__(self, name, min_amount, max_amount):
        self.name = name
        self.min_amount = min_amount
        self.max_amount = max_amount
    
    def is_valid_investment(self, amount):
        """Check if the given amount is within the valid range for this plan."""
        return self.min_amount <= amount <= self.max_amount


class InvestmentValidator:
    """Class to validate user investments against defined plans."""
    
    def __init__(self):
        # Define investment plans with their corresponding limits
        self.plans = {
            "Starter": InvestmentPlan("Starter", 10, 100),
            "Basic": InvestmentPlan("Basic", 101, 1000),
            "Golden": InvestmentPlan("Golden", 1001, 5000),
            "VIP": InvestmentPlan("VIP", 5001, 10000),
        }

    def validate_investment(self, plan_name, amount):
        """Validate the investment amount against the specified plan."""
        plan = self.plans.get(plan_name)
        
        if plan is None:
            raise ValueError(f"Investment plan '{plan_name}' does not exist.")
        
        if not isinstance(amount, (int, float)):
            raise TypeError("Investment amount must be a number.")
        
        if amount < 0:
            raise ValueError("Investment amount cannot be negative.")
        
        return plan.is_valid_investment(amount)


def main():
    """Main function to execute the investment validation script."""
    validator = InvestmentValidator()
    
    # Example user input for testing
    user_input = [
        ("Starter", 50),
        ("Basic", 200),
        ("Golden", 10000),  # Invalid for Golden
        ("VIP", 6000),
        ("InvalidPlan", 500),  # Invalid plan
        ("Starter", -20),  # Invalid amount
    ]
    
    for plan_name, amount in user_input:
        try:
            is_valid = validator.validate_investment(plan_name, amount)
            if is_valid:
                print(f"Investment of ${amount} is valid for the {plan_name} plan.")
            else:
                print(f"Investment of ${amount} is NOT valid for the {plan_name} plan.")
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
