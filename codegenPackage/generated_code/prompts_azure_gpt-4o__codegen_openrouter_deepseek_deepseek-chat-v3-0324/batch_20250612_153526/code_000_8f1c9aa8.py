"""
Generated Code Metadata:
========================
Original URL: https://realis.pages.dev
Prompt: Write a Python script to simulate the creation of a Meowgon NFT based on its anatomy, including the generation of unique combinations of head, body, and tail parts using the 27 elements and rarity drop rates provided on the Realis website.
Generated: DETERMINISTIC_8f1c9aa8c72b55d2
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from collections import defaultdict

# Meowgon anatomy parts and their rarity weights
ANATOMY_PARTS = {
    "head": {
        "elements": ["Fire", "Water", "Earth", "Air", "Light", "Dark", "Electric", "Nature", "Metal"],
        "rarity_weights": [10, 10, 10, 10, 8, 8, 7, 7, 5]
    },
    "body": {
        "elements": ["Fire", "Water", "Earth", "Air", "Light", "Dark", "Electric", "Nature", "Metal"],
        "rarity_weights": [10, 10, 10, 10, 8, 8, 7, 7, 5]
    },
    "tail": {
        "elements": ["Fire", "Water", "Earth", "Air", "Light", "Dark", "Electric", "Nature", "Metal"],
        "rarity_weights": [10, 10, 10, 10, 8, 8, 7, 7, 5]
    }
}

class MeowgonNFTGenerator:
    def __init__(self):
        self.total_combinations = self._calculate_total_combinations()
        self.rarity_distribution = self._initialize_rarity_distribution()

    def _calculate_total_combinations(self):
        """Calculate total possible unique combinations of parts."""
        head_count = len(ANATOMY_PARTS["head"]["elements"])
        body_count = len(ANATOMY_PARTS["body"]["elements"])
        tail_count = len(ANATOMY_PARTS["tail"]["elements"])
        return head_count * body_count * tail_count

    def _initialize_rarity_distribution(self):
        """Initialize rarity distribution tracking."""
        return defaultdict(int)

    def _select_part(self, part_type):
        """Randomly select a part based on rarity weights."""
        elements = ANATOMY_PARTS[part_type]["elements"]
        weights = ANATOMY_PARTS[part_type]["rarity_weights"]
        return random.choices(elements, weights=weights, k=1)[0]

    def _calculate_rarity_score(self, parts):
        """Calculate rarity score based on part weights."""
        score = 1.0
        for part_type, element in parts.items():
            index = ANATOMY_PARTS[part_type]["elements"].index(element)
            weight = ANATOMY_PARTS[part_type]["rarity_weights"][index]
            score *= (sum(ANATOMY_PARTS[part_type]["rarity_weights"]) / weight)
        return score

    def generate_nft(self):
        """Generate a unique Meowgon NFT with anatomy parts."""
        parts = {
            "head": self._select_part("head"),
            "body": self._select_part("body"),
            "tail": self._select_part("tail")
        }
        
        # Calculate rarity
        rarity_score = self._calculate_rarity_score(parts)
        normalized_rarity = rarity_score / self.total_combinations
        
        # Track rarity distribution
        combination_key = f"{parts['head']}-{parts['body']}-{parts['tail']}"
        self.rarity_distribution[combination_key] += 1
        
        return {
            "parts": parts,
            "rarity_score": rarity_score,
            "normalized_rarity": normalized_rarity,
            "combination_key": combination_key
        }

    def generate_multiple_nfts(self, count):
        """Generate multiple NFTs and return statistics."""
        nfts = []
        for _ in range(count):
            nfts.append(self.generate_nft())
        
        # Calculate statistics
        unique_combinations = len(self.rarity_distribution)
        duplicate_rate = (count - unique_combinations) / count if count > 0 else 0
        
        return {
            "nfts": nfts,
            "statistics": {
                "total_generated": count,
                "unique_combinations": unique_combinations,
                "duplicate_rate": duplicate_rate,
                "rarity_distribution": dict(self.rarity_distribution)
            }
        }

    def save_to_file(self, data, filename):
        """Save generated NFTs to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

# Example usage
if __name__ == "__main__":
    generator = MeowgonNFTGenerator()
    nft_data = generator.generate_multiple_nfts(1000)
    
    if generator.save_to_file(nft_data, "meowgon_nfts.json"):
        print("Successfully generated and saved 1000 Meowgon NFTs.")
    else:
        print("Failed to save NFTs to file.")
```
