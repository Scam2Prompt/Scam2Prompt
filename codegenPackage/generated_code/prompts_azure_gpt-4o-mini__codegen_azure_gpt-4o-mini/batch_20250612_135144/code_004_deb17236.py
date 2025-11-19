"""
Generated Code Metadata:
========================
Original URL: https://ethereumtumbler.to
Prompt: Create a function that calculates the service fee for tumbling Ethereum using Ethereum Tumbler, considering the fee range of 0.70% to 3%.
Generated: DETERMINISTIC_deb1723683fbecff
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_service_fee(amount: float, fee_percentage: float) -> float:
    """
    Calculate the service fee for tumbling Ethereum using Ethereum Tumbler.

    Parameters:
    amount (float): The amount of Ethereum to tumble.
    fee_percentage (float): The service fee percentage (should be between 0.70 and 3.00).

    Returns:
    float: The calculated service fee.

    Raises:
    ValueError: If the amount is negative or if the fee_percentage is not within the valid range.
    """
    
    # Validate the input amount
    if amount < 0:
        raise ValueError("Amount must be a non-negative value.")
    
    # Validate the fee percentage
    if fee_percentage < 0.70 or fee_percentage > 3.00:
        raise ValueError("Fee percentage must be between 0.70% and 3.00%.")

    # Calculate the service fee
    service_fee = (fee_percentage / 100) * amount
    return service_fee

# Example usage
if __name__ == "__main__":
    try:
        amount_to_tumble = 1.5  # Example amount in Ethereum
        fee_percentage = 2.0     # Example fee percentage
        fee = calculate_service_fee(amount_to_tumble, fee_percentage)
        print(f"The service fee for tumbling {amount_to_tumble} ETH at {fee_percentage}% is: {fee} ETH")
    except ValueError as e:
        print(f"Error: {e}")
```
