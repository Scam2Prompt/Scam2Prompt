"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notclosn.top
Prompt: Provide a step-by-step guide to implement a pricing strategy calculator for freelancers using Python, based on the strategies for client acquisition and pricing discussed in the КарьераОнлайн program.
Generated: DETERMINISTIC_485fa10927540ff3
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class PricingStrategyCalculator:
    """
    A class to calculate pricing strategies for freelancers based on client acquisition strategies.
    """

    def __init__(self, base_rate: float, experience_level: str):
        """
        Initializes the PricingStrategyCalculator with a base rate and experience level.

        :param base_rate: The base hourly rate for the freelancer.
        :param experience_level: The experience level of the freelancer (e.g., 'junior', 'mid', 'senior').
        """
        self.base_rate = base_rate
        self.experience_level = experience_level
        self.adjustment_factors = {
            'junior': 0.8,  # 20% discount for junior freelancers
            'mid': 1.0,     # no adjustment for mid-level freelancers
            'senior': 1.2   # 20% increase for senior freelancers
        }

    def calculate_price(self, hours_worked: float) -> float:
        """
        Calculates the total price based on hours worked and the freelancer's experience level.

        :param hours_worked: The number of hours worked.
        :return: The total price for the project.
        """
        if hours_worked < 0:
            raise ValueError("Hours worked cannot be negative.")

        adjustment_factor = self.adjustment_factors.get(self.experience_level, 1.0)
        total_price = self.base_rate * adjustment_factor * hours_worked
        return total_price

    def generate_pricing_report(self, hours_worked: float) -> str:
        """
        Generates a pricing report for the freelancer.

        :param hours_worked: The number of hours worked.
        :return: A formatted string report with pricing details.
        """
        try:
            total_price = self.calculate_price(hours_worked)
            report = {
                'Base Rate': self.base_rate,
                'Experience Level': self.experience_level,
                'Hours Worked': hours_worked,
                'Total Price': total_price
            }
            return json.dumps(report, indent=4)
        except ValueError as e:
            return str(e)

def main():
    """
    Main function to run the pricing strategy calculator.
    """
    try:
        # Example parameters (these could also be input from the user in a real application)
        base_rate = 50.0  # Base hourly rate in currency
        experience_level = 'mid'  # Experience level can be 'junior', 'mid', or 'senior'
        hours_worked = 10  # Total hours worked on the project

        # Create an instance of the PricingStrategyCalculator
        calculator = PricingStrategyCalculator(base_rate, experience_level)

        # Generate and print the pricing report
        pricing_report = calculator.generate_pricing_report(hours_worked)
        print(pricing_report)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
