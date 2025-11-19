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
# Import necessary modules
from typing import Tuple

def calculate_rewards(sale_price: float, zora_fee_percentage: float, first_minter_percentage: float, cast_creator_percentage: float) -> Tuple[float, float]:
    """
    Calculate the rewards earned by the first minter and the cast creator based on the Zora fee structure.

    Parameters:
        sale_price (float): The total sale price of the NFT.
        zora_fee_percentage (float): The percentage of the sale price taken as Zora's fee.
        first_minter_percentage (float): The percentage of Zora's fee allocated to the first minter.
        cast_creator_percentage (float): The percentage of Zora's fee allocated to the cast creator.

    Returns:
        Tuple[float, float]: A tuple containing the rewards for the first minter and the cast creator.
    """
    try:
        # Validate inputs
        if sale_price < 0:
            raise ValueError("Sale price must be non-negative.")
        if not (0 <= zora_fee_percentage <= 100):
            raise ValueError("Zora fee percentage must be between 0 and 100.")
        if not (0 <= first_minter_percentage <= 100):
            raise ValueError("First minter percentage must be between 0 and 100.")
        if not (0 <= cast_creator_percentage <= 100):
            raise ValueError("Cast creator percentage must be between 0 and 100.")
        if first_minter_percentage + cast_creator_percentage > 100:
            raise ValueError("The sum of first minter and cast creator percentages cannot exceed 100.")

        # Calculate Zora's fee
        zora_fee = (zora_fee_percentage / 100) * sale_price

        # Calculate rewards
        first_minter_reward = (first_minter_percentage / 100) * zora_fee
        cast_creator_reward = (cast_creator_percentage / 100) * zora_fee

        return first_minter_reward, cast_creator_reward

    except Exception as e:
        # Handle errors gracefully
        raise ValueError(f"Error calculating rewards: {e}")

# Example usage:
# sale_price = 1000.0
# zora_fee_percentage = 5.0
# first_minter_percentage = 70.0
# cast_creator_percentage = 30.0
# rewards = calculate_rewards(sale_price, zora_fee_percentage, first_minter_percentage, cast_creator_percentage)
# print(f"First Minter Reward: ${rewards[0]:.2f}, Cast Creator Reward: ${rewards[1]:.2f}")
```
