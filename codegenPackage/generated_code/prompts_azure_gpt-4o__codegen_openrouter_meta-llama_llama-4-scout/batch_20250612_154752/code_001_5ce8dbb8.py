"""
Generated Code Metadata:
========================
Original URL: https://fairmints.fun
Prompt: Generate code to calculate the holder distribution percentages for the $FAIR token using wallet addresses and balances provided by the FairMint Mint Market.
Generated: DETERMINISTIC_5ce8dbb8dc39a43a
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List
from collections import defaultdict

def calculate_holder_distribution(
    wallet_balances: List[Dict[str, str]], 
    total_supply: float
) -> Dict[str, float]:
    """
    Calculate the holder distribution percentages for the $FAIR token.

    Args:
    - wallet_balances (List[Dict[str, str]]): A list of dictionaries containing wallet addresses and their corresponding $FAIR token balances.
    - total_supply (float): The total supply of $FAIR tokens.

    Returns:
    - A dictionary where keys are wallet addresses and values are their corresponding $FAIR token distribution percentages.
    """

    # Initialize a dictionary to store the distribution percentages
    distribution_percentages = {}

    # Check if total supply is zero to avoid division by zero error
    if total_supply == 0:
        raise ValueError("Total supply cannot be zero")

    # Iterate over each wallet balance
    for wallet_balance in wallet_balances:
        # Extract wallet address and balance
        wallet_address = wallet_balance['wallet_address']
        balance = float(wallet_balance['balance'])

        # Calculate distribution percentage
        distribution_percentage = (balance / total_supply) * 100

        # Store distribution percentage in the dictionary
        distribution_percentages[wallet_address] = distribution_percentage

    return distribution_percentages


def get_top_holders(
    distribution_percentages: Dict[str, float], 
    num_top_holders: int
) -> List[Dict[str, float]]:
    """
    Get the top holders by their $FAIR token distribution percentages.

    Args:
    - distribution_percentages (Dict[str, float]): A dictionary where keys are wallet addresses and values are their corresponding $FAIR token distribution percentages.
    - num_top_holders (int): The number of top holders to retrieve.

    Returns:
    - A list of dictionaries containing the wallet addresses and distribution percentages of the top holders.
    """

    # Sort distribution percentages in descending order
    sorted_distribution_percentages = sorted(
        distribution_percentages.items(), 
        key=lambda x: x[1], 
        reverse=True
    )

    # Get the top holders
    top_holders = []
    for wallet_address, distribution_percentage in sorted_distribution_percentages[:num_top_holders]:
        top_holders.append({
            'wallet_address': wallet_address,
            'distribution_percentage': distribution_percentage
        })

    return top_holders


def main():
    try:
        # Example usage
        wallet_balances = [
            {'wallet_address': '0x123', 'balance': '1000'},
            {'wallet_address': '0x456', 'balance': '2000'},
            {'wallet_address': '0x789', 'balance': '3000'}
        ]
        total_supply = 6000

        distribution_percentages = calculate_holder_distribution(wallet_balances, total_supply)
        print("Holder Distribution Percentages:")
        for wallet_address, distribution_percentage in distribution_percentages.items():
            print(f"{wallet_address}: {distribution_percentage}%")

        num_top_holders = 2
        top_holders = get_top_holders(distribution_percentages, num_top_holders)
        print(f"\nTop {num_top_holders} Holders:")
        for top_holder in top_holders:
            print(f"{top_holder['wallet_address']}: {top_holder['distribution_percentage']}%")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
