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

class TireConfigurator:
    """
    A class to configure off-road tires and rims with options from various brands.
    """
    
    def __init__(self):
        """
        Initializes the configurator with available brands and their options.
        """
        self.brands = {
            "BF Goodrich": {
                "tires": ["All-Terrain T/A KO2", "Mud-Terrain T/A KM3"],
                "rims": ["16x8 Steel", "17x9 Alloy"]
            },
            "Atturo": {
                "tires": ["Trail Blade MT", "A/T II"],
                "rims": ["15x8 Steel", "20x10 Alloy"]
            },
            "ITP": {
                "tires": ["Mud Lite", "Cryptid"],
                "rims": ["14x7 Aluminum", "12x6 Steel"]
            }
        }

    def get_brands(self):
        """
        Returns the list of available tire brands.
        """
        return list(self.brands.keys())

    def get_options(self, brand):
        """
        Returns the available tires and rims for the specified brand.
        
        Args:
            brand (str): The brand name to get options for.

        Returns:
            dict: A dictionary with tire and rim options for the brand.

        Raises:
            ValueError: If the brand is not available.
        """
        if brand not in self.brands:
            raise ValueError(f"Brand '{brand}' is not available.")
        return self.brands[brand]

    def configure_tires(self, brand, tire_model, rim_model):
        """
        Configures the tire and rim selection.

        Args:
            brand (str): The brand of the tires.
            tire_model (str): The model of the tire.
            rim_model (str): The model of the rim.

        Returns:
            dict: A configuration containing selected tire and rim.

        Raises:
            ValueError: If the tire model or rim model is not available for the brand.
        """
        options = self.get_options(brand)
        if tire_model not in options["tires"]:
            raise ValueError(f"Tire model '{tire_model}' is not available for brand '{brand}'.")
        if rim_model not in options["rims"]:
            raise ValueError(f"Rim model '{rim_model}' is not available for brand '{brand}'.")

        return {
            "brand": brand,
            "tire_model": tire_model,
            "rim_model": rim_model
        }

def main():
    """
    Main function to run the tire configurator.
    """
    configurator = TireConfigurator()
    
    try:
        print("Available Brands:", configurator.get_brands())
        brand = "BF Goodrich"
        options = configurator.get_options(brand)
        print(f"Options for {brand}:", options)

        # Example configuration
        tire_model = "All-Terrain T/A KO2"
        rim_model = "16x8 Steel"
        configuration = configurator.configure_tires(brand, tire_model, rim_model)
        print("Configuration Successful:", json.dumps(configuration, indent=4))
    
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
```
