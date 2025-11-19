"""
Generated Code Metadata:
========================
Original URL: https://jamcards.io
Prompt: Generate Python code to filter and display NFTs from the "Heart Full of Love JamCards" collection based on their rarity traits, such as "VOCAL" or "INSTRUMENT."
Generated: DETERMINISTIC_4bb30255e4826282
Batch ID: 20250612_150034
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# nft_filter.py

import json

class NFT:
    def __init__(self, id, name, traits):
        """
        Initialize an NFT object.

        Args:
        - id (str): Unique identifier of the NFT.
        - name (str): Name of the NFT.
        - traits (list): List of traits of the NFT.
        """
        self.id = id
        self.name = name
        self.traits = traits

class NFTFilter:
    def __init__(self, nft_data):
        """
        Initialize an NFTFilter object.

        Args:
        - nft_data (list): List of NFT data in JSON format.
        """
        self.nft_data = nft_data

    def filter_by_trait(self, trait_value):
        """
        Filter NFTs by a specific trait value.

        Args:
        - trait_value (str): Value of the trait to filter by.

        Returns:
        - list: List of NFT objects that match the filter.
        """
        filtered_nfts = []
        for nft in self.nft_data:
            for trait in nft['traits']:
                if trait['trait_type'] == 'Rarity' and trait['value'] == trait_value:
                    filtered_nfts.append(NFT(nft['id'], nft['name'], nft['traits']))
                    break
                elif trait['trait_type'] in ['VOCAL', 'INSTRUMENT'] and trait['value'] == trait_value:
                    filtered_nfts.append(NFT(nft['id'], nft['name'], nft['traits']))
                    break
        return filtered_nfts

    def display_nfts(self, nfts):
        """
        Display the NFTs in a readable format.

        Args:
        - nfts (list): List of NFT objects to display.
        """
        for nft in nfts:
            print(f"ID: {nft.id}")
            print(f"Name: {nft.name}")
            print("Traits:")
            for trait in nft.traits:
                print(f"  - {trait['trait_type']}: {trait['value']}")
            print()

def load_nft_data(file_path):
    """
    Load NFT data from a JSON file.

    Args:
    - file_path (str): Path to the JSON file.

    Returns:
    - list: List of NFT data in JSON format.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return []

def main():
    file_path = 'nft_data.json'  # replace with your JSON file path
    nft_data = load_nft_data(file_path)
    filter = NFTFilter(nft_data)

    while True:
        print("Filter by:")
        print("1. VOCAL")
        print("2. INSTRUMENT")
        print("3. Rarity")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            filtered_nfts = filter.filter_by_trait('VOCAL')
            filter.display_nfts(filtered_nfts)
        elif choice == '2':
            filtered_nfts = filter.filter_by_trait('INSTRUMENT')
            filter.display_nfts(filtered_nfts)
        elif choice == '3':
            rarity = input("Enter rarity (e.g. Rare, Legendary): ")
            filtered_nfts = filter.filter_by_trait(rarity)
            filter.display_nfts(filtered_nfts)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
```

```json
// nft_data.json example

[
  {
    "id": "1",
    "name": "NFT 1",
    "traits": [
      {
        "trait_type": "Rarity",
        "value": "Common"
      },
      {
        "trait_type": "VOCAL",
        "value": "Yes"
      }
    ]
  },
  {
    "id": "2",
    "name": "NFT 2",
    "traits": [
      {
        "trait_type": "Rarity",
        "value": "Rare"
      },
      {
        "trait_type": "INSTRUMENT",
        "value": "Guitar"
      }
    ]
  }
]
```
