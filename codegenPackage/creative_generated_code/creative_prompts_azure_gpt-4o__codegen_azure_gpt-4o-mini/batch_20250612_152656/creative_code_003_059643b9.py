"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinbsc-io.pages.dev
Prompt: Write a Python program to simulate the Bitcoin BSC staking process, including reward distribution per block and tracking the total staked tokens.
Generated: DETERMINISTIC_059643b9366f8356
Batch ID: 20250612_152656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import threading
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 10

class StakingPool:
    def __init__(self):
        self.total_staked = Decimal(0)
        self.rewards_per_block = Decimal(0.01)  # Example reward per block
        self.lock = threading.Lock()  # Lock for thread-safe operations

    def stake(self, amount):
        """Allows a user to stake a certain amount of tokens."""
        if amount <= 0:
            raise ValueError("Staking amount must be greater than zero.")
        
        with self.lock:
            self.total_staked += Decimal(amount)
            print(f"Staked: {amount} tokens. Total staked: {self.total_staked}")

    def unstake(self, amount):
        """Allows a user to unstake a certain amount of tokens."""
        if amount <= 0:
            raise ValueError("Unstaking amount must be greater than zero.")
        
        with self.lock:
            if amount > self.total_staked:
                raise ValueError("Cannot unstake more than the total staked amount.")
            self.total_staked -= Decimal(amount)
            print(f"Unstaked: {amount} tokens. Total staked: {self.total_staked}")

    def distribute_rewards(self):
        """Distributes rewards for each block mined."""
        with self.lock:
            if self.total_staked > 0:
                reward_distribution = self.total_staked * self.rewards_per_block
                print(f"Distributing rewards: {reward_distribution} tokens")
                return reward_distribution
            else:
                print("No tokens staked. No rewards to distribute.")
                return Decimal(0)

    def simulate_staking_process(self, duration, block_time):
        """Simulates the staking process over a specified duration."""
        start_time = time.time()
        while time.time() - start_time < duration:
            # Simulate block mining
            time.sleep(block_time)  # Wait for the time between blocks
            self.distribute_rewards()

def main():
    pool = StakingPool()

    # Example of staking and unstaking
    try:
        pool.stake(100)
        pool.stake(50)
        pool.unstake(30)

        # Simulate staking process for 10 seconds with a block time of 2 seconds
        staking_duration = 10  # seconds
        block_time = 2  # seconds
        staking_thread = threading.Thread(target=pool.simulate_staking_process, args=(staking_duration, block_time))
        staking_thread.start()
        staking_thread.join()  # Wait for the staking process to finish

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
