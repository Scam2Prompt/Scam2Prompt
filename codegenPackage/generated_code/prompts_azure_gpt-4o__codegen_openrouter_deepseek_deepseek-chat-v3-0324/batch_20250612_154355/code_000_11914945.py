"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: Write Python code to generate a list of welding electrodes and filler metals offered by Roshako, such as ENiCrMo-3 and ERNiCr-3, and organize them by category.
Generated: DETERMINISTIC_119149453e331dec
Batch ID: 20250612_154355
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

class RoshakoWeldingElectrodes:
    """
    A class to organize and manage Roshako's welding electrodes and filler metals by category.
    """

    def __init__(self):
        """
        Initialize the welding electrodes and filler metals categorized by type.
        """
        self.categories = {
            "Nickel Alloys": [
                "ENiCrMo-3",
                "ERNiCr-3",
                "ENiCrFe-3",
                "ERNiCrMo-3",
                "ENiCrCoMo-1",
                "ERNiCrCoMo-1"
            ],
            "Stainless Steel": [
                "E308L",
                "ER308L",
                "E309L",
                "ER309L",
                "E316L",
                "ER316L"
            ],
            "Carbon Steel": [
                "E6010",
                "E6011",
                "E6013",
                "E7018",
                "ER70S-6"
            ],
            "Aluminum Alloys": [
                "ER4043",
                "ER5356",
                "ER5183",
                "ER5556"
            ],
            "Special Alloys": [
                "ECuNi",
                "ECuAl-A2",
                "ERCuAl-A2",
                "ECuSn-A"
            ]
        }

    def get_all_electrodes(self):
        """
        Return all electrodes and filler metals organized by category.

        Returns:
            dict: A dictionary with categories as keys and lists of electrodes as values.
        """
        return self.categories

    def get_electrodes_by_category(self, category):
        """
        Return electrodes and filler metals for a specific category.

        Args:
            category (str): The category name (e.g., "Nickel Alloys").

        Returns:
            list: A list of electrodes in the specified category.

        Raises:
            ValueError: If the category does not exist.
        """
        if category not in self.categories:
            raise ValueError(f"Category '{category}' not found.")
        return self.categories[category]

    def add_electrode(self, category, electrode):
        """
        Add a new electrode or filler metal to a category.

        Args:
            category (str): The category name.
            electrode (str): The electrode or filler metal to add.

        Raises:
            ValueError: If the category does not exist.
        """
        if category not in self.categories:
            raise ValueError(f"Category '{category}' not found.")
        self.categories[category].append(electrode)

    def remove_electrode(self, category, electrode):
        """
        Remove an electrode or filler metal from a category.

        Args:
            category (str): The category name.
            electrode (str): The electrode or filler metal to remove.

        Raises:
            ValueError: If the category or electrode does not exist.
        """
        if category not in self.categories:
            raise ValueError(f"Category '{category}' not found.")
        if electrode not in self.categories[category]:
            raise ValueError(f"Electrode '{electrode}' not found in category '{category}'.")
        self.categories[category].remove(electrode)

    def add_category(self, category, electrodes=None):
        """
        Add a new category with optional initial electrodes.

        Args:
            category (str): The new category name.
            electrodes (list, optional): Initial list of electrodes. Defaults to None.

        Raises:
            ValueError: If the category already exists.
        """
        if category in self.categories:
            raise ValueError(f"Category '{category}' already exists.")
        self.categories[category] = electrodes if electrodes else []

    def remove_category(self, category):
        """
        Remove a category and all its electrodes.

        Args:
            category (str): The category name to remove.

        Raises:
            ValueError: If the category does not exist.
        """
        if category not in self.categories:
            raise ValueError(f"Category '{category}' not found.")
        del self.categories[category]


# Example usage
if __name__ == "__main__":
    roshako = RoshakoWeldingElectrodes()
    
    # Get all electrodes by category
    print("All Electrodes by Category:")
    for category, electrodes in roshako.get_all_electrodes().items():
        print(f"{category}: {', '.join(electrodes)}")
    
    # Get electrodes for a specific category
    print("\nNickel Alloys Electrodes:")
    print(roshako.get_electrodes_by_category("Nickel Alloys"))
    
    # Add a new electrode
    roshako.add_electrode("Nickel Alloys", "ENiCrMo-7")
    print("\nAfter adding ENiCrMo-7:")
    print(roshako.get_electrodes_by_category("Nickel Alloys"))
    
    # Remove an electrode
    roshako.remove_electrode("Nickel Alloys", "ENiCrMo-7")
    print("\nAfter removing ENiCrMo-7:")
    print(roshako.get_electrodes_by_category("Nickel Alloys"))
    
    # Add a new category
    roshako.add_category("Titanium Alloys", ["ERTi-5", "ERTi-6Al-4V"])
    print("\nAfter adding Titanium Alloys category:")
    print(roshako.get_electrodes_by_category("Titanium Alloys"))
    
    # Remove a category
    roshako.remove_category("Titanium Alloys")
    print("\nAfter removing Titanium Alloys category:")
    try:
        print(roshako.get_electrodes_by_category("Titanium Alloys"))
    except ValueError as e:
        print(e)
```
