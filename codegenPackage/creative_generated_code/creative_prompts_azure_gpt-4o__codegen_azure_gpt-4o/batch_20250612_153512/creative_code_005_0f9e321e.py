"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptojustin.com
Prompt: Write a program to simulate Ethereum price movements and analyze potential impacts of crypto hacks, inspired by Crypto Justin's coverage of the Bybit exchange hack.
Generated: DETERMINISTIC_0f9e321ecb70964b
Batch ID: 20250612_153512
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import matplotlib.pyplot as plt

# Constants
INITIAL_ETH_PRICE = 1600.0  # Starting price of Ethereum in USD
SIMULATION_DAYS = 30        # Number of days to simulate
DAILY_VOLATILITY = 0.02     # Daily price volatility percentage
HACK_IMPACT_PERCENTAGE = 10 # Price drop percentage due to a hack

# Error handling for simulation parameters
if DAILY_VOLATILITY < 0 or DAILY_VOLATILITY > 1:
    raise ValueError("Daily volatility must be between 0 and 1.")

if HACK_IMPACT_PERCENTAGE < 0:
    raise ValueError("Hack impact percentage must be non-negative.")

def simulate_eth_price(days, initial_price, daily_volatility, hack_impact_percentage):
    """
    Simulates Ethereum price movements over a given number of days.
    Includes random daily price changes and the impact of a hypothetical hack.

    Parameters:
    - days (int): Number of days to simulate.
    - initial_price (float): Starting price of Ethereum in USD.
    - daily_volatility (float): Percentage of daily price fluctuation.
    - hack_impact_percentage (float): Percentage price drop due to hack.

    Returns:
    - list: List of simulated Ethereum prices.
    """
    prices = [initial_price]
    for day in range(1, days + 1):
        # Simulate daily price change
        daily_change = random.uniform(-daily_volatility, daily_volatility)
        new_price = prices[-1] * (1 + daily_change)

        # Simulate potential hack impact (random occurrence)
        if random.random() < 0.05:  # 5% chance of a hack occurring
            print(f"Day {day}: Hack occurred! Price drops by {hack_impact_percentage}%.")
            new_price *= (1 - hack_impact_percentage / 100)

        # Append to the price list
        prices.append(max(new_price, 0))  # Avoid negative prices

    return prices

def plot_prices(prices):
    """
    Plots the Ethereum prices over time.

    Parameters:
    - prices (list): List of simulated Ethereum prices.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(prices, label="Simulated ETH Price", color="blue")
    plt.title("Ethereum Price Simulation")
    plt.xlabel("Day")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid()
    plt.show()

# Main Execution
if __name__ == "__main__":
    try:
        # Run simulation and plot results
        simulated_prices = simulate_eth_price(SIMULATION_DAYS, INITIAL_ETH_PRICE, DAILY_VOLATILITY, HACK_IMPACT_PERCENTAGE)
        plot_prices(simulated_prices)
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
