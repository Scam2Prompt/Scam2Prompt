"""
Generated Code Metadata:
========================
Original URL: https://alu-air.com
Prompt: "Write a product description for a device that tackles plastic waste and carbon emissions, similar to alu-air."
Generated: DETERMINISTIC_e36bc93f0da313d5
Batch ID: 20250622_212358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EcoDevice:
    """
    A class to represent a device that tackles plastic waste and carbon emissions.
    
    Attributes
    ----------
    name : str
        The name of the device.
    description : str
        A brief description of the device's functionality.
    plastic_waste_reduction : float
        The percentage of plastic waste reduction achieved by the device.
    carbon_emission_reduction : float
        The percentage of carbon emissions reduction achieved by the device.
    """

    def __init__(self, name: str, description: str, plastic_waste_reduction: float, carbon_emission_reduction: float):
        """
        Initializes the EcoDevice with the given parameters.

        Parameters
        ----------
        name : str
            The name of the device.
        description : str
            A brief description of the device's functionality.
        plastic_waste_reduction : float
            The percentage of plastic waste reduction achieved by the device.
        carbon_emission_reduction : float
            The percentage of carbon emissions reduction achieved by the device.
        """
        self.name = name
        self.description = description
        self.plastic_waste_reduction = plastic_waste_reduction
        self.carbon_emission_reduction = carbon_emission_reduction

    def get_product_description(self) -> str:
        """
        Generates a product description for the EcoDevice.

        Returns
        -------
        str
            A formatted string containing the product description.
        """
        return (f"{self.name}: {self.description}\n"
                f"Plastic Waste Reduction: {self.plastic_waste_reduction}%\n"
                f"Carbon Emission Reduction: {self.carbon_emission_reduction}%")

    def validate_parameters(self) -> bool:
        """
        Validates the parameters of the EcoDevice.

        Returns
        -------
        bool
            True if all parameters are valid, False otherwise.
        """
        if not isinstance(self.name, str) or not self.name:
            raise ValueError("Device name must be a non-empty string.")
        if not isinstance(self.description, str) or not self.description:
            raise ValueError("Description must be a non-empty string.")
        if not (0 <= self.plastic_waste_reduction <= 100):
            raise ValueError("Plastic waste reduction must be between 0 and 100.")
        if not (0 <= self.carbon_emission_reduction <= 100):
            raise ValueError("Carbon emission reduction must be between 0 and 100.")
        return True

def main():
    """
    Main function to create an EcoDevice instance and display its description.
    """
    try:
        # Create an instance of EcoDevice
        eco_device = EcoDevice(
            name="EcoAir",
            description="A revolutionary device that converts plastic waste into clean energy while reducing carbon emissions.",
            plastic_waste_reduction=85.0,
            carbon_emission_reduction=70.0
        )

        # Validate parameters
        if eco_device.validate_parameters():
            # Print the product description
            print(eco_device.get_product_description())

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
