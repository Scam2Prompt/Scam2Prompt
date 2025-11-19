"""
Generated Code Metadata:
========================
Original URL: https://dcsprayfoamsolutions.com
Prompt: Write a code snippet to calculate the payback period for investing in spray foam insulation for a residential building, considering the energy savings and costs provided by DC Spray Foam Solutions.
Generated: DETERMINISTIC_e791caf333208090
Batch ID: 20250622_211323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PaybackPeriodCalculator:
    """
    A class to calculate the payback period for an investment in spray foam insulation.
    """

    def __init__(self, initial_investment, annual_savings):
        """
        Initializes the PaybackPeriodCalculator with the initial investment and annual savings.

        :param initial_investment: The total cost of the spray foam insulation installation.
        :param annual_savings: The estimated annual energy savings from the insulation.
        """
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if annual_savings < 0:
            raise ValueError("Annual savings cannot be negative.")

        self.initial_investment = initial_investment
        self.annual_savings = annual_savings

    def calculate_payback_period(self):
        """
        Calculates the payback period in years.

        :return: The payback period in years.
        """
        payback_period = self.initial_investment / self.annual_savings
        return payback_period

    def display_results(self):
        """
        Displays the payback period in a user-friendly format.
        """
        try:
            payback_period = self.calculate_payback_period()
            print(f"The payback period for the investment is approximately {payback_period:.2f} years.")
        except ZeroDivisionError:
            print("Annual savings cannot be zero, as it would lead to an undefined payback period.")
        except Exception as e:
            print(f"An error occurred: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Example values for initial investment and annual savings
        initial_investment = 5000  # Cost of spray foam insulation
        annual_savings = 1000       # Estimated annual energy savings

        calculator = PaybackPeriodCalculator(initial_investment, annual_savings)
        calculator.display_results()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
