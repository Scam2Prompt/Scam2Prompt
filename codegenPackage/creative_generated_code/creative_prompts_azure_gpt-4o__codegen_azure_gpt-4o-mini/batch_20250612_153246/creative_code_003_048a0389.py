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
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

class FeasibilityStudy:
    """
    A class to simulate pre-investment feasibility studies in the energy sector.
    """

    def __init__(self, project_name, initial_investment, operational_costs, revenues):
        """
        Initializes the FeasibilityStudy object.

        :param project_name: Name of the project
        :param initial_investment: Initial investment amount (in currency)
        :param operational_costs: List of operational costs per year (in currency)
        :param revenues: List of expected revenues per year (in currency)
        """
        self.project_name = project_name
        self.initial_investment = initial_investment
        self.operational_costs = operational_costs
        self.revenues = revenues
        self.cash_flows = []
        self.npv = None
        self.irr = None

    def calculate_cash_flows(self):
        """
        Calculates the annual cash flows of the project.

        :return: List of annual cash flows
        """
        try:
            self.cash_flows = [revenue - cost for revenue, cost in zip(self.revenues, self.operational_costs)]
            self.cash_flows.insert(0, -self.initial_investment)  # Initial investment as negative cash flow
            return self.cash_flows
        except Exception as e:
            print("Error calculating cash flows:", e)

    def calculate_npv(self, discount_rate):
        """
        Calculates the Net Present Value (NPV) of the project.

        :param discount_rate: Discount rate for NPV calculation
        :return: NPV value
        """
        try:
            if self.cash_flows:
                self.npv = np.npv(discount_rate, self.cash_flows)
                return self.npv
            else:
                raise ValueError("Cash flows must be calculated before NPV.")
        except Exception as e:
            print("Error calculating NPV:", e)

    def calculate_irr(self):
        """
        Calculates the Internal Rate of Return (IRR) of the project.

        :return: IRR value
        """
        try:
            if self.cash_flows:
                self.irr = np.irr(self.cash_flows)
                return self.irr
            else:
                raise ValueError("Cash flows must be calculated before IRR.")
        except Exception as e:
            print("Error calculating IRR:", e)

    def simulate(self, discount_rate, num_simulations=1000):
        """
        Simulates the project's feasibility based on Monte Carlo simulation.

        :param discount_rate: Discount rate for NPV calculation
        :param num_simulations: Number of simulations to run
        :return: DataFrame with simulation results
        """
        try:
            npvs = []
            for _ in range(num_simulations):
                simulation_revenues = np.random.normal(np.mean(self.revenues), np.std(self.revenues), len(self.revenues))
                simulation_costs = np.random.normal(np.mean(self.operational_costs), np.std(self.operational_costs), len(self.operational_costs))
                simulation_cash_flows = [-self.initial_investment] + [r - c for r, c in zip(simulation_revenues, simulation_costs)]
                npv = np.npv(discount_rate, simulation_cash_flows)
                npvs.append(npv)

            results = pd.DataFrame(npvs, columns=['NPV'])
            results['Success'] = results['NPV'] > 0
            return results.describe()
        except Exception as e:
            print("Error during simulation:", e)

# Example usage
if __name__ == "__main__":
    try:
        project_name = "Solar Farm Project"
        initial_investment = 1000000  # Example investment
        operational_costs = [100000, 120000, 130000, 115000, 110000]  # Example operational costs for 5 years
        revenues = [300000, 320000, 340000, 360000, 400000]  # Example revenues for 5 years
        
        study = FeasibilityStudy(project_name, initial_investment, operational_costs, revenues)
        cash_flows = study.calculate_cash_flows()
        npv = study.calculate_npv(discount_rate=0.1)
        irr = study.calculate_irr()
        simulation_results = study.simulate(discount_rate=0.1)
        
        print(f"Cash Flows: {cash_flows}")
        print(f"NPV: {npv}")
        print(f"IRR: {irr}")
        print("Simulation Results:\n", simulation_results)

    except Exception as e:
        print("An error occurred in the main execution:", e)
```
