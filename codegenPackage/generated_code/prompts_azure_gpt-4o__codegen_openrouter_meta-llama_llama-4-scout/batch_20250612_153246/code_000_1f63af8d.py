"""
Generated Code Metadata:
========================
Original URL: https://vfmadvisory.com
Prompt: Write Python code to create a financial model for a public-private partnership (PPP) project, incorporating feasibility study elements and transaction advisory insights as described on VfM Advisory's website.
Generated: DETERMINISTIC_1f63af8d7c73a326
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financial_model.py

import numpy as np
import pandas as pd

class PPPFinancialModel:
    """
    A financial model for a public-private partnership (PPP) project.

    Attributes:
        project_name (str): The name of the project.
        concession_period (int): The concession period in years.
        construction_period (int): The construction period in years.
        operating_period (int): The operating period in years.
        total_investment (float): The total investment in the project.
        equity_contribution (float): The equity contribution from the private partner.
        debt_contribution (float): The debt contribution from the private partner.
        interest_rate (float): The interest rate on debt.
        inflation_rate (float): The inflation rate.
        discount_rate (float): The discount rate.
    """

    def __init__(self, project_name, concession_period, construction_period, operating_period,
                 total_investment, equity_contribution, debt_contribution, interest_rate,
                 inflation_rate, discount_rate):
        self.project_name = project_name
        self.concession_period = concession_period
        self.construction_period = construction_period
        self.operating_period = operating_period
        self.total_investment = total_investment
        self.equity_contribution = equity_contribution
        self.debt_contribution = debt_contribution
        self.interest_rate = interest_rate
        self.inflation_rate = inflation_rate
        self.discount_rate = discount_rate

    def calculate_debt_service(self):
        """
        Calculate the debt service.

        Returns:
            float: The debt service.
        """
        debt_service = self.debt_contribution * self.interest_rate
        return debt_service

    def calculate_equity_return(self):
        """
        Calculate the equity return.

        Returns:
            float: The equity return.
        """
        equity_return = self.equity_contribution * self.discount_rate
        return equity_return

    def calculate_project_cash_flow(self):
        """
        Calculate the project cash flow.

        Returns:
            pandas.DataFrame: A DataFrame containing the project cash flow.
        """
        project_cash_flow = pd.DataFrame({
            'Year': range(self.concession_period + 1),
            'Investment': [self.total_investment if year == 0 else 0 for year in range(self.concession_period + 1)],
            'Debt Service': [self.calculate_debt_service() if year > 0 else 0 for year in range(self.concession_period + 1)],
            'Equity Return': [self.calculate_equity_return() if year > 0 else 0 for year in range(self.concession_period + 1)],
            'Cash Flow': [0] * (self.concession_period + 1)
        })

        project_cash_flow['Cash Flow'] = project_cash_flow['Investment'] + project_cash_flow['Debt Service'] + project_cash_flow['Equity Return']

        return project_cash_flow

    def calculate_vfm(self):
        """
        Calculate the Value for Money (VfM) metrics.

        Returns:
            dict: A dictionary containing the VfM metrics.
        """
        project_cash_flow = self.calculate_project_cash_flow()

        npv = np.sum([project_cash_flow.loc[i, 'Cash Flow'] / (1 + self.discount_rate) ** i for i in range(self.concession_period + 1)])
        irr = self.calculate_irr(project_cash_flow)

        vfm_metrics = {
            'NPV': npv,
            'IRR': irr
        }

        return vfm_metrics

    def calculate_irr(self, project_cash_flow):
        """
        Calculate the Internal Rate of Return (IRR).

        Args:
            project_cash_flow (pandas.DataFrame): A DataFrame containing the project cash flow.

        Returns:
            float: The IRR.
        """
        def irr_func(rate):
            return np.sum([project_cash_flow.loc[i, 'Cash Flow'] / (1 + rate) ** i for i in range(self.concession_period + 1)])

        irr = 0
        while irr_func(irr) < 0:
            irr += 0.01

        return irr


def main():
    try:
        project_name = 'PPP Project'
        concession_period = 20
        construction_period = 2
        operating_period = 18
        total_investment = 100000000
        equity_contribution = 30000000
        debt_contribution = 70000000
        interest_rate = 0.08
        inflation_rate = 0.02
        discount_rate = 0.10

        ppp_model = PPPFinancialModel(project_name, concession_period, construction_period, operating_period,
                                      total_investment, equity_contribution, debt_contribution, interest_rate,
                                      inflation_rate, discount_rate)

        project_cash_flow = ppp_model.calculate_project_cash_flow()
        vfm_metrics = ppp_model.calculate_vfm()

        print('# Project Cash Flow')
        print(project_cash_flow)
        print('\n# VfM Metrics')
        print(vfm_metrics)

    except Exception as e:
        print(f'An error occurred: {e}')


if __name__ == '__main__':
    main()
```
