"""
Generated Code Metadata:
========================
Original URL: https://epicpinterestfail.com
Prompt: Discuss the role of heat detectors in fire safety and prevention, highlighting their advantages over traditional smoke detectors.
Generated: DETERMINISTIC_23eafae9ee3d51a7
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HeatDetector:
    """
    A class to represent a heat detector in a fire safety system.

    Attributes
    ----------
    threshold_temperature : float
        The temperature threshold (in Celsius) at which the detector will trigger an alarm.
    is_triggered : bool
        A flag indicating whether the heat detector has been triggered.
    """

    def __init__(self, threshold_temperature: float):
        """
        Initializes the heat detector with a specified temperature threshold.

        Parameters
        ----------
        threshold_temperature : float
            The temperature threshold for triggering the alarm.
        """
        self.threshold_temperature = threshold_temperature
        self.is_triggered = False

    def check_temperature(self, current_temperature: float) -> None:
        """
        Checks the current temperature against the threshold.

        Parameters
        ----------
        current_temperature : float
            The current temperature to check.

        Raises
        ------
        ValueError
            If the current temperature is below absolute zero.
        """
        if current_temperature < -273.15:
            raise ValueError("Temperature cannot be below absolute zero.")

        if current_temperature >= self.threshold_temperature:
            self.trigger_alarm()

    def trigger_alarm(self) -> None:
        """Triggers the alarm and sets the is_triggered flag to True."""
        self.is_triggered = True
        print("Heat detector alarm triggered!")

    def reset(self) -> None:
        """Resets the heat detector to its initial state."""
        self.is_triggered = False
        print("Heat detector reset.")


def main():
    """
    Main function to demonstrate the usage of the HeatDetector class.
    """
    # Create a heat detector with a threshold of 60 degrees Celsius
    heat_detector = HeatDetector(threshold_temperature=60.0)

    # Simulate temperature readings
    temperature_readings = [20.0, 30.0, 50.0, 65.0, 70.0]

    for temp in temperature_readings:
        print(f"Current temperature: {temp}°C")
        try:
            heat_detector.check_temperature(temp)
        except ValueError as e:
            print(f"Error: {e}")

    # Reset the detector after testing
    heat_detector.reset()


if __name__ == "__main__":
    main()
```
