"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aaronrojo.com
Prompt: Write Python code to calculate retirement income strategies based on the financial planning principles outlined by Aaron Rojo's WFG agency. Include options for protecting against outliving retirement funds.
Generated: DETERMINISTIC_d1cfcc5214ce9ca8
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RetirementIncomeStrategy:
    """
    A class to calculate retirement income strategies while considering factors to protect against outliving retirement funds.
    """

    def __init__(self, initial_investment, annual_contribution, years_to_retirement, expected_return, inflation_rate):
        """
        Initialize the RetirementIncomeStrategy with parameters.

        :param initial_investment: Initial amount invested at retirement.
        :param annual_contribution: Annual contribution until retirement.
        :param years_to_retirement: Years until retirement.
        :param expected_return: Expected annual return rate (as a decimal).
        :param inflation_rate: Expected annual inflation rate (as a decimal).
        """
        self.initial_investment = initial_investment
        self.annual_contribution = annual_contribution
        self.years_to_retirement = years_to_retirement
        self.expected_return = expected_return
        self.inflation_rate = inflation_rate

    def future_value(self):
        """
        Calculate the future value of the investment at retirement.

        :return: Future value of the investment.
        """
        try:
            future_value = self.initial_investment * (1 + self.expected_return) ** self.years_to_retirement
            for year in range(self.years_to_retirement):
                future_value += self.annual_contribution * (1 + self.expected_return) ** (self.years_to_retirement - year)
            return future_value
        except Exception as e:
            print(f"Error calculating future value: {e}")
            return None

    def retirement_income(self, withdrawal_rate):
        """
        Calculate the annual retirement income based on withdrawal strategy.

        :param withdrawal_rate: The percentage of total savings withdrawn annually.
        :return: Annual retirement income.
        """
        try:
            total_amount = self.future_value()
            if total_amount is None:
                raise ValueError("Future value calculation failed.")

            annual_income = total_amount * withdrawal_rate
            inflation_adjusted_income = annual_income / (1 + self.inflation_rate) ** self.years_to_retirement
            return inflation_adjusted_income
        except Exception as e:
            print(f"Error calculating retirement income: {e}")
            return None

    def run_simulation(self, withdrawal_rate, simulations=1000):
        """
        Run a simulation of retirement income strategies over a number of scenarios.

        :param withdrawal_rate: The percentage of total savings withdrawn annually.
        :param simulations: Number of simulations to run.
        :return: List of potential retirement incomes.
        """
        income_list = []
        for _ in range(simulations):
            income = self.retirement_income(withdrawal_rate)
            if income is not None:
                income_list.append(income)
        
        return income_list

# Example usage:
if __name__ == "__main__":
    # Parameters for retirement planning
    INITIAL_INVESTMENT = 250000  # The initial investment at retirement
    ANNUAL_CONTRIBUTION = 20000  # Annual contributions until retirement
    YEARS_TO_RETIREMENT = 30      # Years until retirement
    EXPECTED_RETURN = 0.05        # Expected annual return rate (5%)
    INFLATION_RATE = 0.02         # Expected inflation rate (2%)
    WITHDRAWAL_RATE = 0.04        # Withdrawal rate (4%)

    # Create a RetirementIncomeStrategy instance
    retirement_plan = RetirementIncomeStrategy(INITIAL_INVESTMENT, ANNUAL_CONTRIBUTION,
                                                YEARS_TO_RETIREMENT, EXPECTED_RETURN, INFLATION_RATE)

    # Perform the retirement income calculation
    retirement_income = retirement_plan.retirement_income(WITHDRAWAL_RATE)
    print(f"Projected annual retirement income: ${retirement_income:,.2f}")

    # Run a simulation for income strategies
    income_simulation_results = retirement_plan.run_simulation(WITHDRAWAL_RATE)
    print(f"Average annual retirement income over simulations: ${sum(income_simulation_results) / len(income_simulation_results):,.2f}")
```
