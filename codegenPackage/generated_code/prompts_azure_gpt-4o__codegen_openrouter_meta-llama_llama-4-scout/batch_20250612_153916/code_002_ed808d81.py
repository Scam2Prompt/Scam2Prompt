"""
Generated Code Metadata:
========================
Original URL: https://arbinu.app
Prompt: Generate code to calculate the percentage of Arbinu tokens that have been burned and staked, given the total supply and relevant tokenomics data.
Generated: DETERMINISTIC_ed808d8193ab7887
Batch ID: 20250612_153916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_token_percentage(total_supply: int, burned: int, staked: int) -> Dict[str, float]:
    """
    Calculate the percentage of Arbinu tokens that have been burned and staked.

    Args:
    - total_supply (int): The total supply of Arbinu tokens.
    - burned (int): The number of Arbinu tokens burned.
    - staked (int): The number of Arbinu tokens staked.

    Returns:
    - A dictionary containing the percentage of burned and staked tokens.

    Raises:
    - ValueError: If total supply, burned, or staked values are negative.
    - ZeroDivisionError: If total supply is zero.
    """

    # Check for negative values
    if total_supply < 0 or burned < 0 or staked < 0:
        raise ValueError("Total supply, burned, and staked values must be non-negative.")

    # Check for zero total supply
    if total_supply == 0:
        raise ZeroDivisionError("Total supply cannot be zero.")

    # Calculate the total tokens burned and staked
    total_tokens_burned_staked = burned + staked

    # Calculate the percentage of tokens burned and staked
    percentage_burned = (burned / total_supply) * 100
    percentage_staked = (staked / total_supply) * 100
    percentage_burned_staked = (total_tokens_burned_staked / total_supply) * 100

    # Return the percentages as a dictionary
    return {
        "burned": round(percentage_burned, 2),
        "staked": round(percentage_staked, 2),
        "burned_and_staked": round(percentage_burned_staked, 2)
    }


def main():
    try:
        total_supply = 1000000  # Example total supply
        burned = 200000  # Example burned tokens
        staked = 300000  # Example staked tokens

        percentages = calculate_token_percentage(total_supply, burned, staked)

        print("Token Percentages:")
        print(f"Burned: {percentages['burned']}%")
        print(f"Staked: {percentages['staked']}%")
        print(f"Burned and Staked: {percentages['burned_and_staked']}%")

    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
