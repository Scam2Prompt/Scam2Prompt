"""
Generated Code Metadata:
========================
Original URL: https://www.marodconsultores.com.pe
Prompt: Create a script for simulating pre-investment feasibility studies in the energy sector, using MAROD Consultores SAC's expertise in economic evaluations.
Generated: DETERMINISTIC_048a0389618b58c6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Pre-Investment Feasibility Study Simulator for Energy Sector

This script simulates pre-investment feasibility studies in the energy sector.
It uses a basic Discounted Cash Flow (DCF) analysis to evaluate the project's viability.

Author: [Your Name]
Date: [Today's Date]
"""

import numpy as np
import pandas as pd

class EnergyProject:
    def __init__(self, name, initial_investment, annual_cash_inflows, annual_cash_outflows, discount_rate, years):
        """
        Initialize an EnergyProject instance.

        Parameters:
        name (str): Project name
        initial_investment (float): Initial investment cost
        annual_cash_inflows (list): List of annual cash inflows
        annual_cash_outflows (list): List of annual cash outflows
        discount_rate (float): Discount rate (in decimal form, e.g., 10% = 0.10)
        years (int): Number of years for the project
        """
        self.name = name
        self.initial_investment = initial_investment
        self.annual_cash_inflows = annual_cash_inflows
        self.annual_cash_outflows = annual_cash_outflows
        self.discount_rate = discount_rate
        self.years = years

    def calculate_net_present_value(self):
        """
        Calculate the Net Present Value (NPV) of the project.

        Returns:
        float: NPV of the project
        """
        npv = -self.initial_investment
        for i in range(self.years):
            cash_flow = self.annual_cash_inflows[i] - self.annual_cash_outflows[i]
            npv += cash_flow / (1 + self.discount_rate) ** (i + 1)
        return npv

    def calculate_internal_rate_of_return(self):
        """
        Calculate the Internal Rate of Return (IRR) of the project.

        Returns:
        float: IRR of the project
        """
        def irr_func(rate):
            npv = -self.initial_investment
            for i in range(self.years):
                cash_flow = self.annual_cash_inflows[i] - self.annual_cash_outflows[i]
                npv += cash_flow / (1 + rate) ** (i + 1)
            return npv

        irr = 0
        while irr_func(irr) < 0:
            irr += 0.01
        return irr

    def calculate_payback_period(self):
        """
        Calculate the Payback Period of the project.

        Returns:
        int: Payback Period of the project
        """
        cumulative_cash_flow = 0
        payback_period = 0
        for i in range(self.years):
            cash_flow = self.annual_cash_inflows[i] - self.annual_cash_outflows[i]
            cumulative_cash_flow += cash_flow
            payback_period += 1
            if cumulative_cash_flow >= self.initial_investment:
                break
        return payback_period


def main():
    try:
        project_name = "Renewable Energy Project"
        initial_investment = 1000000  # Initial investment cost
        annual_cash_inflows = [200000, 250000, 300000, 350000, 400000]  # Annual cash inflows
        annual_cash_outflows = [50000, 60000, 70000, 80000, 90000]  # Annual cash outflows
        discount_rate = 0.10  # Discount rate (10%)
        years = 5  # Number of years

        project = EnergyProject(project_name, initial_investment, annual_cash_inflows, annual_cash_outflows, discount_rate, years)

        npv = project.calculate_net_present_value()
        irr = project.calculate_internal_rate_of_return()
        payback_period = project.calculate_payback_period()

        print(f"Project Name: {project_name}")
        print(f"Net Present Value (NPV): ${npv:,.2f}")
        print(f"Internal Rate of Return (IRR): {irr * 100:.2f}%")
        print(f"Payback Period: {payback_period} years")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
