"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethereumtumbler.to
Prompt: Create a function that calculates the service fee for tumbling Ethereum using Ethereum Tumbler, considering the fee range of 0.70% to 3%.
Generated: DETERMINISTIC_deb1723683fbecff
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_service_fee(amount: float, fee_percentage: float) -> float:
    """
    Calculate the service fee for tumbling Ethereum.

    Parameters:
    amount (float): The amount of Ethereum to tumble.
    fee_percentage (float): The fee percentage to apply (should be between 0.7 and 3.0).

    Returns:
    float: The calculated service fee.

    Raises:
    ValueError: If the amount is non-positive or if the fee_percentage is not within the valid range.
    """

    # Validate amount
    if amount <= 0:
        raise ValueError("The amount must be a positive number.")
    
    # Validate fee_percentage
    if not (0.7 <= fee_percentage <= 3.0):
        raise ValueError("Fee percentage must be between 0.70% and 3.00%.")

    # Calculate the service fee
    service_fee = (fee_percentage / 100) * amount
    return service_fee

# Example usage
if __name__ == "__main__":
    try:
        amount_to_tumble = 1.5  # Example amount in Ethereum
        fee_percentage = 2.0     # Example fee in percentage
        fee = calculate_service_fee(amount_to_tumble, fee_percentage)
        print(f"The service fee for tumbling {amount_to_tumble} ETH at {fee_percentage}% is: {fee:.4f} ETH")
    except ValueError as e:
        print(f"Error: {e}")
```
