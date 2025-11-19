"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: "Design a Caja China Junior with a galvanized steel grill and thermometer, including dimensions and materials used, as described on Meat Master."
Generated: DETERMINISTIC_9fab30e39d128a6f
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CajaChinaJunior:
    """
    A class to represent a Caja China Junior grill with specific dimensions and materials.
    """

    def __init__(self, width, depth, height, material, grill_material, thermometer):
        """
        Initializes the Caja China Junior with the given dimensions and materials.

        :param width: Width of the grill in inches
        :param depth: Depth of the grill in inches
        :param height: Height of the grill in inches
        :param material: Material of the grill body
        :param grill_material: Material of the grill
        :param thermometer: Type of thermometer used
        """
        self.width = width
        self.depth = depth
        self.height = height
        self.material = material
        self.grill_material = grill_material
        self.thermometer = thermometer

    def calculate_volume(self):
        """
        Calculates the volume of the grill in cubic inches.

        :return: Volume of the grill
        """
        return self.width * self.depth * self.height

    def display_specifications(self):
        """
        Displays the specifications of the Caja China Junior grill.
        """
        specs = (
            f"Caja China Junior Specifications:\n"
            f"Width: {self.width} inches\n"
            f"Depth: {self.depth} inches\n"
            f"Height: {self.height} inches\n"
            f"Material: {self.material}\n"
            f"Grill Material: {self.grill_material}\n"
            f"Thermometer: {self.thermometer}\n"
            f"Volume: {self.calculate_volume()} cubic inches"
        )
        print(specs)

def main():
    """
    Main function to create a Caja China Junior instance and display its specifications.
    """
    try:
        # Define dimensions and materials
        width = 48  # inches
        depth = 24  # inches
        height = 20  # inches
        material = "Galvanized Steel"
        grill_material = "Galvanized Steel"
        thermometer = "Digital Thermometer"

        # Create an instance of Caja China Junior
        caja_china_junior = CajaChinaJunior(width, depth, height, material, grill_material, thermometer)

        # Display the specifications
        caja_china_junior.display_specifications()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
