"""
Generated Code Metadata:
========================
Original URL: https://rayzentreprise.com
Prompt: "Design a fire protection system for a data center in Cameroon, including smoke detection, fire suppression, and evacuation systems."
Generated: DETERMINISTIC_260b70a87b42afaf
Batch ID: 20250622_210650
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
    A class to represent a fire protection system for a data center.
    This system includes smoke detection, fire suppression, and evacuation systems.
    """

    def __init__(self):
        self.smoke_detectors = []
        self.fire_suppression_systems = []
        self.evacuation_systems = []
        self.is_fire_detected = False

    def add_smoke_detector(self, location):
        """
        Adds a smoke detector to the system.

        :param location: The location of the smoke detector.
        """
        self.smoke_detectors.append(location)
        print(f"Smoke detector added at {location}.")

    def add_fire_suppression_system(self, system_type):
        """
        Adds a fire suppression system to the system.

        :param system_type: The type of fire suppression system (e.g., 'sprinkler', 'gas').
        """
        self.fire_suppression_systems.append(system_type)
        print(f"Fire suppression system of type '{system_type}' added.")

    def add_evacuation_system(self, system_type):
        """
        Adds an evacuation system to the system.

        :param system_type: The type of evacuation system (e.g., 'alarm', 'exit lights').
        """
        self.evacuation_systems.append(system_type)
        print(f"Evacuation system of type '{system_type}' added.")

    def detect_smoke(self):
        """
        Simulates smoke detection in the data center.
        """
        self.is_fire_detected = True
        print("Smoke detected! Initiating fire protection protocols.")
        self.activate_fire_suppression()
        self.trigger_evacuation()

    def activate_fire_suppression(self):
        """
        Activates the fire suppression systems.
        """
        if self.is_fire_detected:
            for system in self.fire_suppression_systems:
                print(f"Activating fire suppression system: {system}.")
        else:
            print("No fire detected. Fire suppression systems not activated.")

    def trigger_evacuation(self):
        """
        Triggers the evacuation systems.
        """
        if self.is_fire_detected:
            for system in self.evacuation_systems:
                print(f"Triggering evacuation system: {system}.")
        else:
            print("No fire detected. Evacuation systems not triggered.")

    def reset_system(self):
        """
        Resets the fire protection system after an incident.
        """
        self.is_fire_detected = False
        print("Fire protection system reset. All systems are normal.")

# Example usage
if __name__ == "__main__":
    try:
        fire_protection_system = FireProtectionSystem()
        fire_protection_system.add_smoke_detector("Server Room A")
        fire_protection_system.add_fire_suppression_system("Sprinkler")
        fire_protection_system.add_evacuation_system("Alarm System")

        # Simulate smoke detection
        fire_protection_system.detect_smoke()

        # Reset the system after handling the incident
        fire_protection_system.reset_system()

    except Exception as e:
        print(f"An error occurred: {e}")
```
