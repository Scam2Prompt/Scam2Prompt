"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Compare the properties of ALLOY 17-4PH and ALLOY 1.4923 in terms of their uses in various industries.
Generated: DETERMINISTIC_90162743143c36f0
Batch ID: 20250622_212806
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# alloy_comparator.py

class Alloy:
    """Represents a metal alloy with its properties and uses."""

    def __init__(self, name, description, composition, industries):
        """
        Initializes an Alloy object.

        Args:
            name (str): The name of the alloy.
            description (str): A brief description of the alloy.
            composition (dict): A dictionary of the alloy's chemical composition.
            industries (list): A list of industries that use the alloy.
        """
        self.name = name
        self.description = description
        self.composition = composition
        self.industries = industries

    def __str__(self):
        return f"{self.name}: {self.description}"

    def get_composition(self):
        return self.composition

    def get_industries(self):
        return self.industries


class AlloyComparator:
    """Compares the properties of different alloys."""

    def __init__(self):
        self.alloys = {}

    def add_alloy(self, alloy):
        """
        Adds an alloy to the comparator.

        Args:
            alloy (Alloy): The alloy to add.
        """
        self.alloys[alloy.name] = alloy

    def compare_alloys(self, alloy1_name, alloy2_name):
        """
        Compares the properties of two alloys.

        Args:
            alloy1_name (str): The name of the first alloy.
            alloy2_name (str): The name of the second alloy.

        Returns:
            dict: A dictionary containing the comparison results.
        """
        if alloy1_name not in self.alloys or alloy2_name not in self.alloys:
            raise ValueError("Both alloys must be added to the comparator")

        alloy1 = self.alloys[alloy1_name]
        alloy2 = self.alloys[alloy2_name]

        comparison_results = {
            "Alloy 1": alloy1.name,
            "Alloy 2": alloy2.name,
            "Description": f"{alloy1.description} vs {alloy2.description}",
            "Composition": {
                "Alloy 1": alloy1.get_composition(),
                "Alloy 2": alloy2.get_composition(),
            },
            "Industries": {
                "Alloy 1": alloy1.get_industries(),
                "Alloy 2": alloy2.get_industries(),
            },
        }

        return comparison_results


def main():
    comparator = AlloyComparator()

    # Define alloys
    alloy_17_4ph = Alloy(
        "ALLOY17-4PH",
        "A precipitation-hardened stainless steel alloy",
        {
            "Cr": 15.5,
            "Ni": 4.5,
            "Cu": 3.5,
            "Nb": 0.3,
        },
        ["Aerospace", "Chemical Processing", "Oil and Gas"],
    )

    alloy_1_4923 = Alloy(
        "ALLOY1.4923",
        "A martensitic stainless steel alloy",
        {
            "Cr": 11.5,
            "Ni": 0.5,
            "Mo": 0.5,
            "V": 0.3,
        },
        ["Power Generation", "Chemical Processing", "Petrochemical"],
    )

    # Add alloys to comparator
    comparator.add_alloy(alloy_17_4ph)
    comparator.add_alloy(alloy_1_4923)

    try:
        # Compare alloys
        comparison_results = comparator.compare_alloys("ALLOY17-4PH", "ALLOY1.4923")

        # Print comparison results
        print("Alloy Comparison Results:")
        print(f"Alloy 1: {comparison_results['Alloy 1']}")
        print(f"Alloy 2: {comparison_results['Alloy 2']}")
        print(f"Description: {comparison_results['Description']}")
        print("Composition:")
        for alloy, composition in comparison_results["Composition"].items():
            print(f"  {alloy}:")
            for element, percentage in composition.items():
                print(f"    {element}: {percentage}%")
        print("Industries:")
        for alloy, industries in comparison_results["Industries"].items():
            print(f"  {alloy}: {', '.join(industries)}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
