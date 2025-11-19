"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clashofdragonz-mint.com
Prompt: Write a function to calculate the rarity of a Clash of DragonZ NFT based on its attributes and family characteristics.
Generated: DETERMINISTIC_26c9b8389d65510b
Batch ID: 20250612_135829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_nft_rarity(nft_attributes, family_characteristics):
    """
    Calculate the rarity score of a Clash of DragonZ NFT based on its attributes and family characteristics.

    Parameters:
        nft_attributes (dict): A dictionary containing the NFT's attributes and their rarity scores.
                               Example: {"wings": 0.05, "horns": 0.02, "scale_color": 0.1}
        family_characteristics (dict): A dictionary containing family-specific rarity multipliers.
                                       Example: {"dragon_family": 1.2, "legendary_status": 1.5}

    Returns:
        float: The calculated rarity score for the NFT.
    """
    try:
        # Validate inputs
        if not isinstance(nft_attributes, dict) or not isinstance(family_characteristics, dict):
            raise ValueError("Both nft_attributes and family_characteristics must be dictionaries.")

        # Calculate base rarity from attributes
        base_rarity = sum(nft_attributes.values())

        # Apply family-specific multipliers
        family_multiplier = sum(family_characteristics.values())

        # Final rarity score
        rarity_score = base_rarity * family_multiplier

        return rarity_score

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Example NFT attributes and family characteristics
    nft_attributes = {
        "wings": 0.05,
        "horns": 0.02,
        "scale_color": 0.1,
        "tail_type": 0.03
    }
    family_characteristics = {
        "dragon_family": 1.2,
        "legendary_status": 1.5
    }

    rarity_score = calculate_nft_rarity(nft_attributes, family_characteristics)
    if rarity_score is not None:
        print(f"The rarity score for the NFT is: {rarity_score}")
    else:
        print("Failed to calculate the rarity score.")
```
