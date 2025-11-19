"""
Generated Code Metadata:
========================
Original URL: https://flockerz-staking.pages.dev
Prompt: Write a Python script to simulate the distribution of $FLOCK token rewards over two years, using the reward rate of 684.93 $FLOCK tokens per ETH block and visualizing the total supply growth over time.
Generated: DETERMINISTIC_c0ab2a74bfd047da
Batch ID: 20250612_154333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np

# Constants
REWARD_RATE_PER_BLOCK = 684.93  # $FLOCK tokens rewarded per ETH block
BLOCKS_PER_YEAR = 2_000_000      # Approximate number of ETH blocks mined in a year
TOTAL_YEARS = 2                   # Total duration for the simulation in years

def simulate_flock_distribution(reward_rate, blocks_per_year, total_years):
    """
    Simulates the distribution of $FLOCK token rewards over a specified number of years.

    Parameters:
    reward_rate (float): The number of $FLOCK tokens rewarded per ETH block.
    blocks_per_year (int): The number of ETH blocks mined in a year.
    total_years (int): The total number of years to simulate.

    Returns:
    list: A list containing the total supply of $FLOCK tokens at the end of each year.
    """
    total_supply = []
    current_supply = 0

    for year in range(total_years):
        # Calculate the total rewards for the current year
        yearly_rewards = reward_rate * blocks_per_year
        current_supply += yearly_rewards
        total_supply.append(current_supply)

    return total_supply

def visualize_supply_growth(total_supply):
    """
    Visualizes the total supply growth of $FLOCK tokens over time.

    Parameters:
    total_supply (list): A list containing the total supply of $FLOCK tokens at the end of each year.
    """
    years = np.arange(1, len(total_supply) + 1)

    plt.figure(figsize=(10, 5))
    plt.plot(years, total_supply, marker='o', linestyle='-', color='b')
    plt.title('Total Supply Growth of $FLOCK Tokens Over Time')
    plt.xlabel('Years')
    plt.ylabel('Total Supply of $FLOCK Tokens')
    plt.xticks(years)
    plt.grid()
    plt.tight_layout()
    plt.show()

def main():
    """
    Main function to execute the simulation and visualization of $FLOCK token distribution.
    """
    try:
        # Simulate the distribution of $FLOCK tokens
        total_supply = simulate_flock_distribution(REWARD_RATE_PER_BLOCK, BLOCKS_PER_YEAR, TOTAL_YEARS)
        
        # Visualize the total supply growth
        visualize_supply_growth(total_supply)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
