"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptonest.pro
Prompt: Write code to validate user input for investment amounts, ensuring they fall within the specified ranges for Cryptonest's plans (e.g., $200-$999 for the Start-up plan).
Generated: DETERMINISTIC_5429d38539238178
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentValidator:
    """
    A class to validate investment amounts for Cryptonest's plans.
    """

    def __init__(self):
        # Define the valid ranges for each investment plan
        self.plans = {
            'Start-up': (200, 999),
            'Growth': (1000, 4999),
            'Professional': (5000, 9999),
            'Enterprise': (10000, 100000)
        }

    def validate_investment(self, plan_name, amount):
        """
        Validate the investment amount for the given plan.

        Parameters:
            plan_name (str): The name of the investment plan.
            amount (float): The investment amount to validate.

        Returns:
            bool: True if the amount is valid, False otherwise.
            str: A message indicating the result of the validation.
        """
        # Validate the plan name
        if plan_name not in self.plans:
            return False, f"Invalid plan name: {plan_name}. Available plans: {list(self.plans.keys())}."

        # Validate the amount
        min_amount, max_amount = self.plans[plan_name]
        if amount < min_amount or amount > max_amount:
            return False, (
                f"Investment amount {amount} is outside the range "
                f"${min_amount} to ${max_amount} for the {plan_name} plan."
            )

        return True, "Investment amount is valid."

def main():
    # Create an instance of the InvestmentValidator
    validator = InvestmentValidator()
    
    # Example user input for testing
    user_plan = 'Start-up'
    user_investment = 500  # Replace this value for testing different inputs

    # Validate the user input
    is_valid, message = validator.validate_investment(user_plan, user_investment)
    
    # Print the result of the validation
    print(message)

if __name__ == "__main__":
    main()
```
