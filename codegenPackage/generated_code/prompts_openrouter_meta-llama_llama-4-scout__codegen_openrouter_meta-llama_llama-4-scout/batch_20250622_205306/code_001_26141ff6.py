"""
Generated Code Metadata:
========================
Original URL: https://apperley.ca
Prompt: Generate a genealogy report on the Hallen or Holland family, referencing Arthur W. Cornelius Hallen's 1885 account.
Generated: DETERMINISTIC_26141ff64e9c588f
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# genealogy_report.py

import json
from datetime import datetime

class GenealogyReport:
    def __init__(self, family_name, reference_source):
        """
        Initialize the GenealogyReport class.

        Args:
            family_name (str): The name of the family (e.g., Hallen, Holland).
            reference_source (str): The source of the reference (e.g., Arthur W. Cornelius Hallen's 1885 account).
        """
        self.family_name = family_name
        self.reference_source = reference_source
        self.family_tree = {}

    def add_ancestor(self, name, birth_year, death_year=None, spouse=None, children=None):
        """
        Add an ancestor to the family tree.

        Args:
            name (str): The name of the ancestor.
            birth_year (int): The birth year of the ancestor.
            death_year (int, optional): The death year of the ancestor. Defaults to None.
            spouse (str, optional): The name of the spouse. Defaults to None.
            children (list, optional): A list of children. Defaults to None.
        """
        self.family_tree[name] = {
            "birth_year": birth_year,
            "death_year": death_year,
            "spouse": spouse,
            "children": children if children else []
        }

    def generate_report(self):
        """
        Generate the genealogy report.

        Returns:
            str: The genealogy report.
        """
        report = f"Genealogy Report for the {self.family_name} Family\n"
        report += f"Reference Source: {self.reference_source}\n\n"

        for ancestor, details in self.family_tree.items():
            report += f"Ancestor: {ancestor}\n"
            report += f"  Birth Year: {details['birth_year']}\n"
            if details["death_year"]:
                report += f"  Death Year: {details['death_year']}\n"
            if details["spouse"]:
                report += f"  Spouse: {details['spouse']}\n"
            if details["children"]:
                report += f"  Children: {', '.join(details['children'])}\n\n"

        return report

def load_reference_source(file_path):
    """
    Load the reference source from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The reference source data.
    """
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return {}
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
        return {}

def main():
    # Load reference source from JSON file
    reference_source_data = load_reference_source("hallen_1885_account.json")

    # Create a GenealogyReport instance
    report = GenealogyReport("Hallen", "Arthur W. Cornelius Hallen's 1885 account")

    # Add ancestors to the family tree
    report.add_ancestor(
        "Arthur W. Cornelius Hallen",
        1850,
        spouse="Elizabeth Hallen",
        children=["William Hallen", "Emily Hallen"]
    )
    report.add_ancestor(
        "William Hallen",
        1880,
        birth_year=1880,
        death_year=1960,
        spouse="Margaret Hallen",
        children=["James Hallen", "Elizabeth Hallen"]
    )

    # Generate the genealogy report
    genealogy_report = report.generate_report()

    # Print the genealogy report
    print(genealogy_report)

if __name__ == "__main__":
    main()
```

```json
// hallen_1885_account.json

{
    "author": "Arthur W. Cornelius Hallen",
    "year": 1885,
    "account": "This is a sample account of the Hallen family."
}
```
