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
# fire_protection_system.py

class SmokeDetector:
    """Represents a smoke detector in the fire protection system."""

    def __init__(self, detector_id, location):
        """
        Initializes a smoke detector.

        Args:
            detector_id (str): Unique identifier for the detector.
            location (str): Physical location of the detector in the data center.
        """
        self.detector_id = detector_id
        self.location = location
        self.is_smoke_detected = False

    def detect_smoke(self):
        """Simulates smoke detection."""
        # Replace with actual sensor reading logic
        self.is_smoke_detected = True
        return self.is_smoke_detected


class FireSuppressionSystem:
    """Represents a fire suppression system in the fire protection system."""

    def __init__(self, system_id, location):
        """
        Initializes a fire suppression system.

        Args:
            system_id (str): Unique identifier for the system.
            location (str): Physical location of the system in the data center.
        """
        self.system_id = system_id
        self.location = location
        self.is_activated = False

    def activate(self):
        """Activates the fire suppression system."""
        self.is_activated = True
        print(f"Fire suppression system {self.system_id} activated at {self.location}")

    def deactivate(self):
        """Deactivates the fire suppression system."""
        self.is_activated = False
        print(f"Fire suppression system {self.system_id} deactivated at {self.location}")


class EvacuationSystem:
    """Represents an evacuation system in the fire protection system."""

    def __init__(self, system_id, location):
        """
        Initializes an evacuation system.

        Args:
            system_id (str): Unique identifier for the system.
            location (str): Physical location of the system in the data center.
        """
        self.system_id = system_id
        self.location = location
        self.is_activated = False

    def activate(self):
        """Activates the evacuation system."""
        self.is_activated = True
        print(f"Evacuation system {self.system_id} activated at {self.location}")

    def deactivate(self):
        """Deactivates the evacuation system."""
        self.is_activated = False
        print(f"Evacuation system {self.system_id} deactivated at {self.location}")


class FireProtectionSystem:
    """Represents the fire protection system for the data center."""

    def __init__(self, data_center_location):
        """
        Initializes the fire protection system.

        Args:
            data_center_location (str): Physical location of the data center.
        """
        self.data_center_location = data_center_location
        self.smoke_detectors = []
        self.fire_suppression_systems = []
        self.evacuation_systems = []

    def add_smoke_detector(self, detector):
        """Adds a smoke detector to the system."""
        self.smoke_detectors.append(detector)

    def add_fire_suppression_system(self, system):
        """Adds a fire suppression system to the system."""
        self.fire_suppression_systems.append(system)

    def add_evacuation_system(self, system):
        """Adds an evacuation system to the system."""
        self.evacuation_systems.append(system)

    def monitor_smoke_detectors(self):
        """Monitors smoke detectors and activates systems if necessary."""
        for detector in self.smoke_detectors:
            if detector.detect_smoke():
                print(f"Smoke detected at {detector.location}")
                self.activate_systems(detector.location)

    def activate_systems(self, location):
        """Activates fire suppression and evacuation systems."""
        for system in self.fire_suppression_systems:
            if system.location == location:
                system.activate()

        for system in self.evacuation_systems:
            if system.location == location:
                system.activate()


def main():
    # Create fire protection system for data center in Cameroon
    data_center_location = "Cameroon Data Center"
    fps = FireProtectionSystem(data_center_location)

    # Create smoke detectors
    detector1 = SmokeDetector("Detector 1", "Server Room")
    detector2 = SmokeDetector("Detector 2", "Storage Room")

    # Create fire suppression systems
    suppression_system1 = FireSuppressionSystem("Suppression System 1", "Server Room")
    suppression_system2 = FireSuppressionSystem("Suppression System 2", "Storage Room")

    # Create evacuation systems
    evacuation_system1 = EvacuationSystem("Evacuation System 1", "Server Room")
    evacuation_system2 = EvacuationSystem("Evacuation System 2", "Storage Room")

    # Add systems to fire protection system
    fps.add_smoke_detector(detector1)
    fps.add_smoke_detector(detector2)
    fps.add_fire_suppression_system(suppression_system1)
    fps.add_fire_suppression_system(suppression_system2)
    fps.add_evacuation_system(evacuation_system1)
    fps.add_evacuation_system(evacuation_system2)

    try:
        # Monitor smoke detectors
        fps.monitor_smoke_detectors()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
