"""
Generated Code Metadata:
========================
Original URL: https://raydium-ui-v3-inner-gxpo3g8fm-raydium.vercel.app
Prompt: Generate a function that calculates the estimated fees for a swap on Raydium based on user input.
Generated: DETERMINISTIC_07345e3371755355
Batch ID: 20250612_160353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_raydium_swap_fees(
    amount_in: float, 
    token_in: str, 
    token_out: str, 
    pool_liquidity: Dict[str, float], 
    fee_percentage: float = 0.001  # 0.1% default fee
) -> Dict[str, float]:
    """
    Calculates the estimated fees for a swap on Raydium.

    Args:
    - amount_in (float): The amount of token_in to swap.
    - token_in (str): The address of the token being swapped in.
    - token_out (str): The address of the token being swapped out.
    - pool_liquidity (Dict[str, float]): A dictionary containing the liquidity of the pool in quote currency (e.g., {token_in: 1000000, token_out: 2000000}).
    - fee_percentage (float, optional): The percentage of the swap amount to be used as the fee. Defaults to 0.001 (0.1%).

    Returns:
    - Dict[str, float]: A dictionary containing the estimated fees for the swap.
    """

    try:
        # Validate input parameters
        if amount_in <= 0:
            raise ValueError("Amount in must be greater than zero.")
        if fee_percentage < 0 or fee_percentage > 1:
            raise ValueError("Fee percentage must be between 0 and 1.")

        # Calculate the fee amount
        fee_amount = amount_in * fee_percentage

        # Calculate the estimated output amount (without fees)
        # For simplicity, assume a constant price impact
        price_impact = 0.01  # 1% price impact
        estimated_output_amount = amount_in * (1 - price_impact)

        # Calculate the liquidity ratio
        if token_in not in pool_liquidity or token_out not in pool_liquidity:
            raise ValueError("Pool liquidity not found for one or both tokens.")
        liquidity_in = pool_liquidity[token_in]
        liquidity_out = pool_liquidity[token_out]
        liquidity_ratio = liquidity_out / liquidity_in

        # Adjust estimated output amount based on liquidity ratio
        estimated_output_amount *= liquidity_ratio

        # Return the estimated fees
        return {
            "fee_amount": fee_amount,
            "estimated_output_amount": estimated_output_amount,
            "fee_percentage": fee_percentage
        }

    except Exception as e:
        # Log and re-raise the exception
        print(f"An error occurred: {str(e)}")
        raise


# Example usage:
if __name__ == "__main__":
    pool_liquidity = {
        "tokenA": 1000000,
        "tokenB": 2000000
    }
    result = calculate_raydium_swap_fees(
        amount_in=100,
        token_in="tokenA",
        token_out="tokenB",
        pool_liquidity=pool_liquidity
    )
    print(result)
```
