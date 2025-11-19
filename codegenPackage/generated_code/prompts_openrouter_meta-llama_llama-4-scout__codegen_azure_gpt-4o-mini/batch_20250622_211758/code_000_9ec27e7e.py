"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: "Design a rubber flooring system for a jogging track in Indonesia using Eva Mats and Rubber Tiles."
Generated: DETERMINISTIC_9ec27e7e90e5ce92
Batch ID: 20250622_211758
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FlooringMaterial:
    """
    A class to represent a flooring material.
    """

    def __init__(self, name, thickness, durability, cost_per_square_meter):
        """
        Initializes the flooring material with its properties.

        :param name: Name of the flooring material
        :param thickness: Thickness of the material in cm
        :param durability: Durability rating (1-10)
        :param cost_per_square_meter: Cost per square meter in local currency
        """
        self.name = name
        self.thickness = thickness
        self.durability = durability
        self.cost_per_square_meter = cost_per_square_meter

    def __str__(self):
        return f"{self.name} (Thickness: {self.thickness} cm, Durability: {self.durability}/10, Cost: {self.cost_per_square_meter} per m²)"


class JoggingTrack:
    """
    A class to represent a jogging track.
    """

    def __init__(self, length, width):
        """
        Initializes the jogging track with its dimensions.

        :param length: Length of the track in meters
        :param width: Width of the track in meters
        """
        self.length = length
        self.width = width
        self.materials = []

    def add_material(self, material):
        """
        Adds a flooring material to the jogging track.

        :param material: An instance of FlooringMaterial
        """
        if not isinstance(material, FlooringMaterial):
            raise ValueError("Material must be an instance of FlooringMaterial")
        self.materials.append(material)

    def calculate_total_cost(self):
        """
        Calculates the total cost of the flooring materials for the track.

        :return: Total cost in local currency
        """
        total_area = self.length * self.width  # Area in square meters
        total_cost = sum(material.cost_per_square_meter * total_area for material in self.materials)
        return total_cost

    def __str__(self):
        materials_str = ', '.join(str(material) for material in self.materials)
        return f"Jogging Track (Length: {self.length} m, Width: {self.width} m, Materials: [{materials_str}])"


def main():
    """
    Main function to create a jogging track and add flooring materials.
    """
    try:
        # Create flooring materials
        eva_mats = FlooringMaterial("Eva Mats", thickness=1.5, durability=8, cost_per_square_meter=150)
        rubber_tiles = FlooringMaterial("Rubber Tiles", thickness=2.0, durability=9, cost_per_square_meter=200)

        # Create a jogging track
        jogging_track = JoggingTrack(length=400, width=5)

        # Add materials to the track
        jogging_track.add_material(eva_mats)
        jogging_track.add_material(rubber_tiles)

        # Calculate and print the total cost
        total_cost = jogging_track.calculate_total_cost()
        print(f"Total cost for flooring the jogging track: {total_cost} local currency")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
