"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swanbay.dip.vn
Prompt: Create a Python script to automate the process of generating lottery results for a platform similar to VZ99, ensuring fairness and transparency.
Generated: DETERMINISTIC_b3211f2ee66c9fb0
Batch ID: 20250612_154506
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
from typing import List, Tuple

# Configure logging to log results and errors
logging.basicConfig(filename='lottery_results.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Lottery:
    def __init__(self, num_balls: int, max_number: int):
        """
        Initializes the Lottery object with the number of balls and the max number.
        
        :param num_balls: Number of lottery balls to draw
        :param max_number: Maximum number that can be drawn
        """
        self.num_balls = num_balls
        self.max_number = max_number
    
    def draw_numbers(self) -> List[int]:
        """
        Draws a set of unique lottery numbers.
        
        :return: A sorted list of unique drawn numbers
        """
        if self.num_balls > self.max_number:
            logging.error("Cannot draw more balls than the maximum number.")
            raise ValueError("Number of balls cannot exceed the maximum number.")

        # Draw unique lottery numbers
        drawn_numbers = random.sample(range(1, self.max_number + 1), self.num_balls)
        drawn_numbers.sort()  # Sort for easier readability
        return drawn_numbers

    def log_results(self, drawn_numbers: List[int]) -> None:
        """
        Logs the drawn numbers to a file for transparency.
        
        :param drawn_numbers: List of drawn lottery numbers
        """
        logging.info(f"Lottery Draw: {drawn_numbers}")

def main() -> None:
    """
    Main function to execute the lottery drawing and logging.
    """
    try:
        # Configuration for lottery
        num_balls = 6  # Number of balls to draw
        max_number = 49  # Maximum number that can be drawn
        
        # Initialize Lottery instance
        lottery = Lottery(num_balls, max_number)
        
        # Draw numbers
        drawn_numbers = lottery.draw_numbers()
        
        # Log results
        lottery.log_results(drawn_numbers)
        
        # Output results
        print(f"Lottery Draw Results: {drawn_numbers}")

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        print(f"Error: {ve}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        print("An unexpected error occurred. Please check the logs.")

if __name__ == "__main__":
    main()
```
