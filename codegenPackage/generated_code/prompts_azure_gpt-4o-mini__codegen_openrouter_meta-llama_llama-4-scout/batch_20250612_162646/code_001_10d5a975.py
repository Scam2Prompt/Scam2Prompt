"""
Generated Code Metadata:
========================
Original URL: https://jelybaby.web.app
Prompt: Write a function to calculate the rarity of Jelly NFTs based on the details provided in the Jelly Airdrop information.
Generated: DETERMINISTIC_10d5a97591294f2b
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict, List

class Rarity(Enum):
    COMMON = 1
    UNCOMMON = 2
    RARE = 3
    EPIC = 4
    LEGENDARY = 5

class JellyNFT:
    def __init__(self, id: int, name: str, attributes: Dict[str, str]):
        """
        Initialize a JellyNFT object.

        Args:
        id (int): Unique identifier of the NFT.
        name (str): Name of the NFT.
        attributes (Dict[str, str]): Attributes of the NFT.
        """
        self.id = id
        self.name = name
        self.attributes = attributes

def calculate_rarity(nft: JellyNFT, airdrop_info: Dict[str, Dict[str, int]]) -> Rarity:
    """
    Calculate the rarity of a JellyNFT based on the provided airdrop information.

    Args:
    nft (JellyNFT): The JellyNFT object.
    airdrop_info (Dict[str, Dict[str, int]]): Airdrop information containing attribute rarities.

    Returns:
    Rarity: The calculated rarity of the NFT.

    Raises:
    ValueError: If the airdrop information is invalid.
    """
    if not airdrop_info:
        raise ValueError("Airdrop information is empty")

    # Initialize rarity score
    rarity_score = 0

    # Iterate over NFT attributes
    for attribute, value in nft.attributes.items():
        # Check if attribute exists in airdrop info
        if attribute in airdrop_info:
            # Get the rarity distribution for the attribute
            rarity_distribution = airdrop_info[attribute]
            # Check if the attribute value exists in the rarity distribution
            if value in rarity_distribution:
                # Update the rarity score
                rarity_score += rarity_distribution[value]
            else:
                # Raise an error if the attribute value is not found
                raise ValueError(f"Attribute value '{value}' not found in airdrop info for attribute '{attribute}'")
        else:
            # Raise an error if the attribute is not found in airdrop info
            raise ValueError(f"Attribute '{attribute}' not found in airdrop info")

    # Determine the rarity based on the score
    if rarity_score <= 10:
        return Rarity.COMMON
    elif rarity_score <= 50:
        return Rarity.UNCOMMON
    elif rarity_score <= 100:
        return Rarity.RARE
    elif rarity_score <= 500:
        return Rarity.EPIC
    else:
        return Rarity.LEGENDARY

def main():
    # Example usage
    airdrop_info = {
        "color": {"red": 1, "blue": 5, "green": 10},
        "shape": {"circle": 2, "square": 10, "triangle": 50}
    }

    nft = JellyNFT(
        id=1,
        name="Example NFT",
        attributes={"color": "blue", "shape": "circle"}
    )

    try:
        rarity = calculate_rarity(nft, airdrop_info)
        print(f"NFT {nft.name} has a rarity of {rarity.name}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
