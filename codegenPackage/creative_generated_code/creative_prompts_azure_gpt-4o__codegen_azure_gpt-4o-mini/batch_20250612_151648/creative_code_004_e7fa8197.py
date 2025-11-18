"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinminetrix-en.web.app
Prompt: Write a Python function that calculates the total BTC mining power earned by burning mining credits, based on the tokenomics and staking rules outlined by Bitcoin Minetrix.
Generated: DETERMINISTIC_e7fa819776a0d5ae
Batch ID: 20250612_151648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MiningCreditsError(Exception):
    """Custom exception for errors related to mining credits."""
    pass


def calculate_btc_mining_power(credits_burned: float, staking_factor: float) -> float:
    """
    Calculate the total Bitcoin (BTC) mining power earned by burning mining credits.

    Parameters:
    - credits_burned (float): The amount of mining credits burned.
    - staking_factor (float): A multiplier that determines the effectiveness of the burned credits.

    Returns:
    - float: The total BTC mining power earned.

    Raises:
    - MiningCreditsError: If credits_burned or staking_factor is invalid (negative or zero).
    """
    
    # Validate inputs
    if credits_burned <= 0:
        raise MiningCreditsError("Credits burned must be greater than zero.")
    
    if staking_factor <= 0:
        raise MiningCreditsError("Staking factor must be greater than zero.")
    
    # Calculate BTC mining power based on the credits burned and staking factor
    mining_power = credits_burned * staking_factor
    
    return mining_power


# Example usage
if __name__ == "__main__":
    try:
        credits = 100.0  # Example amount of credits burned
        staking = 2.5    # Example staking factor

        # Calculate BTC mining power
        total_power = calculate_btc_mining_power(credits, staking)
        print(f"Total BTC Mining Power Earned: {total_power} BTC")
        
    except MiningCreditsError as e:
        print(f"Error calculating BTC mining power: {e}")
```
