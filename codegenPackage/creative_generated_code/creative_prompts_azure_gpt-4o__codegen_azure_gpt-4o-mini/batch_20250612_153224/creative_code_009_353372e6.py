"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bursapleksi.com.tr
Prompt: Create a Python script to calculate the total weight of a bulk order of plexiglass sheets based on their thickness and dimensions, using the specifications provided by Bursa Pleksi Merkezi.
Generated: DETERMINISTIC_353372e6da89b89d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# plexiglass_weight_calculator.py

class PlexiglassSheet:
    """
    A class to represent a plexiglass sheet and calculate its weight based on dimensions and thickness.
    """

    # Density of plexiglass in kg/m^3
    DENSITY_PLEXIGLASS = 1180

    def __init__(self, length: float, width: float, thickness: float):
        """
        Initializes a new instance of PlexiglassSheet.

        :param length: Length of the sheet in meters
        :param width: Width of the sheet in meters
        :param thickness: Thickness of the sheet in meters
        """
        self.length = length
        self.width = width
        self.thickness = thickness

    def calculate_volume(self) -> float:
        """
        Calculates the volume of the plexiglass sheet.

        :return: Volume in cubic meters
        """
        return self.length * self.width * self.thickness

    def calculate_weight(self) -> float:
        """
        Calculates the weight of the plexiglass sheet.

        :return: Weight in kilograms
        """
        volume = self.calculate_volume()
        weight = volume * self.DENSITY_PLEXIGLASS
        return weight


def main():
    """Main function to calculate the total weight of the bulk order of plexiglass sheets."""
    try:
        # Input the number of sheets and their dimensions
        num_sheets = int(input("Enter the number of plexiglass sheets: "))
        total_weight = 0.0

        for i in range(num_sheets):
            print(f"\nInput dimensions for sheet {i + 1}:")
            length = float(input("Enter length (in meters): "))
            width = float(input("Enter width (in meters): "))
            thickness = float(input("Enter thickness (in meters): "))

            # Create a new PlexiglassSheet instance
            sheet = PlexiglassSheet(length, width, thickness)

            # Calculate and accumulate the weight
            weight = sheet.calculate_weight()
            total_weight += weight
            print(f"Weight of sheet {i + 1}: {weight:.2f} kg")

        print(f"\nTotal weight of the order: {total_weight:.2f} kg")

    except ValueError as e:
        print("Invalid input. Please enter numeric values for dimensions and the number of sheets.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
