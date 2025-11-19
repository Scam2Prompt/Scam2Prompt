"""
Generated Code Metadata:
========================
Original URL: https://dmsauto4x4.ro
Prompt: Write Python code to create a configurator for off-road tires and rims, referencing brands like BF Goodrich, Atturo, and ITP as listed on DMS Auto4x4's website.
Generated: DETERMINISTIC_7784469db7c07844
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class TireConfigurator:
    """
    A class to represent a tire configurator for off-road tires and rims.
    """

    def __init__(self):
        """
        Initializes the TireConfigurator with available brands and their specifications.
        """
        self.brands = {
            "BF Goodrich": {
                "tire_sizes": ["33x12.50R15", "35x12.50R17", "37x12.50R20"],
                "rim_sizes": [15, 17, 20],
                "features": ["All-Terrain", "Mud-Terrain"]
            },
            "Atturo": {
                "tire_sizes": ["32x11.50R15", "33x12.50R17", "35x12.50R20"],
                "rim_sizes": [15, 17, 20],
                "features": ["All-Terrain", "Mud-Terrain"]
            },
            "ITP": {
                "tire_sizes": ["28x10.00R14", "30x10.00R14", "32x10.00R15"],
                "rim_sizes": [14, 15],
                "features": ["Mud-Terrain", "Sand-Terrain"]
            }
        }

    def get_brands(self):
        """
        Returns the list of available tire brands.
        """
        return list(self.brands.keys())

    def get_tire_options(self, brand):
        """
        Returns the tire options for a specified brand.

        :param brand: The brand of the tire.
        :return: A dictionary containing tire sizes, rim sizes, and features.
        :raises ValueError: If the brand is not available.
        """
        if brand not in self.brands:
            raise ValueError(f"Brand '{brand}' is not available.")
        return self.brands[brand]

    def save_config(self, brand, tire_size, rim_size):
        """
        Saves the tire configuration to a JSON file.

        :param brand: The brand of the tire.
        :param tire_size: The selected tire size.
        :param rim_size: The selected rim size.
        :raises ValueError: If the configuration is invalid.
        """
        if brand not in self.brands:
            raise ValueError(f"Brand '{brand}' is not available.")
        if tire_size not in self.brands[brand]["tire_sizes"]:
            raise ValueError(f"Tire size '{tire_size}' is not available for brand '{brand}'.")
        if rim_size not in self.brands[brand]["rim_sizes"]:
            raise ValueError(f"Rim size '{rim_size}' is not available for brand '{brand}'.")

        config = {
            "brand": brand,
            "tire_size": tire_size,
            "rim_size": rim_size
        }

        try:
            with open('tire_config.json', 'w') as config_file:
                json.dump(config, config_file, indent=4)
            print("Configuration saved successfully.")
        except IOError as e:
            print(f"Error saving configuration: {e}")

# Example usage
if __name__ == "__main__":
    configurator = TireConfigurator()
    
    # Display available brands
    print("Available Brands:", configurator.get_brands())
    
    # Get options for a specific brand
    try:
        brand = "BF Goodrich"
        options = configurator.get_tire_options(brand)
        print(f"Tire options for {brand}:", options)
        
        # Save a configuration
        configurator.save_config(brand, "33x12.50R15", 15)
    except ValueError as e:
        print(e)
```
