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
import sys

def calculate_total_raised(price_per_token: float, swap_amount: int) -> float:
    """
    Calculate the total amount raised for a token swap.

    Args:
        price_per_token (float): The price of a single token in the swap.
        swap_amount (int): The total number of tokens swapped.

    Returns:
        float: The total amount raised for the token swap.
    """
    try:
        # Ensure inputs are valid
        if price_per_token <= 0:
            raise ValueError("Price per token must be greater than zero.")
        if swap_amount <= 0:
            raise ValueError("Swap amount must be greater than zero.")

        # Calculate the total amount raised
        total_raised = price_per_token * swap_amount
        return total_raised

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Example usage:
    try:
        # Prompt user for price per token and swap amount
        price_per_token_input = input("Enter the price per token: ")
        swap_amount_input = input("Enter the swap amount (number of tokens): ")

        # Convert inputs to appropriate types
        price_per_token = float(price_per_token_input)
        swap_amount = int(swap_amount_input)

        # Calculate and display the total raised amount
        total_raised = calculate_total_raised(price_per_token, swap_amount)
        print(f"Total amount raised for the WORK token swap: ${total_raised:.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values for price per token and swap amount.")
    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
