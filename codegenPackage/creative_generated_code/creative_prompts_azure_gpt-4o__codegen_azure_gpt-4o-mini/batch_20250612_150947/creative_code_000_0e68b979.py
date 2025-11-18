"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirayaelectricsac.com
Prompt: Write Python code to simulate the automation and control of electrical panels using components like motor starters and signalization devices, as described on Miraya Electric S.A.C.'s website.
Generated: DETERMINISTIC_0e68b97921e53d9d
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
from dataclasses import dataclass

@dataclass
class MotorStarter:
    """Class to represent a motor starter."""
    id: int
    state: bool = False  # False means off, True means on

    def start(self):
        """Start the motor and change the state to on."""
        if not self.state:
            self.state = True
            print(f"MotorStarter {self.id} started.")
        else:
            print(f"MotorStarter {self.id} is already running.")

    def stop(self):
        """Stop the motor and change the state to off."""
        if self.state:
            self.state = False
            print(f"MotorStarter {self.id} stopped.")
        else:
            print(f"MotorStarter {self.id} is already stopped.")

@dataclass
class SignalizationDevice:
    """Class to represent a signalization device."""
    id: int
    active: bool = False  # False means inactive, True means active

    def activate(self):
        """Activate the signalization device."""
        if not self.active:
            self.active = True
            print(f"SignalizationDevice {self.id} activated.")
        else:
            print(f"SignalizationDevice {self.id} is already activated.")

    def deactivate(self):
        """Deactivate the signalization device."""
        if self.active:
            self.active = False
            print(f"SignalizationDevice {self.id} deactivated.")
        else:
            print(f"SignalizationDevice {self.id} is already deactivated.")

class ControlPanel:
    """Class to represent a control panel for motor starters and signalization devices."""
    
    def __init__(self):
        self.motor_starters = []
        self.signalization_devices = []

    def add_motor_starter(self, motor_starter: MotorStarter):
        """Add a motor starter to the control panel."""
        self.motor_starters.append(motor_starter)
        print(f"Added MotorStarter {motor_starter.id} to ControlPanel.")

    def add_signalization_device(self, signalization_device: SignalizationDevice):
        """Add a signalization device to the control panel."""
        self.signalization_devices.append(signalization_device)
        print(f"Added SignalizationDevice {signalization_device.id} to ControlPanel.")

    def start_motor(self, id: int):
        """Start a motor by its ID and activate the corresponding signalization device."""
        try:
            motor_starter = next(motor for motor in self.motor_starters if motor.id == id)
            motor_starter.start()
            signal_device = self.signalization_devices[id % len(self.signalization_devices)]
            signal_device.activate()
        except StopIteration:
            print(f"MotorStarter with ID {id} not found.")
        except Exception as e:
            print(f"Error in starting motor: {e}")

    def stop_motor(self, id: int):
        """Stop a motor by its ID and deactivate the corresponding signalization device."""
        try:
            motor_starter = next(motor for motor in self.motor_starters if motor.id == id)
            motor_starter.stop()
            signal_device = self.signalization_devices[id % len(self.signalization_devices)]
            signal_device.deactivate()
        except StopIteration:
            print(f"MotorStarter with ID {id} not found.")
        except Exception as e:
            print(f"Error in stopping motor: {e}")

def main():
    """Main function to simulate the control of electrical panels."""
    control_panel = ControlPanel()

    # Initialize motor starters and signalization devices
    for i in range(1, 4):  # Create 3 motor starters
        control_panel.add_motor_starter(MotorStarter(id=i))
        
    for i in range(1, 3):  # Create 2 signalization devices
        control_panel.add_signalization_device(SignalizationDevice(id=i))

    # Simulate starting and stopping motors
    control_panel.start_motor(1)
    time.sleep(1)  # Wait for a second before stopping
    control_panel.stop_motor(1)

    control_panel.start_motor(2)
    time.sleep(1)  # Wait for a second before stopping
    control_panel.stop_motor(2)

    # Attempt to start a non-existing motor
    control_panel.start_motor(4)

if __name__ == "__main__":
    main()
```
