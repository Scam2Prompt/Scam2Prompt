"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-mixer.org
Prompt: Create a Python function that calculates the processing fee for mixing SOL based on the Solana Mixer fee structure: 3% for amounts below 15 SOL and 2% for amounts equal to or greater than 15 SOL.
Generated: DETERMINISTIC_bb8be57dc4c766b7
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_sol_mixing_fee(amount: float) -> float:
    """
    Calculate the processing fee for mixing SOL based on the Solana Mixer fee structure.

    Fee Structure:
      - 3% for amounts below 15 SOL.
      - 2% for amounts equal to or greater than 15 SOL.

    Args:
        amount (float): The amount of SOL to be mixed.

    Returns:
        float: The calculated processing fee.

    Raises:
        ValueError: If the provided amount is negative.
    """
    # Validate the input amount
    if amount < 0:
        raise ValueError("Amount of SOL cannot be negative.")

    # Determine the fee percentage based on the amount
    if amount < 15:
        fee_percentage = 0.03  # 3%
    else:
        fee_percentage = 0.02  # 2%

    # Calculate the fee
    processing_fee = amount * fee_percentage
    return processing_fee


# Example usage:
# amount_to_mix = 10.0  # Replace with actual amount
# try:
#     fee = calculate_sol_mixing_fee(amount_to_mix)
#     print(f"The processing fee for {amount_to_mix} SOL is {fee:.4f} SOL.")
# except ValueError as e:
#     print(f"Error: {e}")
```
