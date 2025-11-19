"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-in.pages.dev
Prompt: Explain how to calculate the annual percentage yield (APY) for staking $WAI tokens based on the provided tokenomics.
Generated: DETERMINISTIC_f38c6eb0c4cdd3d8
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_apy(total_staked_tokens: float, total_circulating_supply: float, 
                   staking_reward: float, compounding_frequency: int, 
                   time_period_in_years: int = 1) -> float:
    """
    Calculate the annual percentage yield (APY) for staking $WAI tokens.

    Args:
    - total_staked_tokens (float): The total number of tokens staked.
    - total_circulating_supply (float): The total circulating supply of tokens.
    - staking_reward (float): The total staking reward.
    - compounding_frequency (int): The frequency of compounding per year.
    - time_period_in_years (int, optional): The time period in years. Defaults to 1.

    Returns:
    - float: The annual percentage yield (APY).
    """

    # Check for division by zero errors
    if total_circulating_supply == 0:
        raise ValueError("Total circulating supply cannot be zero.")

    # Calculate the staking ratio
    staking_ratio = total_staked_tokens / total_circulating_supply

    # Check if staking ratio is within valid range (0, 1]
    if staking_ratio < 0 or staking_ratio > 1:
        raise ValueError("Staking ratio must be between 0 and 1.")

    # Calculate the reward per staked token
    reward_per_staked_token = staking_reward / total_staked_tokens

    # Calculate the APY using the formula: APY = (1 + (r/n))^(n) - 1
    apy = (1 + (reward_per_staked_token * compounding_frequency)) ** compounding_frequency - 1

    # Annualize the APY
    apy = (1 + apy) ** time_period_in_years - 1

    # Convert APY to percentage
    apy_percentage = apy * 100

    return apy_percentage


def main():
    try:
        # Example usage
        total_staked_tokens = 1000000.0
        total_circulating_supply = 10000000.0
        staking_reward = 200000.0
        compounding_frequency = 12  # Monthly compounding

        apy = calculate_apy(total_staked_tokens, total_circulating_supply, 
                             staking_reward, compounding_frequency)

        print(f"The annual percentage yield (APY) is: {apy:.2f}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
