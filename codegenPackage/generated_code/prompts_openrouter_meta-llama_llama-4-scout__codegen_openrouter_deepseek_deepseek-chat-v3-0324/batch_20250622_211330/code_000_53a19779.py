"""
Generated Code Metadata:
========================
Original URL: https://zealy.gg
Prompt: "Generate a list of community categories on a platform like Zealy, including descriptions for each."
Generated: DETERMINISTIC_53a197798983c2ba
Batch ID: 20250622_211330
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# community_categories.py
from typing import List, Dict

def get_community_categories() -> List[Dict[str, str]]:
    """
    Generates a list of community categories with descriptions similar to Zealy.
    
    Returns:
        List[Dict[str, str]]: A list of dictionaries where each dictionary contains
                              'name' and 'description' keys for a category.
    """
    categories = [
        {
            "name": "NFT Collectors",
            "description": "Communities centered around NFT collections, trading, and discussions."
        },
        {
            "name": "DeFi Enthusiasts",
            "description": "Groups focused on decentralized finance projects, protocols, and yield farming."
        },
        {
            "name": "Gaming Guilds",
            "description": "Communities for blockchain gaming, play-to-earn, and game development."
        },
        {
            "name": "DAO Contributors",
            "description": "Groups involved in decentralized autonomous organizations and governance."
        },
        {
            "name": "Web3 Developers",
            "description": "Communities for developers building decentralized applications and protocols."
        },
        {
            "name": "Crypto Traders",
            "description": "Groups focused on cryptocurrency trading, market analysis, and strategies."
        },
        {
            "name": "Metaverse Explorers",
            "description": "Communities exploring virtual worlds, VR, and digital ownership."
        },
        {
            "name": "Social Impact",
            "description": "Groups using blockchain for social good, charity, and positive impact."
        },
        {
            "name": "Art & Creativity",
            "description": "Communities for digital artists, creators, and creative projects."
        },
        {
            "name": "Education & Onboarding",
            "description": "Groups focused on educating newcomers about blockchain and Web3."
        }
    ]
    
    return categories

if __name__ == "__main__":
    # Example usage: Print all categories with descriptions
    categories = get_community_categories()
    for category in categories:
        print(f"{category['name']}: {category['description']}\n")
```
