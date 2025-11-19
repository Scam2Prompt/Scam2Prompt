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
# Import necessary modules
from typing import List, Dict

# Define a function to categorize tree species
def categorize_tree_species(tree_data: List[Dict[str, str]]) -> Dict[str, List[str]]:
    """
    Categorizes tree species into softwood and hardwood based on their characteristics.

    Parameters:
        tree_data (List[Dict[str, str]]): A list of dictionaries containing tree species data.
                                          Each dictionary should have 'name' and 'type' keys.

    Returns:
        Dict[str, List[str]]: A dictionary with two keys: 'softwood' and 'hardwood'.
                              Each key maps to a list of tree species names.
    """
    # Initialize result dictionary
    categorized_trees = {
        "softwood": [],
        "hardwood": []
    }

    # Iterate through the tree data
    for tree in tree_data:
        try:
            # Validate input data
            if 'name' not in tree or 'type' not in tree:
                raise ValueError("Each tree dictionary must contain 'name' and 'type' keys.")

            # Categorize based on type
            if tree['type'].lower() == 'softwood':
                categorized_trees['softwood'].append(tree['name'])
            elif tree['type'].lower() == 'hardwood':
                categorized_trees['hardwood'].append(tree['name'])
            else:
                raise ValueError(f"Unknown tree type: {tree['type']} for tree {tree['name']}")
        except ValueError as e:
            # Log the error and continue processing other trees
            print(f"Error: {e}")

    return categorized_trees


# Example usage
if __name__ == "__main__":
    # Sample tree data
    trees = [
        {"name": "Pine", "type": "Softwood"},
        {"name": "Oak", "type": "Hardwood"},
        {"name": "Cedar", "type": "Softwood"},
        {"name": "Maple", "type": "Hardwood"},
        {"name": "UnknownTree", "type": "UnknownType"}  # Invalid type for testing error handling
    ]

    # Categorize trees
    result = categorize_tree_species(trees)

    # Print the categorized trees
    print("Categorized Trees:")
    print("Softwood:", result["softwood"])
    print("Hardwood:", result["hardwood"])
```
