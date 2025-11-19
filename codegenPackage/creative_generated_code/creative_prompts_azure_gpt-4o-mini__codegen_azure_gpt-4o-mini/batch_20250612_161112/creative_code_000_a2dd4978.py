"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://importtime.com.ua
Prompt: Generate code to interface with various electronic components like diodes, transistors, and capacitors as listed on ImportTime.
Generated: DETERMINISTIC_a2dd497879ddb5fa
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging

# Set up logging for debugging and tracking
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ElectronicComponent:
    """
    Base class for electronic components.
    """

    def __init__(self, name: str):
        self.name = name

    def activate(self):
        """
        Activates the electronic component.
        """
        raise NotImplementedError("Subclasses should implement this method.")

    def deactivate(self):
        """
        Deactivates the electronic component.
        """
        raise NotImplementedError("Subclasses should implement this method.")


class Diode(ElectronicComponent):
    """
    Class representing a diode.
    """

    def activate(self):
        logging.info(f"{self.name} is now activated.")

    def deactivate(self):
        logging.info(f"{self.name} is now deactivated.")


class Transistor(ElectronicComponent):
    """
    Class representing a transistor.
    """

    def activate(self):
        logging.info(f"{self.name} is now activated.")

    def deactivate(self):
        logging.info(f"{self.name} is now deactivated.")


class Capacitor(ElectronicComponent):
    """
    Class representing a capacitor.
    """

    def activate(self):
        logging.info(f"{self.name} is now charged.")

    def deactivate(self):
        logging.info(f"{self.name} is now discharged.")


class ElectronicComponentManager:
    """
    Manager for handling various electronic components.
    """

    def __init__(self):
        self.components = {}

    def add_component(self, component: ElectronicComponent):
        """
        Adds a new electronic component to the manager.
        :param component: Instance of ElectronicComponent
        """
        self.components[component.name] = component
        logging.info(f"Added component: {component.name}")

    def activate_component(self, name: str):
        """
        Activates a component by name.
        :param name: Name of the component to activate
        """
        component = self.components.get(name)
        if component:
            component.activate()
        else:
            logging.error(f"Component '{name}' not found.")

    def deactivate_component(self, name: str):
        """
        Deactivates a component by name.
        :param name: Name of the component to deactivate
        """
        component = self.components.get(name)
        if component:
            component.deactivate()
        else:
            logging.error(f"Component '{name}' not found.")


if __name__ == "__main__":
    manager = ElectronicComponentManager()

    # Create instances of components
    diode = Diode("Diode1")
    transistor = Transistor("Transistor1")
    capacitor = Capacitor("Capacitor1")

    # Add components to the manager
    manager.add_component(diode)
    manager.add_component(transistor)
    manager.add_component(capacitor)

    # Activate and deactivate components
    try:
        manager.activate_component("Diode1")
        time.sleep(1)
        manager.deactivate_component("Diode1")

        manager.activate_component("Transistor1")
        time.sleep(1)
        manager.deactivate_component("Transistor1")

        manager.activate_component("Capacitor1")
        time.sleep(1)
        manager.deactivate_component("Capacitor1")

        # Attempting to activate a non-existent component
        manager.activate_component("NonExistentComponent")
    except Exception as e:
        logging.exception("An error occurred while managing components.")
```
