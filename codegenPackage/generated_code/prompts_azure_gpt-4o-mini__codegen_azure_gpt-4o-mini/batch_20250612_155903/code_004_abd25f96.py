"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Create a guide for selecting the right Tube Cleaning Equipment from DBX Tools, focusing on the Electric Tube Cleaning Trolly and its operational parameters.
Generated: DETERMINISTIC_abd25f96a8351441
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TubeCleaningEquipment:
    """
    A class to represent Tube Cleaning Equipment from DBX Tools.
    """

    def __init__(self, model, power, weight, cleaning_speed, max_diameter):
        """
        Initializes the TubeCleaningEquipment with the given parameters.

        :param model: str - The model name of the equipment
        :param power: int - The power of the equipment in watts
        :param weight: float - The weight of the equipment in kilograms
        :param cleaning_speed: float - The cleaning speed in meters per minute
        :param max_diameter: float - The maximum tube diameter it can clean in millimeters
        """
        self.model = model
        self.power = power
        self.weight = weight
        self.cleaning_speed = cleaning_speed
        self.max_diameter = max_diameter

    def display_specifications(self):
        """
        Displays the specifications of the tube cleaning equipment.
        """
        specs = (
            f"Model: {self.model}\n"
            f"Power: {self.power} W\n"
            f"Weight: {self.weight} kg\n"
            f"Cleaning Speed: {self.cleaning_speed} m/min\n"
            f"Max Tube Diameter: {self.max_diameter} mm\n"
        )
        print(specs)

    def is_suitable_for_application(self, tube_diameter):
        """
        Checks if the equipment is suitable for the given tube diameter.

        :param tube_diameter: float - The diameter of the tube to be cleaned in millimeters
        :return: bool - True if suitable, False otherwise
        """
        if tube_diameter <= 0:
            raise ValueError("Tube diameter must be a positive value.")
        return tube_diameter <= self.max_diameter


def main():
    """
    Main function to demonstrate the usage of TubeCleaningEquipment class.
    """
    try:
        # Create an instance of Electric Tube Cleaning Trolley
        electric_trolley = TubeCleaningEquipment(
            model="DBX Electric Tube Cleaning Trolley",
            power=1500,  # in watts
            weight=50.0,  # in kilograms
            cleaning_speed=20.0,  # in meters per minute
            max_diameter=100.0  # in millimeters
        )

        # Display the specifications of the equipment
        electric_trolley.display_specifications()

        # Check if the equipment is suitable for a specific tube diameter
        tube_diameter = 90.0  # in millimeters
        if electric_trolley.is_suitable_for_application(tube_diameter):
            print(f"The equipment is suitable for cleaning a tube with diameter {tube_diameter} mm.")
        else:
            print(f"The equipment is NOT suitable for cleaning a tube with diameter {tube_diameter} mm.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
