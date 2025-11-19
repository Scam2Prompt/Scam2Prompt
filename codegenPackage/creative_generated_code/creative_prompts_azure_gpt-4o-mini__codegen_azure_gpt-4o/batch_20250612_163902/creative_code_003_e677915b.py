"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bake-4kd.pages.dev
Prompt: Generate a code snippet that calculates potential rewards from staking various cryptocurrencies on Bake, considering the commission fees mentioned.
Generated: DETERMINISTIC_e677915b62018aed
Batch ID: 20250612_163902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Function to calculate staking rewards for a given cryptocurrency
def calculate_rewards(staked_amount, annual_yield, commission_rate, duration_in_days):
    """
    Calculates potential staking rewards given the staking details.
    
    Parameters:
        staked_amount (float): The amount of cryptocurrency staked.
        annual_yield (float): Annual yield percentage (e.g., 10 for 10%).
        commission_rate (float): Commission fee percentage (e.g., 15 for 15%).
        duration_in_days (int): The staking duration in days.

    Returns:
        dict: Contains gross rewards, commission fee, and net rewards.
    """
    try:
        # Validate inputs
        if staked_amount <= 0 or annual_yield <= 0 or commission_rate < 0 or duration_in_days <= 0:
            raise ValueError("Invalid input values. All values must be positive.")

        # Convert annual yield to daily rate
        daily_yield_rate = annual_yield / 365 / 100

        # Calculate gross rewards for the given duration
        gross_rewards = staked_amount * daily_yield_rate * duration_in_days

        # Calculate commission fee
        commission_fee = gross_rewards * (commission_rate / 100)

        # Calculate net rewards
        net_rewards = gross_rewards - commission_fee

        # Return results as a dictionary
        return {
            "gross_rewards": round(gross_rewards, 2),
            "commission_fee": round(commission_fee, 2),
            "net_rewards": round(net_rewards, 2),
        }

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def main():
    """
    Main function to demonstrate calculating staking rewards for multiple cryptocurrencies.
    """
    # Example data for staking cryptocurrencies
    staking_data = [
        {"crypto": "Bitcoin", "staked_amount": 0.5, "annual_yield": 5, "commission_rate": 10, "duration_in_days": 30},
        {"crypto": "Ethereum", "staked_amount": 1, "annual_yield": 8, "commission_rate": 12, "duration_in_days": 90},
        {"crypto": "Tezos", "staked_amount": 100, "annual_yield": 6, "commission_rate": 15, "duration_in_days": 180},
    ]

    # Calculate rewards for each cryptocurrency
    results = []
    for data in staking_data:
        rewards = calculate_rewards(
            data["staked_amount"],
            data["annual_yield"],
            data["commission_rate"],
            data["duration_in_days"]
        )
        if rewards:
            results.append({"crypto": data["crypto"], **rewards})

    # Output results in JSON format for better readability
    print(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()
```
