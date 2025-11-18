"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://edgenetwork-claim.pages.dev
Prompt: Write a program to calculate cost savings when switching from AWS to Edge Network's virtual machines, using the provided savings percentages (e.g., 32.78% for AWS).
Generated: DETERMINISTIC_59ebbafda7e1d4ba
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CostSavingsCalculator:
    """
    A class to calculate cost savings when switching from AWS to Edge Network's virtual machines.
    """

    def __init__(self, aws_cost: float, savings_percentage: float):
        """
        Initializes the CostSavingsCalculator with AWS cost and savings percentage.

        Args:
            aws_cost (float): The current monthly cost of AWS services.
            savings_percentage (float): The percentage savings when switching to Edge Network.
        """
        if aws_cost < 0:
            raise ValueError("AWS cost must be a non-negative value.")
        if not (0 <= savings_percentage <= 100):
            raise ValueError("Savings percentage must be between 0 and 100.")

        self.aws_cost = aws_cost
        self.savings_percentage = savings_percentage

    def calculate_savings(self) -> float:
        """
        Calculates the amount saved by switching from AWS to Edge Network.

        Returns:
            float: The calculated savings amount.
        """
        savings_amount = (self.savings_percentage / 100) * self.aws_cost
        return savings_amount

    def calculate_new_cost(self) -> float:
        """
        Calculates the new cost after applying the savings.

        Returns:
            float: The new monthly cost after savings.
        """
        savings_amount = self.calculate_savings()
        new_cost = self.aws_cost - savings_amount
        return new_cost

    def display_savings_info(self):
        """
        Displays the savings information including AWS cost, savings percentage,
        calculated savings amount, and new cost after switching.
        """
        try:
            savings_amount = self.calculate_savings()
            new_cost = self.calculate_new_cost()

            print(f"AWS Monthly Cost: ${self.aws_cost:.2f}")
            print(f"Savings Percentage: {self.savings_percentage:.2f}%")
            print(f"Calculated Savings: ${savings_amount:.2f}")
            print(f"New Monthly Cost after Switching: ${new_cost:.2f}")

        except Exception as e:
            print(f"An error occurred while calculating savings: {e}")


if __name__ == "__main__":
    # Example input values (these can be modified as needed)
    aws_cost = 1000.00  # Current monthly cost of AWS
    savings_percentage = 32.78  # Savings percentage when switching to Edge Network

    # Create an instance of the CostSavingsCalculator
    try:
        calculator = CostSavingsCalculator(aws_cost, savings_percentage)
        calculator.display_savings_info()
    except ValueError as e:
        print(f"Input Error: {e}")
```
