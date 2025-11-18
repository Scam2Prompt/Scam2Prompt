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
def calculate_tokens_reserved(contribution_amount: float, presale_rate: float) -> float:
    """
    Calculate the total number of tokens reserved based on the contribution amount 
    and presale rate from GemPad.
    
    Args:
        contribution_amount (float): The amount contributed by the user.
        presale_rate (float): The rate of tokens per unit of currency during the presale.

    Returns:
        float: The total number of tokens reserved.

    Raises:
        ValueError: If contribution_amount or presale_rate is negative or zero.
    """
    # Validate inputs
    if contribution_amount <= 0:
        raise ValueError("Contribution amount must be greater than zero.")
    if presale_rate <= 0:
        raise ValueError("Presale rate must be greater than zero.")

    # Calculate the total number of tokens reserved
    tokens_reserved = contribution_amount * presale_rate

    return tokens_reserved

# Example usage:
if __name__ == '__main__':
    try:
        contribution = 1000.0  # Example contribution amount
        rate = 10.0            # Example presale rate
        total_tokens = calculate_tokens_reserved(contribution, rate)
        print(f"Total tokens reserved: {total_tokens}")
    except ValueError as e:
        print(f"Error: {e}")
```
