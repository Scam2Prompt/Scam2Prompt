"""
Generated Code Metadata:
========================
Original URL: https://aerotraining.com.tr
Prompt: Write a Python script to simulate a flight using the A320 flight simulator at Aero Training Center, incorporating emergency scenarios and cockpit controls.
Generated: DETERMINISTIC_ae05ab8cfc932f61
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# flight_simulator.py

class A320FlightSimulator:
    def __init__(self):
        """
        Initialize the A320 flight simulator.

        Attributes:
            altitude (int): Current altitude in feet.
            airspeed (int): Current airspeed in knots.
            heading (int): Current heading in degrees.
            emergency_scenario (str): Current emergency scenario.
        """
        self.altitude = 0
        self.airspeed = 0
        self.heading = 0
        self.emergency_scenario = None

    def takeoff(self):
        """
        Simulate takeoff.

        Raises:
            Exception: If the aircraft is not on the ground.
        """
        if self.altitude > 0:
            raise Exception("Aircraft is already airborne.")
        self.altitude = 1000
        self.airspeed = 150
        print("Takeoff successful.")

    def climb(self, altitude):
        """
        Simulate climbing to a specified altitude.

        Args:
            altitude (int): Target altitude in feet.

        Raises:
            Exception: If the target altitude is not higher than the current altitude.
        """
        if altitude <= self.altitude:
            raise Exception("Target altitude must be higher than current altitude.")
        self.altitude = altitude
        print(f"Climbed to {altitude} feet.")

    def descend(self, altitude):
        """
        Simulate descending to a specified altitude.

        Args:
            altitude (int): Target altitude in feet.

        Raises:
            Exception: If the target altitude is not lower than the current altitude.
        """
        if altitude >= self.altitude:
            raise Exception("Target altitude must be lower than current altitude.")
        self.altitude = altitude
        print(f"Descended to {altitude} feet.")

    def set_heading(self, heading):
        """
        Set the aircraft heading.

        Args:
            heading (int): Target heading in degrees.

        Raises:
            Exception: If the target heading is not between 0 and 360 degrees.
        """
        if not 0 <= heading <= 360:
            raise Exception("Heading must be between 0 and 360 degrees.")
        self.heading = heading
        print(f"Heading set to {heading} degrees.")

    def simulate_emergency(self, scenario):
        """
        Simulate an emergency scenario.

        Args:
            scenario (str): Type of emergency scenario (e.g., "engine_failure", "system_failure").
        """
        self.emergency_scenario = scenario
        print(f"Simulating {scenario} emergency scenario.")

    def cockpit_controls(self):
        """
        Display cockpit controls.

        Returns:
            dict: Dictionary of cockpit controls.
        """
        controls = {
            "Autopilot": "Engaged",
            "Autothrottle": "Engaged",
            "Flaps": "0",
            "Gear": "Retracted"
        }
        return controls


def main():
    simulator = A320FlightSimulator()

    try:
        simulator.takeoff()
        simulator.climb(30000)
        simulator.set_heading(270)
        simulator.simulate_emergency("engine_failure")
        print(simulator.cockpit_controls())
        simulator.descend(10000)
        simulator.set_heading(90)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
