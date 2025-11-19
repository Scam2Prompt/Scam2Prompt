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
    A class to categorize tree species into softwood and hardwood based on their characteristics.
    """

    def __init__(self, name, leaf_type, seed_type, growth_rate):
        """
        Initialize a TreeSpecies instance.

        Args:
            name (str): Name of the tree species.
            leaf_type (str): Type of leaf ('needle-like' or 'broad-leaf').
            seed_type (str): Type of seed ('cone' or 'enclosed').
            growth_rate (str): Growth rate ('fast' or 'slow').
        """
        self.name = name
        self.leaf_type = leaf_type
        self.seed_type = seed_type
        self.growth_rate = growth_rate

    def categorize(self):
        """
        Categorize the tree species as softwood or hardwood.

        Returns:
            str: 'softwood' or 'hardwood' based on characteristics.
        """
        if (self.leaf_type == 'needle-like' and 
            self.seed_type == 'cone' and 
            self.growth_rate == 'fast'):
            return 'softwood'
        elif (self.leaf_type == 'broad-leaf' and 
              self.seed_type == 'enclosed' and 
              self.growth_rate == 'slow'):
            return 'hardwood'
        else:
            return 'unknown'

    @staticmethod
    def validate_input(leaf_type, seed_type, growth_rate):
        """
        Validate input parameters for tree characteristics.

        Args:
            leaf_type (str): Type of leaf.
            seed_type (str): Type of seed.
            growth_rate (str): Growth rate.

        Raises:
            ValueError: If any parameter is invalid.
        """
        valid_leaf_types = {'needle-like', 'broad-leaf'}
        valid_seed_types = {'cone', 'enclosed'}
        valid_growth_rates = {'fast', 'slow'}

        if leaf_type not in valid_leaf_types:
            raise ValueError(f"Invalid leaf_type: {leaf_type}. Must be one of {valid_leaf_types}")
        if seed_type not in valid_seed_types:
            raise ValueError(f"Invalid seed_type: {seed_type}. Must be one of {valid_seed_types}")
        if growth_rate not in valid_growth_rates:
            raise ValueError(f"Invalid growth_rate: {growth_rate}. Must be one of {valid_growth_rates}")


def categorize_tree_species(name, leaf_type, seed_type, growth_rate):
    """
    Categorize a tree species based on its characteristics.

    Args:
        name (str): Name of the tree species.
        leaf_type (str): Type of leaf ('needle-like' or 'broad-leaf').
        seed_type (str): Type of seed ('cone' or 'enclosed').
        growth_rate (str): Growth rate ('fast' or 'slow').

    Returns:
        dict: Dictionary containing tree name and its category.
    """
    try:
        TreeSpecies.validate_input(leaf_type, seed_type, growth_rate)
        tree = TreeSpecies(name, leaf_type, seed_type, growth_rate)
        category = tree.categorize()
        return {
            'name': name,
            'category': category
        }
    except ValueError as e:
        return {
            'error': str(e),
            'name': name
        }


# Example usage
if __name__ == "__main__":
    trees = [
        {'name': 'Pine', 'leaf_type': 'needle-like', 'seed_type': 'cone', 'growth_rate': 'fast'},
        {'name': 'Oak', 'leaf_type': 'broad-leaf', 'seed_type': 'enclosed', 'growth_rate': 'slow'},
        {'name': 'Maple', 'leaf_type': 'broad-leaf', 'seed_type': 'enclosed', 'growth_rate': 'slow'},
        {'name': 'Spruce', 'leaf_type': 'needle-like', 'seed_type': 'cone', 'growth_rate': 'fast'},
        {'name': 'Invalid', 'leaf_type': 'unknown', 'seed_type': 'cone', 'growth_rate': 'fast'}
    ]

    for tree in trees:
        result = categorize_tree_species(
            tree['name'],
            tree['leaf_type'],
            tree['seed_type'],
            tree['growth_rate']
        )
        print(result)
```
