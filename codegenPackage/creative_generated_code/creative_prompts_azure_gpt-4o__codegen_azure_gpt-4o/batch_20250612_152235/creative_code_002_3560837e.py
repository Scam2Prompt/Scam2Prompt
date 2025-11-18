"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-gmt-marketplace.pages.dev
Prompt: Create a function to simulate daily BTC rewards for miners created on the GoMining platform, factoring in computing power (TH) and energy efficiency (W/TH).
Generated: DETERMINISTIC_3560837ed09b7807
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def simulate_daily_btc_rewards(computing_power_th, energy_efficiency_w_per_th):
    """
    Simulates daily BTC rewards for miners on the GoMining platform.

    Args:
        computing_power_th (float): The computing power of the miner in terahashes (TH).
        energy_efficiency_w_per_th (float): Energy efficiency of the miner in watts per terahash (W/TH).

    Returns:
        float: Estimated BTC reward for the day.
    """
    try:
        # Validate inputs
        if computing_power_th <= 0:
            raise ValueError("Computing power must be greater than 0.")
        if energy_efficiency_w_per_th <= 0:
            raise ValueError("Energy efficiency must be greater than 0.")

        # Constants
        btc_reward_per_th = 0.00000001  # Example constant reward per TH (for demonstration purposes)
        fluctuation_range_percent = 0.05  # Simulate daily fluctuation in BTC rewards (+/- 5%)

        # Simulate reward fluctuation
        random_fluctuation = random.uniform(-fluctuation_range_percent, fluctuation_range_percent)
        adjusted_btc_reward_per_th = btc_reward_per_th * (1 + random_fluctuation)

        # Calculate BTC reward
        daily_btc_reward = computing_power_th * adjusted_btc_reward_per_th

        return round(daily_btc_reward, 8)  # Rounded to 8 decimal places (BTC precision)

    except Exception as e:
        print(f"Error occurred: {e}")
        return 0.0


# Example usage
if __name__ == "__main__":
    try:
        # Example miner configurations
        computing_power = 100  # 100 TH
        energy_efficiency = 30  # 30 W/TH

        # Simulate daily BTC rewards
        btc_reward = simulate_daily_btc_rewards(computing_power, energy_efficiency)
        print(f"Estimated daily BTC reward: {btc_reward} BTC")

    except Exception as main_exception:
        print(f"An unexpected error occurred: {main_exception}")
```
