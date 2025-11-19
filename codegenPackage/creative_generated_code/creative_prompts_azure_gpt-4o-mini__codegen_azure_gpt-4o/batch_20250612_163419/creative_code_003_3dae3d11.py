"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minucoindapp.pages.dev
Prompt: Create a script that calculates potential daily rewards and ROI for hiring miners with BNB, based on the Minu mining model.
Generated: DETERMINISTIC_3dae3d11f1eb1650
Batch ID: 20250612_163419
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_rewards_and_roi(bnb_investment, daily_reward_rate, miner_cost, num_miners):
    """
    Calculates daily rewards and ROI for hiring miners in the Minu mining model.

    Parameters:
        bnb_investment (float): Amount of BNB invested.
        daily_reward_rate (float): Daily reward percentage (e.g., 0.1 for 10%).
        miner_cost (float): Cost of a single miner in BNB.
        num_miners (int): Number of miners purchased.

    Returns:
        dict: Daily rewards, ROI percentage, and break-even days.
    """

    if miner_cost <= 0 or num_miners <= 0 or daily_reward_rate <= 0 or bnb_investment <= 0:
        raise ValueError("All input values must be positive numbers.")

    # Calculate total cost for miners
    total_miner_cost = miner_cost * num_miners

    # Ensure investment is sufficient for miners
    if total_miner_cost > bnb_investment:
        raise ValueError("Investment is insufficient to purchase the specified number of miners.")

    # Calculate daily rewards
    daily_rewards = total_miner_cost * daily_reward_rate

    # Calculate ROI (Return on Investment) percentage
    roi_percentage = (daily_rewards / bnb_investment) * 100

    # Calculate break-even time in days
    break_even_days = bnb_investment / daily_rewards

    return {
        "Daily Rewards (BNB)": daily_rewards,
        "ROI (%)": roi_percentage,
        "Break-Even Days": break_even_days
    }


def main():
    """
    Main script function to calculate potential daily rewards and ROI based on user input.
    """
    try:
        print("Minu Mining Model Reward Calculator\n")

        # Collect inputs from the user
        bnb_investment = float(input("Enter the total BNB investment: "))
        daily_reward_rate = float(input("Enter the daily reward rate (e.g., 0.1 for 10%): "))
        miner_cost = float(input("Enter the cost of a single miner in BNB: "))
        num_miners = int(input("Enter the number of miners purchased: "))

        # Perform calculations
        results = calculate_rewards_and_roi(bnb_investment, daily_reward_rate, miner_cost, num_miners)

        # Display results
        print("\n--- Calculation Results ---")
        for key, value in results.items():
            print(f"{key}: {value}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
