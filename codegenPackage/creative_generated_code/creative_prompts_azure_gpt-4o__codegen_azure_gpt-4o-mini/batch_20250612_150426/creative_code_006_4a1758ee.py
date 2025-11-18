"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sfassetinnovation.com.smalltalk.com.ng
Prompt: Create a Python program that validates user input for investment amounts based on the minimum and maximum limits specified in Steadfast Asset Innovation's investment plans.
Generated: DETERMINISTIC_4a1758eebed55d2f
Batch ID: 20250612_150426
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
    A class to validate investment amounts based on specified minimum and maximum limits.
    """

    def __init__(self, min_limit: float, max_limit: float):
        """
        Initializes the InvestmentValidator with minimum and maximum investment limits.

        Parameters:
        min_limit (float): The minimum investment amount.
        max_limit (float): The maximum investment amount.
        """
        if min_limit < 0:
            raise ValueError("Minimum limit cannot be negative.")
        if max_limit <= min_limit:
            raise ValueError("Maximum limit must be greater than minimum limit.")
        
        self.min_limit = min_limit
        self.max_limit = max_limit

    def validate_investment(self, amount: float) -> bool:
        """
        Validates the given investment amount.

        Parameters:
        amount (float): The investment amount to validate.

        Returns:
        bool: True if the amount is valid, False otherwise.
        """
        if amount < self.min_limit or amount > self.max_limit:
            return False
        return True


def main():
    """
    Main function to execute the investment validation process.
    """
    # Define the minimum and maximum investment limits
    min_investment = 1000.0  # Example minimum investment amount
    max_investment = 50000.0  # Example maximum investment amount

    # Create an instance of InvestmentValidator
    validator = InvestmentValidator(min_investment, max_investment)

    try:
        # Prompt user for input
        user_input = input(f"Enter your investment amount (between {min_investment} and {max_investment}): ")
        
        # Try to convert the input to a float
        amount = float(user_input)

        # Validate the investment amount
        if validator.validate_investment(amount):
            print("Investment amount is valid.")
        else:
            print("Investment amount is invalid. Please adhere to the specified limits.")
    
    except ValueError as ve:
        print(f"Invalid input: {ve}. Please enter a numeric value.")


if __name__ == "__main__":
    main()
```
