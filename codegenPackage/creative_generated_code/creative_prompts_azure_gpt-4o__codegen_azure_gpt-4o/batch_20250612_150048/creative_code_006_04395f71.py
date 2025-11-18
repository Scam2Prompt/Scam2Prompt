"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdltl0.top
Prompt: Create a function to display gas fees and final received amounts for USDT transfers, based on the "Transfer Connect Token USDT0" system.
Generated: DETERMINISTIC_04395f714a7c7407
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

def calculate_gas_and_final_amounts(amount: float, gas_fee_percentage: float) -> dict:
    """
    Calculate gas fees and final received amounts for USDT transfers.

    Args:
        amount (float): The amount of USDT to be transferred.
        gas_fee_percentage (float): The gas fee percentage applied to the transfer (e.g., 0.5 for 0.5%).

    Returns:
        dict: A dictionary containing:
            - 'original_amount': The original transfer amount.
            - 'gas_fee': The calculated gas fee.
            - 'final_amount': The amount received after deducting the gas fee.
    """
    try:
        # Use Decimal for precise financial calculations
        amount = decimal.Decimal(amount)
        gas_fee_percentage = decimal.Decimal(gas_fee_percentage)
        
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        if gas_fee_percentage < 0:
            raise ValueError("Gas fee percentage must be non-negative.")

        # Calculate gas fee
        gas_fee = amount * (gas_fee_percentage / 100)

        # Calculate final amount received
        final_amount = amount - gas_fee

        # Prepare the result dictionary
        result = {
            'original_amount': round(amount, 2),
            'gas_fee': round(gas_fee, 2),
            'final_amount': round(final_amount, 2)
        }

        return result
    except (ValueError, decimal.InvalidOperation) as e:
        # Handle invalid input and calculation errors
        return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    # Example inputs
    transfer_amount = 1000  # Amount in USDT
    gas_fee_rate = 0.5  # Gas fee as a percentage (e.g., 0.5%)

    # Calculate fees and final amount
    result = calculate_gas_and_final_amounts(transfer_amount, gas_fee_rate)

    # Display result
    if "error" in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Original Amount: {result['original_amount']} USDT")
        print(f"Gas Fee: {result['gas_fee']} USDT")
        print(f"Final Amount Received: {result['final_amount']} USDT")
```
