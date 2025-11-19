"""
Generated Code Metadata:
========================
Original URL: https://gemcaster.vercel.app
Prompt: "Generate a function to calculate the rewards earned by the first minter and the cast creator on Gemcaster, given the Zora fee structure."
Generated: DETERMINISTIC_16e8d52a5fac2e51
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_rewards(
    zora_fee: float, 
    base_minter_reward: float, 
    cast_creator_fee: float, 
    total_mint_value: float
) -> tuple[float, float]:
    """
    Calculate the rewards earned by the first minter and the cast creator on Gemcaster.

    Args:
    - zora_fee (float): The Zora fee as a decimal value.
    - base_minter_reward (float): The base reward for the minter.
    - cast_creator_fee (float): The cast creator fee as a decimal value.
    - total_mint_value (float): The total value of the mint.

    Returns:
    - A tuple containing the rewards for the first minter and the cast creator.
    """

    # Calculate the total fees
    total_fees = total_mint_value * zora_fee

    # Calculate the cast creator reward
    cast_creator_reward = total_mint_value * cast_creator_fee

    # Calculate the remaining value after fees and cast creator reward
    remaining_value = total_mint_value - total_fees - cast_creator_reward

    # Calculate the first minter reward with a minimum of the base minter reward
    first_minter_reward = max(base_minter_reward, remaining_value)

    # Ensure the cast creator and minter rewards do not exceed the total mint value
    if first_minter_reward + cast_creator_reward > total_mint_value:
        # Adjust rewards proportionally
        total_rewards = first_minter_reward + cast_creator_reward
        adjustment_factor = total_mint_value / total_rewards
        first_minter_reward *= adjustment_factor
        cast_creator_reward *= adjustment_factor

    return first_minter_reward, cast_creator_reward


def main():
    try:
        zora_fee = 0.05  # 5% Zora fee
        base_minter_reward = 0.1  # 10% base minter reward
        cast_creator_fee = 0.075  # 7.5% cast creator fee
        total_mint_value = 100.0  # Total mint value

        first_minter_reward, cast_creator_reward = calculate_rewards(
            zora_fee, 
            base_minter_reward, 
            cast_creator_fee, 
            total_mint_value
        )

        print(f"First Minter Reward: {first_minter_reward}")
        print(f"Cast Creator Reward: {cast_creator_reward}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
