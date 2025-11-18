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
def calculate_total_payout(reloads: int, payout_rate: float = 0.00060000) -> float:
    """
    Calculate the total payout of DigiByte (DGB) coins after multiple reloads
    on the Auto-Faucet.

    :param reloads: The number of reloads performed.
    :param payout_rate: The payout rate per reload. Default is 0.00060000 DGB.
    :return: Total payout in DGB.
    :raises ValueError: If the number of reloads is negative.
    """
    if reloads < 0:
        raise ValueError("The number of reloads cannot be negative.")
    
    # Calculate total payout
    total_payout = reloads * payout_rate
    
    return total_payout

# Example usage
if __name__ == "__main__":
    try:
        num_of_reloads = 10  # Example number of reloads
        total_dgb = calculate_total_payout(num_of_reloads)
        print(f"Total payout for {num_of_reloads} reloads is: {total_dgb} DGB")
    except ValueError as e:
        print(f"Error: {e}")
```
