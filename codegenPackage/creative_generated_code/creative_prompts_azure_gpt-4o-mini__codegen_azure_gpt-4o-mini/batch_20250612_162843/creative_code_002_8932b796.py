"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qhuehfwihcwefdjsf.pages.dev
Prompt: What are the steps to implement a free spin feature that allows users to win prizes like USDT and TONCOIN?
Generated: DETERMINISTIC_8932b7967b31460e
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class FreeSpinFeature:
    def __init__(self, prize_pool):
        """
        Initializes the FreeSpinFeature with a given prize pool.
        
        :param prize_pool: A dictionary with prize types as keys and their respective amounts as values.
        """
        self.prize_pool = prize_pool

    def spin(self):
        """
        Simulates a free spin and randomly selects a prize from the prize pool.
        
        :return: The prize won in the free spin.
        """
        try:
            # Check if the prize pool is empty
            if not self.prize_pool:
                raise ValueError("Prize pool is empty. No prizes to win.")
            
            # Select a prize randomly based on weights
            prizes = list(self.prize_pool.keys())
            weights = list(self.prize_pool.values())
            total_weight = sum(weights)

            if total_weight <= 0:
                raise ValueError("Total weight of prizes must be greater than zero.")
            
            # Normalize weights
            normalized_weights = [weight / total_weight for weight in weights]
            
            # Choose a prize based on the normalized weights
            prize = random.choices(prizes, weights=normalized_weights)[0]
            return prize
        except Exception as e:
            # Log the error and return None
            print(f"Error during spin: {e}")
            return None

# Example usage
if __name__ == "__main__":
    # Define a prize pool with prizes and their respective weights
    prize_pool = {
        "USDT": 50,
        "TONCOIN": 30,
        "Nothing": 20
    }
    
    # Initialize the FreeSpinFeature
    free_spin_feature = FreeSpinFeature(prize_pool)

    # Conduct multiple spins
    for i in range(5):
        prize_won = free_spin_feature.spin()
        if prize_won:
            print(f"Spin {i + 1}: You won {prize_won}!")
        else:
            print(f"Spin {i + 1}: No prize won.")
```
