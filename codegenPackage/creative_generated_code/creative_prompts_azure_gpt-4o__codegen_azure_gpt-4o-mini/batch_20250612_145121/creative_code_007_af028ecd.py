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
# total_raise_calculator.py

def calculate_total_raise(swap_price_per_token: float, total_swap_amount: float) -> float:
    """
    Calculate the total raise amount in BUSD for a project on ChainGPT Pad.
    
    Parameters:
    swap_price_per_token (float): The price per token in BUSD.
    total_swap_amount (float): The total amount of tokens to be swapped.
    
    Returns:
    float: The total raise amount in BUSD.
    
    Raises:
    ValueError: If swap_price_per_token or total_swap_amount is not positive.
    """
    # Validate inputs
    if swap_price_per_token <= 0:
        raise ValueError("swap_price_per_token must be a positive number")
    if total_swap_amount <= 0:
        raise ValueError("total_swap_amount must be a positive number")
    
    # Calculate the total raise amount
    total_raise = swap_price_per_token * total_swap_amount
    
    return total_raise

if __name__ == "__main__":
    # Example usage
    try:
        swap_price_per_token = float(input("Enter the swap price per token in BUSD: "))
        total_swap_amount = float(input("Enter the total swap amount of tokens: "))

        total_raise = calculate_total_raise(swap_price_per_token, total_swap_amount)
        print(f"The total raise amount in BUSD is: {total_raise:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
