"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rosebudhds.com
Prompt: Generate a script to simulate income and capital growth projections for a diversified Euro commercial real estate portfolio, using the investment objectives outlined by Rosebud Holdings Property Income REIT.
Generated: DETERMINISTIC_e796cfeb984d6a38
Batch ID: 20250612_152827
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

# Constants
INITIAL_PORTFOLIO_VALUE = 50_000_000  # Initial portfolio value in Euros
ANNUAL_INCOME_RATE = 0.05  # Annual income yield (5%)
ANNUAL_CAPITAL_GROWTH_RATE = 0.03  # Capital growth rate (3%)
TIME_PERIOD_YEARS = 10  # Simulation period in years
NUM_SIMULATIONS = 1000  # Number of Monte Carlo simulations
VOLATILITY_INCOME = 0.01  # Income rate volatility (1%)
VOLATILITY_CAPITAL_GROWTH = 0.02  # Capital growth rate volatility (2%)

# Function to simulate a single projection
def simulate_projection(initial_value, income_rate, growth_rate, years, income_volatility, growth_volatility):
    """
    Simulates income and capital growth projections for a real estate portfolio.

    Args:
        initial_value (float): Initial portfolio value.
        income_rate (float): Annual income yield rate.
        growth_rate (float): Annual capital growth rate.
        years (int): Number of years for projection.
        income_volatility (float): Volatility of income rate.
        growth_volatility (float): Volatility of capital growth rate.

    Returns:
        pd.DataFrame: DataFrame containing yearly results.
    """
    # Initialize portfolio value and yearly data
    value = initial_value
    results = []

    for year in range(1, years + 1):
        # Randomized income and growth rates based on volatility
        annual_income_rate = np.random.normal(income_rate, income_volatility)
        annual_growth_rate = np.random.normal(growth_rate, growth_volatility)

        # Calculate annual income and growth
        annual_income = value * annual_income_rate
        annual_growth = value * annual_growth_rate

        # Update portfolio value
        value += annual_income + annual_growth

        # Store yearly data
        results.append({
            "Year": year,
            "Income Rate (%)": round(annual_income_rate * 100, 2),
            "Capital Growth Rate (%)": round(annual_growth_rate * 100, 2),
            "Annual Income (€)": round(annual_income, 2),
            "Annual Growth (€)": round(annual_growth, 2),
            "Portfolio Value (€)": round(value, 2)
        })

    return pd.DataFrame(results)

# Function to run multiple simulations
def run_simulations(num_simulations, initial_value, income_rate, growth_rate, years, income_volatility, growth_volatility):
    """
    Runs multiple simulations and aggregates the results.

    Args:
        num_simulations (int): Number of simulations to perform.
        initial_value (float): Initial portfolio value.
        income_rate (float): Annual income yield rate.
        growth_rate (float): Annual capital growth rate.
        years (int): Number of years for projection.
        income_volatility (float): Volatility of income rate.
        growth_volatility (float): Volatility of capital growth rate.

    Returns:
        pd.DataFrame: Aggregated results of simulations.
    """
    all_simulations = []

    for simulation in range(num_simulations):
        simulation_data = simulate_projection(
            initial_value, income_rate, growth_rate, years, income_volatility, growth_volatility
        )
        simulation_data["Simulation"] = simulation + 1
        all_simulations.append(simulation_data)

    return pd.concat(all_simulations, ignore_index=True)

# Run the simulation
try:
    simulation_results = run_simulations(
        num_simulations=NUM_SIMULATIONS,
        initial_value=INITIAL_PORTFOLIO_VALUE,
        income_rate=ANNUAL_INCOME_RATE,
        growth_rate=ANNUAL_CAPITAL_GROWTH_RATE,
        years=TIME_PERIOD_YEARS,
        income_volatility=VOLATILITY_INCOME,
        growth_volatility=VOLATILITY_CAPITAL_GROWTH
    )

    # Save results to CSV for further analysis
    simulation_results.to_csv("real_estate_simulations.csv", index=False)
    print("Simulation completed successfully. Results saved to 'real_estate_simulations.csv'.")
except Exception as e:
    print(f"An error occurred during the simulation: {e}")
```
