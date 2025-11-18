"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://west-of-the-sun-nft-airdrop.pages.dev
Prompt: Create a function to track and update the number of NFT claimers in an airdrop system, referencing the "West of the Sun" NFT airdrop example with 6 claimers and 14 NFTs available.
Generated: DETERMINISTIC_ede10324b9de9593
Batch ID: 20250612_151333
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Dict

class NFTAirdrop:
    """
    A class to manage an NFT airdrop system.
    Attributes:
        total_nfts (int): Total NFTs available for the airdrop.
        claimers (Dict[str, int]): A dictionary to track claimers and their claimed NFTs count.
    """

    def __init__(self, total_nfts: int):
        """
        Initialize the NFTAirdrop instance.
        Args:
            total_nfts (int): Total number of NFTs available in the airdrop.
        """
        self.total_nfts = total_nfts
        self.claimers = {}  # Dictionary to store claimers and their claimed counts.

    def claim_nft(self, claimer_name: str) -> str:
        """
        Function to allow a user to claim an NFT.
        Args:
            claimer_name (str): The name of the claimer.
        Returns:
            str: A message indicating the status of the claim.
        """
        # Check if NFTs are still available
        if self.total_nfts <= 0:
            return "All NFTs have been claimed. No more NFTs are available."

        # Update claimer information
        if claimer_name in self.claimers:
            self.claimers[claimer_name] += 1
        else:
            self.claimers[claimer_name] = 1

        # Decrease the total number of NFTs
        self.total_nfts -= 1

        return f"NFT claimed successfully by {claimer_name}. NFTs remaining: {self.total_nfts}"

    def get_claimers(self) -> Dict[str, int]:
        """
        Function to retrieve the list of claimers and the number of NFTs they have claimed.
        Returns:
            Dict[str, int]: A dictionary of claimers and their claimed NFT counts.
        """
        return self.claimers

    def get_nfts_remaining(self) -> int:
        """
        Function to retrieve the number of NFTs still available.
        Returns:
            int: The number of NFTs remaining.
        """
        return self.total_nfts


# Example Usage
if __name__ == "__main__":
    # Initialize the airdrop system with 14 NFTs
    airdrop = NFTAirdrop(total_nfts=14)

    # Simulate 6 claimers claiming NFTs
    print(airdrop.claim_nft("Alice"))
    print(airdrop.claim_nft("Bob"))
    print(airdrop.claim_nft("Charlie"))
    print(airdrop.claim_nft("Alice"))  # Alice claims another NFT
    print(airdrop.claim_nft("Eve"))
    print(airdrop.claim_nft("Mallory"))

    # Display the status of claimers and remaining NFTs
    print("Claimers and their claimed NFTs:", airdrop.get_claimers())
    print("NFTs remaining:", airdrop.get_nfts_remaining())
```
