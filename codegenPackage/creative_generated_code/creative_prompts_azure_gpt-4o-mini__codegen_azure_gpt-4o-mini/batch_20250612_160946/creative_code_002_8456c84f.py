"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appmemekombatclaim.pages.dev
Prompt: Write a function to calculate potential rewards based on the APY of 112% for staked $MK tokens in Meme Kombat.
Generated: DETERMINISTIC_8456c84f21f59cae
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_rewards(staked_amount: float, apy: float, years: float) -> float:
    """
    Calculate potential rewards for staked tokens based on the annual percentage yield (APY).

    Parameters:
    staked_amount (float): The amount of tokens staked.
    apy (float): The annual percentage yield as a decimal (e.g., 112% APY = 1.12).
    years (float): The number of years the tokens are staked for.

    Returns:
    float: The total rewards earned after the specified number of years.

    Raises:
    ValueError: If staked_amount, apy, or years are negative.
    """

    # Validate input values
    if staked_amount < 0:
        raise ValueError("Staked amount must be non-negative.")
    if apy < 0:
        raise ValueError("APY must be non-negative.")
    if years < 0:
        raise ValueError("Years must be non-negative.")

    # Calculate the total rewards using the formula for compound interest
    total_rewards = staked_amount * ((1 + apy) ** years - 1)

    return total_rewards

# Example usage
if __name__ == "__main__":
    try:
        staked_amount = 1000.0  # Example staked amount in $MK tokens
        apy = 1.12  # 112% APY
        years = 3  # Example duration in years

        rewards = calculate_rewards(staked_amount, apy, years)
        print(f"Potential rewards after {years} years: ${rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
