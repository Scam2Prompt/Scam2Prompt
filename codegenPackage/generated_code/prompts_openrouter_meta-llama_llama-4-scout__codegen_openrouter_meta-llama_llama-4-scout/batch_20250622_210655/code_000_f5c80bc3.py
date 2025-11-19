"""
Generated Code Metadata:
========================
Original URL: https://superdar.com
Prompt: Design a rectangular, extendable dining table made of solid wood with a modern design, similar to the "Алана" table.
Generated: DETERMINISTIC_f5c80bc3e2491332
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Define a class for the dining table
class DiningTable:
    def __init__(self, length=180, width=90, material="solid wood", design="modern"):
        """
        Initialize the dining table with default dimensions and material.

        Args:
            length (int): The length of the table in cm. Defaults to 180.
            width (int): The width of the table in cm. Defaults to 90.
            material (str): The material of the table. Defaults to "solid wood".
            design (str): The design style of the table. Defaults to "modern".
        """
        self.length = length
        self.width = width
        self.material = material
        self.design = design
        self.extensions = []

    # Method to add an extension to the table
    def add_extension(self, length):
        """
        Add an extension to the table.

        Args:
            length (int): The length of the extension in cm.

        Raises:
            ValueError: If the extension length is not positive.
        """
        if length <= 0:
            raise ValueError("Extension length must be positive.")
        self.extensions.append(length)

    # Method to calculate the total length of the table
    def calculate_total_length(self):
        """
        Calculate the total length of the table including all extensions.

        Returns:
            int: The total length of the table in cm.
        """
        total_length = self.length
        for extension in self.extensions:
            total_length += extension
        return total_length

    # Method to describe the table
    def describe_table(self):
        """
        Print a description of the table.

        Returns:
            str: A description of the table.
        """
        description = f"This dining table is made of {self.material} with a {self.design} design.\n"
        description += f"Default dimensions: {self.length}cm x {self.width}cm\n"
        if self.extensions:
            description += f"Extensions: {', '.join(str(extension) + 'cm' for extension in self.extensions)}\n"
            description += f"Total length: {self.calculate_total_length()}cm"
        else:
            description += f"Total length: {self.length}cm"
        return description


# Example usage
if __name__ == "__main__":
    try:
        table = DiningTable()
        print(table.describe_table())

        table.add_extension(50)
        table.add_extension(30)
        print("\nAfter adding extensions:")
        print(table.describe_table())

    except Exception as e:
        print(f"An error occurred: {e}")
```
