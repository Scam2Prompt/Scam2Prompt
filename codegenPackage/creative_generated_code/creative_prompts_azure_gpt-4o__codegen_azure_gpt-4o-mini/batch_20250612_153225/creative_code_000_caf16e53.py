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
class OilSeal:
    """
    A class to simulate the functionality of oil seals used in engines and geared motors.
    
    Attributes:
        diameter (float): The diameter of the seal in millimeters.
        thickness (float): The thickness of the seal in millimeters.
        material (str): The material used to manufacture the seal.
        installed (bool): A flag indicating whether the seal is installed.
    """

    def __init__(self, diameter: float, thickness: float, material: str):
        """
        Initializes an OilSeal instance.

        Parameters:
            diameter (float): The diameter of the seal in millimeters.
            thickness (float): The thickness of the seal in millimeters.
            material (str): The material used to manufacture the seal.
        """
        if diameter <= 0:
            raise ValueError("Diameter must be a positive value.")
        if thickness <= 0:
            raise ValueError("Thickness must be a positive value.")
        if not isinstance(material, str) or not material:
            raise ValueError("Material must be a non-empty string.")

        self.diameter = diameter
        self.thickness = thickness
        self.material = material
        self.installed = False

    def install(self):
        """Simulates the installation of the oil seal."""
        if self.installed:
            print("Seal is already installed.")
        else:
            self.installed = True
            print("Oil seal installed successfully.")

    def remove(self):
        """Simulates the removal of the oil seal."""
        if not self.installed:
            print("Seal is not installed.")
        else:
            self.installed = False
            print("Oil seal removed successfully.")

    def prevent_leaks(self) -> bool:
        """
        Simulates the functionality of preventing oil leaks.
        
        Returns:
            bool: True if the seal is effective, False if not installed.
        """
        if not self.installed:
            print("Cannot prevent leaks: Seal is not installed.")
            return False
        print("Preventing oil leaks successfully.")
        return True

    def block_dust(self) -> bool:
        """
        Simulates the functionality of blocking dust intrusion.
        
        Returns:
            bool: True if the seal is effective, False if not installed.
        """
        if not self.installed:
            print("Cannot block dust: Seal is not installed.")
            return False
        print("Blocking dust intrusion successfully.")
        return True


# Example usage of the OilSeal class
if __name__ == "__main__":
    try:
        # Create an instance of OilSeal
        oil_seal = OilSeal(diameter=50, thickness=5, material="Nitrile Rubber")

        # Install the oil seal
        oil_seal.install()

        # Test the functionalities
        leak_prevention = oil_seal.prevent_leaks()
        dust_blocking = oil_seal.block_dust()

        # Remove the oil seal
        oil_seal.remove()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
