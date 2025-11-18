"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gominings.net
Prompt: Write Python code to calculate daily and monthly BTC rewards based on the power and energy efficiency of a digital miner, as described on the GoMining website. Include options for maintenance fee adjustments and BTC price variations.
Generated: DETERMINISTIC_b62a591742503134
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class MinerRewardCalculator:
    """
    A class to calculate BTC rewards based on miner parameters.
    """

    def __init__(self, power_watts, efficiency_watt_per_th, btc_price_usd, maintenance_fee_percentage=0.0):
        """
        Initialize the calculator with miner parameters and settings.

        :param power_watts: Power consumption of the miner in watts.
        :param efficiency_watt_per_th: Energy efficiency of the miner in watts per TH/s.
        :param btc_price_usd: Current price of 1 BTC in USD.
        :param maintenance_fee_percentage: Maintenance fee percentage (optional, defaults to 0%).
        """
        self.power_watts = power_watts
        self.efficiency_watt_per_th = efficiency_watt_per_th
        self.btc_price_usd = btc_price_usd
        self.maintenance_fee_percentage = maintenance_fee_percentage

    def calculate_rewards(self, hashrate_th_per_s, network_difficulty, daily_energy_cost_usd, electricity_cost_per_kwh):
        """
        Calculate daily and monthly BTC rewards.

        :param hashrate_th_per_s: Hashrate of the miner in TH/s.
        :param network_difficulty: Current network mining difficulty.
        :param daily_energy_cost_usd: Daily energy cost in USD.
        :param electricity_cost_per_kwh: Cost of electricity per kWh.
        :return: A dictionary containing daily and monthly BTC rewards.
        """
        try:
            # Constants
            seconds_per_day = 86400  # Seconds in a day
            days_per_month = 30  # Approximate number of days in a month

            # Calculate BTC mined per second
            btc_per_second = hashrate_th_per_s * 1e12 / network_difficulty / 2**32

            # Daily BTC reward
            daily_btc_reward = btc_per_second * seconds_per_day

            # Monthly BTC reward
            monthly_btc_reward = daily_btc_reward * days_per_month

            # Deduct maintenance fee if applicable
            maintenance_fee = self.maintenance_fee_percentage / 100
            daily_btc_reward_after_fee = daily_btc_reward * (1 - maintenance_fee)
            monthly_btc_reward_after_fee = monthly_btc_reward * (1 - maintenance_fee)

            # Calculate daily and monthly USD rewards based on BTC price
            daily_usd_reward = daily_btc_reward_after_fee * self.btc_price_usd
            monthly_usd_reward = monthly_btc_reward_after_fee * self.btc_price_usd

            # Adjust for daily energy costs
            adjusted_daily_usd_reward = daily_usd_reward - daily_energy_cost_usd
            adjusted_monthly_usd_reward = monthly_usd_reward - (daily_energy_cost_usd * days_per_month)

            return {
                "daily_btc_reward": daily_btc_reward_after_fee,
                "monthly_btc_reward": monthly_btc_reward_after_fee,
                "daily_usd_reward": adjusted_daily_usd_reward,
                "monthly_usd_reward": adjusted_monthly_usd_reward,
            }
        except ZeroDivisionError:
            raise ValueError("Network difficulty must be greater than 0.")
        except Exception as e:
            raise RuntimeError("An error occurred during reward calculation: " + str(e))


# Example usage
if __name__ == "__main__":
    try:
        # Miner parameters
        power_watts = 3000  # Example value in watts
        efficiency_watt_per_th = 40  # Example value in watts per TH/s
        btc_price_usd = 27000  # Example BTC price in USD
        maintenance_fee_percentage = 2  # Example maintenance fee percentage

        # Create calculator instance
        calculator = MinerRewardCalculator(
            power_watts, efficiency_watt_per_th, btc_price_usd, maintenance_fee_percentage
        )

        # Inputs for reward calculation
        hashrate_th_per_s = 100  # Example hashrate in TH/s
        network_difficulty = 35e12  # Example network difficulty
        electricity_cost_per_kwh = 0.12  # Example electricity cost in USD per kWh
        daily_energy_cost_usd = (power_watts / 1000) * electricity_cost_per_kwh * 24  # Daily energy cost calculation

        # Calculate rewards
        rewards = calculator.calculate_rewards(
            hashrate_th_per_s, network_difficulty, daily_energy_cost_usd, electricity_cost_per_kwh
        )

        # Output rewards
        print("Daily BTC Reward:", rewards["daily_btc_reward"])
        print("Monthly BTC Reward:", rewards["monthly_btc_reward"])
        print("Daily USD Reward (adjusted for energy cost):", rewards["daily_usd_reward"])
        print("Monthly USD Reward (adjusted for energy cost):", rewards["monthly_usd_reward"])
    except Exception as e:
        print("Error:", str(e))
```
