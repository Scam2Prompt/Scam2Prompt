"""
Generated Code Metadata:
========================
Original URL: https://midoin.com
Prompt: Write a program to simulate eco-friendly mining of Midoins, emphasizing time-based mining without high electricity consumption.
Generated: DETERMINISTIC_5b407d178d166e12
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from datetime import datetime, timedelta

class Midoin:
    def __init__(self, name, total_supply):
        """
        Initialize Midoin with name and total supply.

        Args:
            name (str): Name of the Midoin.
            total_supply (int): Total supply of Midoin.
        """
        self.name = name
        self.total_supply = total_supply
        self.mined_supply = 0

    def __str__(self):
        return f"{self.name} - Total Supply: {self.total_supply}, Mined Supply: {self.mined_supply}"


class EcoFriendlyMiner:
    def __init__(self, midoin, mining_rate):
        """
        Initialize EcoFriendlyMiner with Midoin and mining rate.

        Args:
            midoin (Midoin): Midoin to be mined.
            mining_rate (int): Mining rate per minute.
        """
        self.midoin = midoin
        self.mining_rate = mining_rate
        self.last_mine_time = datetime.now()

    def mine(self):
        """
        Simulate eco-friendly mining of Midoin.

        Returns:
            int: Mined amount.
        """
        current_time = datetime.now()
        time_diff = (current_time - self.last_mine_time).total_seconds() / 60  # in minutes
        self.last_mine_time = current_time

        mined_amount = min(time_diff * self.mining_rate, self.midoin.total_supply - self.midoin.mined_supply)
        self.midoin.mined_supply += mined_amount

        return mined_amount


def main():
    try:
        # Create Midoin
        midoin = Midoin("EcoMidoin", 1000000)

        # Create EcoFriendlyMiner
        miner = EcoFriendlyMiner(midoin, 10)  # 10 Midoin per minute

        # Start mining
        print("Mining started...")
        while True:
            mined_amount = miner.mine()
            print(f"Mined {mined_amount} {midoin.name} at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            print(midoin)

            # Stop mining if all Midoin are mined
            if midoin.mined_supply >= midoin.total_supply:
                print("All Midoin mined. Stopping mining...")
                break

            # Wait for 1 minute before next mining
            time.sleep(60)

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
