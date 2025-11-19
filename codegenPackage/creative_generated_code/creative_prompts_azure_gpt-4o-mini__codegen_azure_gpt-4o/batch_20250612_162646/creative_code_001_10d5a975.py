"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jelybaby.web.app
Prompt: Write a function to calculate the rarity of Jelly NFTs based on the details provided in the Jelly Airdrop information.
Generated: DETERMINISTIC_10d5a97591294f2b
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_nft_rarity(nft_traits, total_supply):
    """
    Calculate the rarity of a Jelly NFT based on its traits and the total supply.

    Args:
        nft_traits (dict): A dictionary where keys are trait names and values are their occurrences in the collection.
                           Example: {"Background": {"Blue": 10, "Red": 20}, "Hat": {"Green": 5, "Black": 15}}
        total_supply (int): Total number of NFTs in the collection.

    Returns:
        dict: A dictionary where keys are trait names and values are dictionaries containing the rarity score for each trait value.
              Example: {"Background": {"Blue": 0.01, "Red": 0.02}, "Hat": {"Green": 0.005, "Black": 0.015}}
    """
    if not isinstance(nft_traits, dict):
        raise ValueError("nft_traits must be a dictionary.")
    if not isinstance(total_supply, int) or total_supply <= 0:
        raise ValueError("total_supply must be a positive integer.")

    rarity_scores = {}

    for trait, values in nft_traits.items():
        if not isinstance(values, dict):
            raise ValueError(f"Trait '{trait}' values must be a dictionary.")
        
        rarity_scores[trait] = {}
        for value, count in values.items():
            if not isinstance(count, int) or count < 0:
                raise ValueError(f"Count for value '{value}' in trait '{trait}' must be a non-negative integer.")
            
            # Calculate rarity score as the inverse of frequency
            rarity_scores[trait][value] = count / total_supply

    return rarity_scores


# Example usage:
if __name__ == "__main__":
    # Example NFT traits details from Jelly Airdrop information
    jelly_nft_traits = {
        "Background": {"Blue": 500, "Red": 300, "Green": 200},
        "Hat": {"None": 700, "Cap": 250, "Helmet": 50},
        "Eyes": {"Normal": 800, "Glasses": 150, "Eye Patch": 50}
    }
    total_nfts = 1000  # Total supply of Jelly NFTs

    try:
        rarity = calculate_nft_rarity(jelly_nft_traits, total_nfts)
        print(json.dumps(rarity, indent=4))
    except ValueError as e:
        print(f"Error: {e}")
```
