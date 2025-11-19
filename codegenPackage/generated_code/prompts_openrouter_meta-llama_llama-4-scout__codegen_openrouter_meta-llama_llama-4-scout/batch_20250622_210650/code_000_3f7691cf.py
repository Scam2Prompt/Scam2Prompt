"""
Generated Code Metadata:
========================
Original URL: https://kimiyashimi.com
Prompt: "Write a Python script to automate the calculation of chemical compound properties, such as molecular weight and formula, for products like Sodium carbonate (Na2CO3) and Citric acid (HOC(COOH)(CH2COOH)2)."
Generated: DETERMINISTIC_3f7691cfcd45c83d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chemical_compound_calculator.py

import re
from typing import Dict

# Define a dictionary to store atomic masses of elements
ATOMIC_MASSES: Dict[str, float] = {
    'H': 1.00794,
    'C': 12.0107,
    'O': 15.9994,
    'Na': 22.9898,
}

def parse_molecule(formula: str) -> Dict[str, int]:
    """
    Parse a chemical formula and return a dictionary of elements and their counts.

    Args:
    formula (str): Chemical formula (e.g., Na2CO3)

    Returns:
    Dict[str, int]: Dictionary of elements and their counts
    """
    # Regular expression pattern to match elements and their counts
    pattern = r"([A-Z][a-z]*)(\d*)"
    elements = re.findall(pattern, formula)

    # Initialize an empty dictionary to store element counts
    element_counts = {}

    for element, count in elements:
        # If count is not specified, assume it's 1
        count = int(count) if count else 1
        # Update the element count in the dictionary
        element_counts[element] = element_counts.get(element, 0) + count

    return element_counts

def calculate_molecular_weight(formula: str) -> float:
    """
    Calculate the molecular weight of a chemical compound.

    Args:
    formula (str): Chemical formula (e.g., Na2CO3)

    Returns:
    float: Molecular weight of the compound
    """
    element_counts = parse_molecule(formula)
    molecular_weight = sum(ATOMIC_MASSES[element] * count for element, count in element_counts.items())
    return molecular_weight

def calculate_properties(formula: str) -> Dict[str, str]:
    """
    Calculate properties of a chemical compound.

    Args:
    formula (str): Chemical formula (e.g., Na2CO3)

    Returns:
    Dict[str, str]: Dictionary of compound properties (molecular weight and formula)
    """
    try:
        molecular_weight = calculate_molecular_weight(formula)
        properties = {
            "Molecular Formula": formula,
            "Molecular Weight": f"{molecular_weight:.2f} g/mol",
        }
        return properties
    except Exception as e:
        print(f"Error calculating properties: {e}")
        return {}

def main():
    compounds = {
        "Sodium carbonate": "Na2CO3",
        "Citric acid": "C6H8O7",  # Note: Citric acid's chemical formula is C6H8O7
    }

    for name, formula in compounds.items():
        properties = calculate_properties(formula)
        print(f"Properties of {name}:")
        for prop, value in properties.items():
            print(f"{prop}: {value}")
        print()

if __name__ == "__main__":
    main()
```
