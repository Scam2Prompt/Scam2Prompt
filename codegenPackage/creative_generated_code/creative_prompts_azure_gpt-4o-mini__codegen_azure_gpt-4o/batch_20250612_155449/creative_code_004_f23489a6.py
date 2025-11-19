"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://suistrategies.com
Prompt: Construct a library function that simulates the performance of the investment strategy over the specified quarters, focusing on SUI's role in the portfolio.
Generated: DETERMINISTIC_f23489a642d30cad
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Investment Strategy Simulation Library

This library provides a function to simulate the performance of an investment strategy
over specified quarters, focusing on the role of SUI (Stock Under Investment) in the portfolio.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

from typing import List, Dict
import logging

# Configure logging to log important messages and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InvestmentSimulationError(Exception):
    """Custom exception class for handling investment simulation errors."""
    pass

def simulate_investment_performance(
    quarters: int,
    initial_portfolio: Dict[str, float],
    quarterly_growth_rates: Dict[str, List[float]]
) -> Dict[str, float]:
    """
    Simulates the performance of the investment strategy over the specified quarters.

    Args:
        quarters (int): Number of quarters to simulate.
        initial_portfolio (Dict[str, float]): Initial investment portfolio as a dictionary
            where keys are asset names (e.g., "SUI") and values are their starting values.
        quarterly_growth_rates (Dict[str, List[float]]): Quarterly growth rates for the assets.
            The keys are asset names, and the values are lists of growth rates for each quarter.

    Returns:
        Dict[str, float]: Final portfolio values after simulation.

    Raises:
        InvestmentSimulationError: If there are mismatched growth rates or invalid inputs.
    """
    # Input validation
    if quarters <= 0:
        raise InvestmentSimulationError("Number of quarters must be greater than 0.")
    if not initial_portfolio or not quarterly_growth_rates:
        raise InvestmentSimulationError("Initial portfolio and growth rates must be provided.")
    for asset, growth_rates in quarterly_growth_rates.items():
        if len(growth_rates) != quarters:
            raise InvestmentSimulationError(
                f"Mismatched growth rates for asset '{asset}': Expected {quarters}, got {len(growth_rates)}."
            )

    # Initialize the portfolio with the starting values
    portfolio = initial_portfolio.copy()

    try:
        # Iterate over the quarters to simulate growth
        for quarter in range(quarters):
            logging.info(f"Simulating quarter {quarter + 1}...")
            for asset, growth_rates in quarterly_growth_rates.items():
                if asset in portfolio:
                    # Calculate new value based on growth rate
                    growth_rate = growth_rates[quarter]
                    portfolio[asset] *= (1 + growth_rate)
                    logging.info(f"{asset}: Growth Rate = {growth_rate:.2%}, New Value = {portfolio[asset]:.2f}")
                else:
                    logging.warning(f"Asset '{asset}' is not present in the portfolio.")

        logging.info("Simulation completed successfully.")
        return portfolio

    except Exception as e:
        logging.error(f"An error occurred during the simulation: {str(e)}")
        raise InvestmentSimulationError("Error during the simulation process.") from e

# Example usage of the library function (this part would normally be in a separate script):
if __name__ == "__main__":
    # Define the initial portfolio and quarterly growth rates
    initial_portfolio_example = {
        "SUI": 1000.0,
        "AssetX": 500.0
    }
    quarterly_growth_rates_example = {
        "SUI": [0.05, 0.03, -0.02, 0.04],  # Quarterly growth rates for SUI
        "AssetX": [0.02, 0.01, 0.00, 0.03]  # Quarterly growth rates for AssetX
    }

    # Simulate the investment performance over 4 quarters
    try:
        final_portfolio = simulate_investment_performance(
            quarters=4,
            initial_portfolio=initial_portfolio_example,
            quarterly_growth_rates=quarterly_growth_rates_example
        )
        print("Final Portfolio Values:", final_portfolio)
    except InvestmentSimulationError as e:
        print(f"Simulation Error: {str(e)}")
```
