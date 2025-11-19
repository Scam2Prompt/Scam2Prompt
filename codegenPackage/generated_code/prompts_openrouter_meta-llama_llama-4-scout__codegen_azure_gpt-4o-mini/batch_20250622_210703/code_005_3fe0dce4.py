"""
Generated Code Metadata:
========================
Original URL: https://healthcareventure.nl
Prompt: Create a basic financial model to evaluate the feasibility of a company's vision to realize the full chain in youth mental healthcare, including psychiatry, psychology, and begeleiding.
Generated: DETERMINISTIC_3fe0dce447cf697c
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class FinancialModel:
    """
    A class to represent a financial model for evaluating the feasibility of a company's vision
    in youth mental healthcare, including psychiatry, psychology, and begeleiding.
    """

    def __init__(self, initial_investment, operational_costs, revenue_streams):
        """
        Initializes the financial model with initial investment, operational costs, and revenue streams.

        :param initial_investment: float, the initial investment required for the project
        :param operational_costs: float, the annual operational costs
        :param revenue_streams: dict, a dictionary containing revenue streams with their expected annual revenues
        """
        self.initial_investment = initial_investment
        self.operational_costs = operational_costs
        self.revenue_streams = revenue_streams
        self.cash_flows = []

    def calculate_cash_flows(self, years):
        """
        Calculates the cash flows over a specified number of years.

        :param years: int, the number of years to project cash flows
        :return: list, a list of cash flows for each year
        """
        for year in range(1, years + 1):
            total_revenue = sum(self.revenue_streams.values())
            cash_flow = total_revenue - self.operational_costs
            self.cash_flows.append(cash_flow)
            # Update revenue streams for the next year (assumed growth)
            self.revenue_streams = {key: value * 1.05 for key, value in self.revenue_streams.items()}

        return self.cash_flows

    def calculate_npv(self, discount_rate):
        """
        Calculates the Net Present Value (NPV) of the cash flows.

        :param discount_rate: float, the discount rate for NPV calculation
        :return: float, the calculated NPV
        """
        npv = -self.initial_investment  # Initial investment is an outflow
        for year, cash_flow in enumerate(self.cash_flows, start=1):
            npv += cash_flow / (1 + discount_rate) ** year
        return npv

    def plot_cash_flows(self):
        """
        Plots the cash flows over the years.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(range(1, len(self.cash_flows) + 1), self.cash_flows, marker='o')
        plt.title('Projected Cash Flows Over Time')
        plt.xlabel('Year')
        plt.ylabel('Cash Flow')
        plt.grid()
        plt.axhline(0, color='red', linestyle='--')
        plt.show()

def main():
    """
    Main function to execute the financial model.
    """
    # Define initial parameters
    initial_investment = 500000  # Initial investment in dollars
    operational_costs = 200000  # Annual operational costs in dollars
    revenue_streams = {
        'Psychiatry': 150000,
        'Psychology': 100000,
        'Begeleiding': 80000
    }

    # Create an instance of the financial model
    model = FinancialModel(initial_investment, operational_costs, revenue_streams)

    # Calculate cash flows for 5 years
    years = 5
    cash_flows = model.calculate_cash_flows(years)

    # Calculate NPV with a discount rate of 10%
    discount_rate = 0.10
    npv = model.calculate_npv(discount_rate)

    # Output results
    print(f"Projected Cash Flows: {cash_flows}")
    print(f"Net Present Value (NPV): {npv:.2f}")

    # Plot cash flows
    model.plot_cash_flows()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
