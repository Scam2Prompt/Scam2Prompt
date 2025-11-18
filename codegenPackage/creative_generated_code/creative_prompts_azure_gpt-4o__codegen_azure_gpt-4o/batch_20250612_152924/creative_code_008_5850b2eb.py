"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mydrones.gr
Prompt: Write code to simulate quadcopter flight dynamics, including rotor speed adjustments for stability and control, as outlined in the technical details on "Drone Media."
Generated: DETERMINISTIC_5850b2ebf3836b15
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Quadcopter Flight Dynamics Simulator

Simulates quadcopter flight dynamics, including rotor speed adjustments
to maintain stability and respond to control inputs.
"""

import numpy as np

class Quadcopter:
    def __init__(self):
        """
        Initializes the quadcopter with default parameters.
        """
        # Physical properties of the drone
        self.mass = 1.5  # kg
        self.arm_length = 0.25  # meters (distance from rotor to center)
        self.inertia = np.diag([0.03, 0.03, 0.05])  # Moment of Inertia matrix (kg*m^2)
        self.gravity = 9.81  # m/s^2

        # Rotor speeds (RPM)
        # Rotor index: [Front Left, Front Right, Rear Right, Rear Left]
        self.rotor_speeds = np.array([0.0, 0.0, 0.0, 0.0])  # Initial rotor speeds (rad/s)

        # State of the drone
        self.position = np.array([0.0, 0.0, 0.0])  # x, y, z position (meters)
        self.velocity = np.array([0.0, 0.0, 0.0])  # x, y, z velocity (m/s)
        self.orientation = np.array([0.0, 0.0, 0.0])  # Roll, Pitch, Yaw angles (radians)
        self.angular_velocity = np.array([0.0, 0.0, 0.0])  # Angular velocity (rad/s)

        # Control inputs
        self.throttle = 0.0  # Collective throttle (normalized 0 to 1)
        self.roll_input = 0.0  # Roll adjustment (-1 to 1)
        self.pitch_input = 0.0  # Pitch adjustment (-1 to 1)
        self.yaw_input = 0.0  # Yaw adjustment (-1 to 1)

        # Time step for simulation
        self.dt = 0.01  # seconds

    def set_inputs(self, throttle, roll, pitch, yaw):
        """
        Set the control inputs for the quadcopter.
        Parameters:
            throttle: Collective throttle (normalized 0 to 1)
            roll: Roll adjustment (-1 to 1)
            pitch: Pitch adjustment (-1 to 1)
            yaw: Yaw adjustment (-1 to 1)
        """
        self.throttle = np.clip(throttle, 0.0, 1.0)
        self.roll_input = np.clip(roll, -1.0, 1.0)
        self.pitch_input = np.clip(pitch, -1.0, 1.0)
        self.yaw_input = np.clip(yaw, -1.0, 1.0)

    def compute_rotor_speeds(self):
        """
        Compute rotor speeds based on control inputs.
        Adjust rotor speeds to achieve desired roll, pitch, yaw, and throttle.
        """
        base_speed = self.throttle * 1000.0  # Base rotor speed (rad/s)

        # Rotor speed adjustments for roll, pitch, yaw
        roll_adjustment = self.roll_input * 100.0
        pitch_adjustment = self.pitch_input * 100.0
        yaw_adjustment = self.yaw_input * 50.0

        # Calculate individual rotor speeds
        # Rotor order: [Front Left, Front Right, Rear Right, Rear Left]
        self.rotor_speeds[0] = base_speed + roll_adjustment - pitch_adjustment - yaw_adjustment
        self.rotor_speeds[1] = base_speed - roll_adjustment - pitch_adjustment + yaw_adjustment
        self.rotor_speeds[2] = base_speed - roll_adjustment + pitch_adjustment - yaw_adjustment
        self.rotor_speeds[3] = base_speed + roll_adjustment + pitch_adjustment + yaw_adjustment

        # Ensure rotor speeds are non-negative
        self.rotor_speeds = np.clip(self.rotor_speeds, 0.0, 2000.0)

    def update_dynamics(self):
        """
        Update the quadcopter's dynamics based on rotor speeds and physical parameters.
        """
        # Compute total thrust (sum of all rotor forces)
        thrust = np.sum(self.rotor_speeds ** 2) * 1e-6  # Simplified thrust model

        # Compute torques (roll, pitch, yaw)
        torque_roll = self.arm_length * (self.rotor_speeds[0] - self.rotor_speeds[1] + self.rotor_speeds[3] - self.rotor_speeds[2]) * 1e-6
        torque_pitch = self.arm_length * (self.rotor_speeds[0] + self.rotor_speeds[1] - self.rotor_speeds[2] - self.rotor_speeds[3]) * 1e-6
        torque_yaw = (self.rotor_speeds[0] - self.rotor_speeds[1] + self.rotor_speeds[2] - self.rotor_speeds[3]) * 1e-6

        # Update linear acceleration
        acceleration = np.array([0.0, 0.0, thrust / self.mass - self.gravity])
        self.velocity += acceleration * self.dt
        self.position += self.velocity * self.dt

        # Update angular acceleration
        angular_acceleration = np.array([torque_roll, torque_pitch, torque_yaw]) / self.inertia.diagonal()
        self.angular_velocity += angular_acceleration * self.dt
        self.orientation += self.angular_velocity * self.dt

    def simulate_step(self):
        """
        Simulates a single time step of the quadcopter's flight dynamics.
        """
        self.compute_rotor_speeds()
        self.update_dynamics()

    def get_state(self):
        """
        Returns the current state of the quadcopter (position, velocity, orientation, angular velocity).
        """
        return {
            "position": self.position,
            "velocity": self.velocity,
            "orientation": self.orientation,
            "angular_velocity": self.angular_velocity,
            "rotor_speeds": self.rotor_speeds
        }


# Example usage:
if __name__ == "__main__":
    # Create a quadcopter instance
    drone = Quadcopter()

    # Set control inputs (throttle, roll, pitch, yaw)
    drone.set_inputs(throttle=0.5, roll=0.1, pitch=-0.1, yaw=0.05)

    # Simulate for 100 steps
    for _ in range(100):
        drone.simulate_step()
        state = drone.get_state()
        print(state)
```
