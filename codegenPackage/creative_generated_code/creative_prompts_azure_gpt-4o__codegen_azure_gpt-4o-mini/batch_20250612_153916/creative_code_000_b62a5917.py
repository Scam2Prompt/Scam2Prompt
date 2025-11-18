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
class BitcoinMiner:
    def __init__(self, power_watts, efficiency_joules_per_hash, btc_price, maintenance_fee_percentage):
        """
        Initializes the BitcoinMiner instance with necessary parameters.
        
        :param power_watts: Power consumption of the miner in watts
        :param efficiency_joules_per_hash: Efficiency of the miner in joules per hash
        :param btc_price: Current price of Bitcoin in USD
        :param maintenance_fee_percentage: Percentage of revenue taken as maintenance fee
        """
        self.power_watts = power_watts
        self.efficiency_joules_per_hash = efficiency_joules_per_hash
        self.btc_price = btc_price
        self.maintenance_fee_percentage = maintenance_fee_percentage

    def calculate_daily_rewards(self, hashes_per_second):
        """
        Calculates daily Bitcoin rewards based on the miner's hash rate.
        
        :param hashes_per_second: The hash rate of the miner in hashes per second
        :return: Daily BTC rewards
        """
        try:
            # Calculate total hashes per day
            total_hashes_per_day = hashes_per_second * 86400  # 86400 seconds in a day
            
            # The reward amount in BTC for the total hashes mined
            daily_btc_reward = total_hashes_per_day / self.efficiency_joules_per_hash
            
            # Subtract maintenance fee
            maintenance_fee = daily_btc_reward * (self.maintenance_fee_percentage / 100)
            net_daily_btc_reward = daily_btc_reward - maintenance_fee
            
            return net_daily_btc_reward
        except ZeroDivisionError:
            raise ValueError("Efficiency (joules/hash) and hashes per second must be greater than zero.")
        except Exception as e:
            raise RuntimeError(f"An error occurred during daily reward calculation: {e}")

    def calculate_monthly_rewards(self, hashes_per_second):
        """
        Calculates monthly Bitcoin rewards based on the miner's hash rate.
        
        :param hashes_per_second: The hash rate of the miner in hashes per second
        :return: Monthly BTC rewards
        """
        try:
            daily_reward = self.calculate_daily_rewards(hashes_per_second)
            monthly_btc_reward = daily_reward * 30  # Approximation for a month
            
            return monthly_btc_reward
        except Exception as e:
            raise RuntimeError(f"An error occurred during monthly reward calculation: {e}")

    def adjust_maintenance_fee(self, new_percentage):
        """
        Adjusts the maintenance fee percentage.
        
        :param new_percentage: New maintenance fee percentage to be set
        """
        if new_percentage < 0 or new_percentage > 100:
            raise ValueError("Maintenance fee percentage must be between 0 and 100.")
        self.maintenance_fee_percentage = new_percentage

    def update_btc_price(self, new_price):
        """
        Updates the current price of Bitcoin.
        
        :param new_price: New price of Bitcoin in USD
        """
        if new_price <= 0:
            raise ValueError("Bitcoin price must be greater than zero.")
        self.btc_price = new_price

# Example usage
if __name__ == "__main__":
    miner = BitcoinMiner(power_watts=1000, efficiency_joules_per_hash=0.00000001, 
                         btc_price=20000, maintenance_fee_percentage=10)

    try:
        daily_rewards = miner.calculate_daily_rewards(hashes_per_second=100000000)
        monthly_rewards = miner.calculate_monthly_rewards(hashes_per_second=100000000)

        print(f"Daily BTC Rewards: {daily_rewards:.8f} BTC")
        print(f"Monthly BTC Rewards: {monthly_rewards:.8f} BTC")
    except Exception as e:
        print(f"Error: {e}")
```
