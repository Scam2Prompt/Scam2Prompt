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
# rubber_flooring_system.py

class RubberFlooringSystem:
    """
    A class representing a rubber flooring system for a jogging track.

    Attributes:
        track_length (float): The length of the jogging track in meters.
        track_width (float): The width of the jogging track in meters.
        eva_mat_thickness (float): The thickness of the Eva Mats in mm.
        rubber_tile_thickness (float): The thickness of the Rubber Tiles in mm.
        eva_mat_price (float): The price of the Eva Mats per square meter.
        rubber_tile_price (float): The price of the Rubber Tiles per square meter.
    """

    def __init__(self, track_length, track_width, eva_mat_thickness, rubber_tile_thickness, eva_mat_price, rubber_tile_price):
        """
        Initializes a RubberFlooringSystem object.

        Args:
            track_length (float): The length of the jogging track in meters.
            track_width (float): The width of the jogging track in meters.
            eva_mat_thickness (float): The thickness of the Eva Mats in mm.
            rubber_tile_thickness (float): The thickness of the Rubber Tiles in mm.
            eva_mat_price (float): The price of the Eva Mats per square meter.
            rubber_tile_price (float): The price of the Rubber Tiles per square meter.
        """
        self.track_length = track_length
        self.track_width = track_width
        self.eva_mat_thickness = eva_mat_thickness
        self.rubber_tile_thickness = rubber_tile_thickness
        self.eva_mat_price = eva_mat_price
        self.rubber_tile_price = rubber_tile_price

    def calculate_track_area(self):
        """
        Calculates the area of the jogging track.

        Returns:
            float: The area of the jogging track in square meters.
        """
        return self.track_length * self.track_width

    def calculate_eva_mat_quantity(self):
        """
        Calculates the quantity of Eva Mats needed.

        Returns:
            float: The quantity of Eva Mats needed in square meters.
        """
        return self.calculate_track_area()

    def calculate_rubber_tile_quantity(self):
        """
        Calculates the quantity of Rubber Tiles needed.

        Returns:
            float: The quantity of Rubber Tiles needed in square meters.
        """
        return self.calculate_track_area()

    def calculate_eva_mat_cost(self):
        """
        Calculates the cost of the Eva Mats.

        Returns:
            float: The cost of the Eva Mats.
        """
        return self.calculate_eva_mat_quantity() * self.eva_mat_price

    def calculate_rubber_tile_cost(self):
        """
        Calculates the cost of the Rubber Tiles.

        Returns:
            float: The cost of the Rubber Tiles.
        """
        return self.calculate_rubber_tile_quantity() * self.rubber_tile_price

    def generate_flooring_plan(self):
        """
        Generates a flooring plan for the jogging track.

        Returns:
            dict: A dictionary containing the flooring plan details.
        """
        try:
            track_area = self.calculate_track_area()
            eva_mat_quantity = self.calculate_eva_mat_quantity()
            rubber_tile_quantity = self.calculate_rubber_tile_quantity()
            eva_mat_cost = self.calculate_eva_mat_cost()
            rubber_tile_cost = self.calculate_rubber_tile_cost()

            flooring_plan = {
                "Track Area": f"{track_area:.2f} sqm",
                "Eva Mat Quantity": f"{eva_mat_quantity:.2f} sqm",
                "Eva Mat Thickness": f"{self.eva_mat_thickness} mm",
                "Eva Mat Cost": f"IDR {eva_mat_cost:.2f}",
                "Rubber Tile Quantity": f"{rubber_tile_quantity:.2f} sqm",
                "Rubber Tile Thickness": f"{self.rubber_tile_thickness} mm",
                "Rubber Tile Cost": f"IDR {rubber_tile_cost:.2f}",
                "Total Cost": f"IDR {eva_mat_cost + rubber_tile_cost:.2f}",
            }

            return flooring_plan

        except Exception as e:
            print(f"An error occurred: {e}")
            return None


def main():
    # Example usage
    track_length = 400  # meters
    track_width = 5  # meters
    eva_mat_thickness = 10  # mm
    rubber_tile_thickness = 15  # mm
    eva_mat_price = 150000  # IDR per sqm
    rubber_tile_price = 250000  # IDR per sqm

    flooring_system = RubberFlooringSystem(track_length, track_width, eva_mat_thickness, rubber_tile_thickness, eva_mat_price, rubber_tile_price)
    flooring_plan = flooring_system.generate_flooring_plan()

    if flooring_plan:
        print("Flooring Plan:")
        for key, value in flooring_plan.items():
            print(f"{key}: {value}")


if __name__ == "__main__":
    main()
```
