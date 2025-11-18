"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cknft.pages.dev
Prompt: Generate code to display NFT traits dynamically, such as "High Fashion traits" including outfit, league, tattoo, and haircut, for a collection like Blvck Phantoms.
Generated: DETERMINISTIC_68c6152b561f4aa3
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class NFTTrait:
    """
    A class to represent a trait of an NFT.
    """
    def __init__(self, trait_type, value):
        self.trait_type = trait_type
        self.value = value

    def __str__(self):
        return f"{self.trait_type}: {self.value}"

class NFT:
    """
    A class to represent an NFT with various traits.
    """
    def __init__(self, name, traits):
        self.name = name
        self.traits = traits

    def display_traits(self):
        """
        Displays the traits of the NFT in a formatted manner.
        """
        print(f"NFT Name: {self.name}")
        print("Traits:")
        for trait in self.traits:
            print(f"  - {trait}")

def load_nft_data(file_path):
    """
    Load NFT data from a JSON file.

    :param file_path: Path to the JSON file containing NFT data.
    :return: List of NFT objects.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            nfts = []
            for item in data:
                traits = [NFTTrait(trait['trait_type'], trait['value']) for trait in item['traits']]
                nfts.append(NFT(item['name'], traits))
            return nfts
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON from the file.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    """
    Main function to load and display NFT traits.
    """
    file_path = 'nfts.json'  # Path to your JSON file
    nfts = load_nft_data(file_path)

    if nfts:  # Check if we have successfully loaded any NFTs
        for nft in nfts:
            nft.display_traits()
            print()  # Print a newline for better readability

if __name__ == "__main__":
    main()
```

**Sample JSON Structure (nfts.json):**
```json
[
    {
        "name": "Blvck Phantom #1",
        "traits": [
            {"trait_type": "Outfit", "value": "Designer Suit"},
            {"trait_type": "League", "value": "Elite"},
            {"trait_type": "Tattoo", "value": "Dragon"},
            {"trait_type": "Haircut", "value": "Buzz Cut"}
        ]
    },
    {
        "name": "Blvck Phantom #2",
        "traits": [
            {"trait_type": "Outfit", "value": "Casual Wear"},
            {"trait_type": "League", "value": "Standard"},
            {"trait_type": "Tattoo", "value": "Skull"},
            {"trait_type": "Haircut", "value": "Long Hair"}
        ]
    }
]
```
