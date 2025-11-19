"""
Generated Code Metadata:
========================
Original URL: https://raydium-ui-v3-inner-101j4nwdn-raydium.vercel.app
Prompt: Generate a code example for calculating the price impact of a token swap on Raydium given the input and output amounts.
Generated: DETERMINISTIC_d69c64008c9020dc
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_price_impact(input_amount, output_amount, pool_input_reserve, pool_output_reserve):
    """
    Calculate the price impact of a token swap on Raydium.

    Parameters:
        input_amount (float): The amount of input tokens being swapped.
        output_amount (float): The amount of output tokens received.
        pool_input_reserve (float): The current reserve of input tokens in the pool.
        pool_output_reserve (float): The current reserve of output tokens in the pool.

    Returns:
        float: The price impact as a percentage.
    """
    try:
        # Validate inputs
        if input_amount <= 0 or output_amount <= 0:
            raise ValueError("Input and output amounts must be greater than zero.")
        if pool_input_reserve <= 0 or pool_output_reserve <= 0:
            raise ValueError("Pool reserves must be greater than zero.")

        # Calculate the initial price (before the swap)
        initial_price = pool_input_reserve / pool_output_reserve

        # Calculate the final price (after the swap)
        final_price = (pool_input_reserve + input_amount) / (pool_output_reserve - output_amount)

        # Calculate the price impact
        price_impact = ((final_price - initial_price) / initial_price) * 100

        return price_impact

    except ZeroDivisionError:
        raise ValueError("Division by zero encountered. Check pool reserves and swap amounts.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while calculating price impact: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Example pool reserves and swap amounts
        pool_input_reserve = 1000000  # Example reserve of input tokens
        pool_output_reserve = 500000  # Example reserve of output tokens
        input_amount = 1000           # Example input token amount
        output_amount = 490           # Example output token amount

        # Calculate price impact
        price_impact = calculate_price_impact(input_amount, output_amount, pool_input_reserve, pool_output_reserve)

        print(f"Price Impact: {price_impact:.2f}%")
    except Exception as e:
        print(f"Error: {e}")
```
