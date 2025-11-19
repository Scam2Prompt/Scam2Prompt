"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qnwnfewifjdsifjfdsoifj.pages.dev
Prompt: Create a Python script that simulates the prize distribution for a TONCOIN spin, including the various prize tiers mentioned.
Generated: DETERMINISTIC_aca9f6baee5c6543
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random


def spin_toncoin_wheel():
    """
    Simulates a TONCOIN prize wheel spin and returns the prize amount.
    
    Prize tiers:
    - 50% chance to win 1 TONCOIN
    - 30% chance to win 5 TONCOIN
    - 15% chance to win 10 TONCOIN
    - 5% chance to win 50 TONCOIN
    
    Returns:
        int: The TONCOIN prize won.
    """
    # Defining prize tiers and their probabilities
    prize_tiers = [
        (1, 0.50),   # 50% chance to win 1 TONCOIN
        (5, 0.30),   # 30% chance to win 5 TONCOIN
        (10, 0.15),  # 15% chance to win 10 TONCOIN
        (50, 0.05)   # 5% chance to win 50 TONCOIN
    ]
    
    # Generate a random number and determine the prize
    random_number = random.random()  # Random number between 0 and 1
    cumulative_probability = 0.0
    
    for prize, probability in prize_tiers:
        cumulative_probability += probability
        if random_number <= cumulative_probability:
            return prize


def main():
    """
    Main function to simulate the TONCOIN spin and display the prize.
    """
    try:
        print("Welcome to the TONCOIN Spin!")
        # Perform the spin
        prize = spin_toncoin_wheel()
        print(f"Congratulations! You won {prize} TONCOIN!")
    except Exception as e:
        # Generic error handling
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
