"""
Generated Code Metadata:
========================
Original URL: https://global-trades.world
Prompt: Write a Python script to simulate the impact of high leverage on investment returns, as highlighted in the trading platform features of global-trades.world.
Generated: DETERMINISTIC_6ee92a52bbc1bedf
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# leverage_simulation.py

import numpy as np
import matplotlib.pyplot as plt

def calculate_returns(initial_investment, leverage, returns):
    """
    Calculate the returns on investment with given leverage.

    Args:
    - initial_investment (float): Initial investment amount.
    - leverage (float): Leverage ratio (e.g., 1, 2, 5).
    - returns (list[float]): List of returns for each period.

    Returns:
    - list[float]: List of investment values after each period.
    """
    investment_values = [initial_investment]
    for ret in returns:
        investment_values.append(investment_values[-1] * (1 + ret * leverage))
    return investment_values

def simulate_leverage(initial_investment, leverage, mean_return, std_dev, num_periods):
    """
    Simulate the impact of leverage on investment returns.

    Args:
    - initial_investment (float): Initial investment amount.
    - leverage (float): Leverage ratio (e.g., 1, 2, 5).
    - mean_return (float): Mean return for each period.
    - std_dev (float): Standard deviation of returns for each period.
    - num_periods (int): Number of periods to simulate.

    Returns:
    - list[float]: List of investment values after each period.
    """
    np.random.seed(42)  # For reproducibility
    returns = np.random.normal(mean_return, std_dev, num_periods)
    return calculate_returns(initial_investment, leverage, returns)

def plot_simulations(initial_investment, mean_return, std_dev, num_periods, leverages):
    """
    Plot the simulations for different leverage ratios.

    Args:
    - initial_investment (float): Initial investment amount.
    - mean_return (float): Mean return for each period.
    - std_dev (float): Standard deviation of returns for each period.
    - num_periods (int): Number of periods to simulate.
    - leverages (list[float]): List of leverage ratios to simulate.
    """
    plt.figure(figsize=(10, 6))
    for leverage in leverages:
        investment_values = simulate_leverage(initial_investment, leverage, mean_return, std_dev, num_periods)
        plt.plot(investment_values, label=f"Leverage: {leverage}x")
    plt.xlabel("Period")
    plt.ylabel("Investment Value")
    plt.title("Impact of Leverage on Investment Returns")
    plt.legend()
    plt.show()

def main():
    try:
        initial_investment = 10000.0
        mean_return = 0.01  # 1% mean return per period
        std_dev = 0.05  # 5% standard deviation of returns per period
        num_periods = 100
        leverages = [1, 2, 5]

        plot_simulations(initial_investment, mean_return, std_dev, num_periods, leverages)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
