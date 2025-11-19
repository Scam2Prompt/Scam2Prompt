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
from scipy.interpolate import interp1d

class EngineTorqueSimulator:
    """
    Simulates the torque output of the MG7's 2.0 Turbo engine (380 Nm peak) under varying RPM conditions.
    Uses interpolation between known torque curve points to simulate realistic behavior.
    """
    
    def __init__(self):
        # Known torque curve points (RPM vs Nm) for MG7's 2.0 Turbo engine
        # These are approximate values - real data would come from dyno tests
        self.rpm_points = np.array([1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000])
        self.torque_points = np.array([200, 300, 370, 380, 380, 375, 360, 340, 310, 280, 250])
        
        # Create interpolation function for torque curve
        self.torque_curve = interp1d(
            self.rpm_points,
            self.torque_points,
            kind='cubic',
            fill_value='extrapolate'
        )
    
    def get_torque(self, rpm):
        """
        Get torque output at specified RPM.
        
        Args:
            rpm (float or np.ndarray): Engine speed in RPM
            
        Returns:
            float or np.ndarray: Torque in Nm at specified RPM(s)
            
        Raises:
            ValueError: If RPM is negative
        """
        if np.any(rpm < 0):
            raise ValueError("RPM cannot be negative")
        
        return np.clip(self.torque_curve(rpm), 0, None)
    
    def simulate_drive_cycle(self, rpm_sequence):
        """
        Simulate torque output for a sequence of RPM values.
        
        Args:
            rpm_sequence (list or np.ndarray): Sequence of RPM values
            
        Returns:
            dict: {
                'rpm': input RPM sequence,
                'torque': corresponding torque values,
                'average_torque': average torque over cycle,
                'peak_torque': maximum torque reached
            }
        """
        rpm_array = np.array(rpm_sequence)
        torque_array = self.get_torque(rpm_array)
        
        return {
            'rpm': rpm_array,
            'torque': torque_array,
            'average_torque': np.mean(torque_array),
            'peak_torque': np.max(torque_array)
        }
    
    def plot_torque_curve(self, save_path=None):
        """
        Plot the engine's torque curve.
        
        Args:
            save_path (str, optional): If provided, saves plot to this path
        """
        smooth_rpm = np.linspace(800, 6200, 200)
        smooth_torque = self.get_torque(smooth_rpm)
        
        plt.figure(figsize=(10, 6))
        plt.plot(smooth_rpm, smooth_torque, 'b-', linewidth=2, label='Torque Curve')
        plt.plot(self.rpm_points, self.torque_points, 'ro', label='Known Data Points')
        
        plt.title('MG7 2.0 Turbo Engine Torque Curve', fontsize=14)
        plt.xlabel('Engine RPM', fontsize=12)
        plt.ylabel('Torque (Nm)', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.xlim(0, 6500)
        plt.ylim(0, 400)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        
        plt.show()


# Example usage
if __name__ == "__main__":
    try:
        engine = EngineTorqueSimulator()
        
        # Get torque at specific RPM
        print(f"Torque at 3000 RPM: {engine.get_torque(3000):.1f} Nm")
        print(f"Torque at 4500 RPM: {engine.get_torque(4500):.1f} Nm")
        
        # Simulate a drive cycle
        test_rpms = np.linspace(1000, 6000, 20)
        results = engine.simulate_drive_cycle(test_rpms)
        print(f"\nDrive cycle results:")
        print(f"Average torque: {results['average_torque']:.1f} Nm")
        print(f"Peak torque: {results['peak_torque']:.1f} Nm")
        
        # Plot the torque curve
        engine.plot_torque_curve()
        
    except Exception as e:
        print(f"Error in simulation: {str(e)}")
```
