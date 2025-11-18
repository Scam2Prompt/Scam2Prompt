"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethminer.world
Prompt: Create a program that simulates ETHMiner's "auto mining 24/7" feature, including a visualization of mining progress and daily payouts for different plans.
Generated: DETERMINISTIC_65ee920da670c069
Batch ID: 20250612_155000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class ETHMiner:
    """
    A class to simulate the ETHMining process with different plans.
    """

    def __init__(self, plan_type="Basic"):
        """
        Initialize the ETHMiner with specified mining plan.
        
        Args:
            plan_type (str): The type of mining plan (Basic, Standard, Premium).
        """
        self.plan_type = plan_type
        self.hash_rate = self.get_hash_rate(plan_type)
        self.daily_payout = self.calculate_daily_payout()
        self.mined_eth = 0

    def get_hash_rate(self, plan_type):
        """
        Get the hash rate based on the mining plan.

        Args:
            plan_type (str): The type of mining plan.

        Returns:
            float: Hash rate in MH/s.
        """
        plans = {
            "Basic": 10,     # 10 MH/s
            "Standard": 20,  # 20 MH/s
            "Premium": 40    # 40 MH/s
        }
        return plans.get(plan_type, 0)

    def calculate_daily_payout(self):
        """
        Calculate the daily payout based on hash rate.

        Returns:
            float: Daily payout in ETH.
        """
        eth_per_mh = 0.01  # Assuming 0.01 ETH per MH per day
        return self.hash_rate * eth_per_mh

    def mine(self, hours=24):
        """
        Simulate mining for a given number of hours.

        Args:
            hours (int): Number of hours to mine.
        """
        for _ in range(hours):
            self.mined_eth += self.daily_payout
            time.sleep(1)  # Simulate the passage of time (for demonstration)

    def get_mined_eth(self):
        """
        Retrieve the total mined ETH.

        Returns:
            float: Total mined ETH.
        """
        return self.mined_eth

def animate(i, miner, eth_data):
    """
    Update the plot for the mining progress.

    Args:
        i (int): Current frame index.
        miner (ETHMiner): The ETHMiner instance.
        eth_data (list): List to store mined ETH values over time.
    """
    miner.mine(1)  # Mine for 1 hour
    eth_data.append(miner.get_mined_eth())
    plt.cla()
    plt.plot(eth_data)
    plt.xlabel('Time (Hours)')
    plt.ylabel('Mined ETH')
    plt.title(f'Mining Progress - {miner.plan_type} Plan')
    plt.ylim(0, max(eth_data) + 1)

def main():
    """
    Main function to run the ETHMiner simulation.
    """
    # Create an ETHMiner instance
    miner = ETHMiner(plan_type="Premium")
    eth_data = []

    # Set up the plot
    plt.figure()
    ani = FuncAnimation(plt.gcf(), animate, fargs=(miner, eth_data), interval=1000)

    try:
        plt.show()
    except KeyboardInterrupt:
        print("Mining simulation ended.")
        print(f"Total Mined ETH: {miner.get_mined_eth():.2f} ETH")

if __name__ == "__main__":
    main()
```
