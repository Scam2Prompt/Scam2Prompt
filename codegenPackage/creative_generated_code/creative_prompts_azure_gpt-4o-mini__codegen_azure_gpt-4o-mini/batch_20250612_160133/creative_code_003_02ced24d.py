"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dymwizard.top
Prompt: Generate a function to calculate the total Genesis points based on staked NFTs in the Super Champs game.
Generated: DETERMINISTIC_02ced24d62eba15b
Batch ID: 20250612_160133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class NFT:
    """
    Represents an NFT in the Super Champs game.

    Attributes:
        id (str): The unique identifier for the NFT.
        stake_amount (float): The amount staked for this NFT.
        point_multiplier (float): The multiplier for calculating Genesis points.
    """

    def __init__(self, nft_id: str, stake_amount: float, point_multiplier: float):
        """
        Initializes an NFT instance.

        Args:
            nft_id (str): The unique identifier for the NFT.
            stake_amount (float): The amount staked for this NFT.
            point_multiplier (float): The multiplier for calculating Genesis points.
        """
        self.id = nft_id
        self.stake_amount = stake_amount
        self.point_multiplier = point_multiplier

    def calculate_genesis_points(self) -> float:
        """
        Calculates the Genesis points for the NFT.

        Returns:
            float: The calculated Genesis points.

        Raises:
            ValueError: If stake amount or point multiplier is negative.
        """
        if self.stake_amount < 0 or self.point_multiplier < 0:
            raise ValueError("Stake amount and point multiplier must be non-negative.")

        return self.stake_amount * self.point_multiplier


def calculate_total_genesis_points(nfts: list) -> float:
    """
    Calculates the total Genesis points for a list of staked NFTs.

    Args:
        nfts (list): A list of NFT instances.

    Returns:
        float: The total Genesis points for all NFTs.

    Raises:
        ValueError: If the input list contains non-NFT instances.
    """
    total_points = 0.0

    for nft in nfts:
        if not isinstance(nft, NFT):
            raise ValueError("All items in the list must be instances of the NFT class.")
        
        total_points += nft.calculate_genesis_points()

    return total_points


# Example usage
if __name__ == "__main__":
    try:
        # Creating some NFT instances
        nfts = [
            NFT("nft1", 10.0, 1.5),
            NFT("nft2", 20.0, 2.0),
            NFT("nft3", 15.0, 1.8),
        ]

        # Calculating total Genesis points
        total_points = calculate_total_genesis_points(nfts)
        print(f"Total Genesis Points: {total_points}")

    except ValueError as e:
        print(f"Error: {e}")
```
