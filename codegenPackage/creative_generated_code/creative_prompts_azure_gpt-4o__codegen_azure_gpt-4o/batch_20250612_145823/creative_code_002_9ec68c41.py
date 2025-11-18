"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappbay-bnbchain-org.pages.dev
Prompt: Create a function that verifies eligibility for the $80K raffle pool based on NFT ownership (3YA, 4YA, or opBNB Genesis NFTs) and snapshot time criteria.
Generated: DETERMINISTIC_9ec68c41400c7a00
Batch ID: 20250612_145823
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime

def is_eligible_for_raffle(nft_owned, snapshot_time):
    """
    Verifies eligibility for the $80K raffle pool based on NFT ownership and snapshot criteria.

    Args:
        nft_owned (list): A list of NFT identifiers owned by the user (e.g. ['3YA', 'opBNB Genesis']).
        snapshot_time (datetime): The snapshot time when eligibility is checked.

    Returns:
        bool: True if eligible for the raffle, False otherwise.
    """
    # Define the eligible NFTs
    eligible_nfts = {"3YA", "4YA", "opBNB Genesis"}

    # Define the snapshot time criteria (raffle eligibility cutoff)
    snapshot_cutoff = datetime(2023, 10, 1, 0, 0, 0)  # Example cutoff date and time.

    # Check if the snapshot time is before or equal to the cutoff
    if snapshot_time > snapshot_cutoff:
        return False  # Not eligible, snapshot time is after the cutoff.

    # Check if user owns at least one eligible NFT
    for nft in nft_owned:
        if nft in eligible_nfts:
            return True  # Eligible for the raffle.

    return False  # Not eligible, no valid NFTs owned.


# Example usage:
try:
    user_nfts = ['opBNB Genesis', 'SomeOtherNFT']  # NFTs owned by the user.
    snapshot_date = datetime(2023, 9, 30, 23, 59, 59)  # User's snapshot time.

    if is_eligible_for_raffle(user_nfts, snapshot_date):
        print("Congratulations! You are eligible for the $80K raffle.")
    else:
        print("Sorry, you are not eligible for the $80K raffle.")
except Exception as e:
    # Catch any unexpected errors
    print(f"An error occurred: {e}")
```
