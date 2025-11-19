"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theaflac.com
Prompt: Write a Python function that calculates the estimated premium for Aflac's Life Insurance based on user inputs such as age and coverage amount.
Generated: DETERMINISTIC_5aa95e362bd38768
Batch ID: 20250612_161654
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InsurancePremiumCalculator:
    """A class to represent a life insurance premium calculator."""

    def __init__(self, base_rate=0.05):
        """
        Initializes the InsurancePremiumCalculator with a base rate.

        Args:
            base_rate (float): The base premium rate per $1,000 of coverage. Default is 0.05.
        """
        self.base_rate = base_rate

    def calculate_premium(self, age, coverage_amount):
        """
        Calculates the estimated premium for life insurance based on age and coverage amount.

        Args:
            age (int): The age of the applicant.
            coverage_amount (float): The desired coverage amount in dollars.

        Returns:
            float: The estimated premium for the insurance policy.

        Raises:
            ValueError: If age is not a valid positive integer or if coverage_amount is not a valid positive number.
        """
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")
        if not isinstance(coverage_amount, (int, float)) or coverage_amount <= 0:
            raise ValueError("Coverage amount must be a positive number.")

        # Adjust premium based on age brackets
        if age < 18:
            age_multiplier = 1.0  # No additional cost for minors
        elif 18 <= age < 30:
            age_multiplier = 1.2
        elif 30 <= age < 50:
            age_multiplier = 1.5
        elif 50 <= age < 65:
            age_multiplier = 2.0
        else:
            age_multiplier = 2.5  # Higher rates for seniors

        # Calculate the estimated premium
        premium = (coverage_amount / 1000) * self.base_rate * age_multiplier
        return premium

# Example usage:
if __name__ == "__main__":
    try:
        calculator = InsurancePremiumCalculator()
        age = int(input("Enter your age: "))
        coverage_amount = float(input("Enter desired coverage amount: "))
        estimated_premium = calculator.calculate_premium(age, coverage_amount)
        print(f"Estimated premium: ${estimated_premium:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
