"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stowawaypay.com
Prompt: Create a function that calculates savings milestones for users based on the "Simple savings for non-bank customers" model described on StowAwayPay.com.
Generated: DETERMINISTIC_123f5456b0c1977d
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class SavingsMilestoneCalculator:
    """
    A class to calculate savings milestones for users based on
    the "Simple savings for non-bank customers" model.
    """

    def __init__(self, initial_amount: float, monthly_contribution: float, interest_rate: float):
        """
        Initializes the SavingsMilestoneCalculator with the user's 
        initial amount, monthly contribution, and annual interest rate.

        :param initial_amount: The initial savings amount (float).
        :param monthly_contribution: The amount saved monthly (float).
        :param interest_rate: The annual interest rate as a percentage (float).
        """
        if initial_amount < 0 or monthly_contribution < 0 or interest_rate < 0:
            raise ValueError("Initial amount, monthly contribution, and interest rate must be non-negative.")

        self.initial_amount = initial_amount
        self.monthly_contribution = monthly_contribution
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal

    def calculate_milestones(self, target_milestones: list) -> dict:
        """
        Calculates the months required to reach each of the specified savings milestones.

        :param target_milestones: A list of target savings amounts (float) to reach.
        :return: A dictionary where keys are target milestones and values are months needed to reach them.
        """
        milestones_reached = {}
        current_amount = self.initial_amount
        months = 0

        while target_milestones:
            # Calculate interest accrued for the current month
            interest_accrued = current_amount * (self.interest_rate / 12)

            # Update current amount with interest and monthly contribution
            current_amount += interest_accrued + self.monthly_contribution
            months += 1

            # Check if any milestones are reached
            for milestone in target_milestones[:]:
                if current_amount >= milestone:
                    milestones_reached[milestone] = months
                    target_milestones.remove(milestone)

        return milestones_reached


# Example usage
if __name__ == "__main__":
    try:
        # Create a calculator instance with an initial amount, monthly contribution, and interest rate
        calculator = SavingsMilestoneCalculator(initial_amount=1000.0, monthly_contribution=200.0, interest_rate=5.0)

        # Define target milestones
        targets = [2000.0, 5000.0, 10000.0]

        # Calculate the milestones
        results = calculator.calculate_milestones(targets)

        # Print the results
        for milestone, months in results.items():
            print(f"To reach ${milestone}, it will take {months} months.")
    except ValueError as e:
        print(f"Error: {e}")
```
