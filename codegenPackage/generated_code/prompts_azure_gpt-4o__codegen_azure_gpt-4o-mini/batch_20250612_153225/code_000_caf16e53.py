"""
Generated Code Metadata:
========================
Original URL: https://silverseals.co
Prompt: Write Python code to simulate the functionality of oil seals used in engines and geared motors to prevent oil leaks and block dust intrusion, referencing the product descriptions from Silver Seals.
Generated: DETERMINISTIC_caf16e53c6beb338
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class OilSeal:
    """
    A class to simulate the functionality of oil seals used in engines and geared motors.
    
    Attributes:
        diameter (float): The outer diameter of the oil seal in millimeters.
        thickness (float): The thickness of the oil seal in millimeters.
        material (str): The material of the oil seal (e.g., rubber, silicone).
        is_installed (bool): Status of whether the oil seal is installed.
    """

    def __init__(self, diameter: float, thickness: float, material: str):
        """
        Initializes an OilSeal instance with specified dimensions and material.
        
        Args:
            diameter (float): The outer diameter of the oil seal.
            thickness (float): The thickness of the oil seal.
            material (str): The material of the oil seal.
        
        Raises:
            ValueError: If diameter or thickness is non-positive.
        """
        if diameter <= 0 or thickness <= 0:
            raise ValueError("Diameter and thickness must be positive values.")
        
        self.diameter = diameter
        self.thickness = thickness
        self.material = material
        self.is_installed = False

    def install(self):
        """Simulates the installation of the oil seal."""
        if self.is_installed:
            print("Oil seal is already installed.")
        else:
            self.is_installed = True
            print(f"Oil seal with diameter {self.diameter} mm and thickness {self.thickness} mm installed.")

    def remove(self):
        """Simulates the removal of the oil seal."""
        if not self.is_installed:
            print("Oil seal is not installed.")
        else:
            self.is_installed = False
            print("Oil seal removed.")

    def check_leakage(self) -> bool:
        """
        Checks for oil leakage based on the installation status.
        
        Returns:
            bool: True if there is a leak (not installed), False otherwise.
        """
        if not self.is_installed:
            print("Leak detected: Oil seal is not installed.")
            return True
        print("No leak detected: Oil seal is properly installed.")
        return False

    def __str__(self):
        """Returns a string representation of the oil seal."""
        return (f"OilSeal(diameter={self.diameter} mm, "
                f"thickness={self.thickness} mm, "
                f"material='{self.material}', "
                f"is_installed={self.is_installed})")


# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of OilSeal
        oil_seal = OilSeal(diameter=50.0, thickness=10.0, material="Nitrile Rubber")
        
        # Install the oil seal
        oil_seal.install()
        
        # Check for leakage
        oil_seal.check_leakage()
        
        # Remove the oil seal
        oil_seal.remove()
        
        # Check for leakage again
        oil_seal.check_leakage()
        
    except ValueError as e:
        print(f"Error: {e}")
```
