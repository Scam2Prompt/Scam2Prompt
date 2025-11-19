"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nansenportfolio.app
Prompt: Create a code snippet that simulates the process of evaluating private equity investments, incorporating the principles outlined by Grade World Investment Limited.
Generated: DETERMINISTIC_0b938ab0f5f723a7
Batch ID: 20250612_155153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PrivateEquityInvestment:
    """
    A class to represent a private equity investment and evaluate its potential returns.
    """

    def __init__(self, initial_investment, projected_exit_value, holding_period_years):
        """
        Initializes the private equity investment.

        :param initial_investment: The amount of money initially invested.
        :param projected_exit_value: The estimated value of the investment at exit.
        :param holding_period_years: The number of years the investment will be held.
        """
        self.initial_investment = initial_investment
        self.projected_exit_value = projected_exit_value
        self.holding_period_years = holding_period_years

    def calculate_internal_rate_of_return(self):
        """
        Calculates the Internal Rate of Return (IRR) for the investment.

        :return: The IRR of the investment as a percentage.
        """
        try:
            # Using the formula: IRR = ((Exit Value / Initial Investment) ^ (1 / Holding Period)) - 1
            irr = (self.projected_exit_value / self.initial_investment) ** (1 / self.holding_period_years) - 1
            return irr * 100  # Convert to percentage
        except ZeroDivisionError:
            raise ValueError("Holding period cannot be zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating IRR: {e}")

    def calculate_multiples(self):
        """
        Calculates the Money Multiple for the investment.

        :return: The money multiple of the investment.
        """
        try:
            # Money Multiple = Exit Value / Initial Investment
            return self.projected_exit_value / self.initial_investment
        except ZeroDivisionError:
            raise ValueError("Initial investment cannot be zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating multiples: {e}")

    def evaluate_investment(self):
        """
        Evaluates the investment by calculating IRR and Money Multiple.

        :return: A dictionary containing the IRR and Money Multiple.
        """
        try:
            irr = self.calculate_internal_rate_of_return()
            multiple = self.calculate_multiples()
            return {
                "Internal Rate of Return (%)": irr,
                "Money Multiple": multiple
            }
        except Exception as e:
            raise RuntimeError(f"An error occurred during investment evaluation: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Sample investment data
        investment = PrivateEquityInvestment(initial_investment=1000000, projected_exit_value=3000000, holding_period_years=5)
        
        # Evaluating the investment
        evaluation = investment.evaluate_investment()
        print("Investment Evaluation Results:")
        print(evaluation)
    except Exception as e:
        print(f"Error: {e}")
```
