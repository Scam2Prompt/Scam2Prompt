"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unijoin.xyz
Prompt: Create a step-by-step Python script that simulates the process of mixing traceable coins and receiving untraceable coins, as outlined in UniJoin's "5 Simple Steps to Use Us."
Generated: DETERMINISTIC_9588c3cc2082eb6c
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging for tracking the process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CoinMixer:
    def __init__(self):
        self.traceable_coins = 0
        self.untraceable_coins = 0

    def receive_traceable_coins(self, amount):
        """Receive a specified amount of traceable coins."""
        if amount < 0:
            raise ValueError("Amount of traceable coins must be non-negative.")
        self.traceable_coins += amount
        logging.info(f"Received {amount} traceable coins. Total: {self.traceable_coins}")

    def mix_coins(self):
        """Simulate the mixing process of traceable coins."""
        if self.traceable_coins == 0:
            raise ValueError("No traceable coins available to mix.")
        
        # Randomly determine the amount of untraceable coins to give back
        self.untraceable_coins = random.randint(1, self.traceable_coins)
        logging.info(f"Mixing complete. Generated {self.untraceable_coins} untraceable coins.")

        # Reset traceable coins after mixing
        self.traceable_coins = 0

    def receive_untraceable_coins(self):
        """Retrieve the generated untraceable coins."""
        if self.untraceable_coins == 0:
            raise ValueError("No untraceable coins available to receive.")
        
        logging.info(f"Received {self.untraceable_coins} untraceable coins.")
        return self.untraceable_coins

def main():
    """Main function to execute the coin mixing simulation."""
    try:
        mixer = CoinMixer()

        # Step 1: Receiving traceable coins
        mixer.receive_traceable_coins(20)

        # Step 2: Mixing coins
        mixer.mix_coins()

        # Step 3: Receiving untraceable coins
        untraceable_received = mixer.receive_untraceable_coins()

        # Step 4: Display the result
        print(f"Successfully received {untraceable_received} untraceable coins.")

    except ValueError as e:
        logging.error(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
