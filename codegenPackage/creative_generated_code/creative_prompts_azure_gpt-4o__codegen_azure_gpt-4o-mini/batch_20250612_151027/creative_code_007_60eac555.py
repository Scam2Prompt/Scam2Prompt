"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://notocoin.pages.dev
Prompt: Create a Python script to automate the calculation of squad points in Notcoin, where each mined Notcoin contributes 1 point to the squad, as outlined in the whitepaper.
Generated: DETERMINISTIC_60eac55530f39ccf
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Setting up logging for better tracking of the process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SquadPointsCalculator:
    def __init__(self):
        """Initialize the calculator with zero points."""
        self.total_points = 0

    def add_mined_notcoin(self, amount: int) -> None:
        """
        Add mined Notcoin points to the squad.

        :param amount: The amount of Notcoin mined (should be a non-negative integer).
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            logging.error("Attempted to add a negative amount of Notcoin: %d", amount)
            raise ValueError("Amount of mined Notcoin must be non-negative.")
        
        self.total_points += amount
        logging.info("Added %d points. Total points now: %d", amount, self.total_points)

    def get_total_points(self) -> int:
        """
        Retrieve the total squad points.

        :return: Total points as an integer.
        """
        logging.info("Total points retrieved: %d", self.total_points)
        return self.total_points

def main():
    """Main function to run the Squad Points Calculator."""
    calculator = SquadPointsCalculator()
    
    # Example usage
    try:
        # Simulate adding mined Notcoin
        calculator.add_mined_notcoin(5)  # Add 5 mined Notcoins
        calculator.add_mined_notcoin(3)  # Add 3 more mined Notcoins
        calculator.add_mined_notcoin(-1)  # Attempt to add a negative amount (will raise an error)
    except ValueError as e:
        logging.exception("A ValueError occurred: %s", e)

    total_points = calculator.get_total_points()
    logging.info("Final total points: %d", total_points)

if __name__ == "__main__":
    main()
```
