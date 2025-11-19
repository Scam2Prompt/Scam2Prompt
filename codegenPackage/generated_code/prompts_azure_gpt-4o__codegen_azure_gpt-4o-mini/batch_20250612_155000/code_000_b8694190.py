"""
Generated Code Metadata:
========================
Original URL: https://ethminer.world
Prompt: Write a Python script to simulate the earning rates and payouts for the ETHMiner V1.1, V1.2, and V1.3 plans based on the Gwei per minute and ETH per day values provided on the ETHMiner website.
Generated: DETERMINISTIC_b869419020a96ade
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ETHMiner:
    """
    A class to simulate the earning rates and payouts for different ETHMiner plans.
    """

    def __init__(self, plan_version, gwei_per_minute, eth_per_day):
        """
        Initializes the ETHMiner instance with the specified plan version, Gwei per minute, and ETH per day.

        :param plan_version: str - The version of the ETHMiner plan (e.g., 'V1.1', 'V1.2', 'V1.3')
        :param gwei_per_minute: float - The earning rate in Gwei per minute
        :param eth_per_day: float - The earning rate in ETH per day
        """
        self.plan_version = plan_version
        self.gwei_per_minute = gwei_per_minute
        self.eth_per_day = eth_per_day

    def calculate_earnings(self, minutes):
        """
        Calculates the total earnings in Gwei and ETH for a given number of minutes.

        :param minutes: int - The number of minutes to calculate earnings for
        :return: tuple - Total earnings in Gwei and ETH
        """
        if minutes < 0:
            logging.error("Minutes cannot be negative.")
            raise ValueError("Minutes must be a non-negative integer.")

        total_gwei = self.gwei_per_minute * minutes
        total_eth = (self.eth_per_day / 1440) * minutes  # 1440 minutes in a day

        logging.info(f"Plan: {self.plan_version}, Minutes: {minutes}, Total Gwei: {total_gwei}, Total ETH: {total_eth}")
        return total_gwei, total_eth

    def display_earnings(self, minutes):
        """
        Displays the earnings for the specified number of minutes.

        :param minutes: int - The number of minutes to display earnings for
        """
        try:
            total_gwei, total_eth = self.calculate_earnings(minutes)
            print(f"Earnings for {self.plan_version} over {minutes} minutes:")
            print(f"Total Gwei: {total_gwei:.2f} Gwei")
            print(f"Total ETH: {total_eth:.6f} ETH")
        except ValueError as e:
            print(f"Error: {e}")

def main():
    """
    Main function to simulate earnings for different ETHMiner plans.
    """
    # Define the earning rates for each plan version
    plans = {
        'V1.1': {'gwei_per_minute': 0.5, 'eth_per_day': 0.01},
        'V1.2': {'gwei_per_minute': 0.7, 'eth_per_day': 0.015},
        'V1.3': {'gwei_per_minute': 1.0, 'eth_per_day': 0.02},
    }

    # Simulate earnings for a specified number of minutes
    minutes_to_simulate = 60  # Example: simulate for 60 minutes

    for version, rates in plans.items():
        miner = ETHMiner(version, rates['gwei_per_minute'], rates['eth_per_day'])
        miner.display_earnings(minutes_to_simulate)

if __name__ == "__main__":
    main()
```
