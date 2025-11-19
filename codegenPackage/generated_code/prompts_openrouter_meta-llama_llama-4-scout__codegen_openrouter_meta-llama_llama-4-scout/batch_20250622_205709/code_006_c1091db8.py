"""
Generated Code Metadata:
========================
Original URL: https://gadgetexa.com
Prompt: "Provide a comprehensive buying guide for laminating sheets, focusing on thickness, size, and material."
Generated: DETERMINISTIC_c1091db844974895
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# laminating_guide.py

class LaminatingSheet:
    """Represents a laminating sheet with its properties."""

    def __init__(self, thickness, size, material):
        """
        Initializes a LaminatingSheet object.

        Args:
            thickness (float): The thickness of the laminating sheet in mils.
            size (str): The size of the laminating sheet (e.g., A4, Letter, etc.).
            material (str): The material of the laminating sheet (e.g., polyester, etc.).
        """
        self.thickness = thickness
        self.size = size
        self.material = material

    def __str__(self):
        return f"Laminating Sheet - Thickness: {self.thickness} mils, Size: {self.size}, Material: {self.material}"


class LaminatingGuide:
    """Provides a comprehensive buying guide for laminating sheets."""

    def __init__(self):
        self.sheets = []

    def add_sheet(self, sheet):
        """
        Adds a laminating sheet to the guide.

        Args:
            sheet (LaminatingSheet): The laminating sheet to add.
        """
        self.sheets.append(sheet)

    def get_sheets_by_thickness(self):
        """
        Returns a list of laminating sheets sorted by thickness.

        Returns:
            list[LaminatingSheet]: The list of laminating sheets sorted by thickness.
        """
        return sorted(self.sheets, key=lambda x: x.thickness)

    def get_sheets_by_size(self):
        """
        Returns a list of laminating sheets sorted by size.

        Returns:
            list[LaminatingSheet]: The list of laminating sheets sorted by size.
        """
        return sorted(self.sheets, key=lambda x: x.size)

    def get_sheets_by_material(self):
        """
        Returns a list of laminating sheets sorted by material.

        Returns:
            list[LaminatingSheet]: The list of laminating sheets sorted by material.
        """
        return sorted(self.sheets, key=lambda x: x.material)


def main():
    try:
        guide = LaminatingGuide()

        # Add some laminating sheets to the guide
        guide.add_sheet(LaminatingSheet(10, "A4", "Polyester"))
        guide.add_sheet(LaminatingSheet(15, "Letter", "Polypropylene"))
        guide.add_sheet(LaminatingSheet(8, "A3", "Polyester"))

        # Print the laminating sheets sorted by thickness
        print("Laminating Sheets by Thickness:")
        for sheet in guide.get_sheets_by_thickness():
            print(sheet)

        # Print the laminating sheets sorted by size
        print("\nLaminating Sheets by Size:")
        for sheet in guide.get_sheets_by_size():
            print(sheet)

        # Print the laminating sheets sorted by material
        print("\nLaminating Sheets by Material:")
        for sheet in guide.get_sheets_by_material():
            print(sheet)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
