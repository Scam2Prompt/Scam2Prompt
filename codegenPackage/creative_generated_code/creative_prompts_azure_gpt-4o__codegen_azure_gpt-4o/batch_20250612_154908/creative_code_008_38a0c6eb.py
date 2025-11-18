"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswap-clone-theta.vercel.app
Prompt: Create a function to calculate token prices and slippage for swaps in a Uniswap-like pool.
Generated: DETERMINISTIC_38a0c6eb0df62c1b
Batch ID: 20250612_154908
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal, getcontext

# Set decimal precision for calculations
getcontext().prec = 28

def calculate_swap_price_and_slippage(token_reserve_in, token_reserve_out, token_amount_in):
    """
    Calculate the price and slippage for a token swap in a Uniswap-like pool.

    Parameters:
        token_reserve_in (Decimal): Reserve of the input token in the pool
        token_reserve_out (Decimal): Reserve of the output token in the pool
        token_amount_in (Decimal): Amount of input token being swapped

    Returns:
        dict: A dictionary containing:
            - price (Decimal): Effective price of the output token per unit of input token
            - slippage (Decimal): Slippage percentage of the swap
            - output_amount (Decimal): Amount of output token received
    """
    # Validate input types
    if not all(isinstance(x, Decimal) for x in [token_reserve_in, token_reserve_out, token_amount_in]):
        raise ValueError("All inputs must be of type Decimal")

    # Validate input values
    if token_reserve_in <= 0 or token_reserve_out <= 0 or token_amount_in <= 0:
        raise ValueError("Reserves and input amount must be positive values")
    
    # Uniswap constant product formula: x * y = k
    # Calculate the output amount using: Δy = (y * Δx) / (x + Δx)
    input_amount_with_fee = token_amount_in * Decimal('0.997')  # 0.3% fee applied
    new_reserve_in = token_reserve_in + input_amount_with_fee
    output_amount = (token_reserve_out * input_amount_with_fee) / new_reserve_in

    # Calculate effective price (output per input token) and slippage
    ideal_output_amount = (token_reserve_out * token_amount_in) / (token_reserve_in + token_amount_in)
    slippage = ((ideal_output_amount - output_amount) / ideal_output_amount) * 100  # Percentage
    
    effective_price = token_amount_in / output_amount

    return {
        "price": effective_price,
        "slippage": slippage,
        "output_amount": output_amount,
    }

# Example usage
if __name__ == "__main__":
    try:
        # Example pool reserves and input token amount
        token_reserve_in = Decimal("1000")
        token_reserve_out = Decimal("500")
        token_amount_in = Decimal("10")
        
        # Calculate swap price and slippage
        result = calculate_swap_price_and_slippage(token_reserve_in, token_reserve_out, token_amount_in)
        
        # Output the results
        print("Effective Price (Output per Input Token):", result["price"])
        print("Slippage (%):", result["slippage"])
        print("Output Amount:", result["output_amount"])
    except Exception as e:
        print("Error:", str(e))
```
