"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-ai.pages.dev
Prompt: Create a visualization in Python using Matplotlib to plot the projected $SCOTTY token rewards over time, based on the staking pool dynamics and the monthly reward rate.
Generated: DETERMINISTIC_0bcc0866ebbd4a8e
Batch ID: 20250612_152620
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

def calculate_rewards(initial_investment, monthly_rate, months):
    """
    Calculate projected rewards over time based on initial investment, monthly rate, and duration in months.
    
    Args:
        initial_investment (float): The initial amount staked in the pool.
        monthly_rate (float): The monthly reward rate (as a decimal).
        months (int): The number of months to project rewards for.
        
    Returns:
        list: A list of projected rewards for each month.
    """
    rewards = []
    current_balance = initial_investment

    for month in range(months):
        reward = current_balance * monthly_rate
        rewards.append(reward)
        current_balance += reward  # Update balance with rewards

    return rewards

def plot_rewards(initial_investment, monthly_rate, months):
    """
    Create a line plot of projected SCOTTY token rewards over time.

    Args:
        initial_investment (float): The initial amount staked in the pool.
        monthly_rate (float): The monthly reward rate (as a decimal).
        months (int): The number of months to project rewards for.
    """
    try:
        # Validate inputs
        if initial_investment <= 0:
            raise ValueError("Initial investment must be greater than zero.")
        if not (0 <= monthly_rate <= 1):
            raise ValueError("Monthly rate must be between 0 and 1.")
        if months <= 0:
            raise ValueError("Number of months must be greater than zero.")

        # Calculate rewards
        rewards = calculate_rewards(initial_investment, monthly_rate, months)

        # Prepare data for plotting
        months_range = np.arange(1, months + 1)

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(months_range, np.cumsum(rewards), marker='o', linestyle='-', color='blue', label='Projected Rewards')
        plt.title('Projected SCOTTY Token Rewards Over Time')
        plt.xlabel('Months')
        plt.ylabel('Cumulative Rewards (in SCOTTY tokens)')
        plt.xticks(months_range)
        plt.grid()
        plt.legend()
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    # Example parameters
    initial_investment = 1000  # Initial investment amount in SCOTTY tokens
    monthly_rate = 0.05         # Monthly reward rate (5%)
    months = 12                 # Projected duration in months

    # Plot the rewards
    plot_rewards(initial_investment, monthly_rate, months)
```
