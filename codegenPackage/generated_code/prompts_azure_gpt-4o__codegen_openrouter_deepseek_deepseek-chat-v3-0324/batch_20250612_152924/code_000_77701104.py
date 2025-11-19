"""
Generated Code Metadata:
========================
Original URL: https://mydrones.gr
Prompt: Write Python code to simulate the speed variation of quadcopter rotors to achieve specific thrust and control, as described on the "Drone Media" website.
Generated: DETERMINISTIC_77701104826820a8
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
import time

class Quadcopter:
    """
    A class to simulate quadcopter rotor speed control for thrust and attitude control.
    
    Attributes:
        mass (float): Mass of the quadcopter in kg.
        gravity (float): Acceleration due to gravity (m/s^2).
        arm_length (float): Length of the quadcopter arm in meters.
        thrust_coefficient (float): Thrust coefficient (N/(rad/s)^2).
        drag_coefficient (float): Drag coefficient (Nm/(rad/s)^2).
        inertia (np.array): Moment of inertia matrix (3x3) in kg*m^2.
        max_rpm (float): Maximum rotor RPM.
        min_rpm (float): Minimum rotor RPM.
        rotor_speeds (np.array): Current rotor speeds in rad/s (4 elements).
    """
    
    def __init__(self, mass=1.0, arm_length=0.25, thrust_coefficient=1e-5, 
                 drag_coefficient=1e-6, max_rpm=10000, min_rpm=2000):
        """
        Initialize the quadcopter with given parameters.
        
        Args:
            mass: Mass in kg (default 1.0).
            arm_length: Arm length in meters (default 0.25).
            thrust_coefficient: Thrust coefficient in N/(rad/s)^2 (default 1e-5).
            drag_coefficient: Drag coefficient in Nm/(rad/s)^2 (default 1e-6).
            max_rpm: Maximum rotor RPM (default 10000).
            min_rpm: Minimum rotor RPM (default 2000).
        """
        self.mass = mass
        self.gravity = 9.81
        self.arm_length = arm_length
        self.thrust_coefficient = thrust_coefficient
        self.drag_coefficient = drag_coefficient
        self.max_rpm = max_rpm
        self.min_rpm = min_rpm
        
        # Moment of inertia matrix (simplified as diagonal)
        self.inertia = np.diag([0.01, 0.01, 0.02])
        
        # Initialize rotor speeds (in rad/s)
        self.rotor_speeds = np.zeros(4)
        
    def rpm_to_rads(self, rpm):
        """Convert RPM to rad/s."""
        return rpm * (2 * np.pi) / 60
    
    def rads_to_rpm(self, rads):
        """Convert rad/s to RPM."""
        return rads * 60 / (2 * np.pi)
    
    def clamp_speed(self, speed):
        """Clamp rotor speed within min/max limits."""
        max_rads = self.rpm_to_rads(self.max_rpm)
        min_rads = self.rpm_to_rads(self.min_rpm)
        return np.clip(speed, min_rads, max_rads)
    
    def calculate_thrust(self, speeds):
        """Calculate total thrust from rotor speeds."""
        return self.thrust_coefficient * np.sum(speeds**2)
    
    def calculate_torques(self, speeds):
        """Calculate torques (roll, pitch, yaw) from rotor speeds."""
        # Thrust differences for roll and pitch
        roll_torque = self.arm_length * self.thrust_coefficient * (speeds[0]**2 - speeds[1]**2)
        pitch_torque = self.arm_length * self.thrust_coefficient * (speeds[2]**2 - speeds[3]**2)
        
        # Yaw torque from drag differences
        yaw_torque = self.drag_coefficient * (speeds[0]**2 + speeds[1]**2 - speeds[2]**2 - speeds[3]**2)
        
        return np.array([roll_torque, pitch_torque, yaw_torque])
    
    def update_rotor_speeds(self, thrust_command, roll_command, pitch_command, yaw_command):
        """
        Update rotor speeds based on control commands.
        
        Args:
            thrust_command: Desired total thrust (N).
            roll_command: Desired roll torque (Nm).
            pitch_command: Desired pitch torque (Nm).
            yaw_command: Desired yaw torque (Nm).
            
        Returns:
            Updated rotor speeds in rad/s.
        """
        # Convert commands to rotor speed changes
        a = self.thrust_coefficient
        b = self.drag_coefficient
        L = self.arm_length
        
        # Mixing matrix (converts commands to individual rotor speeds)
        mixing_matrix = np.array([
            [1, 1, 1, 1],     # Thrust
            [1, -1, 0, 0],    # Roll
            [0, 0, 1, -1],    # Pitch
            [1, 1, -1, -1]    # Yaw
        ])
        
        # Command vector
        commands = np.array([
            thrust_command / (4 * a),
            roll_command / (2 * a * L),
            pitch_command / (2 * a * L),
            yaw_command / (4 * b)
        ])
        
        # Solve for squared rotor speeds
        squared_speeds = np.linalg.solve(mixing_matrix, commands)
        
        # Ensure all squared speeds are positive
        squared_speeds = np.maximum(squared_speeds, 0)
        
        # Calculate actual speeds
        new_speeds = np.sqrt(squared_speeds)
        
        # Clamp speeds to valid range
        self.rotor_speeds = self.clamp_speed(new_speeds)
        
        return self.rotor_speeds
    
    def hover_control(self, dt=0.01, tolerance=0.1):
        """
        Simple hover control loop to maintain altitude.
        
        Args:
            dt: Time step for control loop (default 0.01s).
            tolerance: Thrust tolerance for hover (default 0.1N).
        """
        target_thrust = self.mass * self.gravity
        current_thrust = self.calculate_thrust(self.rotor_speeds)
        
        while abs(current_thrust - target_thrust) > tolerance:
            # Simple proportional control
            error = target_thrust - current_thrust
            thrust_command = current_thrust + error * 0.5
            
            # Update rotor speeds with zero attitude commands
            self.update_rotor_speeds(thrust_command, 0, 0, 0)
            current_thrust = self.calculate_thrust(self.rotor_speeds)
            
            # Simulate time passing
            time.sleep(dt)
    
    def get_rotor_rpms(self):
        """Get current rotor speeds in RPM."""
        return np.array([self.rads_to_rpm(speed) for speed in self.rotor_speeds])
    
    def print_status(self):
        """Print current quadcopter status."""
        rpms = self.get_rotor_rpms()
        thrust = self.calculate_thrust(self.rotor_speeds)
        torques = self.calculate_torques(self.rotor_speeds)
        
        print(f"Rotor RPMs: {rpms}")
        print(f"Total Thrust: {thrust:.2f} N")
        print(f"Torques (Roll, Pitch, Yaw): {torques} Nm")


# Example usage
if __name__ == "__main__":
    # Create a quadcopter instance
    drone = Quadcopter(mass=1.5, arm_length=0.3)
    
    # Initial rotor speed update
    print("Initializing rotors...")
    drone.update_rotor_speeds(thrust_command=14.715, roll_command=0, pitch_command=0, yaw_command=0)
    drone.print_status()
    
    # Simulate hover
    print("\nInitiating hover control...")
    drone.hover_control()
    drone.print_status()
    
    # Simulate a maneuver
    print("\nPerforming roll maneuver...")
    drone.update_rotor_speeds(thrust_command=14.715, roll_command=0.5, pitch_command=0, yaw_command=0)
    drone.print_status()
```
