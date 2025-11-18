"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mine-runecoinio.pages.dev
Prompt: Write a script to simulate the halvening rune allocation raffle, assigning tickets based on consecutive blocks held by an RSIC at a specific address.
Generated: DETERMINISTIC_812fb98af1ed6327
Batch ID: 20250612_152422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class Raffle:
    def __init__(self):
        # Dictionary to hold addresses and their consecutive block counts
        self.address_blocks: Dict[str, int] = {}

    def add_blocks(self, address: str, block_count: int):
        """
        Add consecutive blocks held by the given address.

        :param address: The address of the RSIC.
        :param block_count: The number of consecutive blocks held.
        """
        if block_count < 0:
            raise ValueError("Block count must be non-negative.")
        
        # Update the block count for the address
        if address in self.address_blocks:
            self.address_blocks[address] += block_count
        else:
            self.address_blocks[address] = block_count

    def draw_winner(self) -> str:
        """
        Simulate the raffle drawing.

        :return: The address of the winning ticket holder.
        """
        total_tickets = sum(self.address_blocks.values())
        
        if total_tickets == 0:
            raise RuntimeError("No tickets available to draw a winner.")

        # Randomly select a winner based on the weighted tickets
        rand_value = random.randint(1, total_tickets)
        current_sum = 0

        for address, ticket_count in self.address_blocks.items():
            current_sum += ticket_count
            if current_sum >= rand_value:
                return address

        # This line should never be reached if the total is correctly calculated
        raise RuntimeError("Failed to draw a winner.")

    def reset_raffle(self):
        """
        Reset the raffle for a new round.
        """
        self.address_blocks.clear()

# Example usage
if __name__ == "__main__":
    raffle = Raffle()

    # Adding blocks held by various addresses
    try:
        raffle.add_blocks("address1", 5)
        raffle.add_blocks("address2", 3)
        raffle.add_blocks("address3", 7)
        
        # Draw a winner
        winner = raffle.draw_winner()
        print(f"The winner is: {winner}")

    except (ValueError, RuntimeError) as e:
        print(f"An error occurred: {str(e)}")
    
    # Reset the raffle for another round
    raffle.reset_raffle()
```
