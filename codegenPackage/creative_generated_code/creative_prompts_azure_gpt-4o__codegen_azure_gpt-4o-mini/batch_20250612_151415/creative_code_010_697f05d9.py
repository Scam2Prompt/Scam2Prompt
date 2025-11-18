"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Build a function to estimate retirement savings under the National Pension System (NPS), referencing the NPS Calculator tool on the IFSC Finder webpage.
Generated: DETERMINISTIC_697f05d9398d4ea9
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NPSCalculator:
    def __init__(self, current_age, retirement_age, monthly_contribution, expected_return_rate):
        """
        Initialize the NPSCalculator with user details.

        :param current_age: int - Current age of the individual
        :param retirement_age: int - Age at which the individual plans to retire
        :param monthly_contribution: float - Monthly contribution made to NPS
        :param expected_return_rate: float - Expected annual return rate (in percentage)
        """
        if not (0 <= current_age < retirement_age):
            raise ValueError("Current age must be non-negative and less than retirement age.")
        if monthly_contribution < 0:
            raise ValueError("Monthly contribution must be non-negative.")
        if expected_return_rate < 0:
            raise ValueError("Expected return rate must be non-negative.")

        self.current_age = current_age
        self.retirement_age = retirement_age
        self.monthly_contribution = monthly_contribution
        self.expected_return_rate = expected_return_rate / 100  # Convert percentage to decimal

    def calculate_total_savings(self):
        """
        Calculate the estimated total savings at retirement age.

        :return: float - Total estimated savings at retirement age
        """
        years_to_retirement = self.retirement_age - self.current_age
        months_to_retirement = years_to_retirement * 12
        
        # Future Value of a series formula: FV = P * (((1 + r)^n - 1) / r)
        # where P is the monthly contribution, r is the monthly interest rate, and n is the total number of contributions
        monthly_rate_of_return = self.expected_return_rate / 12  # Convert annual rate to monthly
        total_savings = self.monthly_contribution * (((1 + monthly_rate_of_return) ** months_to_retirement - 1) / monthly_rate_of_return)

        return total_savings

def main():
    """
    Main function to execute the NPS savings estimation.
    """
    try:
        # User inputs
        current_age = int(input("Enter your current age: "))
        retirement_age = int(input("Enter your retirement age: "))
        monthly_contribution = float(input("Enter your monthly contribution to NPS: "))
        expected_return_rate = float(input("Enter your expected annual return rate (in %): "))

        # Create NPSCalculator instance
        nps_calculator = NPSCalculator(current_age, retirement_age, monthly_contribution, expected_return_rate)
        
        # Calculate and display total savings
        total_savings = nps_calculator.calculate_total_savings()
        print(f"Estimated total savings at retirement age: ${total_savings:,.2f}")

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
