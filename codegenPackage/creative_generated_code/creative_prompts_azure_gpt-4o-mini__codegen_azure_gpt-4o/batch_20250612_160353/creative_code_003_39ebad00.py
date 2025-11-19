"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raydium-ui-v3-inner-e259flm87-raydium.vercel.app
Prompt: Generate a function that calculates the minimum received amount and price impact for a swap on Raydium.
Generated: DETERMINISTIC_39ebad005a93a665
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_swap_details(input_amount, pool_reserve_in, pool_reserve_out, swap_fee):
    """
    Calculate the minimum received amount and price impact for a swap on Raydium.

    Args:
        input_amount (float): The amount of tokens to be swapped (input amount).
        pool_reserve_in (float): The reserve of the input token in the pool.
        pool_reserve_out (float): The reserve of the output token in the pool.
        swap_fee (float): The swap fee percentage (e.g., 0.003 for 0.3%).

    Returns:
        dict: 
            min_received (float): Minimum amount of output tokens received after swap and fees.
            price_impact (float): Percentage impact on the price due to the swap.
    """

    try:
        # Validate inputs
        if input_amount <= 0:
            raise ValueError("Input amount must be greater than 0.")
        if pool_reserve_in <= 0 or pool_reserve_out <= 0:
            raise ValueError("Pool reserves must be greater than 0.")
        if not (0 <= swap_fee < 1):
            raise ValueError("Swap fee must be between 0 and 1.")

        # Calculate output amount without fees using x * y = k formula
        k = pool_reserve_in * pool_reserve_out
        new_pool_reserve_in = pool_reserve_in + input_amount
        new_pool_reserve_out = k / new_pool_reserve_in
        output_amount_without_fee = pool_reserve_out - new_pool_reserve_out

        # Apply swap fee
        output_amount_with_fee = output_amount_without_fee * (1 - swap_fee)

        # Calculate price impact
        price_before_swap = pool_reserve_out / pool_reserve_in
        price_after_swap = (pool_reserve_out - output_amount_with_fee) / (pool_reserve_in + input_amount)
        price_impact = ((price_before_swap - price_after_swap) / price_before_swap) * 100

        # Return minimum received amount and price impact
        return {
            "min_received": output_amount_with_fee,
            "price_impact": price_impact
        }
    except Exception as e:
        # Handle errors gracefully
        print(f"Error: {e}")
        return None


# Example usage:
if __name__ == "__main__":
    # Replace these values with actual pool data and user input
    input_amount = 100.0   # Input amount to swap
    pool_reserve_in = 50000.0  # Reserve of input token in the pool
    pool_reserve_out = 20000.0  # Reserve of output token in the pool
    swap_fee = 0.003  # Swap fee percentage (0.3%)

    result = calculate_swap_details(input_amount, pool_reserve_in, pool_reserve_out, swap_fee)
    if result:
        print(f"Minimum Received: {result['min_received']:.6f}")
        print(f"Price Impact: {result['price_impact']:.6f}%")
```
