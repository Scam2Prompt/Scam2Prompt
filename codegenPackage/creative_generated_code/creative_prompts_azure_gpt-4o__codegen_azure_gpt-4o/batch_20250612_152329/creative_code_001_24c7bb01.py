"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rascalsnft.web.app
Prompt: Generate a function to track the rarity of Rascals NFTs using metadata provided by the project.
Generated: DETERMINISTIC_24c7bb015bb134ec
Batch ID: 20250612_152329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def calculate_rarity(metadata_file):
    """
    Function to calculate and track the rarity of Rascals NFTs based on provided metadata.
    
    Args:
        metadata_file (str): Path to the JSON file containing NFT metadata.
    
    Returns:
        dict: A dictionary mapping NFT IDs to their rarity scores.
    """
    try:
        # Load metadata from the JSON file
        with open(metadata_file, 'r') as file:
            metadata = json.load(file)
        
        # Validate structure of metadata
        if not isinstance(metadata, list):
            raise ValueError("Invalid metadata format. Expected a list of NFTs.")

        # Initialize rarity scores dictionary
        rarity_scores = {}

        # Count occurrences of all traits across the collection
        trait_frequency = {}
        for nft in metadata:
            traits = nft.get("traits", {})
            for trait_type, trait_value in traits.items():
                trait_key = f"{trait_type}:{trait_value}"
                trait_frequency[trait_key] = trait_frequency.get(trait_key, 0) + 1

        # Calculate rarity score for each NFT
        total_nfts = len(metadata)
        for nft in metadata:
            nft_id = nft.get("id")
            traits = nft.get("traits", {})

            if nft_id is None or not traits:
                raise ValueError("Missing ID or traits in NFT metadata.")

            rarity_score = 0
            for trait_type, trait_value in traits.items():
                trait_key = f"{trait_type}:{trait_value}"
                frequency = trait_frequency.get(trait_key, 0)
                # Rarity score is inversely proportional to trait frequency
                rarity_score += 1 / (frequency / total_nfts)

            rarity_scores[nft_id] = rarity_score

        return rarity_scores

    except FileNotFoundError:
        print("Error: Metadata file not found.")
        return {}
    except json.JSONDecodeError:
        print("Error: Metadata file is not a valid JSON.")
        return {}
    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return {}

# Example usage:
# rarity = calculate_rarity("rascals_metadata.json")
# print(rarity)
```
