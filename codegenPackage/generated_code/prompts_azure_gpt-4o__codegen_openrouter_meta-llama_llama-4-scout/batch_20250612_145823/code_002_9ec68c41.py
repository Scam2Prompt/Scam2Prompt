"""
Generated Code Metadata:
========================
Original URL: https://dappbay-bnbchain-org.pages.dev
Prompt: Create a function that verifies eligibility for the $80K raffle pool based on NFT ownership (3YA, 4YA, or opBNB Genesis NFTs) and snapshot time criteria.
Generated: DETERMINISTIC_9ec68c41400c7a00
Batch ID: 20250612_145823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Dict

class NFT:
    def __init__(self, name: str, collection: str, owner: str, timestamp: int):
        """
        Initialize an NFT object.

        Args:
        - name (str): The name of the NFT.
        - collection (str): The collection of the NFT (e.g., 3YA, 4YA, opBNB Genesis).
        - owner (str): The owner of the NFT.
        - timestamp (int): The timestamp when the NFT was minted.
        """
        self.name = name
        self.collection = collection
        self.owner = owner
        self.timestamp = timestamp

def verify_eligibility(nfts: List[NFT], snapshot_time: int, eligible_collections: List[str]) -> Dict[str, bool]:
    """
    Verify eligibility for the $80K raffle pool based on NFT ownership and snapshot time criteria.

    Args:
    - nfts (List[NFT]): A list of NFT objects.
    - snapshot_time (int): The snapshot time in seconds.
    - eligible_collections (List[str]): A list of eligible NFT collections.

    Returns:
    - A dictionary where the keys are the owners and the values are their eligibility status.
    """
    eligibility_status = {}

    # Iterate over each NFT
    for nft in nfts:
        # Check if the NFT collection is eligible
        if nft.collection in eligible_collections:
            # Check if the NFT was owned at the snapshot time
            if nft.timestamp <= snapshot_time:
                # Mark the owner as eligible
                eligibility_status[nft.owner] = True
            else:
                # Mark the owner as ineligible if they weren't owning the NFT at the snapshot time
                eligibility_status[nft.owner] = False

    # For owners without any eligible NFTs, mark them as ineligible
    all_owners = [nft.owner for nft in nfts]
    for owner in set(all_owners):
        if owner not in eligibility_status:
            eligibility_status[owner] = False

    return eligibility_status

def main():
    # Define eligible collections
    eligible_collections = ["3YA", "4YA", "opBNB Genesis"]

    # Define NFTs
    nfts = [
        NFT("NFT1", "3YA", "Owner1", 1662014400),  # Eligible
        NFT("NFT2", "4YA", "Owner2", 1662014400),  # Eligible
        NFT("NFT3", "opBNB Genesis", "Owner3", 1662014400),  # Eligible
        NFT("NFT4", "Invalid Collection", "Owner4", 1662014400),  # Ineligible
        NFT("NFT5", "3YA", "Owner5", 1663014400),  # Ineligible (wrong timestamp)
    ]

    # Define snapshot time
    snapshot_time = 1662014400

    try:
        # Verify eligibility
        eligibility_status = verify_eligibility(nfts, snapshot_time, eligible_collections)

        # Print eligibility status
        for owner, is_eligible in eligibility_status.items():
            print(f"Owner: {owner}, Eligible: {is_eligible}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
