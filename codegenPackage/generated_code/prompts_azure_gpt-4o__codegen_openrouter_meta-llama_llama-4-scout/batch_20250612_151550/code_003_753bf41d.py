"""
Generated Code Metadata:
========================
Original URL: https://hv-mtl-backup-website.pages.dev
Prompt: Create a function to categorize HV-MTL NFTs by their types (e.g., "glitch," "knight," "reaver") and output their unique traits.
Generated: DETERMINISTIC_753bf41dbb42f661
Batch ID: 20250612_151550
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List

class NFT:
    """Represents an HV-MTL NFT with its type and traits."""

    def __init__(self, nft_type: str, traits: List[str]):
        """
        Initializes an NFT object.

        Args:
        - nft_type (str): The type of the NFT (e.g., "glitch," "knight," "reaver").
        - traits (List[str]): A list of unique traits of the NFT.
        """
        self.nft_type = nft_type
        self.traits = traits

def categorize_nfts(nfts: List[NFT]) -> Dict[str, List[str]]:
    """
    Categorizes HV-MTL NFTs by their types and outputs their unique traits.

    Args:
    - nfts (List[NFT]): A list of NFT objects.

    Returns:
    - Dict[str, List[str]]: A dictionary where keys are NFT types and values are lists of unique traits.

    Raises:
    - ValueError: If the input list is empty or None.
    """
    if not nfts:
        raise ValueError("Input list cannot be empty or None")

    categorized_nfts = {}

    for nft in nfts:
        if nft.nft_type not in categorized_nfts:
            categorized_nfts[nft.nft_type] = []

        # Add unique traits to the list
        categorized_nfts[nft.nft_type] = list(set(categorized_nfts[nft.nft_type] + nft.traits))

    return categorized_nfts

def main():
    # Example usage
    nft1 = NFT("glitch", ["trait1", "trait2", "trait3"])
    nft2 = NFT("knight", ["trait4", "trait5", "trait2"])
    nft3 = NFT("reaver", ["trait6", "trait7", "trait3"])
    nft4 = NFT("glitch", ["trait1", "trait8", "trait9"])

    nfts = [nft1, nft2, nft3, nft4]

    try:
        categorized_nfts = categorize_nfts(nfts)
        for nft_type, traits in categorized_nfts.items():
            print(f"NFT Type: {nft_type}")
            print(f"Unique Traits: {traits}")
            print("------------------------")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
