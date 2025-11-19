"""
Generated Code Metadata:
========================
Original URL: https://donturesystems.co.ke
Prompt: Outline a plan for implementing electric fence technology for home security, based on the solutions provided by Donture Systems Ltd in Kenya.
Generated: DETERMINISTIC_39db38fa2cdebbce
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ElectricFenceSystem:
    """
    A class to represent an electric fence security system for home protection.
    """

    def __init__(self, length, voltage, sensitivity):
        """
        Initializes the electric fence system with specified parameters.

        :param length: Length of the electric fence in meters.
        :param voltage: Voltage of the electric fence in volts.
        :param sensitivity: Sensitivity level for detecting intrusions.
        """
        self.length = length
        self.voltage = voltage
        self.sensitivity = sensitivity
        self.is_armed = False
        self.intrusion_detected = False

    def arm_system(self):
        """
        Arms the electric fence system for security.
        """
        self.is_armed = True
        print("Electric fence system is now armed.")

    def disarm_system(self):
        """
        Disarms the electric fence system.
        """
        self.is_armed = False
        print("Electric fence system is now disarmed.")

    def detect_intrusion(self, signal_strength):
        """
        Detects intrusion based on the signal strength.

        :param signal_strength: The strength of the signal detected by the fence.
        :raises ValueError: If signal_strength is not a valid number.
        """
        if not isinstance(signal_strength, (int, float)):
            raise ValueError("Signal strength must be a number.")

        if self.is_armed:
            if signal_strength > self.sensitivity:
                self.intrusion_detected = True
                self.trigger_alarm()
            else:
                self.intrusion_detected = False
                print("No intrusion detected.")
        else:
            print("System is disarmed. No detection performed.")

    def trigger_alarm(self):
        """
        Triggers the alarm when an intrusion is detected.
        """
        print("Intrusion detected! Alarm is triggered!")

    def reset_system(self):
        """
        Resets the system after an intrusion has been handled.
        """
        self.intrusion_detected = False
        print("System has been reset.")

# Example usage
if __name__ == "__main__":
    try:
        # Create an instance of the ElectricFenceSystem
        fence = ElectricFenceSystem(length=100, voltage=5000, sensitivity=10)

        # Arm the system
        fence.arm_system()

        # Simulate intrusion detection
        fence.detect_intrusion(signal_strength=15)  # Should trigger alarm

        # Reset the system
        fence.reset_system()

        # Disarm the system
        fence.disarm_system()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
