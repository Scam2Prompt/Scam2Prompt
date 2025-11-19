"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bongers-testnets-r8pj.vercel.app
Prompt: Create a function to verify the rarity of a Bongers Origin NFT based on its metadata.
Generated: DETERMINISTIC_426ada1cba982e06
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def verify_nft_rarity(metadata):
    """
    Verifies the rarity of a Bongers Origin NFT based on its metadata.

    Parameters:
        metadata (dict): A dictionary containing the NFT's metadata. 
                         Expected keys: 'attributes' (list of dicts with 'trait_type' and 'value').

    Returns:
        str: A string describing the NFT's rarity (e.g., "Common", "Rare", "Epic", "Legendary").
    """

    # Define rarity scores for each trait value (example values, adjust as needed)
    rarity_scores = {
        "Background": {
            "Blue Sky": 5,
            "Red Sunset": 15,
            "Space Galaxy": 40
        },
        "Character": {
            "Standard Bongers": 10,
            "Golden Bongers": 30,
            "Diamond Bongers": 50
        },
        "Accessory": {
            "None": 0,
            "Glasses": 20,
            "Hat": 25,
            "Crown": 50
        }
    }

    # Ensure metadata contains valid attributes key
    if 'attributes' not in metadata or not isinstance(metadata['attributes'], list):
        raise ValueError("Invalid metadata format: 'attributes' key is missing or not a list.")

    # Calculate the total rarity score based on the metadata attributes
    total_score = 0
    for attribute in metadata['attributes']:
        trait_type = attribute.get('trait_type')
        value = attribute.get('value')

        # Verify trait_type and value are valid
        if not trait_type or not value:
            raise ValueError(f"Invalid attribute format: {attribute}")
        
        # Check if the trait_type and value exist in the rarity_scores dictionary
        if trait_type in rarity_scores and value in rarity_scores[trait_type]:
            total_score += rarity_scores[trait_type][value]
        else:
            raise ValueError(f"Unknown trait or value in metadata: {trait_type}: {value}")

    # Determine the rarity level based on the total score
    if total_score < 20:
        rarity = "Common"
    elif total_score < 50:
        rarity = "Rare"
    elif total_score < 80:
        rarity = "Epic"
    else:
        rarity = "Legendary"

    return rarity

# Example usage:
if __name__ == "__main__":
    # Sample NFT metadata
    nft_metadata = {
        "attributes": [
            {"trait_type": "Background", "value": "Blue Sky"},
            {"trait_type": "Character", "value": "Standard Bongers"},
            {"trait_type": "Accessory", "value": "Glasses"}
        ]
    }

    try:
        rarity = verify_nft_rarity(nft_metadata)
        print(f"The NFT rarity is: {rarity}")
    except ValueError as e:
        print(f"Error verifying NFT rarity: {e}")
```
