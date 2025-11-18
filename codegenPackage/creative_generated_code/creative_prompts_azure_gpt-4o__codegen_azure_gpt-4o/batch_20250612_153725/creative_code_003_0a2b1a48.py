"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rodeo.pages.dev
Prompt: Write a function to filter offers on the Rodeo platform, ensuring only offers for owned NFTs are shown.
Generated: DETERMINISTIC_0a2b1a4848f87a78
Batch ID: 20250612_153725
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import List, Dict

def filter_owned_nft_offers(offers: List[Dict], owned_nft_ids: List[str]) -> List[Dict]:
    """
    Filters offers to only include those related to owned NFTs.
    
    Args:
        offers (List[Dict]): A list of offers where each offer is a dictionary containing offer information.
            Example: [{'offer_id': '1', 'nft_id': '101', 'price': 50.0}, ...]
        owned_nft_ids (List[str]): A list of NFT IDs that the user owns.
    
    Returns:
        List[Dict]: A list of offers filtered to include only those related to owned NFTs.
    """
    # Validate input types
    if not isinstance(offers, list) or not all(isinstance(offer, dict) for offer in offers):
        raise ValueError("Offers must be a list of dictionaries.")

    if not isinstance(owned_nft_ids, list) or not all(isinstance(nft_id, str) for nft_id in owned_nft_ids):
        raise ValueError("Owned NFT IDs must be a list of strings.")
    
    # Filter offers to include only those associated with owned NFT IDs
    filtered_offers = [
        offer for offer in offers 
        if 'nft_id' in offer and offer['nft_id'] in owned_nft_ids
    ]
    
    return filtered_offers

# Example usage
if __name__ == "__main__":
    # Example data
    sample_offers = [
        {'offer_id': '1', 'nft_id': '101', 'price': 50.0},
        {'offer_id': '2', 'nft_id': '102', 'price': 75.0},
        {'offer_id': '3', 'nft_id': '103', 'price': 100.0}
    ]
    user_owned_nfts = ['101', '103']
    
    # Filter offers
    try:
        filtered = filter_owned_nft_offers(sample_offers, user_owned_nfts)
        print("Filtered Offers:", filtered)
    except ValueError as e:
        print(f"Input Error: {e}")
```
