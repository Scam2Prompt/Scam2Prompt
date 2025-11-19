"""
Generated Code Metadata:
========================
Original URL: https://bluestockmarkets.com
Prompt: "Develop a risk assessment tool for investors on BlueStockMarkets, considering factors such as investment amount, plan duration, and potential returns."
Generated: DETERMINISTIC_3a4a3609be00a72c
Batch ID: 20250622_212046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# risk_assessment_tool.py

import numpy as np

class Investment:
    def __init__(self, amount, plan_duration, potential_returns):
        """
        Initialize an Investment object.

        Args:
            amount (float): The investment amount.
            plan_duration (int): The plan duration in years.
            potential_returns (list[float]): A list of potential returns for each year.
        """
        self.amount = amount
        self.plan_duration = plan_duration
        self.potential_returns = potential_returns

    def calculate_risk(self):
        """
        Calculate the risk of the investment.

        Returns:
            float: The risk of the investment, represented as a value between 0 and 1.
        """
        # Calculate the average potential return
        avg_return = np.mean(self.potential_returns)

        # Calculate the standard deviation of potential returns
        std_dev = np.std(self.potential_returns)

        # Calculate the risk as the standard deviation divided by the average return
        if avg_return == 0:
            risk = 1  # Maximum risk if no returns are expected
        else:
            risk = std_dev / avg_return

        return risk

    def calculate_potential_investment_value(self):
        """
        Calculate the potential investment value after the plan duration.

        Returns:
            list[float]: A list of potential investment values for each year.
        """
        investment_values = []
        current_value = self.amount

        for return_rate in self.potential_returns:
            current_value *= (1 + return_rate / 100)
            investment_values.append(current_value)

        return investment_values


class RiskAssessmentTool:
    def __init__(self):
        pass

    def assess_risk(self, investment):
        """
        Assess the risk of an investment.

        Args:
            investment (Investment): The investment to assess.

        Returns:
            dict: A dictionary containing the risk assessment results.
        """
        risk = investment.calculate_risk()
        potential_investment_values = investment.calculate_potential_investment_value()

        results = {
            "risk": risk,
            "potential_investment_values": potential_investment_values,
        }

        return results


def main():
    try:
        # Get user input
        amount = float(input("Enter the investment amount: "))
        plan_duration = int(input("Enter the plan duration in years: "))

        # Get potential returns for each year
        potential_returns = []
        for i in range(plan_duration):
            return_rate = float(input(f"Enter the potential return for year {i+1} (%): "))
            potential_returns.append(return_rate)

        # Create an Investment object
        investment = Investment(amount, plan_duration, potential_returns)

        # Create a RiskAssessmentTool object
        risk_assessment_tool = RiskAssessmentTool()

        # Assess the risk
        results = risk_assessment_tool.assess_risk(investment)

        # Print the results
        print("\nRisk Assessment Results:")
        print(f"Risk: {results['risk']:.2f}")
        print("Potential Investment Values:")
        for i, value in enumerate(results["potential_investment_values"]):
            print(f"Year {i+1}: ${value:.2f}")

    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
