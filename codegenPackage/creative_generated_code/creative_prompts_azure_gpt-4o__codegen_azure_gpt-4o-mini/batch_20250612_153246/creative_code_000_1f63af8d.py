"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vfmadvisory.com
Prompt: Write Python code to create a financial model for a public-private partnership (PPP) project, incorporating feasibility study elements and transaction advisory insights as described on VfM Advisory's website.
Generated: DETERMINISTIC_1f63af8d7c73a326
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class PPPFinancialModel:
    def __init__(self, project_name, total_investment, equity_percentage, debt_percentage):
        """
        Initialize the PPP Financial Model.

        :param project_name: Name of the project.
        :param total_investment: Total investment required for the project.
        :param equity_percentage: Percentage of the investment covered by equity.
        :param debt_percentage: Percentage of the investment covered by debt.
        """
        self.project_name = project_name
        self.total_investment = total_investment
        self.equity_percentage = equity_percentage
        self.debt_percentage = debt_percentage
        self.equity_investment = total_investment * equity_percentage
        self.debt_investment = total_investment * debt_percentage

        # Validate the input percentages
        if equity_percentage + debt_percentage != 1:
            raise ValueError("Equity and Debt percentages must sum to 1.")

    def generate_cash_flows(self, years, annual_revenue, operating_costs):
        """
        Generate cash flow projections for the PPP project.

        :param years: Number of years for the cash flow projection.
        :param annual_revenue: Expected annual revenue from the project.
        :param operating_costs: Expected annual operating costs of the project.
        :return: DataFrame containing projected cash flows.
        """
        cash_flows = []
        for year in range(1, years + 1):
            cash_flow = annual_revenue - operating_costs
            cash_flows.append({'Year': year, 'Cash Flow': cash_flow})
        
        cash_flow_df = pd.DataFrame(cash_flows)
        return cash_flow_df

    def calculate_npv(self, cash_flows, discount_rate):
        """
        Calculate the Net Present Value (NPV) of the cash flows.

        :param cash_flows: DataFrame containing cash flows.
        :param discount_rate: Discount rate for NPV calculation.
        :return: Net Present Value of the cash flows.
        """
        npv = 0
        for index, row in cash_flows.iterrows():
            npv += row['Cash Flow'] / ((1 + discount_rate) ** row['Year'])
        return npv

    def plot_cash_flows(self, cash_flows):
        """
        Plot the projected cash flows over the project duration.

        :param cash_flows: DataFrame containing cash flows.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(cash_flows['Year'], cash_flows['Cash Flow'], marker='o')
        plt.title(f'Projected Cash Flows for {self.project_name}')
        plt.xlabel('Year')
        plt.ylabel('Cash Flow')
        plt.grid(True)
        plt.show()

# Example Usage
if __name__ == "__main__":
    try:
        # Create a PPP financial model instance
        model = PPPFinancialModel(project_name="City Transport Project",
                                   total_investment=5000000,
                                   equity_percentage=0.4,
                                   debt_percentage=0.6)

        # Generate cash flows
        cash_flows = model.generate_cash_flows(years=10, annual_revenue=800000, operating_costs=300000)

        # Calculate NPV
        npv = model.calculate_npv(cash_flows, discount_rate=0.08)
        print(f'Net Present Value (NPV) of the project: ${npv:,.2f}')

        # Plot cash flows
        model.plot_cash_flows(cash_flows)

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
