"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mistnft-migration.pages.dev
Prompt: Write a function that filters NFT items in the Mist Marketplace based on tier and payment token options.
Generated: DETERMINISTIC_115584bd00df3a67
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict, Optional

# Define a function to filter NFT items
def filter_nft_items(
    nft_items: List[Dict],
    tier: Optional[str] = None,
    payment_token: Optional[str] = None
) -> List[Dict]:
    """
    Filters NFT items based on tier and payment token options.
    
    Args:
        nft_items (List[Dict]): A list of NFT items where each item is a dictionary.
        tier (Optional[str]): Tier to filter by (e.g., "Gold", "Silver", "Bronze"). Defaults to None.
        payment_token (Optional[str]): Payment token to filter by (e.g., "ETH", "MIST"). Defaults to None.
    
    Returns:
        List[Dict]: A list of filtered NFT items matching the criteria.
    """
    # Validate input parameters
    if not isinstance(nft_items, list):
        raise ValueError("nft_items must be a list of dictionaries.")
    if tier and not isinstance(tier, str):
        raise ValueError("tier must be a string.")
    if payment_token and not isinstance(payment_token, str):
        raise ValueError("payment_token must be a string.")

    # Filter NFT items based on criteria
    filtered_items = [
        item for item in nft_items
        if (tier is None or item.get("tier") == tier) and
           (payment_token is None or item.get("payment_token") == payment_token)
    ]

    return filtered_items


# Example usage (for testing purposes):
if __name__ == "__main__":
    # Sample NFT items
    sample_nft_items = [
        {"id": 1, "name": "NFT1", "tier": "Gold", "payment_token": "ETH"},
        {"id": 2, "name": "NFT2", "tier": "Silver", "payment_token": "MIST"},
        {"id": 3, "name": "NFT3", "tier": "Bronze", "payment_token": "ETH"},
        {"id": 4, "name": "NFT4", "tier": "Gold", "payment_token": "MIST"},
        {"id": 5, "name": "NFT5", "tier": "Silver", "payment_token": "ETH"}
    ]

    # Filter by tier and payment token
    filtered = filter_nft_items(sample_nft_items, tier="Gold", payment_token="ETH")
    print(filtered)  # Output: [{'id': 1, 'name': 'NFT1', 'tier': 'Gold', 'payment_token': 'ETH'}]
```
