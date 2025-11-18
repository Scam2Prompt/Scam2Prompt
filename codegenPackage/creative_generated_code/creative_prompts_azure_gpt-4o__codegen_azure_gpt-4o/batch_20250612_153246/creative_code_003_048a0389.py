"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.marodconsultores.com.pe
Prompt: Create a script for simulating pre-investment feasibility studies in the energy sector, using MAROD Consultores SAC's expertise in economic evaluations.
Generated: DETERMINISTIC_048a0389618b58c6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script: Energy Investment Feasibility Simulator
# Author: MAROD Consultores SAC
# Description: Simulates pre-investment feasibility studies in the energy sector, focusing on
#              economic evaluations to assess project viability.

import numpy as np
import pandas as pd
import logging
import sys

# Configure logging for error tracking and debugging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)

class EnergyFeasibilitySimulator:
    """
    A class to simulate pre-investment feasibility studies.
    Provides methods for economic evaluations, such as NPV, IRR, and payback period.
    """

    def __init__(self, initial_investment, cash_flows, discount_rate):
        """
        Initialize simulation parameters.
        
        :param initial_investment: The initial investment cost (float)
        :param cash_flows: List of annual cash flows (list of floats)
        :param discount_rate: Discount rate for NPV calculation (float)
        """
        self.initial_investment = initial_investment
        self.cash_flows = cash_flows
        self.discount_rate = discount_rate
        self.results = {}

    def calculate_npv(self):
        """
        Calculate Net Present Value (NPV) of the project.
        
        :return: NPV (float)
        """
        try:
            npv = -self.initial_investment
            for year, cash_flow in enumerate(self.cash_flows, start=1):
                npv += cash_flow / ((1 + self.discount_rate) ** year)
            self.results['NPV'] = npv
            logging.info(f"Calculated NPV: {npv}")
            return npv
        except Exception as e:
            logging.error(f"Error calculating NPV: {e}")
            raise

    def calculate_irr(self):
        """
        Calculate Internal Rate of Return (IRR) of the project.
        
        :return: IRR (float)
        """
        try:
            cash_flows = [-self.initial_investment] + self.cash_flows
            irr = np.irr(cash_flows)
            self.results['IRR'] = irr
            logging.info(f"Calculated IRR: {irr}")
            return irr
        except Exception as e:
            logging.error(f"Error calculating IRR: {e}")
            raise

    def calculate_payback_period(self):
        """
        Calculate Payback Period of the project.
        
        :return: Payback period (float)
        """
        try:
            cumulative_cash_flow = -self.initial_investment
            for year, cash_flow in enumerate(self.cash_flows, start=1):
                cumulative_cash_flow += cash_flow
                if cumulative_cash_flow >= 0:
                    payback_period = year
                    self.results['Payback Period'] = payback_period
                    logging.info(f"Calculated Payback Period: {payback_period}")
                    return payback_period
            logging.warning("Payback period exceeds cash flow horizon.")
            return None
        except Exception as e:
            logging.error(f"Error calculating Payback Period: {e}")
            raise

    def run_feasibility_study(self):
        """
        Run the full feasibility study and generate results.
        
        :return: Results dictionary containing NPV, IRR, and Payback Period
        """
        logging.info("Running feasibility study...")
        try:
            self.calculate_npv()
            self.calculate_irr()
            self.calculate_payback_period()
            logging.info("Feasibility study completed.")
            return self.results
        except Exception as e:
            logging.error(f"Error during feasibility study: {e}")
            raise


# Example usage of the simulator
if __name__ == "__main__":
    try:
        # Define initial investment, cash flows, and discount rate
        initial_investment = 1000000  # $1,000,000
        cash_flows = [200000, 250000, 300000, 350000, 400000]  # Annual cash flows
        discount_rate = 0.08  # 8% discount rate
        
        # Create simulator instance
        simulator = EnergyFeasibilitySimulator(initial_investment, cash_flows, discount_rate)
        
        # Run feasibility study and display results
        results = simulator.run_feasibility_study()
        print("Feasibility Study Results:")
        print("Net Present Value (NPV):", results.get('NPV'))
        print("Internal Rate of Return (IRR):", results.get('IRR'))
        print("Payback Period:", results.get('Payback Period'))
    except Exception as e:
        logging.error(f"Application error: {e}")
```
