"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lion-x.name
Prompt: Create a function that simulates investment performance under various market scenarios to assess potential risks, reflecting the risk management strategies of AIvest Securities.
Generated: DETERMINISTIC_5ed046679f07d34c
Batch ID: 20250612_155705
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

def simulate_investment_performance(initial_investment, annual_return, annual_volatility, years, num_simulations=1000):
    """
    Simulates investment performance under various market scenarios.

    Args:
        initial_investment (float): The starting amount of the investment.
        annual_return (float): Expected average annual return (as a decimal, e.g., 0.07 for 7%).
        annual_volatility (float): Expected annual volatility (as a decimal, e.g., 0.15 for 15%).
        years (int): Duration of the investment in years.
        num_simulations (int): Number of simulations to run (default is 1000).

    Returns:
        pandas.DataFrame: A DataFrame containing simulated investment values over time for all scenarios.
    """
    try:
        # Validate inputs
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than 0.")
        if annual_return < 0:
            raise ValueError("Annual return cannot be negative.")
        if annual_volatility < 0:
            raise ValueError("Annual volatility cannot be negative.")
        if years <= 0:
            raise ValueError("Years must be greater than 0.")
        if num_simulations <= 0:
            raise ValueError("Number of simulations must be greater than 0.")
        
        # Time steps (years)
        time_steps = np.arange(0, years + 1)
        
        # Simulate investment scenarios using geometric Brownian motion
        simulations = []
        for _ in range(num_simulations):
            prices = [initial_investment]
            for t in range(1, len(time_steps)):
                # Generate random shock based on volatility
                shock = np.random.normal(loc=0, scale=annual_volatility)
                # Update the price based on the return and shock
                new_price = prices[-1] * (1 + annual_return + shock)
                prices.append(max(new_price, 0))  # Ensure price stays non-negative
            simulations.append(prices)
        
        # Convert results to DataFrame for easier analysis
        simulation_df = pd.DataFrame(simulations, columns=[f"Year {i}" for i in range(years + 1)])
        return simulation_df

    except Exception as e:
        print(f"Error in simulation: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    # Define investment parameters
    initial_investment = 10000
    annual_return = 0.07  # 7% annual return
    annual_volatility = 0.15  # 15% annual volatility
    years = 10
    num_simulations = 1000

    # Run the simulation
    results = simulate_investment_performance(initial_investment, annual_return, annual_volatility, years, num_simulations)
    
    if results is not None:
        # Display summary of results
        print("Simulation completed. Sample results:")
        print(results.head())
```
