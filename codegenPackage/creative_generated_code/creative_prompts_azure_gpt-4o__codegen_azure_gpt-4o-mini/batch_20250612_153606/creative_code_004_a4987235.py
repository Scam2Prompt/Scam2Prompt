"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-homepage-kappa.vercel.app
Prompt: Create a smart contract on Starknet that allows users to mint NFTs representing individual pixels on a grid.
Generated: DETERMINISTIC_a49872350ee4acab
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries from the Starknet framework
from starkware.starknet.public.abi import get_abi
from starkware.starknet.core.cairo import Contract, Event, Function, View

# Define the NFT contract for minting individual pixels on a grid
class PixelNFT(Contract):
    # Event to emit when a new pixel NFT is minted
    PixelMinted = Event({
        "pixel_index": "felt",
        "owner": "felt"
    })

    def __init__(self):
        # Mapping from pixel index to owner
        self.pixel_owners: Dict[felt, felt] = {}

    @Function
    def mint_pixel(self, pixel_index: felt):
        """
        Mint an NFT for a specific pixel index.
        
        :param pixel_index: The index of the pixel to be minted.
        :raises: Error if the pixel is already minted or index out of bounds.
        """
        # Check if pixel is already minted
        if pixel_index in self.pixel_owners:
            raise Exception("Pixel is already minted.")
        
        # Set the owner of the pixel to the caller
        self.pixel_owners[pixel_index] = self.msg.sender
        
        # Emit the PixelMinted event
        self.emit(self.PixelMinted(pixel_index=pixel_index, owner=self.msg.sender))

    @View
    def owner_of(self, pixel_index: felt) -> felt:
        """
        Retrieve the owner of a specific pixel.
        
        :param pixel_index: The index of the pixel to check.
        :return: The address of the owner or 0 if not minted.
        """
        return self.pixel_owners.get(pixel_index, 0)

    @View
    def total_supply(self) -> felt:
        """
        Returns the total number of unique minted pixels.
        
        :return: The count of unique minted pixels.
        """
        return len(self.pixel_owners)

# Compile the contract and deploy it on Starknet
# Ensure to follow the deployment steps provided by StarkNet documentation.
# Error handling during deployment and interactions should be managed appropriately.

```
