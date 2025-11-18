"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinof-inance.github.io
Prompt: Write a script to calculate transaction fees for swapping assets across different chains using Rhino.fi's low-cost fee model.
Generated: DETERMINISTIC_66485815b9212bcd
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

# Define a custom exception for handling errors in fee calculation
class FeeCalculationError(Exception):
    pass

# Function to calculate transaction fees based on Rhino.fi's low-cost fee model
def calculate_transaction_fee(asset_amount, base_fee, chain_fee_factor, swap_fee_factor):
    """
    Calculate transaction fee for swapping assets across chains.

    Parameters:
        asset_amount (Decimal): The amount of the asset being swapped.
        base_fee (Decimal): The fixed base fee for the transaction.
        chain_fee_factor (Decimal): A multiplier that accounts for the cost of operating on the specific chain.
        swap_fee_factor (Decimal): A multiplier for the cost of swapping assets.

    Returns:
        Decimal: The total transaction fee.

    Raises:
        FeeCalculationError: If invalid input parameters are provided.
    """
    try:
        # Validate input parameters
        if asset_amount <= 0:
            raise FeeCalculationError("Asset amount must be greater than zero.")
        if base_fee < 0 or chain_fee_factor < 0 or swap_fee_factor < 0:
            raise FeeCalculationError("Fee parameters must be non-negative.")

        # Calculate individual fee components
        chain_fee = asset_amount * chain_fee_factor
        swap_fee = asset_amount * swap_fee_factor

        # Calculate total transaction fee
        total_fee = base_fee + chain_fee + swap_fee

        return total_fee
    except Exception as e:
        raise FeeCalculationError(f"Error occurred during fee calculation: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Set asset amount and fee parameters
        asset_amount = decimal.Decimal("100.0")  # Asset amount (e.g., 100 units)
        base_fee = decimal.Decimal("0.50")      # Fixed base fee
        chain_fee_factor = decimal.Decimal("0.01")  # Chain fee multiplier
        swap_fee_factor = decimal.Decimal("0.005")  # Swap fee multiplier

        # Calculate transaction fee
        total_fee = calculate_transaction_fee(asset_amount, base_fee, chain_fee_factor, swap_fee_factor)

        # Display the result
        print(f"Transaction Fee: {total_fee:.2f} units")

    except FeeCalculationError as e:
        print(f"Failed to calculate transaction fee: {e}")
```
