"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pad-chaingpt.pages.dev
Prompt: Write a script to calculate the total raise amount in BUSD for a project on ChainGPT Pad, given the swap price per token and the total swap amount.
Generated: DETERMINISTIC_af028ecd2f3d8826
Batch ID: 20250612_145121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the total raise amount in BUSD for a project on ChainGPT Pad
# given the swap price per token and the total swap amount.

def calculate_total_raise(swap_price_per_token: float, total_swap_amount: int) -> float:
    """
    Calculate the total raise amount in BUSD.
    
    Args:
        swap_price_per_token (float): The price of one token in BUSD.
        total_swap_amount (int): The total number of tokens to be swapped.

    Returns:
        float: The total raise amount in BUSD.
    """
    try:
        # Validate inputs
        if swap_price_per_token <= 0:
            raise ValueError("Swap price per token must be greater than 0.")
        if total_swap_amount <= 0:
            raise ValueError("Total swap amount must be greater than 0.")
        
        # Calculate total raise amount
        total_raise = swap_price_per_token * total_swap_amount
        
        return total_raise
    except ValueError as e:
        # Handle invalid inputs
        print(f"Error: {e}")
        return 0.0
    except Exception as e:
        # Handle unexpected exceptions
        print(f"Unexpected error occurred: {e}")
        return 0.0

if __name__ == "__main__":
    # Example usage:
    
    # Inputs
    try:
        swap_price_per_token = float(input("Enter swap price per token (in BUSD): "))
        total_swap_amount = int(input("Enter total swap amount (number of tokens): "))
        
        # Calculate and display the total raise amount
        total_raise = calculate_total_raise(swap_price_per_token, total_swap_amount)
        if total_raise > 0:
            print(f"Total raise amount in BUSD: {total_raise:.2f}")
        else:
            print("Failed to calculate the total raise amount due to invalid input.")
    except ValueError:
        print("Please enter valid numeric values for swap price and total swap amount.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
