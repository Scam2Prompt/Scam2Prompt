"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dmsauto4x4.ro
Prompt: Write Python code to create a configurator for off-road tires and rims, referencing brands like BF Goodrich, Atturo, and ITP as listed on DMS Auto4x4's website.
Generated: DETERMINISTIC_7784469db7c07844
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a class to manage the configurator for off-road tires and rims
class OffRoadConfigurator:
    def __init__(self):
        """
        Initialize the configurator with predefined brands and their products.
        This data simulates what might be retrieved from DMS Auto4x4's website.
        """
        self.brands = {
            "BF Goodrich": {
                "tires": ["Mud-Terrain T/A KM3", "All-Terrain T/A KO2", "Trail-Terrain T/A"],
                "rims": ["Black Rhino", "Fuel Off-Road"]
            },
            "Atturo": {
                "tires": ["Trail Blade M/T", "Trail Blade A/T", "Trail Blade X/T"],
                "rims": ["Moto Metal", "Pro Comp"]
            },
            "ITP": {
                "tires": ["Mud Lite II", "Blackwater Evolution", "Trail Wolf"],
                "rims": ["SS Alloy", "Delta Steel"]
            }
        }

    def list_brands(self):
        """
        List all available brands.
        Returns:
            list: A list of available brands.
        """
        return list(self.brands.keys())

    def list_products_by_brand(self, brand):
        """
        List all products (tires and rims) for a given brand.
        Args:
            brand (str): The brand name.
        Returns:
            dict: A dictionary containing available tires and rims for the brand.
        """
        try:
            if brand not in self.brands:
                raise ValueError(f"Brand '{brand}' not found.")
            return self.brands[brand]
        except ValueError as e:
            print(f"Error: {e}")
            return {}

    def configure(self, brand, tire, rim):
        """
        Configure an off-road setup with the chosen tire and rim for a specific brand.
        Args:
            brand (str): The brand name.
            tire (str): The chosen tire model.
            rim (str): The chosen rim model.
        Returns:
            dict: The configuration details.
        """
        try:
            if brand not in self.brands:
                raise ValueError(f"Brand '{brand}' not found.")
            if tire not in self.brands[brand]["tires"]:
                raise ValueError(f"Tire '{tire}' not available for brand '{brand}'.")
            if rim not in self.brands[brand]["rims"]:
                raise ValueError(f"Rim '{rim}' not available for brand '{brand}'.")
            
            configuration = {
                "brand": brand,
                "tire": tire,
                "rim": rim
            }
            return configuration
        except ValueError as e:
            print(f"Error: {e}")
            return {}

    def save_configuration(self, configuration, file_path="configuration.json"):
        """
        Save the configuration to a JSON file.
        Args:
            configuration (dict): The configuration details.
            file_path (str): The path to save the configuration file.
        Returns:
            bool: True if saved successfully, False otherwise.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump(configuration, file, indent=4)
            print(f"Configuration saved to {file_path}.")
            return True
        except Exception as e:
            print(f"Error saving configuration: {e}")
            return False


# Example usage of the OffRoadConfigurator class
if __name__ == "__main__":
    configurator = OffRoadConfigurator()

    # Display available brands
    print("Available Brands:")
    for brand in configurator.list_brands():
        print(f"- {brand}")

    # Choose a brand and list its products
    selected_brand = "BF Goodrich"
    print(f"\nProducts for {selected_brand}:")
    products = configurator.list_products_by_brand(selected_brand)
    print(json.dumps(products, indent=4))  # Display products in a structured format

    # Configure a setup
    selected_tire = "Mud-Terrain T/A KM3"
    selected_rim = "Black Rhino"
    setup = configurator.configure(selected_brand, selected_tire, selected_rim)

    if setup:
        print("\nConfiguration Details:")
        print(json.dumps(setup, indent=4))

        # Save the configuration to a file
        configurator.save_configuration(setup)
```
