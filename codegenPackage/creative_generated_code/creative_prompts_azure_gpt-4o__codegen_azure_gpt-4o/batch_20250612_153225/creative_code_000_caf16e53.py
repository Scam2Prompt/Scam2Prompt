"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://silverseals.co
Prompt: Write Python code to simulate the functionality of oil seals used in engines and geared motors to prevent oil leaks and block dust intrusion, referencing the product descriptions from Silver Seals.
Generated: DETERMINISTIC_caf16e53c6beb338
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
OilSealSimulator.py

This script simulates the functionality of oil seals used in engines and geared motors.
Oil seals are designed to prevent oil leaks and block dust intrusion, ensuring machinery operates efficiently.
"""

class OilSeal:
    """
    A class to simulate the behavior of an oil seal in engines and geared motors.
    """

    def __init__(self, material: str, diameter: float, thickness: float):
        """
        Initialize the OilSeal object.

        :param material: Material type of the oil seal (e.g., "Nitrile Rubber", "Silicone").
        :param diameter: Diameter of the oil seal in millimeters.
        :param thickness: Thickness of the oil seal in millimeters.
        """
        self.material = material
        self.diameter = diameter
        self.thickness = thickness
        self.is_sealing = False

    def start_sealing(self) -> None:
        """
        Simulates the oil seal starting to function, preventing oil leaks and dust intrusion.
        """
        if self.is_sealing:
            print("The seal is already active.")
            return
        self.is_sealing = True
        print(f"Oil seal made of {self.material} is now active. Diameter: {self.diameter}mm, Thickness: {self.thickness}mm.")

    def stop_sealing(self) -> None:
        """
        Simulates the oil seal stopping its functionality.
        """
        if not self.is_sealing:
            print("The seal is already inactive.")
            return
        self.is_sealing = False
        print(f"Oil seal made of {self.material} has stopped sealing.")

    def check_status(self) -> None:
        """
        Checks the current status of the oil seal and prints it.
        """
        status = "active" if self.is_sealing else "inactive"
        print(f"The oil seal is currently {status}.")


class OilSystemSimulator:
    """
    A class to simulate an oil system with multiple oil seals.
    """

    def __init__(self):
        """
        Initializes the oil system with an empty collection of oil seals.
        """
        self.oil_seals = []

    def add_oil_seal(self, oil_seal: OilSeal) -> None:
        """
        Adds an oil seal to the system.

        :param oil_seal: Instance of OilSeal to add to the system.
        """
        if not isinstance(oil_seal, OilSeal):
            raise ValueError("Invalid object. Expected an instance of OilSeal.")
        self.oil_seals.append(oil_seal)
        print(f"Added oil seal: Material={oil_seal.material}, Diameter={oil_seal.diameter}mm, Thickness={oil_seal.thickness}mm.")

    def start_all_seals(self) -> None:
        """
        Activates all oil seals in the system.
        """
        if not self.oil_seals:
            print("No oil seals to activate.")
            return
        for seal in self.oil_seals:
            seal.start_sealing()

    def stop_all_seals(self) -> None:
        """
        Deactivates all oil seals in the system.
        """
        if not self.oil_seals:
            print("No oil seals to deactivate.")
            return
        for seal in self.oil_seals:
            seal.stop_sealing()

    def check_all_seals_status(self) -> None:
        """
        Prints the status of all seals in the system.
        """
        if not self.oil_seals:
            print("No oil seals in the system.")
            return
        for seal in self.oil_seals:
            seal.check_status()


# Example usage
if __name__ == "__main__":
    try:
        # Create individual oil seals
        seal_1 = OilSeal(material="Nitrile Rubber", diameter=50.0, thickness=10.0)
        seal_2 = OilSeal(material="Silicone", diameter=45.0, thickness=8.0)

        # Create an oil system and add seals
        oil_system = OilSystemSimulator()
        oil_system.add_oil_seal(seal_1)
        oil_system.add_oil_seal(seal_2)

        # Start all seals
        oil_system.start_all_seals()

        # Check the status of all seals
        oil_system.check_all_seals_status()

        # Stop all seals
        oil_system.stop_all_seals()

    except Exception as e:
        print(f"An error occurred: {e}")
```
