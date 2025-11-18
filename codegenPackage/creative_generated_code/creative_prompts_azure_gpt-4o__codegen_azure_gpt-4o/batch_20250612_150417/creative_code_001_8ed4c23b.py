"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-mixer.com
Prompt: Generate code to calculate the fees for mixing TONCOIN using the TONCOIN Mixer fee structure (fixed fee of 0.001 TONCOIN and less than 2% variable fee).
Generated: DETERMINISTIC_8ed4c23bd89ad2df
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the fees for mixing TONCOIN using the TONCOIN Mixer fee structure.

def calculate_mixing_fee(amount: float, variable_fee_percentage: float = 1.9) -> float:
    """
    Calculate the total mixing fee for TONCOIN.

    Args:
        amount (float): The amount of TONCOIN to be mixed.
        variable_fee_percentage (float): The variable fee percentage (default is 1.9%).

    Returns:
        float: The total fee for mixing TONCOIN.

    Raises:
        ValueError: If the provided amount is less than or equal to zero.
    """
    if amount <= 0:
        raise ValueError("The amount to be mixed must be greater than zero.")

    # Fixed fee in TONCOIN
    fixed_fee = 0.001

    # Calculate the variable fee as a percentage of the amount
    variable_fee = (variable_fee_percentage / 100) * amount

    # Total fee is the sum of the fixed fee and the variable fee
    total_fee = fixed_fee + variable_fee

    return total_fee


def main():
    """
    Main function to demonstrate the TONCOIN mixing fee calculation.
    """
    try:
        # Example TONCOIN amount to be mixed
        amount_to_mix = float(input("Enter the amount of TONCOIN to be mixed: "))
        
        # Call the function to calculate the fee
        fee = calculate_mixing_fee(amount_to_mix)

        # Print the calculated fee
        print(f"The total mixing fee for {amount_to_mix} TONCOIN is: {fee:.6f} TONCOIN")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
