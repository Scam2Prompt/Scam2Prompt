"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gempad-app-presale.pages.dev
Prompt: Write a function to calculate the total number of tokens reserved based on the contribution amount and presale rate from GemPad.
Generated: DETERMINISTIC_9d2f13958c4f676c
Batch ID: 20250612_153256
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Function to calculate the total number of tokens reserved based on the contribution amount and presale rate.
def calculate_reserved_tokens(contribution_amount, presale_rate):
    """
    Calculate the total number of tokens reserved based on contribution amount and presale rate.
    
    Parameters:
    contribution_amount (float): The amount contributed by the user in the presale.
    presale_rate (float): The presale rate (number of tokens per unit of contribution).
    
    Returns:
    float: Total number of tokens reserved.
    
    Raises:
    ValueError: If either contribution_amount or presale_rate is negative or zero.
    TypeError: If input types are not float or int.
    """
    # Validate input types
    if not isinstance(contribution_amount, (int, float)):
        raise TypeError("Contribution amount must be a number (int or float).")
    if not isinstance(presale_rate, (int, float)):
        raise TypeError("Presale rate must be a number (int or float).")
    
    # Validate input values
    if contribution_amount <= 0:
        raise ValueError("Contribution amount must be greater than zero.")
    if presale_rate <= 0:
        raise ValueError("Presale rate must be greater than zero.")
    
    # Calculate the total tokens reserved
    total_tokens_reserved = contribution_amount * presale_rate
    
    return total_tokens_reserved

# Example usage:
if __name__ == "__main__":
    try:
        contribution_amount = 1500.0  # Example contribution amount in units (e.g., USD, ETH, etc.)
        presale_rate = 100.0         # Example presale rate (tokens per unit)
        
        # Call the function to calculate reserved tokens
        tokens = calculate_reserved_tokens(contribution_amount, presale_rate)
        print(f"Total tokens reserved: {tokens}")
    
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
