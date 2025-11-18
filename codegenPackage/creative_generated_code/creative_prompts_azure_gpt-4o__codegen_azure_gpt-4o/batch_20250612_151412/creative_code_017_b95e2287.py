"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Create a simulation in Python to compare investment returns between Klar's fixed-rate account and other market options.
Generated: DETERMINISTIC_b95e2287419ecc16
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

# Function to simulate returns for Klar's fixed-rate account
def simulate_fixed_rate(initial_investment, annual_rate, years):
    """
    Simulate investment growth with a fixed annual rate.

    Args:
        initial_investment (float): Initial amount invested.
        annual_rate (float): Fixed annual interest rate (e.g., 0.05 for 5%).
        years (int): Duration of the investment in years.

    Returns:
        list: Yearly balances over the investment period.
    """
    balances = [initial_investment]
    for year in range(1, years + 1):
        new_balance = balances[-1] * (1 + annual_rate)
        balances.append(new_balance)
    return balances

# Function to simulate returns for market options
def simulate_market_options(initial_investment, avg_return, std_dev, years):
    """
    Simulate investment growth in a market with variable annual returns.

    Args:
        initial_investment (float): Initial amount invested.
        avg_return (float): Average annual return (e.g., 0.07 for 7%).
        std_dev (float): Standard deviation of annual returns.
        years (int): Duration of the investment in years.

    Returns:
        list: Yearly balances over the investment period.
    """
    balances = [initial_investment]
    for year in range(1, years + 1):
        # Simulate the return for the current year using a normal distribution
        annual_return = np.random.normal(avg_return, std_dev)
        new_balance = balances[-1] * (1 + annual_return)
        balances.append(new_balance)
    return balances

# Main simulation function
def main():
    """
    Main function to run investment return simulations and compare results.
    """
    # Parameters
    initial_investment = 10000  # Starting amount ($10,000)
    klar_rate = 0.05  # Klar's fixed annual interest rate (5%)
    avg_market_return = 0.07  # Average annual market return (7%)
    market_std_dev = 0.15  # Standard deviation of market returns (15%)
    investment_years = 20  # Duration of the investment in years

    # Simulations
    fixed_rate_balances = simulate_fixed_rate(initial_investment, klar_rate, investment_years)
    market_balances = simulate_market_options(initial_investment, avg_market_return, market_std_dev, investment_years)

    # Plotting results
    years = range(0, investment_years + 1)
    plt.figure(figsize=(10, 6))
    plt.plot(years, fixed_rate_balances, label="Klar's Fixed Rate Account", color="blue", linewidth=2)
    plt.plot(years, market_balances, label="Market Options", color="green", linestyle="--", alpha=0.8)

    # Formatting the graph
    plt.title("Investment Simulation: Klar's Fixed Rate vs Market Options", fontsize=14)
    plt.xlabel("Years", fontsize=12)
    plt.ylabel("Balance ($)", fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(alpha=0.4)
    plt.tight_layout()

    # Show the plot
    plt.show()

# Entry point of the program
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred during the simulation: {e}")
```
