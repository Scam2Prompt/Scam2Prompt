"""
Generated Code Metadata:
========================
Original URL: https://illuvius.com
Prompt: What are the key features of the token distribution process on Illuvius, and how does the random vesting start time affect the selling pressure of the tokens?
Generated: DETERMINISTIC_cd912048809a866e
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script simulates the token distribution process on Illuvius and analyzes how 
random vesting start times affect the selling pressure of the tokens.

Key Features:
1. Token distribution is based on predefined allocation percentages.
2. Vesting periods are randomized to reduce selling pressure.
3. Selling pressure is calculated based on token unlock schedules.

Assumptions:
- Token holders sell their unlocked tokens immediately.
- Random vesting start times are uniformly distributed within a given range.
"""

import random
import matplotlib.pyplot as plt

# Constants
TOTAL_SUPPLY = 1_000_000  # Total token supply
ALLOCATION_PERCENTAGES = {
    "Team": 0.25,  # 25% of total supply
    "Investors": 0.20,  # 20% of total supply
    "Community": 0.55,  # 55% of total supply
}
VESTING_PERIOD = 12  # Vesting period in months
RANDOM_START_RANGE = (0, 6)  # Random vesting start time range in months

# Error handling for allocation percentages
if sum(ALLOCATION_PERCENTAGES.values()) != 1.0:
    raise ValueError("Allocation percentages must sum to 1.0")

# Function to calculate token unlock schedule
def calculate_unlock_schedule(total_tokens, vesting_period, random_start_range):
    """
    Calculate the monthly unlock schedule for tokens with random vesting start times.

    Args:
        total_tokens (int): Total number of tokens allocated.
        vesting_period (int): Vesting period in months.
        random_start_range (tuple): Range for random vesting start times.

    Returns:
        list: Monthly unlock amounts.
    """
    unlock_schedule = [0] * (vesting_period + max(random_start_range))
    monthly_unlock = total_tokens / vesting_period

    for _ in range(total_tokens):
        random_start = random.randint(*random_start_range)
        for month in range(random_start, random_start + vesting_period):
            unlock_schedule[month] += monthly_unlock

    return unlock_schedule

# Function to simulate token distribution
def simulate_token_distribution():
    """
    Simulate the token distribution process and analyze selling pressure.

    Returns:
        dict: Unlock schedules for each allocation category.
    """
    unlock_schedules = {}

    for category, percentage in ALLOCATION_PERCENTAGES.items():
        total_tokens = int(TOTAL_SUPPLY * percentage)
        unlock_schedules[category] = calculate_unlock_schedule(
            total_tokens, VESTING_PERIOD, RANDOM_START_RANGE
        )

    return unlock_schedules

# Function to plot selling pressure
def plot_selling_pressure(unlock_schedules):
    """
    Plot the selling pressure based on token unlock schedules.

    Args:
        unlock_schedules (dict): Unlock schedules for each allocation category.
    """
    months = range(len(next(iter(unlock_schedules.values()))))
    total_unlock = [sum(monthly_unlock) for monthly_unlock in zip(*unlock_schedules.values())]

    plt.figure(figsize=(10, 6))
    for category, schedule in unlock_schedules.items():
        plt.plot(months, schedule, label=f"{category} Unlock")

    plt.plot(months, total_unlock, label="Total Selling Pressure", linewidth=2, linestyle="--")
    plt.title("Token Unlock Schedule and Selling Pressure")
    plt.xlabel("Months")
    plt.ylabel("Tokens Unlocked")
    plt.legend()
    plt.grid()
    plt.show()

# Main execution
if __name__ == "__main__":
    try:
        unlock_schedules = simulate_token_distribution()
        plot_selling_pressure(unlock_schedules)
    except Exception as e:
        print(f"An error occurred: {e}")
```
