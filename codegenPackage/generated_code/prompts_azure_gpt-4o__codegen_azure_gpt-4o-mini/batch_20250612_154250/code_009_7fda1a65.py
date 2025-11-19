"""
Generated Code Metadata:
========================
Original URL: https://tari.ee
Prompt: Create a tool for comparing architectural project designs, inspired by the diverse projects listed on Tari.ee, such as Hornslandet and Päästeamet.
Generated: DETERMINISTIC_7fda1a65ba48ca8a
Batch ID: 20250612_154250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from typing import List, Dict, Any

class DesignComparator:
    """
    A class to compare architectural project designs based on their attributes.
    """

    def __init__(self, design_files: List[str]):
        """
        Initializes the DesignComparator with a list of design file paths.

        :param design_files: List of paths to design JSON files.
        """
        self.designs = self.load_designs(design_files)

    def load_designs(self, design_files: List[str]) -> List[Dict[str, Any]]:
        """
        Loads design data from JSON files.

        :param design_files: List of paths to design JSON files.
        :return: List of design dictionaries.
        """
        designs = []
        for file in design_files:
            try:
                with open(file, 'r') as f:
                    design = json.load(f)
                    designs.append(design)
            except (FileNotFoundError, json.JSONDecodeError) as e:
                print(f"Error loading {file}: {e}")
        return designs

    def compare_designs(self) -> List[Dict[str, Any]]:
        """
        Compares the loaded designs and returns a summary of differences.

        :return: List of dictionaries containing comparison results.
        """
        if len(self.designs) < 2:
            raise ValueError("At least two designs are required for comparison.")

        comparison_results = []
        base_design = self.designs[0]

        for design in self.designs[1:]:
            differences = self.find_differences(base_design, design)
            comparison_results.append({
                'base': base_design.get('name'),
                'comparison': design.get('name'),
                'differences': differences
            })

        return comparison_results

    def find_differences(self, design1: Dict[str, Any], design2: Dict[str, Any]) -> Dict[str, Any]:
        """
        Finds differences between two design dictionaries.

        :param design1: First design dictionary.
        :param design2: Second design dictionary.
        :return: Dictionary of differences.
        """
        differences = {}
        for key in set(design1.keys()).union(design2.keys()):
            if design1.get(key) != design2.get(key):
                differences[key] = {
                    'design1': design1.get(key),
                    'design2': design2.get(key)
                }
        return differences

    def display_comparison(self, comparison_results: List[Dict[str, Any]]) -> None:
        """
        Displays the comparison results in a readable format.

        :param comparison_results: List of comparison results.
        """
        for result in comparison_results:
            print(f"Comparing '{result['base']}' with '{result['comparison']}':")
            for key, diff in result['differences'].items():
                print(f"  - {key}: {diff['design1']} vs {diff['design2']}")
            print("\n")

if __name__ == "__main__":
    # Example usage
    design_files = [
        'design1.json',
        'design2.json',
        'design3.json'
    ]

    comparator = DesignComparator(design_files)
    try:
        results = comparator.compare_designs()
        comparator.display_comparison(results)
    except ValueError as e:
        print(f"Comparison error: {e}")
```

This code provides a tool for comparing architectural project designs stored in JSON files. It includes error handling for file loading and comparison, and it is structured to be easily extendable and maintainable.
