"""
Generated Code Metadata:
========================
Original URL: https://solana-mixer.org
Prompt: Create a Python function that calculates the processing fee for mixing SOL based on the Solana Mixer fee structure: 3% for amounts below 15 SOL and 2% for amounts equal to or greater than 15 SOL.
Generated: DETERMINISTIC_bb8be57dc4c766b7
Batch ID: 20250612_155048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_processing_fee(amount: float) -> float:
    """
    Calculate the processing fee for mixing SOL based on the Solana Mixer fee structure.

    Parameters:
    amount (float): The amount of SOL to be mixed.

    Returns:
    float: The calculated processing fee.

    Raises:
    ValueError: If the amount is negative.
    """
    # Validate the input amount
    if amount < 0:
        raise ValueError("Amount must be a non-negative value.")

    # Define the fee structure
    if amount < 15:
        fee_percentage = 0.03  # 3% fee for amounts below 15 SOL
    else:
        fee_percentage = 0.02  # 2% fee for amounts equal to or greater than 15 SOL

    # Calculate the processing fee
    processing_fee = amount * fee_percentage

    return processing_fee

# Example usage
if __name__ == "__main__":
    try:
        amount_to_mix = 10.0  # Example amount
        fee = calculate_processing_fee(amount_to_mix)
        print(f"The processing fee for mixing {amount_to_mix} SOL is: {fee:.2f} SOL")
    except ValueError as e:
        print(f"Error: {e}")
```
