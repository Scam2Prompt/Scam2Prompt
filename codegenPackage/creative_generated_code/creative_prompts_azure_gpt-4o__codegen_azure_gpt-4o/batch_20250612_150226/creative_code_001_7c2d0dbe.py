"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rplanet-io.vercel.app
Prompt: Create a Python script to analyze NFT data from R-Planet Conquest, categorizing them into Land, Hero, Hero's Items, Items for one-time use, and Artifacts.
Generated: DETERMINISTIC_7c2d0dbe037e63ed
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class NFTAnalyzer:
    """
    A class to analyze and categorize NFT data from R-Planet Conquest.
    """

    def __init__(self, nft_data):
        """
        Initializes the NFTAnalyzer with NFT data.

        Parameters:
        nft_data (list): List of NFT data dictionaries.
        """
        self.nft_data = nft_data
        self.categories = {
            "Land": [],
            "Hero": [],
            "Hero's Items": [],
            "Items for One-Time Use": [],
            "Artifacts": [],
        }

    def categorize_nfts(self):
        """
        Categorizes NFTs based on their type into predefined categories.
        """
        for nft in self.nft_data:
            try:
                nft_type = nft.get("type", None)
                if nft_type in self.categories:
                    self.categories[nft_type].append(nft)
                else:
                    raise ValueError(f"Unknown NFT type: {nft_type}")
            except ValueError as ve:
                print(f"Error categorizing NFT: {ve}")
            except Exception as e:
                print(f"Unexpected error: {e}")

    def get_category(self, category_name):
        """
        Retrieves NFTs from a specific category.

        Parameters:
        category_name (str): The name of the category.

        Returns:
        list: List of NFTs in the requested category.
        """
        return self.categories.get(category_name, [])

    def save_categories_to_file(self, output_file):
        """
        Saves categorized NFTs to a JSON file.

        Parameters:
        output_file (str): Path to the output JSON file.
        """
        try:
            with open(output_file, "w") as file:
                json.dump(self.categories, file, indent=4)
            print(f"Categorized NFT data saved to {output_file}")
        except Exception as e:
            print(f"Error saving categorized data: {e}")


# Example usage
if __name__ == "__main__":
    # Sample NFT data (replace with actual data from R-Planet Conquest)
    sample_nft_data = [
        {"id": 1, "name": "Land of Fire", "type": "Land"},
        {"id": 2, "name": "Hero John", "type": "Hero"},
        {"id": 3, "name": "Sword of Valor", "type": "Hero's Items"},
        {"id": 4, "name": "Healing Potion", "type": "Items for One-Time Use"},
        {"id": 5, "name": "Ancient Artifact", "type": "Artifacts"},
    ]

    # Initialize the analyzer with NFT data
    analyzer = NFTAnalyzer(sample_nft_data)

    # Categorize the NFTs
    analyzer.categorize_nfts()

    # Print categorized data
    for category, items in analyzer.categories.items():
        print(f"\nCategory: {category}")
        for item in items:
            print(f"  - {item['name']}")

    # Save categorized data to file
    analyzer.save_categories_to_file("categorized_nft_data.json")
```
