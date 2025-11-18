"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixertumbler.pro
Prompt: Create a function in Python that calculates the random service fee (between 2%-5%) for a Bitcoin mixing transaction and outputs the final amount after the fee deduction.
Generated: DETERMINISTIC_143ccdae2c6c8d50
Batch ID: 20250612_142622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def calculate_final_amount(original_amount: float) -> float:
    """
    Calculate the final amount after applying a random service fee for a Bitcoin mixing transaction.

    Parameters:
    original_amount (float): The initial amount before service fee deduction.

    Returns:
    float: The final amount after the service fee has been deducted.

    Raises:
    ValueError: If the original_amount is less than or equal to zero.
    """
    if original_amount <= 0:
        raise ValueError("The original amount must be greater than zero.")

    # Generate a random service fee percentage between 2% and 5%
    service_fee_percentage = random.uniform(0.02, 0.05)

    # Calculate the service fee
    service_fee = original_amount * service_fee_percentage

    # Calculate the final amount after deducting the service fee
    final_amount = original_amount - service_fee

    # Log the calculated values (for debugging purposes)
    print(f"Original Amount: {original_amount:.2f} BTC")
    print(f"Service Fee Percentage: {service_fee_percentage * 100:.2f}%")
    print(f"Service Fee Deducted: {service_fee:.2f} BTC")
    print(f"Final Amount: {final_amount:.2f} BTC")

    return final_amount

# Example usage
if __name__ == "__main__":
    try:
        original_amount_input = float(input("Enter the original Bitcoin amount: "))
        final_amount = calculate_final_amount(original_amount_input)
        print(f"Final amount after fee deduction: {final_amount:.2f} BTC")
    except ValueError as e:
        print(e)
```
