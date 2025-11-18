"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-pro.nfts2.me
Prompt: Implement a function to calculate referral fees for NFT mints completed via a referral link on the ZKsync Era chain, using the reward structure described on NFTs2Me.com.
Generated: DETERMINISTIC_58ea1e1016db2b43
Batch ID: 20250612_154029
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Module: nft_referral_fee_calculator.py

Description:
This module calculates referral fees for NFT mints completed via a referral link
on the ZKsync Era chain, following the reward structure defined on NFTs2Me.com.

Author:
Your Name

Date:
YYYY-MM-DD
"""

def calculate_referral_fee(mint_price: float, reward_percentage: float) -> float:
    """
    Calculate the referral fee for an NFT mint based on the mint price
    and reward percentage provided.

    Parameters:
        mint_price (float): The price of the NFT mint in USD (or equivalent token).
        reward_percentage (float): The percentage of the mint price awarded as a referral fee.
                                   Example: 5.0 for 5%.

    Returns:
        float: The referral fee calculated based on the given parameters.

    Raises:
        ValueError: If mint_price or reward_percentage is negative.
        ValueError: If reward_percentage is greater than 100.
    """
    # Input validation
    if mint_price < 0:
        raise ValueError("Mint price must be non-negative.")
    if reward_percentage < 0 or reward_percentage > 100:
        raise ValueError("Reward percentage must be between 0 and 100.")

    # Calculate referral fee
    referral_fee = mint_price * (reward_percentage / 100)

    return referral_fee


if __name__ == '__main__':
    # Example usage
    try:
        mint_price = float(input("Enter NFT mint price (USD): "))
        reward_percentage = float(input("Enter referral reward percentage: "))

        fee = calculate_referral_fee(mint_price, reward_percentage)
        print(f"The referral fee is: ${fee:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")
```
