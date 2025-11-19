"""
Generated Code Metadata:
========================
Original URL: https://asdasdwer23wrt23r23r23.pages.dev
Prompt: Develop a function to calculate the total ETH spent on buying GRAPE NFTs and determine the bonus allocation.
Generated: DETERMINISTIC_4399043a36ad0494
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class NFT:
    def __init__(self, name: str, price: float, bonus: float):
        """
        Initialize an NFT object.

        Args:
        - name (str): The name of the NFT.
        - price (float): The price of the NFT in ETH.
        - bonus (float): The bonus allocation for the NFT.
        """
        self.name = name
        self.price = price
        self.bonus = bonus

def calculate_total_eth_spent(nfts_bought: List[NFT]) -> float:
    """
    Calculate the total ETH spent on buying NFTs.

    Args:
    - nfts_bought (List[NFT]): A list of NFT objects bought.

    Returns:
    - float: The total ETH spent.
    """
    total_eth_spent = sum(nft.price for nft in nfts_bought)
    return total_eth_spent

def calculate_bonus_allocation(nfts_bought: List[NFT]) -> Dict[str, float]:
    """
    Calculate the bonus allocation for each NFT bought.

    Args:
    - nfts_bought (List[NFT]): A list of NFT objects bought.

    Returns:
    - Dict[str, float]: A dictionary with NFT names as keys and bonus allocations as values.
    """
    bonus_allocation = {nft.name: nft.bonus for nft in nfts_bought}
    return bonus_allocation

def main():
    try:
        # Example usage
        grape_nft1 = NFT("GRAPE-1", 1.5, 0.1)
        grape_nft2 = NFT("GRAPE-2", 2.0, 0.2)

        nfts_bought = [grape_nft1, grape_nft2]

        total_eth_spent = calculate_total_eth_spent(nfts_bought)
        bonus_allocation = calculate_bonus_allocation(nfts_bought)

        print(f"Total ETH spent: {total_eth_spent} ETH")
        print("Bonus Allocation:")
        for nft, bonus in bonus_allocation.items():
            print(f"- {nft}: {bonus} ETH")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
