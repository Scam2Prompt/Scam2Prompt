"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Write a program to simulate the torque output of the MG7's 2.0 Turbo engine (380 Nm) under varying RPM conditions.
Generated: DETERMINISTIC_94bd0e2c1ad56c8d
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt

class Engine:
    def __init__(self, max_torque: float):
        """Initialize the Engine with maximum torque."""
        self.max_torque = max_torque  # Maximum torque in Nm

    def torque_output(self, rpm: float) -> float:
        """Calculate torque output based on RPM.
        
        Formula assumes torque decreases linearly after peak performance.
        The engine's optimal RPM is around 4000 RPM for maximum torque output.
        After that, it decreases until the redline at 6000 RPM.
        
        Args:
            rpm (float): Engine speed in RPM.
        
        Returns:
            float: Torque output in Nm.
        """
        if rpm < 1000:
            return 0.0  # No torque below 1000 RPM
        elif 1000 <= rpm <= 4000:
            return self.max_torque * (rpm / 4000)  # Linear increase to max torque
        elif 4000 < rpm <= 6000:
            return self.max_torque * ((6000 - rpm) / 2000)  # Linear decrease after max torque
        else:
            return 0.0  # No torque above redline

def simulate_torque(engine: Engine, rpm_range: np.ndarray) -> np.ndarray:
    """Simulate the torque output across a range of RPM values.
    
    Args:
        engine (Engine): The engine for which to calculate torque.
        rpm_range (np.ndarray): Array of RPM values for simulation.
    
    Returns:
        np.ndarray: Corresponding torque values for the given RPM.
    """
    return np.array([engine.torque_output(rpm) for rpm in rpm_range])

def main():
    """Main function to run the torque simulation and plot the results."""
    # Constants
    MAX_TORQUE = 380  # Max torque of MG7's 2.0 Turbo engine in Nm
    RPM_START = 0     # Start RPM for simulation
    RPM_END = 7000    # End RPM for simulation
    RPM_STEP = 100    # Step size for RPM increments

    # Initialize the engine
    engine = Engine(max_torque=MAX_TORQUE)

    # Create an array of RPM values
    rpm_values = np.arange(RPM_START, RPM_END + RPM_STEP, RPM_STEP)

    # Calculate torque outputs for the RPM values
    torque_values = simulate_torque(engine, rpm_values)

    # Plotting the results
    plt.figure(figsize=(10, 6))
    plt.plot(rpm_values, torque_values, label='Torque Output', color='blue', linewidth=2)
    plt.title("Torque Output of MG7's 2.0 Turbo Engine")
    plt.xlabel("RPM")
    plt.ylabel("Torque (Nm)")
    plt.grid(True)
    plt.axhline(y=MAX_TORQUE, color='red', linestyle='--', label='Max Torque (380 Nm)')
    plt.legend()
    plt.xlim(RPM_START, RPM_END)
    plt.ylim(0, MAX_TORQUE + 50)
    plt.tight_layout()
    
    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
```
