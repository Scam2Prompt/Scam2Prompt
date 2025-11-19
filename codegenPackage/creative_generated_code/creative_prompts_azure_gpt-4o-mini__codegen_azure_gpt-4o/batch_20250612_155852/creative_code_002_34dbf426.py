"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bridgetensor.org
Prompt: Create a function that calculates the fees for bridging TAO to wTAO using the fee structure provided by BridgeTensor, ensuring it accounts for both the gas fee and the percentage fee.
Generated: DETERMINISTIC_34dbf426408e4ff7
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required modules
from typing import Union

def calculate_bridge_fee(amount: Union[int, float], gas_fee: Union[int, float], percentage_fee: Union[int, float]) -> Union[int, float]:
    """
    Calculate the total fees for bridging TAO to wTAO.

    Parameters:
    - amount (Union[int, float]): The amount of TAO to be bridged.
    - gas_fee (Union[int, float]): The fixed gas fee for the bridging operation.
    - percentage_fee (Union[int, float]): The percentage fee for the bridging operation (e.g., 0.01 for 1%).

    Returns:
    - Union[int, float]: The total fee for bridging TAO to wTAO.

    Raises:
    - ValueError: If input values are negative or if percentage_fee is greater than 1.
    """
    # Input validation
    if amount < 0:
        raise ValueError("The amount must be a non-negative value.")
    if gas_fee < 0:
        raise ValueError("The gas fee must be a non-negative value.")
    if not (0 <= percentage_fee <= 1):
        raise ValueError("The percentage fee must be between 0 and 1.")

    # Calculate the percentage fee based on the amount
    calculated_percentage_fee = amount * percentage_fee

    # Calculate the total fee by summing the gas fee and the percentage fee
    total_fee = gas_fee + calculated_percentage_fee

    # Return the total fee
    return total_fee

# Example usage:
# amount_to_bridge = 1000
# fixed_gas_fee = 5
# bridge_percentage_fee = 0.01  # 1%
# print(calculate_bridge_fee(amount_to_bridge, fixed_gas_fee, bridge_percentage_fee))
```
