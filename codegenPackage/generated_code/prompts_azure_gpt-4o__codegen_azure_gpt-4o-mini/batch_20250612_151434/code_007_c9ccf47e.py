"""
Generated Code Metadata:
========================
Original URL: https://tromba-sa.com.ar
Prompt: Generate code for designing a turnkey fire protection system, referencing the E-PCI Sistemas contra Incendio Llave en Mano solution from the TROMBA website.
Generated: DETERMINISTIC_c9ccf47ed6ae7ab2
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FireProtectionSystem:
    """
    A class to represent a turnkey fire protection system.
    This system includes various components such as alarms, sprinklers, and control panels.
    """

    def __init__(self, system_id, location):
        """
        Initializes the fire protection system with a unique ID and location.

        :param system_id: Unique identifier for the fire protection system
        :param location: Location where the system is installed
        """
        self.system_id = system_id
        self.location = location
        self.components = []
        self.is_active = False

    def add_component(self, component):
        """
        Adds a component to the fire protection system.

        :param component: An instance of a fire protection component
        """
        if not isinstance(component, FireProtectionComponent):
            raise ValueError("Component must be an instance of FireProtectionComponent")
        self.components.append(component)

    def activate_system(self):
        """
        Activates the fire protection system.
        """
        if not self.components:
            raise RuntimeError("Cannot activate system: No components added.")
        self.is_active = True
        print(f"Fire protection system {self.system_id} activated at {self.location}.")

    def deactivate_system(self):
        """
        Deactivates the fire protection system.
        """
        self.is_active = False
        print(f"Fire protection system {self.system_id} deactivated.")

    def check_system_status(self):
        """
        Checks the status of the fire protection system and its components.

        :return: Status report of the system
        """
        status_report = {
            "system_id": self.system_id,
            "location": self.location,
            "is_active": self.is_active,
            "components": [component.get_status() for component in self.components]
        }
        return status_report


class FireProtectionComponent:
    """
    A class to represent a component of the fire protection system.
    """

    def __init__(self, name, component_type):
        """
        Initializes the fire protection component with a name and type.

        :param name: Name of the component
        :param component_type: Type of the component (e.g., 'Alarm', 'Sprinkler')
        """
        self.name = name
        self.component_type = component_type
        self.is_functional = True

    def get_status(self):
        """
        Returns the status of the component.

        :return: A dictionary containing the component's status
        """
        return {
            "name": self.name,
            "type": self.component_type,
            "is_functional": self.is_functional
        }

    def malfunction(self):
        """
        Simulates a malfunction of the component.
        """
        self.is_functional = False
        print(f"Component {self.name} has malfunctioned.")


# Example usage
if __name__ == "__main__":
    try:
        # Create a fire protection system
        fire_system = FireProtectionSystem(system_id="FPS-001", location="Main Building")

        # Add components to the system
        alarm = FireProtectionComponent(name="Main Alarm", component_type="Alarm")
        sprinkler = FireProtectionComponent(name="Sprinkler System", component_type="Sprinkler")

        fire_system.add_component(alarm)
        fire_system.add_component(sprinkler)

        # Activate the system
        fire_system.activate_system()

        # Check system status
        status = fire_system.check_system_status()
        print(status)

        # Simulate a malfunction
        alarm.malfunction()

        # Check system status again
        status = fire_system.check_system_status()
        print(status)

        # Deactivate the system
        fire_system.deactivate_system()

    except Exception as e:
        print(f"An error occurred: {e}")
```
