"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Write a Python code snippet to categorize tree species into soft wood and hard wood based on their characteristics.
Generated: DETERMINISTIC_f1ceeaea26af4687
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TreeSpecies:
    """
    A class to represent a tree species and categorize it as softwood or hardwood.
    """

    def __init__(self, name, wood_type, characteristics):
        """
        Initializes a TreeSpecies instance.

        :param name: str - The name of the tree species.
        :param wood_type: str - The type of wood ('softwood' or 'hardwood').
        :param characteristics: dict - A dictionary of characteristics of the tree species.
        """
        self.name = name
        self.wood_type = wood_type.lower()
        self.characteristics = characteristics

        # Validate wood type
        if self.wood_type not in ['softwood', 'hardwood']:
            raise ValueError("wood_type must be either 'softwood' or 'hardwood'.")

    def get_info(self):
        """
        Returns a summary of the tree species information.

        :return: str - A formatted string containing the tree species information.
        """
        return f"Tree Species: {self.name}\n" \
               f"Wood Type: {self.wood_type.capitalize()}\n" \
               f"Characteristics: {self.characteristics}"

def categorize_trees(trees):
    """
    Categorizes a list of tree species into softwood and hardwood.

    :param trees: list - A list of TreeSpecies instances.
    :return: dict - A dictionary with 'softwood' and 'hardwood' as keys and lists of tree names as values.
    """
    categorized_trees = {
        'softwood': [],
        'hardwood': []
    }

    for tree in trees:
        if not isinstance(tree, TreeSpecies):
            raise TypeError("All items in the list must be instances of TreeSpecies.")
        
        categorized_trees[tree.wood_type].append(tree.name)

    return categorized_trees

# Example usage
if __name__ == "__main__":
    try:
        # Create instances of TreeSpecies
        pine = TreeSpecies("Pine", "softwood", {"needle-like leaves": True, "coniferous": True})
        oak = TreeSpecies("Oak", "hardwood", {"broad leaves": True, "deciduous": True})
        cedar = TreeSpecies("Cedar", "softwood", {"aromatic wood": True, "resistant to decay": True})

        # List of tree species
        tree_list = [pine, oak, cedar]

        # Categorize trees
        categorized = categorize_trees(tree_list)

        # Print categorized trees
        print("Categorized Trees:")
        for wood_type, names in categorized.items():
            print(f"{wood_type.capitalize()}: {', '.join(names)}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
