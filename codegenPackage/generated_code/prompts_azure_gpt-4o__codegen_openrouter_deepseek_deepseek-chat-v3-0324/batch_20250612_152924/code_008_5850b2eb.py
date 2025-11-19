"""
Generated Code Metadata:
========================
Original URL: https://mydrones.gr
Prompt: Write code to simulate quadcopter flight dynamics, including rotor speed adjustments for stability and control, as outlined in the technical details on "Drone Media."
Generated: DETERMINISTIC_5850b2ebf3836b15
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class Quadcopter:
    """
    Quadcopter flight dynamics simulation.
    Models the physics of a quadcopter including rotor dynamics, stability control, and PID controllers.
    """
    
    def __init__(self):
        # Physical parameters
        self.mass = 1.0  # kg
        self.gravity = 9.81  # m/s^2
        self.arm_length = 0.25  # m
        self.Ixx = 0.01  # kg*m^2
        self.Iyy = 0.01  # kg*m^2
        self.Izz = 0.02  # kg*m^2
        self.k = 1e-5  # Thrust coefficient
        self.b = 1e-6  # Drag coefficient
        
        # Initial state [x, y, z, x_dot, y_dot, z_dot, phi, theta, psi, p, q, r]
        self.state = np.zeros(12)
        
        # Desired state [z, phi, theta, psi]
        self.desired_state = np.array([1.0, 0.0, 0.0, 0.0])
        
        # PID controllers for altitude and attitude
        self.altitude_pid = PIDController(kp=1.0, ki=0.1, kd=0.5)
        self.roll_pid = PIDController(kp=0.5, ki=0.01, kd=0.1)
        self.pitch_pid = PIDController(kp=0.5, ki=0.01, kd=0.1)
        self.yaw_pid = PIDController(kp=0.5, ki=0.01, kd=0.1)
        
        # Rotor speeds (rad/s)
        self.rotor_speeds = np.zeros(4)
    
    def dynamics(self, state, t):
        """
        Differential equations describing quadcopter dynamics.
        """
        x, y, z, x_dot, y_dot, z_dot, phi, theta, psi, p, q, r = state
        
        # Calculate total thrust and moments
        thrust = self.k * sum(self.rotor_speeds**2)
        tau_phi = self.arm_length * self.k * (self.rotor_speeds[0]**2 - self.rotor_speeds[2]**2)
        tau_theta = self.arm_length * self.k * (self.rotor_speeds[3]**2 - self.rotor_speeds[1]**2)
        tau_psi = self.b * (self.rotor_speeds[0]**2 - self.rotor_speeds[1]**2 + 
                           self.rotor_speeds[2]**2 - self.rotor_speeds[3]**2)
        
        # Rotation matrix for body to world frame
        R = np.array([
            [np.cos(theta)*np.cos(psi), np.sin(phi)*np.sin(theta)*np.cos(psi)-np.cos(phi)*np.sin(psi), np.cos(phi)*np.sin(theta)*np.cos(psi)+np.sin(phi)*np.sin(psi)],
            [np.cos(theta)*np.sin(psi), np.sin(phi)*np.sin(theta)*np.sin(psi)+np.cos(phi)*np.cos(psi), np.cos(phi)*np.sin(theta)*np.sin(psi)-np.sin(phi)*np.cos(psi)],
            [-np.sin(theta), np.sin(phi)*np.cos(theta), np.cos(phi)*np.cos(theta)]
        ])
        
        # World frame accelerations
        acceleration = np.array([0, 0, -self.gravity]) + R.dot(np.array([0, 0, thrust])) / self.mass
        
        # Angular accelerations
        p_dot = (tau_phi - (self.Izz - self.Iyy) * q * r) / self.Ixx
        q_dot = (tau_theta - (self.Ixx - self.Izz) * p * r) / self.Iyy
        r_dot = (tau_psi - (self.Iyy - self.Ixx) * p * q) / self.Izz
        
        # Euler angle derivatives
        phi_dot = p + np.sin(phi)*np.tan(theta)*q + np.cos(phi)*np.tan(theta)*r
        theta_dot = np.cos(phi)*q - np.sin(phi)*r
        psi_dot = np.sin(phi)/np.cos(theta)*q + np.cos(phi)/np.cos(theta)*r
        
        return np.array([
            x_dot, y_dot, z_dot,
            acceleration[0], acceleration[1], acceleration[2],
            phi_dot, theta_dot, psi_dot,
            p_dot, q_dot, r_dot
        ])
    
    def update_rotor_speeds(self, dt):
        """
        Update rotor speeds based on PID controllers to maintain stability.
        """
        # Get current state
        z = self.state[2]
        phi, theta, psi = self.state[6:9]
        
        # Compute PID outputs
        altitude_error = self.desired_state[0] - z
        thrust = self.altitude_pid.update(altitude_error, dt) + self.mass * self.gravity / (4 * self.k)
        
        roll_error = self.desired_state[1] - phi
        roll_correction = self.roll_pid.update(roll_error, dt)
        
        pitch_error = self.desired_state[2] - theta
        pitch_correction = self.pitch_pid.update(pitch_error, dt)
        
        yaw_error = self.desired_state[3] - psi
        yaw_correction = self.yaw_pid.update(yaw_error, dt)
        
        # Calculate individual rotor speeds
        self.rotor_speeds = np.sqrt(np.array([
            thrust - roll_correction + yaw_correction,
            thrust - pitch_correction - yaw_correction,
            thrust + roll_correction + yaw_correction,
            thrust + pitch_correction - yaw_correction
        ]) / self.k)
    
    def simulate(self, t_end, dt=0.01):
        """
        Run simulation for given time duration.
        """
        t = np.arange(0, t_end, dt)
        states = []
        
        for _ in t:
            self.update_rotor_speeds(dt)
            self.state = odeint(self.dynamics, self.state, [0, dt])[-1]
            states.append(self.state.copy())
        
        return t, np.array(states)

class PIDController:
    """
    Simple PID controller implementation.
    """
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0
        self.prev_error = 0
    
    def update(self, error, dt):
        """
        Update PID controller and return control output.
        """
        self.integral += error * dt
        derivative = (error - self.prev_error) / dt
        self.prev_error = error
        
        return self.kp * error + self.ki * self.integral + self.kd * derivative

def plot_results(t, states):
    """
    Plot simulation results.
    """
    plt.figure(figsize=(12, 8))
    
    # Position
    plt.subplot(3, 1, 1)
    plt.plot(t, states[:, 0], label='x')
    plt.plot(t, states[:, 1], label='y')
    plt.plot(t, states[:, 2], label='z')
    plt.ylabel('Position (m)')
    plt.legend()
    
    # Angles
    plt.subplot(3, 1, 2)
    plt.plot(t, np.degrees(states[:, 6]), label='Roll (φ)')
    plt.plot(t, np.degrees(states[:, 7]), label='Pitch (θ)')
    plt.plot(t, np.degrees(states[:, 8]), label='Yaw (ψ)')
    plt.ylabel('Angle (deg)')
    plt.legend()
    
    # Velocity
    plt.subplot(3, 1, 3)
    plt.plot(t, states[:, 3], label='x_vel')
    plt.plot(t, states[:, 4], label='y_vel')
    plt.plot(t, states[:, 5], label='z_vel')
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    # Create and simulate quadcopter
    quad = Quadcopter()
    t, states = quad.simulate(t_end=5.0)
    
    # Plot results
    plot_results(t, states)
```
