"""
Generated Code Metadata:
========================
Original URL: https://owlto-finance.top
Prompt: Generate a function to calculate the Genesis NFT holder multiplier for the Super Champs staking system.
Generated: DETERMINISTIC_3824df8ed053c1f8
Batch ID: 20250612_160241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_genesis_nft_holder_multiplier(
    genesis_nft_holders: Dict[str, int], 
    user_address: str, 
    total_genesis_nft_supply: int
) -> float:
    """
    Calculate the Genesis NFT holder multiplier for the Super Champs staking system.

    Args:
    - genesis_nft_holders (Dict[str, int]): A dictionary mapping user addresses to their Genesis NFT holdings.
    - user_address (str): The address of the user for whom to calculate the multiplier.
    - total_genesis_nft_supply (int): The total supply of Genesis NFTs.

    Returns:
    - float: The Genesis NFT holder multiplier for the specified user.

    Raises:
    - ValueError: If the total Genesis NFT supply is zero.
    """

    # Check for division by zero
    if total_genesis_nft_supply == 0:
        raise ValueError("Total Genesis NFT supply cannot be zero")

    # Get the user's Genesis NFT holdings
    try:
        user_holdings = genesis_nft_holders[user_address]
    except KeyError:
        # If the user has no Genesis NFTs, their multiplier is 1.0
        return 1.0

    # Calculate the multiplier based on the user's holdings and the total supply
    # For this example, let's assume the multiplier is the user's holdings divided by the total supply, 
    # with a minimum multiplier of 1.0 and a maximum multiplier of 5.0
    multiplier = min(
        max(
            1.0, 
            (user_holdings / total_genesis_nft_supply) * 5.0
        ), 
        5.0
    )

    return multiplier


# Example usage
if __name__ == "__main__":
    genesis_nft_holders = {
        "0xUser1": 5,
        "0xUser2": 10,
        "0xUser3": 1
    }

    total_genesis_nft_supply = 100

    user_addresses = ["0xUser1", "0xUser2", "0xUser3", "0xUser4"]

    for user_address in user_addresses:
        try:
            multiplier = calculate_genesis_nft_holder_multiplier(
                genesis_nft_holders, 
                user_address, 
                total_genesis_nft_supply
            )
            print(f"Multiplier for {user_address}: {multiplier}")
        except Exception as e:
            print(f"Error calculating multiplier for {user_address}: {str(e)}")
```
