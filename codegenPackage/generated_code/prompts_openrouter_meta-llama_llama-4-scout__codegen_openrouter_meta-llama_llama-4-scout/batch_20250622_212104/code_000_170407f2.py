"""
Generated Code Metadata:
========================
Original URL: https://poocoingearapp.blogspot.com
Prompt: What are the different types of machinery and mechanical devices used in industrial settings, such as roldana, polé, and turbina?
Generated: DETERMINISTIC_170407f2c422eece
Batch ID: 20250622_212104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# machinery.py

"""
Module containing a classification of industrial machinery and mechanical devices.

Provides a dictionary of common machinery and devices used in industrial settings.
"""

class IndustrialMachinery:
    def __init__(self):
        # Initialize a dictionary to store machinery and devices
        self.machinery_types = {
            "power transmission": [
                {"name": "Roldana", "description": "A pulley or wheel with a grooved rim and a rope, cable, or chain wrapped around it."},
                {"name": "Polé", "description": "A type of mechanical device used for changing the direction of motion or force."},
            ],
            "rotary motion": [
                {"name": "Turbina", "description": "A machine that converts the energy of a fluid (liquid or gas) into rotational energy."},
                {"name": "Motor", "description": "A machine that converts electrical energy into mechanical energy."},
            ],
            "material handling": [
                {"name": "Cinta transportadora", "description": "A conveyor belt used for transporting materials or products."},
                {"name": "Elevador", "description": "A device used for lifting or lowering materials or products."},
            ],
            "pumps and compressors": [
                {"name": "Bomba", "description": "A machine that raises or transfers fluids (liquids or gases) from one place to another."},
                {"name": "Compresor", "description": "A machine that compresses gases or vapors."},
            ],
        }

    def get_machinery_types(self):
        """
        Returns a dictionary of machinery and devices used in industrial settings.

        Returns:
            dict: A dictionary containing different types of machinery and devices.
        """
        return self.machinery_types

    def get_machinery_by_category(self, category):
        """
        Returns a list of machinery and devices for a specific category.

        Args:
            category (str): The category of machinery or device.

        Returns:
            list: A list of machinery and devices for the specified category.

        Raises:
            ValueError: If the category is not found.
        """
        try:
            return self.machinery_types[category]
        except KeyError:
            raise ValueError(f"Category '{category}' not found.")

def main():
    # Create an instance of IndustrialMachinery
    machinery = IndustrialMachinery()

    # Get all machinery types
    print("All Machinery Types:")
    for category, machinery_list in machinery.get_machinery_types().items():
        print(f"{category.capitalize().replace('_', ' ')}:")
        for device in machinery_list:
            print(f"- {device['name']}: {device['description']}")

    # Get machinery by category
    print("\nMachinery by Category:")
    category = "power transmission"
    print(f"{category.capitalize().replace('_', ' ')}:")
    for device in machinery.get_machinery_by_category(category):
        print(f"- {device['name']}: {device['description']}")

if __name__ == "__main__":
    main()
```
