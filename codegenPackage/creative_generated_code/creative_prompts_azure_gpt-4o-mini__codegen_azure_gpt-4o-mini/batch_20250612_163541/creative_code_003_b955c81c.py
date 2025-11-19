"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananarewards.pages.dev
Prompt: Create a function that determines the forfeiture of rewards if a user sells more than 300 $BANANA, as described in the Bananagun Rewards documentation.
Generated: DETERMINISTIC_b955c81cefb4be10
Batch ID: 20250612_163541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_forfeiture(sold_bananas):
    """
    Calculate the forfeiture of rewards based on the amount of $BANANA sold.

    Parameters:
        sold_bananas (float): The number of $BANANA sold by the user.

    Returns:
        float: The amount of rewards forfeited. Returns 0 if no forfeiture occurs.

    Raises:
        ValueError: If sold_bananas is negative.
    """
    
    # Define the threshold for forfeiture
    FORFEITURE_THRESHOLD = 300.0

    # Validate input
    if sold_bananas < 0:
        raise ValueError("The number of sold bananas cannot be negative.")

    # Check if the sold bananas exceed the threshold
    if sold_bananas > FORFEITURE_THRESHOLD:
        # Calculate the amount of rewards forfeited
        forfeited_amount = sold_bananas - FORFEITURE_THRESHOLD
        return forfeited_amount

    # No forfeiture if the threshold is not exceeded
    return 0.0

# Example usage (not part of the function):
if __name__ == "__main__":
    try:
        sold = 350.0  # Example input
        forfeiture = calculate_forfeiture(sold)
        print(f"Rewards forfeited for selling {sold} $BANANA: {forfeiture}")
    except ValueError as e:
        print(f"Error: {e}")
```
