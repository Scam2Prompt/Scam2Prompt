"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pad-chaingpt.pages.dev
Prompt: Generate a script to calculate the total amount raised for the WORK token swap on ChainGPT Pad based on the price per token and swap amount.
Generated: DETERMINISTIC_a2b9f1c4565c4662
Batch ID: 20250612_160656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_total_amount(price_per_token: float, swap_amount: int) -> float:
    """
    Calculate the total amount raised for the WORK token swap.

    Args:
        price_per_token (float): The price of a single WORK token.
        swap_amount (int): The number of WORK tokens being swapped.

    Returns:
        float: The total amount raised for the token swap.

    Raises:
        ValueError: If price_per_token or swap_amount is negative.
    """
    if price_per_token < 0 or swap_amount < 0:
        raise ValueError("Price per token and swap amount must be non-negative.")

    total_amount = price_per_token * swap_amount
    return total_amount


def main():
    """
    Main function to execute the total amount calculation for the WORK token swap.
    """
    try:
        # Example input values
        price_per_token = 0.5  # Price of a single WORK token in USD
        swap_amount = 1000      # Number of tokens being swapped

        total_raised = calculate_total_amount(price_per_token, swap_amount)
        print(f"Total amount raised for the WORK token swap: ${total_raised:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
