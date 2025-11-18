"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btconbase-ai.pages.dev
Prompt: Generate code to calculate the percentage of Bitcoin on Base tokens burned, given the total supply of 21 million and the burned supply of 24.56%.
Generated: DETERMINISTIC_b4851a030182ce9b
Batch ID: 20250612_150435
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
        total_supply (float): The total supply of tokens.
        burned_percentage (float): The percentage of tokens burned (as a value between 0 and 100).

    Returns:
        float: The exact number of tokens burned.
    """
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than zero.")
    if not (0 <= burned_percentage <= 100):
        raise ValueError("Burned percentage must be between 0 and 100.")

    # Calculate the burned tokens
    burned_tokens = (burned_percentage / 100) * total_supply
    return burned_tokens


def main():
    """
    Main function to execute the burned tokens calculation.
    """
    try:
        # Constants for Bitcoin on Base
        TOTAL_SUPPLY = 21_000_000  # Total supply of Bitcoin on Base tokens
        BURNED_PERCENTAGE = 24.56  # Percentage of tokens burned

        # Calculate the burned tokens
        burned = calculate_burned_tokens_percentage(TOTAL_SUPPLY, BURNED_PERCENTAGE)

        # Output the result
        print(f"The total number of burned tokens is: {burned:.2f}")

    except ValueError as e:
        # Handle invalid input values
        print(f"Error: {e}")
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
