"""
Generated Code Metadata:
========================
Original URL: https://ethereumonthlyreturns.com
Prompt: "What are the projected dates and halving percentages for the next Bitcoin halving events based on previous and average block generation times?"
Generated: DETERMINISTIC_d84ed0229133438a
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class BitcoinHalving:
    def __init__(self, initial_block_reward=50, halving_interval=210000):
        """
        Initializes the BitcoinHalving class with the initial block reward and halving interval.
        
        :param initial_block_reward: The initial reward for mining a block (default is 50 BTC).
        :param halving_interval: The number of blocks after which the reward halves (default is 210,000).
        """
        self.initial_block_reward = initial_block_reward
        self.halving_interval = halving_interval
        self.halvings = []

    def calculate_halvings(self, current_block_height, average_block_time_seconds):
        """
        Calculates the projected dates and halving percentages for future Bitcoin halving events.
        
        :param current_block_height: The current block height in the Bitcoin blockchain.
        :param average_block_time_seconds: The average time taken to mine a block in seconds.
        :return: A list of tuples containing the projected date and halving percentage.
        """
        try:
            # Calculate the number of halvings that have occurred
            halvings_occurred = current_block_height // self.halving_interval
            
            # Calculate the next halving block height
            next_halving_block_height = (halvings_occurred + 1) * self.halving_interval
            
            # Calculate the projected date of the next halving
            blocks_until_next_halving = next_halving_block_height - current_block_height
            projected_time_until_next_halving = blocks_until_next_halving * average_block_time_seconds
            
            # Calculate the projected date
            projected_date = datetime.datetime.now() + datetime.timedelta(seconds=projected_time_until_next_halving)
            
            # Calculate the new block reward after the next halving
            new_block_reward = self.initial_block_reward / (2 ** (halvings_occurred + 1))
            
            # Store the halving information
            self.halvings.append((projected_date, new_block_reward))
            
            return self.halvings
        
        except Exception as e:
            print(f"An error occurred while calculating halvings: {e}")
            return []

# Example usage
if __name__ == "__main__":
    # Current block height and average block time (in seconds)
    current_block_height = 800000  # Example current block height
    average_block_time_seconds = 600  # Average block time of 10 minutes

    # Create an instance of BitcoinHalving
    bitcoin_halving = BitcoinHalving()

    # Calculate and print the projected halving dates and rewards
    projected_halvings = bitcoin_halving.calculate_halvings(current_block_height, average_block_time_seconds)
    
    for date, reward in projected_halvings:
        print(f"Projected Halving Date: {date}, New Block Reward: {reward:.2f} BTC")
```
