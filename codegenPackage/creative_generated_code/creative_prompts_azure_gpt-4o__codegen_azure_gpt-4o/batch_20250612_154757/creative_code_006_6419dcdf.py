"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artocean.org
Prompt: Develop a script to filter and display NFT collections based on item count and highest bid values, similar to the "Top Collection" section on Artlife.
Generated: DETERMINISTIC_6419dcdf330bda87
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def filter_nft_collections(collections, min_item_count, min_highest_bid):
    """
    Filters NFT collections based on minimum item count and highest bid values.

    Args:
        collections (list): A list of NFT collections. Each collection is a dictionary containing
                            `name`, `item_count`, and `highest_bid`.
        min_item_count (int): Minimum number of items required for a collection to pass the filter.
        min_highest_bid (float): Minimum highest bid value required for a collection to pass the filter.

    Returns:
        list: A list of filtered NFT collections.
    """
    filtered_collections = []
    for collection in collections:
        try:
            # Ensure the collection has all required fields and meets the criteria
            if (
                'name' in collection and
                'item_count' in collection and
                'highest_bid' in collection and
                isinstance(collection['item_count'], int) and
                isinstance(collection['highest_bid'], (int, float)) and
                collection['item_count'] >= min_item_count and
                collection['highest_bid'] >= min_highest_bid
            ):
                filtered_collections.append(collection)
        except Exception as e:
            print(f"Error processing collection {collection.get('name', 'Unknown')}: {e}")
            continue  # Skip to the next collection if an error occurs
    return filtered_collections

def display_collections(collections):
    """
    Displays NFT collections in a formatted way.

    Args:
        collections (list): A list of NFT collections to display.
    """
    print("Top NFT Collections:")
    print("--------------------")
    for collection in collections:
        try:
            print(f"Name: {collection['name']}, Items: {collection['item_count']}, Highest Bid: ${collection['highest_bid']:.2f}")
        except KeyError as e:
            print(f"Error displaying collection: Missing key {e}")
        except Exception as e:
            print(f"An unexpected error occurred while displaying a collection: {e}")

# Example data representing NFT collections
example_collections = [
    {"name": "Collection A", "item_count": 150, "highest_bid": 250.5},
    {"name": "Collection B", "item_count": 80, "highest_bid": 120},
    {"name": "Collection C", "item_count": 200, "highest_bid": 500},
    {"name": "Collection D", "item_count": 50, "highest_bid": 75},
    {"name": "Collection E", "item_count": 300, "highest_bid": 1000},
]

if __name__ == "__main__":
    # Define filter criteria
    MIN_ITEM_COUNT = 100  # Minimum items required
    MIN_HIGHEST_BID = 200.0  # Minimum highest bid in dollars

    # Filter collections based on criteria
    filtered = filter_nft_collections(example_collections, MIN_ITEM_COUNT, MIN_HIGHEST_BID)

    # Display the filtered collections
    display_collections(filtered)
```
