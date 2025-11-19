"""
Generated Code Metadata:
========================
Original URL: https://qnwnfewifjdsifjfdsoifj.pages.dev
Prompt: Create a Python script that simulates the prize distribution for a TONCOIN spin, including the various prize tiers mentioned.
Generated: DETERMINISTIC_aca9f6baee5c6543
Batch ID: 20250612_162849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def simulate_toncoin_spin():
    """
    Simulates a TONCOIN spin and returns the prize won.
    
    Prize tiers:
    - Grand Prize: 1 TONCOIN (1% chance)
    - First Prize: 0.5 TONCOIN (5% chance)
    - Second Prize: 0.1 TONCOIN (20% chance)
    - Consolation Prize: 0.01 TONCOIN (74% chance)
    """
    try:
        # Define prize tiers and their probabilities
        prize_tiers = [
            {"name": "Grand Prize", "amount": 1.0, "probability": 0.01},
            {"name": "First Prize", "amount": 0.5, "probability": 0.05},
            {"name": "Second Prize", "amount": 0.1, "probability": 0.20},
            {"name": "Consolation Prize", "amount": 0.01, "probability": 0.74},
        ]

        # Generate a random number between 0 and 1
        spin_result = random.random()

        # Determine the prize based on the spin result
        cumulative_probability = 0.0
        for tier in prize_tiers:
            cumulative_probability += tier["probability"]
            if spin_result <= cumulative_probability:
                return f"Congratulations! You won the {tier['name']} worth {tier['amount']} TONCOIN."

        # Fallback in case probabilities are misconfigured
        return "Error: Unable to determine prize. Please check prize configuration."

    except Exception as e:
        # Handle unexpected errors gracefully
        return f"An error occurred during the spin simulation: {str(e)}"


if __name__ == "__main__":
    # Simulate a TONCOIN spin and display the result
    print(simulate_toncoin_spin())
```
