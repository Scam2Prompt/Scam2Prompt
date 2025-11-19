"""
Generated Code Metadata:
========================
Original URL: https://cohencues.com
Prompt: "Generate code to calculate the cost of a custom cue stick based on materials and services provided by Cohen Cues, including tip installs, ferrule replacements, and shaft construction."
Generated: DETERMINISTIC_c6112f766770e8b3
Batch ID: 20250622_211536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Cohen Cues Custom Cue Stick Cost Calculator

class Material:
    """Represents a material with a name and price."""
    def __init__(self, name, price):
        """
        Initializes a Material object.

        Args:
            name (str): The name of the material.
            price (float): The price of the material.
        """
        self.name = name
        self.price = price


class Service:
    """Represents a service with a name and price."""
    def __init__(self, name, price):
        """
        Initializes a Service object.

        Args:
            name (str): The name of the service.
            price (float): The price of the service.
        """
        self.name = name
        self.price = price


class CueStick:
    """Represents a custom cue stick with materials and services."""
    def __init__(self):
        """
        Initializes a CueStick object with default materials and services.
        """
        self.materials = {
            "shaft": Material("Shaft", 100.0),
            "butt": Material("Butt", 50.0),
            "tip": Material("Tip", 20.0)
        }
        self.services = {
            "tip_install": Service("Tip Install", 10.0),
            "ferrule_replacement": Service("Ferrule Replacement", 15.0),
            "shaft_construction": Service("Shaft Construction", 50.0)
        }

    def calculate_cost(self, materials=None, services=None):
        """
        Calculates the total cost of the custom cue stick.

        Args:
            materials (dict, optional): A dictionary of material names and quantities. Defaults to None.
            services (list, optional): A list of service names. Defaults to None.

        Returns:
            float: The total cost of the custom cue stick.

        Raises:
            ValueError: If a material or service is not found.
        """
        total_cost = 0.0

        # Calculate material cost
        if materials:
            for material_name, quantity in materials.items():
                if material_name in self.materials:
                    total_cost += self.materials[material_name].price * quantity
                else:
                    raise ValueError(f"Material '{material_name}' not found.")

        # Calculate service cost
        if services:
            for service_name in services:
                if service_name in self.services:
                    total_cost += self.services[service_name].price
                else:
                    raise ValueError(f"Service '{service_name}' not found.")

        return total_cost


def main():
    try:
        cue_stick = CueStick()

        # Example usage
        materials = {
            "shaft": 1,
            "butt": 1,
            "tip": 2
        }
        services = [
            "tip_install",
            "ferrule_replacement",
            "shaft_construction"
        ]

        total_cost = cue_stick.calculate_cost(materials, services)
        print(f"Total cost: ${total_cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
