"""
Generated Code Metadata:
========================
Original URL: https://rplanet-io.vercel.app
Prompt: Create a Python script to analyze NFT data from R-Planet Conquest, categorizing them into Land, Hero, Hero's Items, Items for one-time use, and Artifacts.
Generated: DETERMINISTIC_7c2d0dbe037e63ed
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_categorizer.py

import json
from enum import Enum
from typing import Dict, List

class NFTCategory(Enum):
    """Enum for NFT categories."""
    LAND = "Land"
    HERO = "Hero"
    HERO_ITEMS = "Hero's Items"
    ITEMS_ONE_TIME_USE = "Items for one-time use"
    ARTIFACTS = "Artifacts"
    UNKNOWN = "Unknown"

class NFT:
    """Class representing an NFT."""
    def __init__(self, id: str, name: str, type: str, category: str):
        self.id = id
        self.name = name
        self.type = type
        self.category = category

    def __repr__(self):
        return f"NFT(id={self.id}, name={self.name}, type={self.type}, category={self.category})"

def categorize_nft(nft: NFT) -> NFTCategory:
    """Categorize an NFT based on its type and category."""
    if nft.category == "land":
        return NFTCategory.LAND
    elif nft.category == "hero":
        return NFTCategory.HERO
    elif nft.category in ["hero_item", "hero's item"]:
        return NFTCategory.HERO_ITEMS
    elif nft.category == "item":
        if nft.type == "consumable":
            return NFTCategory.ITEMS_ONE_TIME_USE
        else:
            return NFTCategory.ARTIFACTS
    else:
        return NFTCategory.UNKNOWN

def load_nft_data(file_path: str) -> List[NFT]:
    """Load NFT data from a JSON file."""
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return [NFT(nft["id"], nft["name"], nft["type"], nft["category"]) for nft in data]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return []

def categorize_nfts(nfts: List[NFT]) -> Dict[NFTCategory, List[NFT]]:
    """Categorize a list of NFTs."""
    categorized_nfts = {category: [] for category in NFTCategory}
    for nft in nfts:
        category = categorize_nft(nft)
        categorized_nfts[category].append(nft)
    return categorized_nfts

def main():
    file_path = "nft_data.json"  # replace with your file path
    nft_data = load_nft_data(file_path)
    categorized_nfts = categorize_nfts(nft_data)

    for category, nfts in categorized_nfts.items():
        if nfts:
            print(f"**{category.value}**")
            for nft in nfts:
                print(nft)
            print()

if __name__ == "__main__":
    main()
```

```json
// nft_data.json example

[
    {
        "id": "1",
        "name": "Land 1",
        "type": "",
        "category": "land"
    },
    {
        "id": "2",
        "name": "Hero 1",
        "type": "",
        "category": "hero"
    },
    {
        "id": "3",
        "name": "Sword",
        "type": "",
        "category": "hero_item"
    },
    {
        "id": "4",
        "name": "Potion",
        "type": "consumable",
        "category": "item"
    },
    {
        "id": "5",
        "name": "Artifact 1",
        "type": "",
        "category": "item"
    }
]
```
