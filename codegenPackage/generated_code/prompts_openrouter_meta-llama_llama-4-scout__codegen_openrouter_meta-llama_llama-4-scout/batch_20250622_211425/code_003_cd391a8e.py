"""
Generated Code Metadata:
========================
Original URL: https://glisten.site
Prompt: Create a Python script to generate a catalog of iPhone cases with different designs and prices, similar to the ones listed on Glisten's website.
Generated: DETERMINISTIC_cd391a8e4233b33b
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# iphone_case_catalog.py

class IPhoneCase:
    """Represents an iPhone case with a design and price."""

    def __init__(self, design: str, price: float, compatibility: str):
        """
        Initializes an iPhone case.

        Args:
            design (str): The design of the iPhone case.
            price (float): The price of the iPhone case.
            compatibility (str): The iPhone model compatibility.
        """
        self.design = design
        self.price = price
        self.compatibility = compatibility

    def __str__(self):
        return f"{self.design} - ${self.price:.2f} ({self.compatibility})"


class IPhoneCaseCatalog:
    """Represents a catalog of iPhone cases."""

    def __init__(self):
        self.cases = []

    def add_case(self, case: IPhoneCase):
        """
        Adds an iPhone case to the catalog.

        Args:
            case (IPhoneCase): The iPhone case to add.
        """
        self.cases.append(case)

    def remove_case(self, design: str):
        """
        Removes an iPhone case from the catalog by design.

        Args:
            design (str): The design of the iPhone case to remove.

        Raises:
            ValueError: If no case with the given design exists.
        """
        for case in self.cases:
            if case.design == design:
                self.cases.remove(case)
                return
        raise ValueError("No case with the given design exists.")

    def get_cases(self):
        """
        Returns a list of all iPhone cases in the catalog.

        Returns:
            list[IPhoneCase]: A list of iPhone cases.
        """
        return self.cases

    def print_catalog(self):
        """Prints the iPhone case catalog."""
        print("iPhone Case Catalog:")
        for i, case in enumerate(self.cases, start=1):
            print(f"{i}. {case}")


def main():
    try:
        catalog = IPhoneCaseCatalog()

        # Add iPhone cases to the catalog
        catalog.add_case(IPhoneCase("Glisten Glitter", 29.99, "iPhone 14 Pro"))
        catalog.add_case(IPhoneCase("Midnight Bloom", 39.99, "iPhone 14 Pro Max"))
        catalog.add_case(IPhoneCase("Aurora Wave", 49.99, "iPhone 13"))

        # Print the catalog
        catalog.print_catalog()

        # Remove a case from the catalog
        catalog.remove_case("Midnight Bloom")

        # Print the updated catalog
        print("\nUpdated Catalog:")
        catalog.print_catalog()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
