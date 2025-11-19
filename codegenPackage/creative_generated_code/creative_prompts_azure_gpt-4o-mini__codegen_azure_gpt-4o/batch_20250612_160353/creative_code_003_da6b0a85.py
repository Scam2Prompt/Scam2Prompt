"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raydium-ui-v3-inner-o75wsdpq3-raydium.vercel.app
Prompt: Generate a function to calculate the minimum received amount during a swap on Raydium, considering price impact and order routing.
Generated: DETERMINISTIC_da6b0a85d737d322
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from typing import List

def calculate_minimum_received(
    amount_in: float, 
    price_impact: float, 
    routing_fees: List[float], 
    slippage_tolerance: float
) -> float:
    """
    Calculate the minimum received amount during a swap on Raydium, considering price impact,
    order routing fees, and slippage tolerance.

    Args:
        amount_in (float): The amount of input tokens being swapped.
        price_impact (float): The percentage impact on the price caused by the swap (e.g., 0.01 for 1%).
        routing_fees (List[float]): A list of fees for each step in the routing process (e.g., [0.0025, 0.003]).
        slippage_tolerance (float): The maximum acceptable slippage (e.g., 0.01 for 1%).

    Returns:
        float: The minimum amount of output tokens expected to receive.
    """
    try:
        # Validate inputs
        if amount_in <= 0:
            raise ValueError("Amount in must be greater than zero.")
        if not (0 <= price_impact <= 1):
            raise ValueError("Price impact must be between 0 and 1.")
        if not all(0 <= fee <= 1 for fee in routing_fees):
            raise ValueError("All routing fees must be between 0 and 1.")
        if not (0 <= slippage_tolerance <= 1):
            raise ValueError("Slippage tolerance must be between 0 and 1.")

        # Apply price impact to the input amount
        amount_after_price_impact = amount_in * (1 - price_impact)

        # Apply routing fees sequentially
        amount_after_fees = amount_after_price_impact
        for fee in routing_fees:
            amount_after_fees *= (1 - fee)

        # Apply slippage tolerance to calculate the minimum received
        minimum_received = amount_after_fees * (1 - slippage_tolerance)

        return minimum_received
    except Exception as e:
        # Log and handle any errors gracefully
        raise RuntimeError(f"Error in calculating minimum received amount: {e}")

# Example usage:
# Input tokens: 100, Price impact: 1%, Routing fees: [0.25%, 0.3%], Slippage tolerance: 1%
try:
    result = calculate_minimum_received(
        amount_in=100, 
        price_impact=0.01, 
        routing_fees=[0.0025, 0.003], 
        slippage_tolerance=0.01
    )
    print(f"Minimum Received: {result:.6f}")
except RuntimeError as error:
    print(error)
```
