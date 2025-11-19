"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Develop a script to automate the comparison of alloy standards (DIN, ASTM, BS) for titanium and stainless steel alloys, such as ALLOY 1.4923, in defense applications.
Generated: DETERMINISTIC_f1009ed7972a7ee9
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# alloy_comparator.py

from typing import Dict, List

class AlloyStandard:
    """Represents an alloy standard with its name and composition."""

    def __init__(self, name: str, composition: Dict[str, float]):
        """
        Initializes an AlloyStandard object.

        Args:
        - name (str): The name of the alloy standard (e.g., DIN, ASTM, BS).
        - composition (Dict[str, float]): A dictionary of element compositions (e.g., {'Cr': 12.0, 'Ni': 10.0}).
        """
        self.name = name
        self.composition = composition

class Alloy:
    """Represents an alloy with its name and standards."""

    def __init__(self, name: str):
        """
        Initializes an Alloy object.

        Args:
        - name (str): The name of the alloy (e.g., ALLOY 1.4923).
        """
        self.name = name
        self.standards = {}

    def add_standard(self, standard: AlloyStandard):
        """
        Adds an alloy standard to the alloy.

        Args:
        - standard (AlloyStandard): The alloy standard to add.
        """
        self.standards[standard.name] = standard

    def compare_standards(self):
        """
        Compares the compositions of the alloy standards.

        Returns:
        - A dictionary with the standard names as keys and their compositions as values.
        """
        return {name: standard.composition for name, standard in self.standards.items()}

def load_alloy_data(alloy_name: str, standards: List[Dict[str, str]]) -> Alloy:
    """
    Loads alloy data from a list of standards.

    Args:
    - alloy_name (str): The name of the alloy.
    - standards (List[Dict[str, str]]): A list of dictionaries containing the standard data.

    Returns:
    - An Alloy object with the loaded data.
    """
    alloy = Alloy(alloy_name)

    for standard in standards:
        name = standard['name']
        composition = {}
        for element, value in standard['composition'].items():
            try:
                composition[element] = float(value)
            except ValueError:
                print(f"Invalid composition value for {element} in {name}")
                continue

        alloy.add_standard(AlloyStandard(name, composition))

    return alloy

def main():
    # Example usage
    alloy_name = "ALLOY 1.4923"
    standards = [
        {'name': 'DIN', 'composition': {'Cr': '12.0', 'Ni': '10.0', 'Mo': '1.0'}},
        {'name': 'ASTM', 'composition': {'Cr': '11.5', 'Ni': '10.5', 'Mo': '1.2'}},
        {'name': 'BS', 'composition': {'Cr': '12.5', 'Ni': '9.5', 'Mo': '1.1'}}
    ]

    alloy = load_alloy_data(alloy_name, standards)
    comparisons = alloy.compare_standards()

    print(f"Alloy: {alloy_name}")
    for standard, composition in comparisons.items():
        print(f"Standard: {standard}")
        for element, value in composition.items():
            print(f"  {element}: {value:.2f}")
        print()

if __name__ == "__main__":
    main()
```
