"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btconbase-en.pages.dev
Prompt: Generate code to calculate the percentage of Bitcoin on Base tokens burned, given the total supply of 21 million and the burned supply of 24.56%.
Generated: DETERMINISTIC_b4851a030182ce9b
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the percentage of Bitcoin on Base tokens burned.

def calculate_burned_tokens_percentage(total_supply: float, burned_percentage: float) -> float:
    """
    Calculate the number of tokens burned given the total supply and burned percentage.

    Args:
        total_supply (float): Total supply of tokens.
        burned_percentage (float): Percentage of tokens burned.

    Returns:
        float: Total number of burned tokens.
    """
    try:
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if not (0 <= burned_percentage <= 100):
            raise ValueError("Burned percentage must be between 0 and 100.")

        # Calculate the burned tokens
        burned_tokens = (total_supply * burned_percentage) / 100
        return burned_tokens
    except ValueError as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    # Constants
    TOTAL_SUPPLY = 21_000_000  # Total supply in Bitcoin on Base
    BURNED_PERCENTAGE = 24.56  # Burned percentage

    # Calculate the burned tokens
    result = calculate_burned_tokens_percentage(TOTAL_SUPPLY, BURNED_PERCENTAGE)

    if result is not None:
        print(f"Total burned tokens: {result:.2f}")
    else:
        print("Calculation could not be completed due to an error.")
```
