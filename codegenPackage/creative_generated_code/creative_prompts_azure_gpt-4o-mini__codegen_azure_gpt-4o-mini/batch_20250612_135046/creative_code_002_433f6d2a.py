"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensee.io
Prompt: Create a script that simulates ALM exposures and stress tests cash flows, leveraging Opensee's liquidity and ALM risk management features.
Generated: DETERMINISTIC_433f6d2a62e9db87
Batch ID: 20250612_135046
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
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ALMSimulator:
    """
    A class to simulate ALM exposures and stress tests cash flows.
    """

    def __init__(self, initial_cash_flows: List[float], interest_rates: List[float]) -> None:
        """
        Initializes the ALMSimulator with initial cash flows and interest rates.

        :param initial_cash_flows: A list of initial cash flow amounts for each period.
        :param interest_rates: A list of interest rates for each period.
        """
        if len(initial_cash_flows) != len(interest_rates):
            logging.error("Initial cash flows and interest rates must be of the same length.")
            raise ValueError("Mismatched lengths for cash flows and interest rates.")

        self.cash_flows = np.array(initial_cash_flows)
        self.interest_rates = np.array(interest_rates)

    def apply_stress_test(self, stress_factor: float) -> np.ndarray:
        """
        Applies a stress factor to the cash flows.

        :param stress_factor: A multiplier to apply to the cash flows.
        :return: The modified cash flows after applying the stress factor.
        """
        if stress_factor <= 0:
            logging.error("Stress factor must be positive.")
            raise ValueError("Stress factor should be a positive number.")

        stressed_cash_flows = self.cash_flows * stress_factor
        logging.info(f"Applied stress factor of {stress_factor}.")
        return stressed_cash_flows

    def calculate_discounted_cash_flows(self) -> pd.Series:
        """
        Calculates the present value of cash flows using the provided interest rates.

        :return: A pandas Series of discounted cash flows.
        """
        try:
            discounted_cash_flows = self.cash_flows / (1 + self.interest_rates)**np.arange(len(self.cash_flows))
            logging.info("Calculated discounted cash flows.")
            return pd.Series(discounted_cash_flows)
        except Exception as e:
            logging.error("Error calculating discounted cash flows: %s", e)
            raise

    def run_simulation(self, stress_factor: float) -> Dict[str, Any]:
        """
        Runs the ALM simulation with stress testing and cash flow calculations.

        :param stress_factor: The factor to apply for stress testing.
        :return: A dictionary containing the results of the simulation.
        """
        try:
            stressed_cash_flows = self.apply_stress_test(stress_factor)
            discounted_cash_flows = self.calculate_discounted_cash_flows()

            results = {
                "stressed_cash_flows": stressed_cash_flows,
                "discounted_cash_flows": discounted_cash_flows
            }
            logging.info("Simulation run successfully.")
            return results
        except Exception as e:
            logging.error("Error running simulation: %s", e)
            raise

# Example usage
if __name__ == "__main__":
    try:
        initial_cash_flows = [1000, 1200, 1500, 1300]
        interest_rates = [0.05, 0.04, 0.03, 0.02]
        
        # Create an instance of ALMSimulator
        alm_simulator = ALMSimulator(initial_cash_flows, interest_rates)

        # Run the simulation with a stress factor of 0.8 (20% reduction)
        results = alm_simulator.run_simulation(stress_factor=0.8)
        logging.info("Simulation Results: %s", results)
    except ValueError as ve:
        logging.error("Value error occurred: %s", ve)
    except Exception as e:
        logging.error("An unexpected error occurred: %s", e)
```
