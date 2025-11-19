"""
Generated Code Metadata:
========================
Original URL: https://shelterder.com
Prompt: Design an outdoor gas fireplace using Shelter's Gas Collection, including safety features and installation requirements.
Generated: DETERMINISTIC_7622483381918b9c
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Outdoor Gas Fireplace Design using Shelter's Gas Collection

class OutdoorGasFireplace:
    def __init__(self, model_number, gas_type, btu_rating, installation_type):
        """
        Initialize the Outdoor Gas Fireplace object.

        Args:
            model_number (str): The model number of the fireplace.
            gas_type (str): The type of gas used (e.g., natural gas, propane).
            btu_rating (int): The BTU rating of the fireplace.
            installation_type (str): The type of installation (e.g., wall-mounted, freestanding).
        """
        self.model_number = model_number
        self.gas_type = gas_type
        self.btu_rating = btu_rating
        self.installation_type = installation_type
        self.safety_features = []

    def add_safety_feature(self, feature):
        """
        Add a safety feature to the fireplace.

        Args:
            feature (str): The safety feature to add (e.g., oxygen depletion sensor, tip-over switch).
        """
        self.safety_features.append(feature)

    def validate_installation(self):
        """
        Validate the installation requirements for the fireplace.

        Raises:
            ValueError: If the installation type is not valid.
        """
        valid_installation_types = ["wall-mounted", "freestanding", "built-in"]
        if self.installation_type not in valid_installation_types:
            raise ValueError("Invalid installation type")

    def check_gas_compatibility(self):
        """
        Check if the gas type is compatible with the fireplace.

        Raises:
            ValueError: If the gas type is not compatible.
        """
        compatible_gas_types = ["natural gas", "propane"]
        if self.gas_type not in compatible_gas_types:
            raise ValueError("Incompatible gas type")

    def display_fireplace_info(self):
        """
        Display the fireplace information, including safety features and installation requirements.
        """
        print(f"Model Number: {self.model_number}")
        print(f"Gas Type: {self.gas_type}")
        print(f"BTU Rating: {self.btu_rating}")
        print(f"Installation Type: {self.installation_type}")
        print("Safety Features:")
        for feature in self.safety_features:
            print(f"- {feature}")


class ShelterGasCollection:
    def __init__(self):
        """
        Initialize the Shelter Gas Collection object.
        """
        self.fireplaces = []

    def add_fireplace(self, fireplace):
        """
        Add a fireplace to the gas collection.

        Args:
            fireplace (OutdoorGasFireplace): The fireplace to add.
        """
        self.fireplaces.append(fireplace)

    def display_gas_collection(self):
        """
        Display all fireplaces in the gas collection.
        """
        for fireplace in self.fireplaces:
            fireplace.display_fireplace_info()
            print()


def main():
    try:
        # Create a Shelter Gas Collection object
        gas_collection = ShelterGasCollection()

        # Create an outdoor gas fireplace object
        fireplace = OutdoorGasFireplace(
            model_number="OGF-1234",
            gas_type="natural gas",
            btu_rating=40000,
            installation_type="freestanding"
        )

        # Add safety features
        fireplace.add_safety_feature("Oxygen Depletion Sensor")
        fireplace.add_safety_feature("Tip-over Switch")

        # Validate installation and gas compatibility
        fireplace.validate_installation()
        fireplace.check_gas_compatibility()

        # Add fireplace to gas collection
        gas_collection.add_fireplace(fireplace)

        # Display gas collection
        gas_collection.display_gas_collection()

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
