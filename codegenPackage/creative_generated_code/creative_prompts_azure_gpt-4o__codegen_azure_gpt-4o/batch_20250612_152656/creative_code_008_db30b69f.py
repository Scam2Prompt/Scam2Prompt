"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notcoin-90l.pages.dev
Prompt: Write a script to simulate the turbo-mode activation in NotCoin mining, ensuring it increases coin generation without consuming energy, as described in the whitepaper.
Generated: DETERMINISTIC_db30b69fc3bf50b1
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
import random

class NotCoinMiner:
    """
    Simulates NotCoin mining with a 'turbo-mode' feature.
    Turbo-mode increases coin generation without additional energy usage.
    """

    def __init__(self):
        """
        Constructor to initialize the miner.
        """
        self.coins_mined = 0
        self.is_turbo_mode_active = False
        self.base_coin_generation_rate = 1  # Coins per second in normal mode
        self.turbo_coin_generation_rate = 5  # Coins per second in turbo mode

    def activate_turbo_mode(self):
        """
        Activate turbo mode to increase coin generation rate.
        """
        if not self.is_turbo_mode_active:
            self.is_turbo_mode_active = True
            print("Turbo mode activated! Mining speed increased.")

    def deactivate_turbo_mode(self):
        """
        Deactivate turbo mode to return to normal mining speed.
        """
        if self.is_turbo_mode_active:
            self.is_turbo_mode_active = False
            print("Turbo mode deactivated. Mining speed returned to normal.")

    def mine_coins(self, duration_seconds=10):
        """
        Simulate coin mining for a given duration.

        :param duration_seconds: Time in seconds to mine coins.
        """
        start_time = time.time()
        while time.time() - start_time < duration_seconds:
            try:
                # Determine mining rate based on turbo mode status
                coin_generation_rate = self.turbo_coin_generation_rate if self.is_turbo_mode_active else self.base_coin_generation_rate
                
                # Simulate mining
                self.coins_mined += coin_generation_rate
                
                # Log mining progress
                print(f"Coins mined so far: {self.coins_mined}")
                
                # Wait for 1 second to simulate real-time mining
                time.sleep(1)
            
            except Exception as e:
                # Handle unexpected errors during mining
                print(f"An error occurred during mining: {e}")
                break

    def get_mined_coins(self):
        """
        Get the total number of coins mined.

        :return: Total coins mined.
        """
        return self.coins_mined


if __name__ == "__main__":
    # Create a NotCoin miner instance
    miner = NotCoinMiner()

    # Simulate normal mining
    print("Starting normal mining...")
    miner.mine_coins(duration_seconds=5)

    # Activate turbo mode and simulate mining
    miner.activate_turbo_mode()
    miner.mine_coins(duration_seconds=5)

    # Deactivate turbo mode and simulate mining
    miner.deactivate_turbo_mode()
    miner.mine_coins(duration_seconds=5)

    # Display final number of coins mined
    print(f"Mining complete. Total coins mined: {miner.get_mined_coins()}")
```
