"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Write a Python script to calculate the rarity of NFTs within a collection like Prime Ape Planet, based on metadata attributes.
Generated: DETERMINISTIC_f0bf08522a5501c1
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from collections import defaultdict
from typing import List, Dict, Any

class NFT:
    def __init__(self, token_id: str, attributes: Dict[str, Any]):
        """Initialize an NFT instance with a token ID and its attributes."""
        self.token_id = token_id
        self.attributes = attributes

    def __repr__(self):
        """Return a string representation of the NFT."""
        return f"NFT(token_id={self.token_id}, attributes={self.attributes})"

def load_nft_data(file_path: str) -> List[NFT]:
    """Load NFT data from a JSON file.

    Args:
        file_path (str): The path to the JSON file containing NFT metadata.

    Returns:
        List[NFT]: A list of NFT instances.

    Raises:
        FileNotFoundError: If the provided file path does not exist.
        json.JSONDecodeError: If the file content is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            nft_data = json.load(file)
            return [NFT(token_id=item['token_id'], attributes=item['attributes']) for item in nft_data]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the provided file.")

def calculate_rarity(nfts: List[NFT]) -> Dict[str, float]:
    """Calculate the rarity score for each NFT based on its attributes.

    Args:
        nfts (List[NFT]): A list of NFT instances.

    Returns:
        Dict[str, float]: A dictionary mapping token IDs to their rarity scores.
    """
    attribute_counts = defaultdict(int)

    # Count occurrences of each attribute across all NFTs
    for nft in nfts:
        for attribute, value in nft.attributes.items():
            attribute_counts[(attribute, value)] += 1

    rarity_scores = {}
    total_nfts = len(nfts)

    # Calculate rarity score: Rarity = (1 / Count) * 100
    for nft in nfts:
        score = 0.0
        for attribute, value in nft.attributes.items():
            count = attribute_counts[(attribute, value)]
            # Avoid division by zero
            if count > 0:
                score += (1 / count) * 100
        rarity_scores[nft.token_id] = score

    return rarity_scores

def main():
    """Main function to execute the NFT rarity calculation."""
    file_path = 'nfts_metadata.json'  # Specify your JSON file path
    try:
        nfts = load_nft_data(file_path)
        rarity_scores = calculate_rarity(nfts)

        # Output the rarity scores
        for token_id, score in rarity_scores.items():
            print(f"NFT Token ID: {token_id} | Rarity Score: {score:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
