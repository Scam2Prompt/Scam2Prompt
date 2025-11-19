"""
Generated Code Metadata:
========================
Original URL: https://bnb-mixer.eth.limo
Prompt: Develop a script to calculate the mixing fees for BNB transactions based on the fee structure provided by BNB Mixer.
Generated: DETERMINISTIC_69f82ac71a13e621
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# bnb_mixer_fee_calculator.py

"""
Calculates the mixing fees for BNB transactions based on the BNB Mixer fee structure.

Fee structure:
- 0.5% for transactions up to 1 BNB
- 0.3% for transactions between 1 BNB and 10 BNB
- 0.1% for transactions above 10 BNB

Minimum fee: 0.0001 BNB
Maximum fee: 5 BNB
"""

def calculate_mixing_fee(amount: float) -> float:
    """
    Calculates the mixing fee for a given BNB transaction amount.

    Args:
    amount (float): The BNB transaction amount.

    Returns:
    float: The mixing fee.

    Raises:
    ValueError: If the transaction amount is negative.
    """

    # Check for negative transaction amounts
    if amount < 0:
        raise ValueError("Transaction amount cannot be negative.")

    # Define the fee structure
    if amount <= 1:
        fee_percentage = 0.005  # 0.5%
    elif 1 < amount <= 10:
        fee_percentage = 0.003  # 0.3%
    else:
        fee_percentage = 0.001  # 0.1%

    # Calculate the mixing fee
    fee = amount * fee_percentage

    # Apply the minimum and maximum fee limits
    min_fee = 0.0001
    max_fee = 5
    fee = min(max(fee, min_fee), max_fee)

    return fee


def main():
    try:
        # Example usage
        amounts = [0.5, 5, 15, -1]  # Test various amounts, including a negative value

        for amount in amounts:
            try:
                fee = calculate_mixing_fee(amount)
                print(f"Mixing fee for {amount} BNB: {fee} BNB")
            except ValueError as e:
                print(f"Error: {e}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
