"""
Generated Code Metadata:
========================
Original URL: https://theprimeapeplanetmint.pages.dev
Prompt: Write a Python script to calculate the rarity of NFTs within a collection like Prime Ape Planet, based on metadata attributes.
Generated: DETERMINISTIC_f0bf08522a5501c1
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
NFT Rarity Calculator

Calculates the rarity of NFTs within a collection based on metadata attributes.

Usage:
    python nft_rarity_calculator.py --collection <collection_name> --metadata <metadata_file>
"""

import argparse
import json
from collections import defaultdict
from typing import Dict, List

def load_metadata(metadata_file: str) -> List[Dict]:
    """
    Loads NFT metadata from a JSON file.

    Args:
        metadata_file (str): Path to the metadata file.

    Returns:
        List[Dict]: A list of NFT metadata dictionaries.
    """
    try:
        with open(metadata_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Metadata file '{metadata_file}' not found.")
        return []
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse metadata file '{metadata_file}': {e}")
        return []

def calculate_rarity(metadata: List[Dict]) -> Dict:
    """
    Calculates the rarity of each NFT based on its metadata attributes.

    Args:
        metadata (List[Dict]): A list of NFT metadata dictionaries.

    Returns:
        Dict: A dictionary mapping NFT IDs to their rarity scores.
    """
    attribute_counts = defaultdict(int)
    nft_attributes = {}

    # Count occurrences of each attribute value
    for nft in metadata:
        nft_id = nft['id']
        nft_attributes[nft_id] = {}
        for attribute, value in nft['attributes'].items():
            attribute_key = f"{attribute}:{value}"
            attribute_counts[attribute_key] += 1
            nft_attributes[nft_id][attribute] = value

    # Calculate rarity scores
    rarity_scores = {}
    for nft_id, attributes in nft_attributes.items():
        rarity_score = 0
        for attribute, value in attributes.items():
            attribute_key = f"{attribute}:{value}"
            rarity_score += 1 / attribute_counts[attribute_key]
        rarity_scores[nft_id] = rarity_score

    return rarity_scores

def main():
    parser = argparse.ArgumentParser(description='NFT Rarity Calculator')
    parser.add_argument('--collection', type=str, help='Collection name')
    parser.add_argument('--metadata', type=str, help='Path to metadata file')
    args = parser.parse_args()

    metadata = load_metadata(args.metadata)
    if not metadata:
        return

    rarity_scores = calculate_rarity(metadata)

    # Print rarity scores
    print("NFT Rarity Scores:")
    for nft_id, rarity_score in rarity_scores.items():
        print(f"{nft_id}: {rarity_score:.4f}")

if __name__ == '__main__':
    main()
```
