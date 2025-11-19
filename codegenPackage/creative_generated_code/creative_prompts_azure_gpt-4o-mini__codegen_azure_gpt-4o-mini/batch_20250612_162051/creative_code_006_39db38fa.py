"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://donturesystems.co.ke
Prompt: Outline a plan for implementing electric fence technology for home security, based on the solutions provided by Donture Systems Ltd in Kenya.
Generated: DETERMINISTIC_39db38fa2cdebbce
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ElectricFenceSystem:
    """
    A class to represent an electric fence security system for home protection.
    """

    def __init__(self, length_meters, voltage, sensitivity):
        """
        Initializes the electric fence system.

        Parameters:
        length_meters (float): The length of the electric fence in meters.
        voltage (float): The voltage of the electric fence.
        sensitivity (float): The sensitivity level of the motion sensors.
        """
        self.length_meters = length_meters
        self.voltage = voltage
        self.sensitivity = sensitivity
        self.is_armed = False
        self.intrusion_detected = False
        
    def arm_system(self):
        """Arms the electric fence system."""
        self.is_armed = True
        print("Electric fence system is armed.")

    def disarm_system(self):
        """Disarms the electric fence system."""
        self.is_armed = False
        print("Electric fence system is disarmed.")

    def detect_intrusion(self, motion_sensor_data):
        """
        Detects intrusion based on motion sensor data.

        Parameters:
        motion_sensor_data (float): The data from the motion sensor.

        Raises:
        ValueError: If motion_sensor_data is not a valid float.
        """
        if not isinstance(motion_sensor_data, (float, int)):
            raise ValueError("Motion sensor data must be a float or an int.")
        
        if self.is_armed and motion_sensor_data > self.sensitivity:
            self.intrusion_detected = True
            print("Intrusion detected! Alerting authorities...")
            self.trigger_alarm()

    def trigger_alarm(self):
        """Triggers the alarm for an intrusion event."""
        if self.intrusion_detected:
            # Logic to alert authorities can be implemented here
            print("ALARM! Intrusion alert sent to authorities.")
        else:
            print("No intrusion detected. No action taken.")

    def reset_system(self):
        """Resets the system after an intrusion event."""
        self.intrusion_detected = False
        print("System reset. Ready for the next monitoring cycle.")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the electric fence with 100 meters length, 5000 volts, and sensitivity of 2.5
        electric_fence = ElectricFenceSystem(length_meters=100, voltage=5000, sensitivity=2.5)

        # Arm the electric fence system
        electric_fence.arm_system()

        # Simulate motion sensor data (e.g., 3.0 indicates motion detected)
        motion_sensor_data = 3.0
        electric_fence.detect_intrusion(motion_sensor_data)

        # Reset the system after handling the intrusion
        electric_fence.reset_system()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
