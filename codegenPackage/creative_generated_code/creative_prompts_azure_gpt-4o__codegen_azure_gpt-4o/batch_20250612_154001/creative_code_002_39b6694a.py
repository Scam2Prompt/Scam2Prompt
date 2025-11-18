"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xai320k.com
Prompt: Generate code to calculate bonus percentages (e.g., up to 200%) for token purchases in a cryptocurrency presale, referencing xAI320K's presale structure.
Generated: DETERMINISTIC_39b6694aa7b0c7fd
Batch ID: 20250612_154001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: presale_bonus_calculator.py

# Import necessary modules
from typing import List, Dict

# Define a function to calculate bonus percentages
def calculate_bonus(purchase_amount: float, presale_structure: List[Dict[str, float]]) -> float:
    """
    Calculate bonus percentage based on the purchase amount and presale tiers.

    Args:
        purchase_amount (float): The amount of tokens purchased.
        presale_structure (List[Dict[str, float]]): Structure of presale tiers.
            Each tier is a dictionary with keys:
            - 'min': Minimum purchase amount for the tier (inclusive).
            - 'max': Maximum purchase amount for the tier (exclusive).
            - 'bonus': Bonus percentage for the tier.

    Returns:
        float: The bonus percentage applicable to the purchase.
    """
    if purchase_amount <= 0:
        raise ValueError("Purchase amount must be greater than 0.")

    for tier in presale_structure:
        if tier['min'] <= purchase_amount < tier['max']:
            return tier['bonus']

    # If no tier matches, return 0 bonus
    return 0.0


# Example presale structure based on xAI320K's presale model
presale_structure = [
    {'min': 0, 'max': 1000, 'bonus': 0.0},     # No bonus for purchases under 1000 tokens
    {'min': 1000, 'max': 5000, 'bonus': 50.0}, # 50% bonus for purchases between 1000 and 5000 tokens
    {'min': 5000, 'max': 10000, 'bonus': 100.0}, # 100% bonus for purchases between 5000 and 10000 tokens
    {'min': 10000, 'max': 20000, 'bonus': 150.0}, # 150% bonus for purchases between 10,000 and 20,000 tokens
    {'min': 20000, 'max': float('inf'), 'bonus': 200.0}, # 200% bonus for purchases over 20,000 tokens
]

# Example usage in production
def main():
    try:
        purchase_amount = float(input("Enter the purchase amount: "))
        bonus = calculate_bonus(purchase_amount, presale_structure)
        print(f"Your bonus percentage is: {bonus}%")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
