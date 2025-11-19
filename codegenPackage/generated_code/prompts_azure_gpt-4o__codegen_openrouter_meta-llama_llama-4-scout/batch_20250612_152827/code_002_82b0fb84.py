"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: Create a script to calculate the cost of a custom packaging box based on variables like quantity, dimensions, material type, and additional processing (e.g., UV coating, embossing), as outlined by Metis.
Generated: DETERMINISTIC_82b0fb841f6f5af4
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# custom_packaging_box_calculator.py

class Material:
    """Represents a material with its cost per unit area."""

    def __init__(self, name, cost_per_unit_area):
        """
        Initializes a Material instance.

        Args:
            name (str): The name of the material.
            cost_per_unit_area (float): The cost per unit area of the material.
        """
        self.name = name
        self.cost_per_unit_area = cost_per_unit_area


class PackagingBox:
    """Represents a custom packaging box."""

    def __init__(self, length, width, height, material, quantity=1):
        """
        Initializes a PackagingBox instance.

        Args:
            length (float): The length of the box.
            width (float): The width of the box.
            height (float): The height of the box.
            material (Material): The material of the box.
            quantity (int, optional): The quantity of boxes. Defaults to 1.
        """
        self.length = length
        self.width = width
        self.height = height
        self.material = material
        self.quantity = quantity
        self.additional_processing = []

    def add_additional_processing(self, processing, cost):
        """
        Adds additional processing to the box.

        Args:
            processing (str): The name of the processing.
            cost (float): The cost of the processing.
        """
        self.additional_processing.append((processing, cost))

    def calculate_surface_area(self):
        """
        Calculates the surface area of the box.

        Returns:
            float: The surface area of the box.
        """
        # Calculate the surface area of the box
        surface_area = 2 * (
            self.length * self.width + self.width * self.height + self.height * self.length
        )
        return surface_area

    def calculate_material_cost(self):
        """
        Calculates the material cost of the box.

        Returns:
            float: The material cost of the box.
        """
        surface_area = self.calculate_surface_area()
        material_cost = surface_area * self.material.cost_per_unit_area * self.quantity
        return material_cost

    def calculate_additional_processing_cost(self):
        """
        Calculates the additional processing cost of the box.

        Returns:
            float: The additional processing cost of the box.
        """
        additional_processing_cost = sum(
            cost * self.quantity for _, cost in self.additional_processing
        )
        return additional_processing_cost

    def calculate_total_cost(self):
        """
        Calculates the total cost of the box.

        Returns:
            float: The total cost of the box.
        """
        material_cost = self.calculate_material_cost()
        additional_processing_cost = self.calculate_additional_processing_cost()
        total_cost = material_cost + additional_processing_cost
        return total_cost


def main():
    try:
        # Define materials
        materials = {
            "paper": Material("paper", 0.05),
            "cardboard": Material("cardboard", 0.10),
            "plastic": Material("plastic", 0.20),
        }

        # Get user input
        length = float(input("Enter the length of the box: "))
        width = float(input("Enter the width of the box: "))
        height = float(input("Enter the height of the box: "))
        material_name = input("Enter the material type (paper, cardboard, plastic): ")
        quantity = int(input("Enter the quantity of boxes: "))

        # Validate material type
        if material_name not in materials:
            raise ValueError("Invalid material type")

        # Create a PackagingBox instance
        material = materials[material_name]
        box = PackagingBox(length, width, height, material, quantity)

        # Add additional processing
        while True:
            processing = input("Enter additional processing (e.g., UV coating, embossing), or 'done' to finish: ")
            if processing.lower() == "done":
                break
            cost = float(input("Enter the cost of the processing: "))
            box.add_additional_processing(processing, cost)

        # Calculate and display the total cost
        total_cost = box.calculate_total_cost()
        print(f"Total cost: ${total_cost:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
