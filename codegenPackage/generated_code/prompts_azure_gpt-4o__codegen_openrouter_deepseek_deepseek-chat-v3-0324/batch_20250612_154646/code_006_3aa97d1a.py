"""
Generated Code Metadata:
========================
Original URL: https://poocoingearapp.blogspot.com
Prompt: Write a program to simulate rodagem silenciosa (silent rolling systems) in industrial machinery and explain the physics behind it.
Generated: DETERMINISTIC_3aa97d1a9688f041
Batch ID: 20250612_154646
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
from scipy.integrate import odeint

class SilentRollingSystem:
    """
    Simulates silent rolling systems in industrial machinery.
    Models the physics of vibration damping in rotating machinery.
    """
    
    def __init__(self, mass=1.0, stiffness=100.0, damping=5.0, imbalance=0.01):
        """
        Initialize the silent rolling system with physical parameters.
        
        Args:
            mass (float): Mass of the rotating component (kg)
            stiffness (float): Stiffness of the support system (N/m)
            damping (float): Damping coefficient (Ns/m)
            imbalance (float): Imbalance mass * eccentricity (kg·m)
        """
        self.m = mass
        self.k = stiffness
        self.c = damping
        self.u = imbalance
        
        # Natural frequency and damping ratio
        self.omega_n = np.sqrt(self.k / self.m)
        self.zeta = self.c / (2 * np.sqrt(self.k * self.m))
        
    def equations_of_motion(self, y, t, omega):
        """
        Differential equations for the system dynamics.
        
        Args:
            y (list): State vector [displacement, velocity]
            t (float): Time
            omega (float): Rotational speed (rad/s)
            
        Returns:
            list: Derivatives of the state vector
        """
        x, v = y
        dxdt = v
        dvdt = (self.u * omega**2 * np.sin(omega * t) - self.c * v - self.k * x) / self.m
        return [dxdt, dvdt]
    
    def simulate(self, omega, t_max=10, dt=0.01):
        """
        Simulate the system response to rotational excitation.
        
        Args:
            omega (float): Rotational speed (rad/s)
            t_max (float): Maximum simulation time (s)
            dt (float): Time step (s)
            
        Returns:
            tuple: (time_array, displacement_array)
        """
        t = np.arange(0, t_max, dt)
        y0 = [0, 0]  # Initial conditions: [displacement, velocity]
        
        # Solve the ODE
        sol = odeint(self.equations_of_motion, y0, t, args=(omega,))
        x = sol[:, 0]  # Displacement
        
        return t, x
    
    def plot_response(self, t, x, omega):
        """
        Plot the displacement response of the system.
        
        Args:
            t (array): Time array
            x (array): Displacement array
            omega (float): Rotational speed (rad/s)
        """
        plt.figure(figsize=(10, 5))
        plt.plot(t, x)
        plt.title(f'System Response at {omega:.1f} rad/s\n'
                 f'Natural Freq: {self.omega_n:.2f} rad/s, Damping Ratio: {self.zeta:.3f}')
        plt.xlabel('Time (s)')
        plt.ylabel('Displacement (m)')
        plt.grid(True)
        plt.show()
    
    def frequency_sweep(self, omega_min=1, omega_max=100, steps=50):
        """
        Perform a frequency sweep to analyze system response.
        
        Args:
            omega_min (float): Minimum rotational speed (rad/s)
            omega_max (float): Maximum rotational speed (rad/s)
            steps (int): Number of frequency steps
            
        Returns:
            tuple: (frequencies, peak_displacements)
        """
        omegas = np.linspace(omega_min, omega_max, steps)
        peaks = []
        
        for omega in omegas:
            t, x = self.simulate(omega, t_max=20, dt=0.01)
            peaks.append(np.max(np.abs(x[-len(x)//2:])))  # Steady-state amplitude
            
        return omegas, np.array(peaks)
    
    def plot_frequency_response(self, omegas, peaks):
        """
        Plot the frequency response of the system.
        
        Args:
            omegas (array): Frequency array
            peaks (array): Peak displacement at each frequency
        """
        plt.figure(figsize=(10, 5))
        plt.plot(omegas, peaks)
        plt.axvline(self.omega_n, color='r', linestyle='--', label='Natural Frequency')
        plt.title('Frequency Response of Silent Rolling System')
        plt.xlabel('Rotational Speed (rad/s)')
        plt.ylabel('Peak Displacement (m)')
        plt.legend()
        plt.grid(True)
        plt.show()

# Example usage
if __name__ == "__main__":
    # Create a system with typical industrial parameters
    system = SilentRollingSystem(mass=50, stiffness=1e5, damping=500, imbalance=0.05)
    
    # Simulate at a specific speed
    omega = 30  # rad/s (~286 RPM)
    t, x = system.simulate(omega)
    system.plot_response(t, x, omega)
    
    # Perform frequency sweep
    omegas, peaks = system.frequency_sweep()
    system.plot_frequency_response(omegas, peaks)
```
