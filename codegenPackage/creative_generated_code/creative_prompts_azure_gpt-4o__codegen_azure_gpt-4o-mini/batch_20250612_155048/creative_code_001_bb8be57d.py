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
def calculate_processing_fee(amount: float) -> float:
    """
    Calculate the processing fee for mixing SOL based on the fee structure:
    - 3% for amounts below 15 SOL
    - 2% for amounts equal to or greater than 15 SOL

    Parameters:
    amount (float): The amount of SOL to process.

    Returns:
    float: The calculated processing fee.

    Raises:
    ValueError: If the amount is negative or not a number.
    """
    
    # Validate the input amount
    if not isinstance(amount, (int, float)):
        raise ValueError("Amount must be a numeric value.")
    if amount < 0:
        raise ValueError("Amount cannot be negative.")

    # Define fee percentages
    if amount < 15:
        fee_percentage = 0.03  # 3%
    else:
        fee_percentage = 0.02  # 2%

    # Calculate the processing fee
    fee = amount * fee_percentage
    return round(fee, 2)  # Round to two decimal places for currency representation

# Example usage:
if __name__ == "__main__":
    try:
        amount_to_process = 10.0  # Example input
        fee = calculate_processing_fee(amount_to_process)
        print(f"Processing fee for {amount_to_process} SOL: {fee} SOL")
    except ValueError as e:
        print(f"Error: {e}")
```
