"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethevent.org
Prompt: Generate a step-by-step guide for designing and upgrading an e-bike, referencing the "Design Your Own E-Bike Upgrade" project on Instructables.
Generated: DETERMINISTIC_00b2a3df0fbc0e57
Batch ID: 20250612_153713
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EBikeUpgrade:
    """
    A class to represent an e-bike upgrade process.
    
    Attributes
    ----------
    bike_model : str
        The model of the e-bike to be upgraded.
    components : dict
        A dictionary to hold components and their specifications.
    """

    def __init__(self, bike_model):
        """
        Initializes the E-Bike Upgrade with a specific bike model.
        
        Parameters
        ----------
        bike_model : str
            The model of the e-bike for upgrading.
        """
        self.bike_model = bike_model
        self.components = {}

    def add_component(self, name, spec):
        """
        Adds a component to the e-bike upgrade.

        Parameters
        ----------
        name : str
            The name of the component (e.g., battery, motor).
        spec : str
            The specifications or details of the component.
        
        Raises
        ------
        ValueError
            If the component name or specification is invalid.
        """
        if not name or not spec:
            raise ValueError("Component name and specification cannot be empty.")
        self.components[name] = spec

    def upgrade_bike(self):
        """
        Upgrades the e-bike with the added components.
        
        Raises
        ------
        RuntimeError
            If no components have been added for upgrading.
        """
        if not self.components:
            raise RuntimeError("No components added for the upgrade.")
        
        print(f"Upgrading {self.bike_model} with the following components:")
        for name, spec in self.components.items():
            print(f"- {name}: {spec}")
        
        print("Upgrade completed successfully.")

# Example usage of the EBikeUpgrade class
if __name__ == "__main__":
    try:
        # Initialize the e-bike upgrade process for a specific bike model
        my_ebike_upgrade = EBikeUpgrade("Mountain Bike X")

        # Adding various components for the upgrade
        my_ebike_upgrade.add_component("Battery", "48V 14Ah Lithium-ion")
        my_ebike_upgrade.add_component("Motor", "750W Brushless Motor")
        my_ebike_upgrade.add_component("Controller", "25A Smart Controller")

        # Perform the upgrade
        my_ebike_upgrade.upgrade_bike()

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except RuntimeError as re:
        print(f"RuntimeError: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
