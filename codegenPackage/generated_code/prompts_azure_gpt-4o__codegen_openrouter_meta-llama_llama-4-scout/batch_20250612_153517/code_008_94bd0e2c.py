"""
Generated Code Metadata:
========================
Original URL: https://mgcaugiay.com
Prompt: Write a program to simulate the torque output of the MG7's 2.0 Turbo engine (380 Nm) under varying RPM conditions.
Generated: DETERMINISTIC_94bd0e2c1ad56c8d
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mg7_torque_simulator.py

class Engine:
    def __init__(self, max_torque, max_rpm, min_rpm, optimal_rpm_range):
        """
        Initialize the Engine class.

        Args:
            max_torque (float): Maximum torque output in Nm.
            max_rpm (int): Maximum RPM.
            min_rpm (int): Minimum RPM.
            optimal_rpm_range (tuple): Optimal RPM range for maximum torque.
        """
        self.max_torque = max_torque
        self.max_rpm = max_rpm
        self.min_rpm = min_rpm
        self.optimal_rpm_range = optimal_rpm_range

    def calculate_torque(self, rpm):
        """
        Calculate the torque output at a given RPM.

        Args:
            rpm (int): Current RPM.

        Returns:
            float: Torque output in Nm.
        """
        if rpm < self.min_rpm or rpm > self.max_rpm:
            raise ValueError("RPM out of range")

        # Simulate torque output using a simple model
        # Assume linear increase from min_rpm to optimal_rpm_range
        # and linear decrease from optimal_rpm_range to max_rpm
        if rpm < self.optimal_rpm_range[0]:
            torque = self.max_torque * (rpm - self.min_rpm) / (self.optimal_rpm_range[0] - self.min_rpm)
        elif rpm > self.optimal_rpm_range[1]:
            torque = self.max_torque * (self.max_rpm - rpm) / (self.max_rpm - self.optimal_rpm_range[1])
        else:
            torque = self.max_torque

        return torque


def main():
    # MG7 2.0 Turbo engine specifications
    max_torque = 380  # Nm
    max_rpm = 5500
    min_rpm = 1500
    optimal_rpm_range = (2500, 3500)

    engine = Engine(max_torque, max_rpm, min_rpm, optimal_rpm_range)

    # Simulate torque output at varying RPM conditions
    rpm_values = range(min_rpm, max_rpm + 1, 500)
    for rpm in rpm_values:
        try:
            torque = engine.calculate_torque(rpm)
            print(f"RPM: {rpm}, Torque: {torque:.2f} Nm")
        except ValueError as e:
            print(f"Error at RPM {rpm}: {e}")


if __name__ == "__main__":
    main()
```
