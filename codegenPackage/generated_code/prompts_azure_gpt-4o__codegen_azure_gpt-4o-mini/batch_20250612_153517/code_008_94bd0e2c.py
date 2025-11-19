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
import numpy as np
import matplotlib.pyplot as plt

class EngineTorqueSimulator:
    """
    A class to simulate the torque output of the MG7's 2.0 Turbo engine.
    The engine has a maximum torque of 380 Nm.
    """

    def __init__(self, max_torque: float = 380.0):
        """
        Initializes the EngineTorqueSimulator with a maximum torque value.

        :param max_torque: Maximum torque output of the engine in Nm.
        """
        self.max_torque = max_torque

    def calculate_torque(self, rpm: float) -> float:
        """
        Calculates the torque output based on the RPM.

        :param rpm: Engine speed in revolutions per minute.
        :return: Torque output in Nm.
        """
        if rpm < 1000:
            return 0.0  # Below idle speed, no torque
        elif rpm > 6000:
            return 0.0  # Above redline, no torque
        else:
            # Simulate a simple torque curve
            # Torque increases linearly from 1000 RPM to 4000 RPM, then decreases to 0 at 6000 RPM
            if rpm <= 4000:
                return (self.max_torque / 3000) * (rpm - 1000)
            else:
                return (self.max_torque / 2000) * (6000 - rpm)

    def simulate_torque_curve(self, rpm_range: np.ndarray) -> np.ndarray:
        """
        Simulates the torque output over a range of RPM values.

        :param rpm_range: A numpy array of RPM values.
        :return: A numpy array of torque values corresponding to the RPM range.
        """
        torque_values = np.array([self.calculate_torque(rpm) for rpm in rpm_range])
        return torque_values

def main():
    """
    Main function to run the torque simulation and plot the results.
    """
    try:
        # Define the RPM range from 800 to 6500
        rpm_range = np.linspace(800, 6500, 1000)

        # Create an instance of the EngineTorqueSimulator
        engine_simulator = EngineTorqueSimulator()

        # Simulate the torque curve
        torque_values = engine_simulator.simulate_torque_curve(rpm_range)

        # Plotting the results
        plt.figure(figsize=(10, 6))
        plt.plot(rpm_range, torque_values, label='Torque Output (Nm)', color='blue')
        plt.title('Torque Output of MG7 2.0 Turbo Engine')
        plt.xlabel('RPM')
        plt.ylabel('Torque (Nm)')
        plt.axhline(y=380, color='r', linestyle='--', label='Max Torque (380 Nm)')
        plt.xlim(800, 6500)
        plt.ylim(0, 400)
        plt.grid()
        plt.legend()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
