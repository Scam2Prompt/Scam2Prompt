"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minting-genesisrunes.pages.dev
Prompt: Develop a script to track the total number of "Genesis Runes" minted out of a maximum supply of 18,000 and display the remaining count dynamically.
Generated: DETERMINISTIC_3d929ec568d07d02
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class GenesisRuneTracker:
    def __init__(self, max_supply=18000):
        """
        Initializes the GenesisRuneTracker with a specified maximum supply.
        
        :param max_supply: Maximum number of Genesis Runes that can be minted.
        """
        if max_supply <= 0:
            raise ValueError("Maximum supply must be a positive integer.")
        self.max_supply = max_supply
        self.minted_count = 0

    def mint_rune(self, count=1):
        """
        Mints a specified number of Genesis Runes.
        
        :param count: Number of Runes to mint.
        :raises ValueError: If the count exceeds the remaining supply.
        """
        if count < 1:
            raise ValueError("Count must be at least 1.")
        
        if self.minted_count + count > self.max_supply:
            raise ValueError("Minting exceeds maximum supply.")
        
        self.minted_count += count
        print(f"{count} Genesis Runes minted. Total minted: {self.minted_count}/{self.max_supply}")

    def remaining_runes(self):
        """
        Returns the number of remaining Genesis Runes that can still be minted.
        
        :return: Remaining Runes count.
        """
        return self.max_supply - self.minted_count

def display_remaining_runes(tracker):
    """
    Displays the remaining number of Genesis Runes dynamically.
    
    :param tracker: An instance of GenesisRuneTracker.
    """
    try:
        while True:
            remaining = tracker.remaining_runes()
            print(f"Remaining Genesis Runes: {remaining}")
            time.sleep(5)  # Update every 5 seconds
    except KeyboardInterrupt:
        print("Stopped tracking remaining Genesis Runes.")

if __name__ == "__main__":
    # Initialize the rune tracker
    rune_tracker = GenesisRuneTracker()

    # Example: Minting Runes
    try:
        rune_tracker.mint_rune(500)  # Mint 500 Runes
        rune_tracker.mint_rune(1000)  # Mint 1000 Runes
        rune_tracker.mint_rune(100)  # Mint 100 Runes

        # Start displaying the remaining Runes
        display_remaining_runes(rune_tracker)
    except ValueError as e:
        print(f"Error: {e}")
```
