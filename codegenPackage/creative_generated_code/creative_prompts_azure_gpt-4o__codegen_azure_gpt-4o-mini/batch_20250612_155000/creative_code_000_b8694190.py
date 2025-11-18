"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethminer.world
Prompt: Write a Python script to simulate the earning rates and payouts for the ETHMiner V1.1, V1.2, and V1.3 plans based on the Gwei per minute and ETH per day values provided on the ETHMiner website.
Generated: DETERMINISTIC_b869419020a96ade
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ETHMiner:
    def __init__(self, plan_version, gwei_per_minute, eth_per_day):
        """
        Initializes the ETHMiner object with specified plan version, gwei per minute, and eth per day.
        
        :param plan_version: Version of the ETHMiner plan (e.g., V1.1, V1.2, V1.3)
        :param gwei_per_minute: Gwei generated per minute by the miner
        :param eth_per_day: ETH generated per day by the miner
        """
        self.plan_version = plan_version
        self.gwei_per_minute = gwei_per_minute
        self.eth_per_day = eth_per_day

    def calculate_monthly_earnings(self):
        """
        Calculates the estimated monthly earnings based on gwei per minute and eth per day.
        
        :return: Total earnings in both Gwei and ETH for the month
        """
        try:
            # Calculate the total Gwei earned in a month (30 days)
            total_gwei_monthly = self.gwei_per_minute * 60 * 24 * 30
            # Calculate the total ETH earned in a month (30 days)
            total_eth_monthly = self.eth_per_day * 30
            
            logging.info(f"Monthly earnings for plan {self.plan_version}: {total_gwei_monthly} Gwei, {total_eth_monthly} ETH")
            return total_gwei_monthly, total_eth_monthly
            
        except Exception as e:
            logging.error(f"Error calculating monthly earnings: {e}")
            return None

def main():
    # Sample data for ETHMiner plans
    plans_data = {
        'V1.1': {'gwei_per_minute': 0.5, 'eth_per_day': 0.02},
        'V1.2': {'gwei_per_minute': 0.7, 'eth_per_day': 0.025},
        'V1.3': {'gwei_per_minute': 1.0, 'eth_per_day': 0.03},
    }

    # Create ETHMiner objects for each plan and calculate monthly earnings
    miners = []
    
    for plan_version, data in plans_data.items():
        miner = ETHMiner(plan_version, data['gwei_per_minute'], data['eth_per_day'])
        miners.append(miner)
        miner.calculate_monthly_earnings()

if __name__ == "__main__":
    main()
```
