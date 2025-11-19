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
def calculate_processing_fee(amount_in_sol: float) -> float:
    """
    Calculates the processing fee for mixing SOL based on the Solana Mixer fee structure.

    Args:
        amount_in_sol (float): The amount of SOL to calculate the fee for.

    Returns:
        float: The processing fee in SOL.

    Raises:
        ValueError: If the amount is negative.
    """

    # Check for negative amounts
    if amount_in_sol < 0:
        raise ValueError("Amount cannot be negative")

    # Define the fee structure
    if amount_in_sol < 15:
        # 3% fee for amounts below 15 SOL
        fee = amount_in_sol * 0.03
    else:
        # 2% fee for amounts equal to or greater than 15 SOL
        fee = amount_in_sol * 0.02

    return fee


def main():
    try:
        # Example usage
        amounts = [10, 15, 20, -5]
        for amount in amounts:
            try:
                fee = calculate_processing_fee(amount)
                print(f"Processing fee for {amount} SOL: {fee} SOL")
            except ValueError as e:
                print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
