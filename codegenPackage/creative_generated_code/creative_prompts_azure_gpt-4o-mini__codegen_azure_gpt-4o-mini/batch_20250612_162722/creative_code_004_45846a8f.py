"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pinguonbase-claims.pages.dev
Prompt: Create a function for the Ice Chest Airdrops mechanism that distributes mystery boxes to Pingu token holders, including Pingu tokens and NFTs, as outlined in the Pingu on Base roadmap.
Generated: DETERMINISTIC_45846a8f022fc550
Batch ID: 20250612_162722
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict, Any

class PinguAirdrop:
    def __init__(self):
        # Initialize the list to hold Pingu token holders
        self.token_holders: List[Dict[str, Any]] = []

    def add_token_holder(self, wallet_address: str, pingu_tokens: int, nfts: List[str]):
        """
        Add a new Pingu token holder to the list.

        :param wallet_address: The unique wallet address of the token holder.
        :param pingu_tokens: The number of Pingu tokens the holder possesses.
        :param nfts: A list of NFTs owned by the holder.
        """
        self.token_holders.append({
            'wallet_address': wallet_address,
            'pingu_tokens': pingu_tokens,
            'nfts': nfts
        })

    def distribute_mystery_boxes(self, total_boxes: int) -> Dict[str, int]:
        """
        Distributes mystery boxes to Pingu token holders based on their holdings.

        :param total_boxes: The total number of mystery boxes to distribute.
        :return: A dictionary mapping wallet addresses to the number of mystery boxes received.
        """
        if total_boxes <= 0:
            raise ValueError("Total boxes must be greater than zero.")

        if not self.token_holders:
            raise ValueError("No token holders available for distribution.")

        # Calculate the total weight based on the number of Pingu tokens
        total_weight = sum(holder['pingu_tokens'] for holder in self.token_holders)

        if total_weight == 0:
            raise ValueError("Total weight is zero. Cannot distribute mystery boxes.")

        # Dictionary to hold the distribution results
        distribution: Dict[str, int] = {holder['wallet_address']: 0 for holder in self.token_holders}

        for _ in range(total_boxes):
            # Select a random holder based on their weight
            selected_holder = self._weighted_random_selection(total_weight)
            distribution[selected_holder] += 1

        return distribution

    def _weighted_random_selection(self, total_weight: int) -> str:
        """
        Select a wallet address based on the weighted distribution of Pingu tokens.

        :param total_weight: The total weight to use for random selection.
        :return: The wallet address of the selected token holder.
        """
        # Generate a random value between 0 and total_weight
        random_value = random.randint(0, total_weight - 1)
        current_weight = 0

        # Iterate through the token holders to find the selected holder
        for holder in self.token_holders:
            current_weight += holder['pingu_tokens']
            if current_weight > random_value:
                return holder['wallet_address']

        raise RuntimeError("Weighted random selection failed.")

# Example usage:
if __name__ == "__main__":
    airdrop = PinguAirdrop()
    airdrop.add_token_holder("wallet1", 10, ["nft1", "nft2"])
    airdrop.add_token_holder("wallet2", 20, ["nft3"])
    airdrop.add_token_holder("wallet3", 0, [])

    try:
        distribution = airdrop.distribute_mystery_boxes(5)
        print("Mystery Box Distribution:", distribution)
    except Exception as e:
        print(f"Error: {e}")
```
