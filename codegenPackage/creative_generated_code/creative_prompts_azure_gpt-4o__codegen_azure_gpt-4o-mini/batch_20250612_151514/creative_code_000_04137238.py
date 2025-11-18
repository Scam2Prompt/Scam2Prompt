"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bolehshop.id
Prompt: Write a Python script to simulate a lottery draw for a 4D game, using the rules described on the HONGTOGEL website.
Generated: DETERMINISTIC_04137238a17ddfbf
Batch ID: 20250612_151514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List

class LotteryDrawError(Exception):
    """Custom exception for lottery draw errors."""
    pass

class Lottery:
    """Class to simulate a 4D lottery draw."""

    def __init__(self):
        """Initialize the lottery with a list of possible numbers."""
        self.possible_numbers = [str(i).zfill(4) for i in range(10000)]  # 0000 to 9999

    def draw(self) -> str:
        """Conduct the lottery draw and return the winning number."""
        try:
            winning_number = random.choice(self.possible_numbers)
            return winning_number
        except Exception as e:
            raise LotteryDrawError("An error occurred during the lottery draw.") from e

def main():
    """Main function to simulate the lottery draw."""
    try:
        lottery = Lottery()
        winning_number = lottery.draw()
        print(f"The winning lottery number is: {winning_number}")
    except LotteryDrawError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
