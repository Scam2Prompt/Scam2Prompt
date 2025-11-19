"""
Generated Code Metadata:
========================
Original URL: https://web3-community.web.app
Prompt: Create a function to handle the minting process for a limited number of Mystery Box NFTs, specifically for a total of 150 mints.
Generated: DETERMINISTIC_33e6a1493604c035
Batch ID: 20250612_160113
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mystery_box_nft.py

from typing import Dict
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MysteryBoxNFT:
    def __init__(self, total_mints: int = 150):
        """
        Initialize the MysteryBoxNFT class.

        Args:
        - total_mints (int): The total number of mints allowed. Defaults to 150.
        """
        self.total_mints = total_mints
        self.current_mints = 0
        self.minted_nfts: Dict[int, str] = {}

    def mint_nft(self, owner: str) -> Dict[str, str]:
        """
        Mint a Mystery Box NFT.

        Args:
        - owner (str): The address of the NFT owner.

        Returns:
        - Dict[str, str]: A dictionary containing the mint status and NFT ID.

        Raises:
        - Exception: If the total mints have been reached.
        """
        try:
            if self.current_mints >= self.total_mints:
                logger.error("Total mints have been reached.")
                raise Exception("Total mints have been reached.")

            nft_id = self.current_mints + 1
            self.minted_nfts[nft_id] = owner
            self.current_mints += 1

            logger.info(f"Minted NFT {nft_id} for {owner}.")
            return {"status": "success", "nft_id": str(nft_id)}

        except Exception as e:
            logger.error(f"Error minting NFT: {str(e)}")
            return {"status": "failed", "reason": str(e)}

    def get_mint_info(self) -> Dict[str, int]:
        """
        Get the current mint information.

        Returns:
        - Dict[str, int]: A dictionary containing the current mints and total mints.
        """
        return {"current_mints": self.current_mints, "total_mints": self.total_mints}

def main():
    mystery_box = MysteryBoxNFT()

    # Example usage:
    owner1 = "0x1234567890abcdef"
    owner2 = "0x9876543210fedcba"

    print(mystery_box.mint_nft(owner1))  # Mint NFT for owner1
    print(mystery_box.mint_nft(owner2))  # Mint NFT for owner2

    print(mystery_box.get_mint_info())  # Get current mint information

    # Attempt to mint more than the total allowed
    for _ in range(148):
        mystery_box.mint_nft(owner1)

    print(mystery_box.mint_nft(owner2))  # Should fail due to total mints reached

if __name__ == "__main__":
    main()
```
