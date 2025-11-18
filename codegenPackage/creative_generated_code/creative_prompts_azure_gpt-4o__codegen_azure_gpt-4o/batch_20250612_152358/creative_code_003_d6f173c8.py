"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appscottyclaims.pages.dev
Prompt: Write a Python program to visualize the total staked $SCOTTY tokens and estimated rewards over time, using the monthly and daily reward percentages provided on the Scotty AI staking platform.
Generated: DETERMINISTIC_d6f173c80b3cb8f3
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import matplotlib.pyplot as plt
import pandas as pd
import datetime

# Function to calculate rewards over time
def calculate_rewards(initial_stake, monthly_reward_percent, daily_reward_percent, duration_days):
    """
    Calculates the total staked tokens and estimated rewards over time.

    :param initial_stake: Initial amount of staked tokens ($SCOTTY).
    :param monthly_reward_percent: Monthly reward percentage (e.g., 5% as 0.05).
    :param daily_reward_percent: Daily reward percentage (e.g., 0.166% as 0.00166).
    :param duration_days: Total number of days to calculate rewards for.
    :return: A DataFrame with dates, total staked, and cumulative rewards.
    """
    data = {
        "Date": [],
        "Total Staked": [],
        "Cumulative Rewards": []
    }

    total_staked = initial_stake
    cumulative_rewards = 0
    current_date = datetime.date.today()

    for day in range(duration_days + 1):
        # Record data for the current day
        data["Date"].append(current_date)
        data["Total Staked"].append(total_staked)
        data["Cumulative Rewards"].append(cumulative_rewards)

        # Calculate daily rewards
        daily_rewards = total_staked * daily_reward_percent
        cumulative_rewards += daily_rewards
        total_staked += daily_rewards  # Compound staking by adding rewards to total staked

        # Increment the date
        current_date += datetime.timedelta(days=1)

    return pd.DataFrame(data)

# Function to visualize the rewards
def visualize_rewards(df):
    """
    Plots the total staked tokens and cumulative rewards over time using matplotlib.

    :param df: DataFrame containing the staking data.
    """
    plt.figure(figsize=(12, 6))

    # Plot total staked tokens
    plt.plot(df["Date"], df["Total Staked"], label="Total Staked ($SCOTTY)", color="blue")

    # Plot cumulative rewards
    plt.plot(df["Date"], df["Cumulative Rewards"], label="Cumulative Rewards ($SCOTTY)", color="green")

    # Add labels, title, and legend
    plt.xlabel("Date")
    plt.ylabel("$SCOTTY Tokens")
    plt.title("Total Staked and Estimated Rewards Over Time")
    plt.legend(loc="upper left")
    plt.grid()

    # Show the plot
    plt.tight_layout()
    plt.show()

# Main Function
def main():
    try:
        # Input parameters
        initial_stake = float(input("Enter initial staked amount ($SCOTTY): "))
        monthly_reward_percent = float(input("Enter monthly reward percentage (e.g., 5 for 5%): ")) / 100
        daily_reward_percent = monthly_reward_percent / 30  # Approximate daily reward percentage
        duration_days = int(input("Enter staking duration in days: "))

        # Validate inputs
        if initial_stake <= 0 or monthly_reward_percent <= 0 or duration_days <= 0:
            raise ValueError("All inputs must be positive numbers.")

        # Calculate rewards
        df = calculate_rewards(initial_stake, monthly_reward_percent, daily_reward_percent, duration_days)

        # Visualize the rewards
        visualize_rewards(df)
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point for the program
if __name__ == "__main__":
    main()
```
