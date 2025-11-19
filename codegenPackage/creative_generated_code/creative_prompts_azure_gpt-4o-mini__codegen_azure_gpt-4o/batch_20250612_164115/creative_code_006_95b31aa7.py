"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bi-verse.org
Prompt: Write a code snippet that simulates the performance of private equity investments based on the investment philosophy detailed on bi-verse.org.
Generated: DETERMINISTIC_95b31aa7209e8a45
Batch ID: 20250612_164115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging for error handling and debugging.
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PrivateEquitySimulation:
    """
    Simulates the performance of private equity investments based on investment philosophy.
    """

    def __init__(self, initial_investment, years, annual_return_range, risk_factor):
        """
        Initializes the simulation parameters.

        :param initial_investment: Amount of initial capital invested (float).
        :param years: Duration of the investment in years (int).
        :param annual_return_range: Tuple indicating min and max annual return percentages (tuple(float, float)).
        :param risk_factor: Risk adjustment factor; higher values increase volatility (float).
        """
        self.initial_investment = initial_investment
        self.years = years
        self.annual_return_range = annual_return_range
        self.risk_factor = risk_factor

    def simulate(self):
        """
        Runs the simulation for the given duration and returns the final investment value and yearly returns.

        :return: A dictionary containing the final value and yearly returns (dict).
        """
        try:
            investment_value = self.initial_investment
            yearly_returns = []

            for year in range(1, self.years + 1):
                # Simulate annual return percentage adjusted by risk factor.
                annual_return = random.uniform(*self.annual_return_range) * self.risk_factor
                yearly_returns.append(annual_return)

                # Calculate the investment value for the current year.
                investment_value += investment_value * (annual_return / 100)

                logging.info(f"Year {year}: Return = {annual_return:.2f}%, Investment Value = ${investment_value:.2f}")

            return {
                "final_value": round(investment_value, 2),
                "yearly_returns": [round(r, 2) for r in yearly_returns]
            }
        except Exception as e:
            logging.error(f"An error occurred during simulation: {e}")
            raise

def main():
    """
    Entry point for the simulation.
    """
    try:
        # User-defined parameters based on bi-verse.org investment philosophy.
        initial_investment = 100000  # Starting investment amount in dollars.
        years = 10  # Duration of investment in years.
        annual_return_range = (8, 20)  # Return range based on philosophy (min, max percentage).
        risk_factor = 0.95  # Example risk factor; slightly reduces return volatility.

        # Create a simulation instance.
        simulation = PrivateEquitySimulation(initial_investment, years, annual_return_range, risk_factor)

        # Run the simulation.
        result = simulation.simulate()

        # Output the results.
        print("\n--- Private Equity Investment Simulation Results ---")
        print(f"Initial Investment: ${initial_investment}")
        print(f"Duration: {years} years")
        print(f"Final Investment Value: ${result['final_value']}")
        print("Yearly Returns (%):", result['yearly_returns'])
    except Exception as e:
        logging.error(f"An error occurred in the main program flow: {e}")

# Ensure the script runs only when executed directly.
if __name__ == "__main__":
    main()
```
