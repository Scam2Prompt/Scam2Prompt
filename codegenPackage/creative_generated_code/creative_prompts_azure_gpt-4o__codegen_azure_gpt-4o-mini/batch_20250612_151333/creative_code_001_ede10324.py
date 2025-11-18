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
class AirdropSystem:
    def __init__(self, total_nfts: int):
        """
        Initialize the AirdropSystem with the total number of NFTs available.

        :param total_nfts: Total number of NFTs available for the airdrop.
        """
        self.total_nfts = total_nfts
        self.claimers = set()  # Store unique claimers to avoid duplicates

    def add_claimer(self, claimer_id: str):
        """
        Add a claimer to the airdrop system.

        :param claimer_id: Unique identifier for the claimer (e.g., wallet address).
        :raises ValueError: If claimer_id is empty or already claimed.
        """
        if not claimer_id:
            raise ValueError("Claimer ID cannot be empty.")

        if claimer_id in self.claimers:
            raise ValueError(f"Claimer ID '{claimer_id}' has already claimed an NFT.")

        if len(self.claimers) >= self.total_nfts:
            raise RuntimeError("No more NFTs available for claiming.")

        self.claimers.add(claimer_id)  # Add claimer to the set
        print(f"Claimer '{claimer_id}' added successfully.")

    def get_claim_count(self) -> int:
        """
        Retrieve the current number of unique claimers.

        :return: The count of unique claimers.
        """
        return len(self.claimers)

    def remaining_nfts(self) -> int:
        """
        Calculate the remaining NFTs available for claiming.

        :return: The number of remaining NFTs available for claiming.
        """
        return self.total_nfts - len(self.claimers)


# Example usage:
if __name__ == "__main__":
    try:
        airdrop = AirdropSystem(total_nfts=14)

        # Adding 6 claimers
        claimers = ["claimer1", "claimer2", "claimer3", "claimer4", "claimer5", "claimer6"]
        for claimer in claimers:
            airdrop.add_claimer(claimer)

        print(f"Total unique claimers: {airdrop.get_claim_count()}")
        print(f"Remaining NFTs: {airdrop.remaining_nfts()}")

        # Attempt to add a duplicate claimer
        airdrop.add_claimer("claimer1")

    except Exception as e:
        print(f"Error: {e}")
```
