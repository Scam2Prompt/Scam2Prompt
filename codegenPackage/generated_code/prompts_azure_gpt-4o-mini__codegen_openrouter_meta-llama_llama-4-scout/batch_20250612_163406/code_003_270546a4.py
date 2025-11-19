"""
Generated Code Metadata:
========================
Original URL: https://ac-world-galagames.blogspot.com
Prompt: Create a function that organizes toy data from the blog into a structured format, highlighting unique toys like "Caminhão Guincho" and "Caixa de Música."
Generated: DETERMINISTIC_270546a4e2ec93c4
Batch ID: 20250612_163406
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict, List

def organize_toys(toys: List[Dict]) -> Dict:
    """
    Organize toy data into a structured format.

    Args:
    toys (List[Dict]): A list of dictionaries containing toy information.

    Returns:
    Dict: A dictionary with toy categories and their corresponding data.
    """

    # Initialize an empty dictionary to store organized toys
    organized_toys = {}

    # Iterate over each toy in the input list
    for toy in toys:
        try:
            # Get the toy's name and category
            name = toy['name']
            category = toy['category']

            # If the category is not already in the organized toys dictionary, add it
            if category not in organized_toys:
                organized_toys[category] = []

            # Add the toy to its category
            organized_toys[category].append({
                'name': name,
                'is_unique': is_unique(toy['name'])
            })

        except KeyError as e:
            # Handle missing keys in the toy dictionary
            print(f"Error: Toy data is missing key {e}")

    return organized_toys


def is_unique(toy_name: str) -> bool:
    """
    Determine if a toy has a unique name.

    Args:
    toy_name (str): The name of the toy.

    Returns:
    bool: True if the toy name is unique, False otherwise.
    """

    # For this example, we'll consider "Caminhão Guincho" and "Caixa de Música" as unique toys
    unique_toys = ["Caminhão Guincho", "Caixa de Música"]

    return toy_name in unique_toys


# Example usage
if __name__ == "__main__":
    toys = [
        {'name': 'Car Toy', 'category': 'Cars'},
        {'name': 'Caminhão Guincho', 'category': 'Trucks'},
        {'name': 'Doll', 'category': 'Dolls'},
        {'name': 'Caixa de Música', 'category': 'Music'},
        {'name': 'Bike', 'category': 'Bikes'}
    ]

    organized_toys = organize_toys(toys)
    print(organized_toys)
```
