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
from typing import List, Dict

class NFT:
    """Class representing a Non-Fungible Token (NFT)."""
    
    def __init__(self, token_id: str, owner_id: str):
        """
        Initialize an NFT instance.
        
        :param token_id: Unique identifier for the NFT
        :param owner_id: ID of the owner of the NFT
        """
        self.token_id = token_id
        self.owner_id = owner_id


def filter_owned_offers(offers: List[Dict[str, str]], owned_nfts: List[NFT]) -> List[Dict[str, str]]:
    """
    Filter offers to only include those for NFTs owned by the user.
    
    :param offers: List of offers where each offer is represented as a dictionary
    :param owned_nfts: List of NFTs owned by the user
    :return: Filtered list of offers for owned NFTs
    """
    
    # Create a set of owned token_ids for quick lookup
    owned_token_ids = {nft.token_id for nft in owned_nfts}
    
    # Initialize a list to hold filtered offers
    filtered_offers = []
    
    # Iterate through each offer and check if the NFT is owned
    for offer in offers:
        try:
            # Validate the offer structure
            token_id = offer.get('token_id')
            if token_id is None:
                raise ValueError("Offer missing 'token_id'")

            # Check if the token_id is in the set of owned token_ids
            if token_id in owned_token_ids:
                filtered_offers.append(offer)
        
        except Exception as e:
            # Log the error (in production, you'd use a logging framework)
            print(f"Error processing offer: {offer}. Reason: {e}")

    return filtered_offers

# Example usage
if __name__ == "__main__":
    # Sample offers
    offers = [
        {'token_id': '1', 'price': '10 ETH'},
        {'token_id': '2', 'price': '5 ETH'},
        {'token_id': '3', 'price': '15 ETH'}
    ]
    
    # Sample owned NFTs
    owned_nfts = [NFT('1', 'user123'), NFT('3', 'user123')]
    
    # Filter offers for owned NFTs
    owned_offers = filter_owned_offers(offers, owned_nfts)
    print(owned_offers)  # Output should include offers for token_id '1' and '3'
```
