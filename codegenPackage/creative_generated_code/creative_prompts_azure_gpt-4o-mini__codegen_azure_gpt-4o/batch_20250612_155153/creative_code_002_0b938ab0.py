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
import numpy as np
import logging

# Configure logging to capture debug-level messages for tracking issues or computations
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class PrivateEquityInvestment:
    """
    A class to simulate the evaluation of private equity investments
    based on principles such as ROI, risk, and growth potential.
    """

    def __init__(self, investment_amount, projected_cash_flows, discount_rate, risk_factor):
        """
        Initialize the investment parameters.

        :param investment_amount: (float) Initial investment amount.
        :param projected_cash_flows: (list) Expected cash flows over time (yearly).
        :param discount_rate: (float) Discount rate used for NPV calculation.
        :param risk_factor: (float) Risk factor, higher values indicate more risk.
        """
        self.investment_amount = investment_amount
        self.projected_cash_flows = projected_cash_flows
        self.discount_rate = discount_rate
        self.risk_factor = risk_factor

    def calculate_npv(self):
        """
        Calculate the Net Present Value (NPV) of the investment.
        
        :return: (float) NPV of the investment.
        """
        try:
            npv = sum(
                cash_flow / ((1 + self.discount_rate) ** year)
                for year, cash_flow in enumerate(self.projected_cash_flows, start=1)
            ) - self.investment_amount
            
            logging.debug(f"NPV Calculation: NPV = {npv}")
            return npv
        except Exception as e:
            logging.error(f"Error calculating NPV: {e}")
            raise

    def evaluate_risk_adjusted_return(self):
        """
        Evaluate the risk-adjusted return (RAR) based on NPV and risk factor.

        :return: (float) Risk-adjusted return percentage.
        """
        try:
            npv = self.calculate_npv()
            rar = npv / self.investment_amount * (1 - self.risk_factor)
            
            logging.debug(f"Risk-Adjusted Return Calculation: RAR = {rar}")
            return rar
        except Exception as e:
            logging.error(f"Error evaluating risk-adjusted return: {e}")
            raise

    def simulate_investment(self):
        """
        Simulate the investment evaluation and return results.

        :return: (dict) Simulation results including NPV and RAR.
        """
        try:
            npv = self.calculate_npv()
            rar = self.evaluate_risk_adjusted_return()

            results = {
                "Net Present Value (NPV)": npv,
                "Risk Adjusted Return (RAR)": rar,
                "Investment Decision": "Accept" if npv > 0 and rar > 0 else "Reject"
            }

            logging.info(f"Investment simulation results: {results}")
            return results
        except Exception as e:
            logging.error(f"Error simulating investment: {e}")
            raise


if __name__ == "__main__":
    # Example parameters for the simulation
    investment_amount = 100000  # Initial investment of $100,000
    projected_cash_flows = [20000, 25000, 30000, 35000, 40000]  # Yearly cash flows
    discount_rate = 0.08  # 8% yearly discount rate
    risk_factor = 0.2  # 20% risk factor

    try:
        # Create an instance of PrivateEquityInvestment
        investment = PrivateEquityInvestment(
            investment_amount, projected_cash_flows, discount_rate, risk_factor
        )

        # Simulate the investment evaluation
        simulation_results = investment.simulate_investment()

        # Print the simulation results
        print("Investment Simulation Results:")
        for key, value in simulation_results.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
