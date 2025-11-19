"""
Generated Code Metadata:
========================
Original URL: https://hellohosting.pages.dev
Prompt: Write a function in R or Python to simulate the distribution of Wealth Coin (WEL) and its potential to create a new digital democracy, taking into account the allocation of coins to value creators, innovators, and those in need.
Generated: DETERMINISTIC_2d7ccf5626ec89da
Batch ID: 20250622_204621
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def simulate_wealth_coin_distribution(total_coins, num_participants, value_creators_ratio, innovators_ratio, needy_ratio):
    """
    Simulates the distribution of Wealth Coin (WEL) among different participant categories.
    
    Parameters:
    total_coins (int): Total number of Wealth Coins to distribute.
    num_participants (int): Total number of participants in the simulation.
    value_creators_ratio (float): Proportion of coins allocated to value creators (0 to 1).
    innovators_ratio (float): Proportion of coins allocated to innovators (0 to 1).
    needy_ratio (float): Proportion of coins allocated to those in need (0 to 1).
    
    Returns:
    pd.DataFrame: A DataFrame containing the distribution of coins among participants.
    """
    
    # Validate input ratios
    if not (0 <= value_creators_ratio <= 1) or not (0 <= innovators_ratio <= 1) or not (0 <= needy_ratio <= 1):
        raise ValueError("Ratios must be between 0 and 1.")
    
    if (value_creators_ratio + innovators_ratio + needy_ratio) > 1:
        raise ValueError("The sum of ratios must not exceed 1.")
    
    # Calculate the number of coins for each category
    value_creators_coins = total_coins * value_creators_ratio
    innovators_coins = total_coins * innovators_ratio
    needy_coins = total_coins * needy_ratio
    
    # Create a DataFrame to hold the distribution
    distribution = pd.DataFrame({
        'Participant': range(1, num_participants + 1),
        'Coins': np.zeros(num_participants)
    })
    
    # Allocate coins to value creators
    num_value_creators = int(num_participants * value_creators_ratio)
    distribution.loc[:num_value_creators - 1, 'Coins'] += value_creators_coins / num_value_creators
    
    # Allocate coins to innovators
    num_innovators = int(num_participants * innovators_ratio)
    distribution.loc[num_value_creators:num_value_creators + num_innovators - 1, 'Coins'] += innovators_coins / num_innovators
    
    # Allocate coins to those in need
    num_needy = int(num_participants * needy_ratio)
    distribution.loc[num_value_creators + num_innovators:num_value_creators + num_innovators + num_needy - 1, 'Coins'] += needy_coins / num_needy
    
    return distribution

def plot_distribution(distribution):
    """
    Plots the distribution of Wealth Coins among participants.
    
    Parameters:
    distribution (pd.DataFrame): A DataFrame containing the distribution of coins among participants.
    """
    plt.figure(figsize=(10, 6))
    plt.bar(distribution['Participant'], distribution['Coins'], color='skyblue')
    plt.title('Wealth Coin Distribution Among Participants')
    plt.xlabel('Participant')
    plt.ylabel('Coins Allocated')
    plt.xticks(distribution['Participant'])
    plt.grid(axis='y')
    plt.show()

# Example usage
if __name__ == "__main__":
    try:
        total_coins = 10000
        num_participants = 100
        value_creators_ratio = 0.4
        innovators_ratio = 0.3
        needy_ratio = 0.3
        
        distribution = simulate_wealth_coin_distribution(total_coins, num_participants, value_creators_ratio, innovators_ratio, needy_ratio)
        print(distribution)
        plot_distribution(distribution)
    except Exception as e:
        print(f"An error occurred: {e}")
```
