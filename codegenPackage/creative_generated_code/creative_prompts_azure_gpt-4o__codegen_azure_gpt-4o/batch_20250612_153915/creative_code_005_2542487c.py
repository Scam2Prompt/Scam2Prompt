"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adrop.one
Prompt: Create a function to calculate fees for claiming rewards in a TON airdrop, considering fees can be denominated in TON or issued tokens.
Generated: DETERMINISTIC_2542487c74036d94
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_reward_claim_fee(claim_amount, fee_percentage, fee_denomination='TON', token_price_in_ton=None):
    """
    Calculate the fees for claiming rewards in a TON airdrop.

    Args:
        claim_amount (float): The amount of rewards being claimed.
        fee_percentage (float): The fee percentage for claiming rewards.
        fee_denomination (str): The denomination for the fee, either 'TON' or 'token'. Default is 'TON'.
        token_price_in_ton (float): The price of the issued token in TON. Required if fee_denomination is 'token'.

    Returns:
        float: The calculated fee in TON if fee_denomination is 'TON', or in tokens if fee_denomination is 'token'.

    Raises:
        ValueError: If an invalid fee_denomination is provided or if required arguments are missing.
    """

    # Validate the fee_denomination
    if fee_denomination not in ['TON', 'token']:
        raise ValueError("Invalid fee_denomination. Must be 'TON' or 'token'.")
    
    # Calculate fee in TON
    if fee_denomination == 'TON':
        fee_in_ton = claim_amount * (fee_percentage / 100)
        return fee_in_ton
    
    # Calculate fee in tokens
    elif fee_denomination == 'token':
        if token_price_in_ton is None:
            raise ValueError("token_price_in_ton is required when fee_denomination is 'token'.")
        fee_in_ton = claim_amount * (fee_percentage / 100)
        fee_in_tokens = fee_in_ton / token_price_in_ton
        return fee_in_tokens


# Example Usage:
try:
    # Fee in TON
    ton_fee = calculate_reward_claim_fee(claim_amount=100, fee_percentage=2, fee_denomination='TON')
    print(f"Fee in TON: {ton_fee}")

    # Fee in Tokens
    token_fee = calculate_reward_claim_fee(claim_amount=100, fee_percentage=2, fee_denomination='token', token_price_in_ton=0.5)
    print(f"Fee in Tokens: {token_fee}")

except ValueError as e:
    print(f"Error: {e}")
```
