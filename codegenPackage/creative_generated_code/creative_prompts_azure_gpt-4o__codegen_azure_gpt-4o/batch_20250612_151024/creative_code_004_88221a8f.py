"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://is2btc.com
Prompt: Write a function to calculate the total payout of DigiByte (DGB) coins after multiple reloads on the Auto-Faucet at https://is2btc.com, considering the payout rate of 0.00060000 DGB per reload.
Generated: DETERMINISTIC_88221a8f0c6d5f88
Batch ID: 20250612_151024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python program to calculate the total payout of DigiByte (DGB) coins
# after multiple reloads on the Auto-Faucet.

def calculate_dgb_payout(reloads: int, payout_rate: float = 0.00060000) -> float:
    """
    Calculate the total payout of DigiByte (DGB) coins based on the number of reloads.

    Args:
        reloads (int): The number of auto-faucet reloads.
        payout_rate (float): The payout rate per reload (default is 0.00060000 DGB).

    Returns:
        float: The total payout in DGB.
    
    Raises:
        ValueError: If `reloads` is negative or a non-integer.
    """
    # Validate inputs
    if not isinstance(reloads, int) or reloads < 0:
        raise ValueError("Reloads must be a non-negative integer.")

    # Calculate total payout
    total_payout = reloads * payout_rate
    
    return total_payout


# Example usage
if __name__ == "__main__":
    try:
        # Number of reloads (user-provided input)
        num_reloads = int(input("Enter the number of reloads: "))
        
        # Calculate total payout
        total_dgb_payout = calculate_dgb_payout(num_reloads)
        
        # Display the result
        print(f"Total payout for {num_reloads} reloads: {total_dgb_payout:.8f} DGB")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
