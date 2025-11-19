"""
Generated Code Metadata:
========================
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: "Explain the concept of dynamic NFTs and how HV-MTL utilizes this concept, including the role of the rift in their evolution."
Generated: DETERMINISTIC_2fd26a78909e4bb9
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DynamicNFT:
    """
    A class to represent a Dynamic Non-Fungible Token (NFT).
    
    Attributes:
        token_id (str): Unique identifier for the NFT.
        metadata (dict): Metadata associated with the NFT.
        evolution_stage (int): Current evolution stage of the NFT.
    """

    def __init__(self, token_id: str, metadata: dict):
        """
        Initializes a DynamicNFT instance.

        Args:
            token_id (str): Unique identifier for the NFT.
            metadata (dict): Initial metadata for the NFT.
        """
        self.token_id = token_id
        self.metadata = metadata
        self.evolution_stage = 0

    def evolve(self):
        """
        Evolves the NFT to the next stage, updating its metadata.
        Raises an exception if the evolution limit is reached.
        """
        if self.evolution_stage >= 5:  # Assuming a max of 5 evolution stages
            raise ValueError("Maximum evolution stage reached.")
        
        self.evolution_stage += 1
        self.update_metadata()

    def update_metadata(self):
        """
        Updates the metadata based on the current evolution stage.
        """
        # Example metadata update logic
        self.metadata['stage'] = self.evolution_stage
        self.metadata['description'] = f"Evolved to stage {self.evolution_stage}"

    def get_metadata(self) -> dict:
        """
        Returns the current metadata of the NFT.

        Returns:
            dict: Current metadata of the NFT.
        """
        return self.metadata


class Rift:
    """
    A class to represent the Rift, which facilitates the evolution of Dynamic NFTs.
    
    Attributes:
        rift_id (str): Unique identifier for the Rift.
        active_nfts (list): List of DynamicNFTs currently affected by the Rift.
    """

    def __init__(self, rift_id: str):
        """
        Initializes a Rift instance.

        Args:
            rift_id (str): Unique identifier for the Rift.
        """
        self.rift_id = rift_id
        self.active_nfts = []

    def activate_rift(self, nft: DynamicNFT):
        """
        Activates the Rift for a given NFT, allowing it to evolve.

        Args:
            nft (DynamicNFT): The NFT to be affected by the Rift.
        """
        if nft not in self.active_nfts:
            self.active_nfts.append(nft)

    def evolve_nfts(self):
        """
        Evolves all NFTs currently affected by the Rift.
        """
        for nft in self.active_nfts:
            try:
                nft.evolve()
            except ValueError as e:
                print(f"Error evolving NFT {nft.token_id}: {e}")

    def get_active_nfts(self) -> list:
        """
        Returns a list of active NFTs affected by the Rift.

        Returns:
            list: List of active DynamicNFTs.
        """
        return self.active_nfts


# Example usage
if __name__ == "__main__":
    # Create a Dynamic NFT
    nft1 = DynamicNFT(token_id="NFT001", metadata={"name": "Dynamic Art", "description": "Initial Stage"})
    
    # Create a Rift
    rift = Rift(rift_id="RIFT001")
    
    # Activate the Rift for the NFT
    rift.activate_rift(nft1)
    
    # Evolve NFTs affected by the Rift
    rift.evolve_nfts()
    
    # Print the updated metadata of the NFT
    print(nft1.get_metadata())
```
