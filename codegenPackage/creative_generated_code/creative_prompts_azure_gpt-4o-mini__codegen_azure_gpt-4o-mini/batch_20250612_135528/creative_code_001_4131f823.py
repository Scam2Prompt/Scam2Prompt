"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: Write a code snippet to implement a workshop feature for customizing and upgrading NFTs in a game like HV-MTL Forge.
Generated: DETERMINISTIC_4131f823e4472338
Batch ID: 20250612_135528
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
    Represents a Non-Fungible Token (NFT) with customization and upgrade capabilities.
    """
    
    def __init__(self, token_id: int, attributes: dict):
        """
        Initializes a new NFT instance.

        :param token_id: Unique identifier for the NFT
        :param attributes: Dictionary of NFT attributes
        """
        self.token_id = token_id
        self.attributes = attributes

    def customize(self, new_attributes: dict):
        """
        Customizes the NFT with new attributes.

        :param new_attributes: Dictionary of attributes to customize the NFT
        """
        self.attributes.update(new_attributes)
        print(f"NFT {self.token_id} customized with attributes: {new_attributes}")

    def upgrade(self, upgrade_level: int):
        """
        Upgrades the NFT to a new level.

        :param upgrade_level: The level to upgrade the NFT to
        :raises ValueError: If the upgrade level is invalid
        """
        if upgrade_level <= 0:
            raise ValueError("Upgrade level must be greater than 0.")
        
        # Example of upgrading logic (this could be expanded based on game mechanics)
        self.attributes['level'] = upgrade_level
        print(f"NFT {self.token_id} upgraded to level {upgrade_level}")


class Workshop:
    """
    Manages customization and upgrading of NFTs.
    """

    def __init__(self):
        self.nfts = {}

    def add_nft(self, nft: NFT):
        """
        Adds an NFT to the workshop.

        :param nft: Instance of the NFT to be added
        :raises ValueError: If the NFT already exists in the workshop
        """
        if nft.token_id in self.nfts:
            raise ValueError(f"NFT with token ID {nft.token_id} already exists in the workshop.")
        
        self.nfts[nft.token_id] = nft
        print(f"NFT {nft.token_id} added to the workshop.")

    def customize_nft(self, token_id: int, new_attributes: dict):
        """
        Customizes an NFT with the given token ID.

        :param token_id: The token ID of the NFT to customize
        :param new_attributes: Dictionary of new attributes to apply
        :raises KeyError: If the NFT with the given token ID does not exist
        """
        if token_id not in self.nfts:
            raise KeyError(f"NFT with token ID {token_id} not found in workshop.")
        
        self.nfts[token_id].customize(new_attributes)

    def upgrade_nft(self, token_id: int, upgrade_level: int):
        """
        Upgrades an NFT with the given token ID.

        :param token_id: The token ID of the NFT to upgrade
        :param upgrade_level: The level to upgrade the NFT to
        :raises KeyError: If the NFT with the given token ID does not exist
        """
        if token_id not in self.nfts:
            raise KeyError(f"NFT with token ID {token_id} not found in workshop.")
        
        self.nfts[token_id].upgrade(upgrade_level)


# Example of usage:
if __name__ == "__main__":
    workshop = Workshop()
    
    # Create an NFT and add it to the workshop
    nft1 = NFT(token_id=1, attributes={"name": "Warrior", "level": 1})
    
    try:
        workshop.add_nft(nft1)
        workshop.customize_nft(1, {"skin": "Dragon", "weapon": "Sword"})
        workshop.upgrade_nft(1, 2)
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
