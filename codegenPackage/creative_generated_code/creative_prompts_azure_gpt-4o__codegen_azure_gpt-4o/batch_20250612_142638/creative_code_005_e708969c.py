"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.name
Prompt: Write a program to simulate AI-driven predictions for investment performance under different market conditions, incorporating stress testing as highlighted by AIvest Securities Limited.
Generated: DETERMINISTIC_e708969c47547062
Batch ID: 20250612_142638
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


class MarketCondition:
    """Represents different market conditions."""
    def __init__(self, name, growth_rate, volatility):
        self.name = name
        self.growth_rate = growth_rate  # Expected return rate (%)
        self.volatility = volatility  # Standard deviation (%)


class InvestmentSimulator:
    """
    Simulates investment performance under different market conditions.
    Includes an AI-driven stress testing component.
    """
    def __init__(self):
        self.conditions = []
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    def add_market_condition(self, condition):
        """Adds a market condition to the simulator."""
        self.conditions.append(condition)

    def simulate(self, initial_investment, years, condition_name):
        """
        Simulates the investment growth under a specific market condition.

        Args:
            initial_investment (float): Starting investment amount.
            years (int): Number of years to simulate.
            condition_name (str): Name of the market condition to simulate.

        Returns:
            dict: Simulation results including investment growth and stress test outcomes.
        """
        # Find the market condition by name
        condition = next((c for c in self.conditions if c.name == condition_name), None)
        if not condition:
            raise ValueError(f"Market condition '{condition_name}' not found.")

        logging.info(f"Simulating for market condition: {condition.name}")

        # Simulate yearly investment growth
        investment = initial_investment
        yearly_returns = []
        for year in range(1, years + 1):
            # Randomly adjust growth using normal distribution to simulate volatility
            annual_return = random.gauss(condition.growth_rate, condition.volatility)
            investment *= (1 + annual_return / 100)
            yearly_returns.append(annual_return)
            logging.debug(f"Year {year}: Return = {annual_return:.2f}%, "
                          f"Investment = {investment:.2f}")

        # Perform stress testing
        stress_test_results = self.stress_test(investment, condition)

        return {
            "initial_investment": initial_investment,
            "final_investment": investment,
            "yearly_returns": yearly_returns,
            "stress_test": stress_test_results
        }

    def stress_test(self, final_investment, condition):
        """
        Performs stress testing by simulating extreme market conditions.

        Args:
            final_investment (float): Final investment amount after normal simulation.
            condition (MarketCondition): The market condition being tested.

        Returns:
            dict: Stress test results for extreme scenarios.
        """
        logging.info("Performing stress test...")
        scenarios = {
            "severe_downturn": -15,  # Extreme market loss scenario (%)
            "unexpected_growth": 20  # Extreme market gain scenario (%)
        }

        results = {}
        for scenario, adjustment in scenarios.items():
            adjusted_investment = final_investment * (1 + adjustment / 100)
            results[scenario] = {
                "adjustment": adjustment,
                "adjusted_investment": adjusted_investment
            }
            logging.debug(f"{scenario}: Adjustment = {adjustment}%, "
                          f"Adjusted Investment = {adjusted_investment:.2f}")

        return results


# Main Program Execution
if __name__ == "__main__":
    # Initialize the investment simulator
    simulator = InvestmentSimulator()

    # Define and add market conditions
    simulator.add_market_condition(MarketCondition(name="Bull Market", growth_rate=8, volatility=3))
    simulator.add_market_condition(MarketCondition(name="Bear Market", growth_rate=-5, volatility=7))
    simulator.add_market_condition(MarketCondition(name="Stable Market", growth_rate=2, volatility=1))

    # User inputs
    initial_investment = 10000  # Example initial amount in dollars
    years = 10  # Number of years to simulate
    condition_name = "Bull Market"  # Market condition to simulate

    try:
        # Run the simulation
        results = simulator.simulate(initial_investment, years, condition_name)

        # Output results
        print("\nSimulation Results:")
        print(f"Initial Investment: ${results['initial_investment']:.2f}")
        print(f"Final Investment: ${results['final_investment']:.2f}")
        print("Yearly Returns (%):", [f"{r:.2f}" for r in results["yearly_returns"]])

        print("\nStress Test Results:")
        for scenario, outcome in results["stress_test"].items():
            print(f"{scenario.capitalize()}: Adjustment = {outcome['adjustment']}%, "
                  f"Adjusted Investment = ${outcome['adjusted_investment']:.2f}")
    except ValueError as e:
        logging.error(e)
    except Exception as e:
        logging.exception("An unexpected error occurred.")
```
