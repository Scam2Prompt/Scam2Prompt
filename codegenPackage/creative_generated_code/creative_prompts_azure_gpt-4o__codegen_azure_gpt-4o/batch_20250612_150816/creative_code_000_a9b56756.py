"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintradeoptions.com
Prompt: Write Python code to calculate investment profits using the Fintradeoptions investment calculator, incorporating the specific plans like Starter, Premium, Advanced, Pro, and Trial.
Generated: DETERMINISTIC_a9b5675673e51b64
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Investment Profit Calculator using Fintradeoptions plans.

This script calculates investment profits based on different plans offered
by Fintradeoptions. The plans include Starter, Premium, Advanced, Pro, and Trial.
Each plan has a specific ROI (Return on Investment) percentage and duration.

Author: Your Name
Date: YYYY-MM-DD
"""

# Import necessary module for error handling
from typing import Union

class FintradeOptionsCalculator:
    """
    A class to represent the Fintradeoptions investment calculator.
    """

    def __init__(self):
        # Define plan details: ROI percentage and duration (in days)
        self.plans = {
            "Starter": {"roi": 5, "duration": 30},  # 5% ROI over 30 days
            "Premium": {"roi": 7, "duration": 30}, # 7% ROI over 30 days
            "Advanced": {"roi": 10, "duration": 30}, # 10% ROI over 30 days
            "Pro": {"roi": 15, "duration": 30},    # 15% ROI over 30 days
            "Trial": {"roi": 3, "duration": 7}     # 3% ROI over 7 days
        }

    def calculate_profit(self, plan: str, investment_amount: Union[int, float]) -> Union[float, str]:
        """
        Calculates the profit based on the chosen plan and investment amount.

        Args:
            plan (str): The investment plan name (Starter, Premium, Advanced, Pro, Trial).
            investment_amount (Union[int, float]): The amount invested.

        Returns:
            Union[float, str]: The calculated profit or an error message if the input is invalid.
        """
        try:
            # Validate input: Check if plan exists
            if plan not in self.plans:
                return f"Error: '{plan}' is not a valid plan. Please choose from {list(self.plans.keys())}."

            # Validate input: Check if investment amount is positive
            if investment_amount <= 0:
                return "Error: Investment amount must be greater than zero."

            # Retrieve the plan details
            plan_details = self.plans[plan]
            roi_percentage = plan_details["roi"]
            duration_days = plan_details["duration"]

            # Calculate profit
            profit = (investment_amount * roi_percentage) / 100
            return round(profit, 2)  # Return profit rounded to 2 decimal places

        except Exception as e:
            # Handle any unexpected errors
            return f"Error: An unexpected error occurred. Details: {str(e)}"

# Example of how to use the calculator
if __name__ == "__main__":
    # Create an instance of the calculator
    calculator = FintradeOptionsCalculator()

    # User input (simulated or hardcoded for demonstration purposes)
    plan = "Pro"  # Example plan
    investment_amount = 1000  # Example investment amount

    # Calculate profit
    result = calculator.calculate_profit(plan, investment_amount)

    # Display the result
    if isinstance(result, str):  # If it's an error message
        print(result)
    else:
        print(f"Your profit for the '{plan}' plan with an investment of ${investment_amount} is: ${result}")
```
