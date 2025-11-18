"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://realis.pages.dev
Prompt: Write a Python script that generates all possible unique Meowgon units (19,683 combinations) based on the 27 elements and their types, as outlined on the Realis website.
Generated: DETERMINISTIC_ed3a7659a97466c2
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import itertools
import json

# Define the elements and their corresponding types
ELEMENTS = {
    'Fire': 'Elemental',
    'Water': 'Elemental',
    'Earth': 'Elemental',
    'Air': 'Elemental',
    'Light': 'Elemental',
    'Dark': 'Elemental',
    'Wood': 'Elemental',
    'Metal': 'Elemental',
    'Stone': 'Elemental',
    'Ice': 'Elemental',
    'Electric': 'Elemental',
    'Psychic': 'Elemental',
    'Poison': 'Elemental',
    'Shadow': 'Elemental',
    'Spirit': 'Elemental',
    'Time': 'Elemental',
    'Space': 'Elemental',
    'Chaos': 'Elemental',
    'Order': 'Elemental',
    'Sound': 'Elemental',
    'Life': 'Elemental',
    'Death': 'Elemental',
    'Nature': 'Elemental',
    'Technology': 'Elemental',
    'Void': 'Elemental',
    'Metallic': 'Elemental',
    'Crystalline': 'Elemental'
}

# Generate all combinations of Meowgon units
def generate_meowgon_units(elements):
    """
    Generate all unique combinations of Meowgon units based on the provided elements.

    Args:
        elements (dict): A dictionary of elements and their types.

    Returns:
        list: A list of unique combinations.
    """
    try:
        # Get the keys (element names) from the ELEMENTS dictionary
        element_names = list(elements.keys())
        # Generate all possible combinations (3 elements each)
        combinations = list(itertools.product(element_names, repeat=3))
        
        # Filter for unique combinations (ignoring order)
        unique_combinations = set(tuple(sorted(comb)) for comb in combinations)

        return unique_combinations
    except Exception as e:
        print(f"Error generating combinations: {e}")
        return []

def save_combinations_to_file(combinations, filename='meowgon_units.json'):
    """
    Save the generated combinations to a JSON file.

    Args:
        combinations (set): A set of unique combinations.
        filename (str): The name of the file to save the combinations.
    """
    try:
        with open(filename, 'w') as file:
            json.dump(list(combinations), file, indent=4)
        print(f"Combinations successfully saved to {filename}")
    except IOError as e:
        print(f"File error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    """
    Main function to generate Meowgon units and save them to a file.
    """
    # Generate Meowgon units
    meowgon_units = generate_meowgon_units(ELEMENTS)

    # Save the combinations to a file
    save_combinations_to_file(meowgon_units)

if __name__ == "__main__":
    main()
```
