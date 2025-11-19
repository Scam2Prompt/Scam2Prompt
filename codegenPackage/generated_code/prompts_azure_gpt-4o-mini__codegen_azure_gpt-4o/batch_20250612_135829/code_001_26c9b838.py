"""
Generated Code Metadata:
========================
Original URL: https://clashofdragonz-mint.com
Prompt: Write a function to calculate the rarity of a Clash of DragonZ NFT based on its attributes and family characteristics.
Generated: DETERMINISTIC_26c9b8389d65510b
Batch ID: 20250612_135829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def calculate_nft_rarity(attributes, family_characteristics):
    """
    Calculate the rarity score of a Clash of DragonZ NFT based on its attributes and family characteristics.

    Parameters:
        attributes (dict): A dictionary containing the NFT's attributes and their rarity scores.
                           Example: {"wings": 0.05, "color": 0.1, "horns": 0.02}
        family_characteristics (dict): A dictionary containing family-specific rarity modifiers.
                                        Example: {"dragon_family": 0.2, "generation": 0.1}

    Returns:
        float: The calculated rarity score of the NFT.
    """
    try:
        # Validate input types
        if not isinstance(attributes, dict) or not isinstance(family_characteristics, dict):
            raise ValueError("Both attributes and family_characteristics must be dictionaries.")

        # Initialize rarity score
        rarity_score = 0.0

        # Calculate rarity score from attributes
        for attribute, rarity in attributes.items():
            if not isinstance(rarity, (int, float)) or rarity < 0:
                raise ValueError(f"Invalid rarity value for attribute '{attribute}': {rarity}")
            rarity_score += rarity

        # Apply family characteristics modifiers
        for characteristic, modifier in family_characteristics.items():
            if not isinstance(modifier, (int, float)) or modifier < 0:
                raise ValueError(f"Invalid modifier value for characteristic '{characteristic}': {modifier}")
            rarity_score += modifier

        return rarity_score

    except Exception as e:
        # Log the error and re-raise it
        print(f"Error calculating NFT rarity: {e}")
        raise

# Example usage
if __name__ == "__main__":
    # Example NFT attributes and family characteristics
    nft_attributes = {
        "wings": 0.05,
        "color": 0.1,
        "horns": 0.02
    }
    nft_family_characteristics = {
        "dragon_family": 0.2,
        "generation": 0.1
    }

    try:
        rarity = calculate_nft_rarity(nft_attributes, nft_family_characteristics)
        print(f"NFT Rarity Score: {rarity}")
    except Exception as e:
        print(f"Failed to calculate rarity: {e}")
```
