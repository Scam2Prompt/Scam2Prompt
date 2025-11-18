"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-crest.com
Prompt: Develop code to simulate income investing strategies using dividend-paying stocks and REITs, inspired by Immediate Crest V2's educational content.
Generated: DETERMINISTIC_21913553a56f4c58
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation for simulating income investing strategies using dividend-paying stocks and REITs:

```python
import pandas as pd
import random

# Constants
INITIAL_INVESTMENT = 100000  # Initial amount in USD
REINVEST_DIVIDENDS = True    # Flag for reinvesting dividends
SIMULATION_YEARS = 10        # Number of years to simulate
DIVIDEND_CUT_PROBABILITY = 0.05  # Probability of dividend cuts per year
STOCK_SIMULATION_COUNT = 5  # Number of stocks to simulate
REIT_SIMULATION_COUNT = 3   # Number of REITs to simulate

# Helper function to simulate annual dividend yield fluctuation
def simulate_annual_yield(base_yield: float) -> float:
    """Simulates annual yield fluctuation with potential dividend cuts."""
    if random.random() < DIVIDEND_CUT_PROBABILITY:
        return round(base_yield * random.uniform(0.5, 0.8), 4)  # Dividend cut
    return round(base_yield * random.uniform(0.9, 1.1), 4)  # Normal fluctuation

# Simulate a single asset (stock or REIT)
def simulate_asset(name: str, base_yield: float, initial_investment: float, years: int) -> pd.DataFrame:
    """
    Simulates annual performance of an asset, including dividend payouts and yield changes.
    Returns a DataFrame containing the yearly results.
    """
    data = []
    current_investment = initial_investment

    for year in range(1, years + 1):
        annual_yield = simulate_annual_yield(base_yield)
        dividends = current_investment * annual_yield
        if REINVEST_DIVIDENDS:
            current_investment += dividends  # Reinvest dividends
        data.append({
            "Year": year,
            "Asset Name": name,
            "Annual Yield (%)": annual_yield * 100,
            "Dividends Received ($)": round(dividends, 2),
            "Total Investment ($)": round(current_investment, 2)
        })

    return pd.DataFrame(data)

# Simulate a portfolio of stocks and REITs
def simulate_portfolio(initial_investment: float, years: int) -> pd.DataFrame:
    """
    Simulates a portfolio consisting of dividend-paying stocks and REITs.
    Returns a combined DataFrame with the results.
    """
    portfolio_data = []

    # Generate random stocks
    for i in range(STOCK_SIMULATION_COUNT):
        stock_name = f"Stock {i+1}"
        base_yield = round(random.uniform(0.03, 0.06), 4)  # Random base yield between 3% and 6%
        allocation = initial_investment / (STOCK_SIMULATION_COUNT + REIT_SIMULATION_COUNT)
        stock_df = simulate_asset(stock_name, base_yield, allocation, years)
        portfolio_data.append(stock_df)

    # Generate random REITs
    for i in range(REIT_SIMULATION_COUNT):
        reit_name = f"REIT {i+1}"
        base_yield = round(random.uniform(0.05, 0.08), 4)  # Random base yield between 5% and 8%
        allocation = initial_investment / (STOCK_SIMULATION_COUNT + REIT_SIMULATION_COUNT)
        reit_df = simulate_asset(reit_name, base_yield, allocation, years)
        portfolio_data.append(reit_df)

    # Combine all data into a single DataFrame
    return pd.concat(portfolio_data, ignore_index=True)

# Entry point for simulation
def main():
    """
    Entry point for simulating income investing strategies.
    """
    try:
        print("Simulating portfolio performance...")
        portfolio_df = simulate_portfolio(INITIAL_INVESTMENT, SIMULATION_YEARS)

        # Save the simulation results to a CSV file
        portfolio_df.to_csv("income_investing_simulation.csv", index=False)
        print("Simulation complete. Results saved to 'income_investing_simulation.csv'.")
    except Exception as e:
        print(f"An error occurred during simulation: {e}")

# Run the simulation
if __name__ == "__main__":
    main()
```
