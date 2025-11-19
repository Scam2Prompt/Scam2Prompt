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
from enum import Enum
from typing import Optional

class SealType(Enum):
    """ Enum for different types of oil seals """
    RADIAL = 1
    FACE = 2
    ROD = 3

class OilSeal:
    """ Simulates the functionality of an oil seal """

    def __init__(self, seal_type: SealType, material: str, size: str):
        """
        Initializes an OilSeal object

        Args:
        - seal_type (SealType): The type of the seal
        - material (str): The material of the seal
        - size (str): The size of the seal
        """
        self.seal_type = seal_type
        self.material = material
        self.size = size
        self.is_installed = False
        self.is_leaking = False
        self.is_dust_intruded = False

    def install(self) -> None:
        """ Installs the oil seal """
        if not self.is_installed:
            self.is_installed = True
            print(f"Oil seal of type {self.seal_type.name} installed successfully.")
        else:
            print("Oil seal is already installed.")

    def simulate_leak(self) -> None:
        """ Simulates an oil leak """
        if self.is_installed and not self.is_leaking:
            self.is_leaking = True
            print(f"Oil leak detected in {self.seal_type.name} oil seal.")
        elif not self.is_installed:
            print("Oil seal is not installed.")
        else:
            print("Oil leak is already detected.")

    def simulate_dust_intrusion(self) -> None:
        """ Simulates dust intrusion """
        if self.is_installed and not self.is_dust_intruded:
            self.is_dust_intruded = True
            print(f"Dust intrusion detected in {self.seal_type.name} oil seal.")
        elif not self.is_installed:
            print("Oil seal is not installed.")
        else:
            print("Dust intrusion is already detected.")

    def replace(self) -> None:
        """ Replaces the oil seal """
        if self.is_installed:
            self.is_installed = False
            self.is_leaking = False
            self.is_dust_intruded = False
            print(f"Oil seal of type {self.seal_type.name} replaced successfully.")
        else:
            print("Oil seal is not installed.")

class Engine:
    """ Simulates an engine with oil seals """

    def __init__(self):
        self.oil_seals: list[OilSeal] = []

    def add_oil_seal(self, oil_seal: OilSeal) -> None:
        """ Adds an oil seal to the engine """
        self.oil_seals.append(oil_seal)

    def display_status(self) -> None:
        """ Displays the status of all oil seals in the engine """
        for i, oil_seal in enumerate(self.oil_seals):
            print(f"Oil Seal {i+1} Status:")
            print(f"Type: {oil_seal.seal_type.name}")
            print(f"Installed: {oil_seal.is_installed}")
            print(f"Leaking: {oil_seal.is_leaking}")
            print(f"Dust Intruded: {oil_seal.is_dust_intruded}")
            print("------------------------")

def main() -> None:
    try:
        engine = Engine()

        radial_seal = OilSeal(SealType.RADIAL, "Nitrile", "20mm")
        face_seal = OilSeal(SealType.FACE, "Silicone", "30mm")

        engine.add_oil_seal(radial_seal)
        engine.add_oil_seal(face_seal)

        radial_seal.install()
        face_seal.install()

        radial_seal.simulate_leak()
        face_seal.simulate_dust_intrusion()

        engine.display_status()

        radial_seal.replace()

        engine.display_status()

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
