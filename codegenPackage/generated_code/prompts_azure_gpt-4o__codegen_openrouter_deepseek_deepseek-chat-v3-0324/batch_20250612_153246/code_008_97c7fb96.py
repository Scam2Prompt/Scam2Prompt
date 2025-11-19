"""
Generated Code Metadata:
========================
Original URL: https://econtrolsa.ch
Prompt: Develop a Python script to simulate dual motor AWD electric vehicle performance, referencing the specifications provided for car models on eControl SA's website.
Generated: DETERMINISTIC_97c7fb96caac1629
Batch ID: 20250612_153246
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
from dataclasses import dataclass
from typing import Optional, Tuple

@dataclass
class MotorSpecs:
    """Dataclass to store motor specifications."""
    max_power_kw: float
    max_torque_nm: float
    efficiency: float  # as a decimal (e.g., 0.95 for 95%)

@dataclass
class BatterySpecs:
    """Dataclass to store battery specifications."""
    capacity_kwh: float
    voltage: float
    max_discharge_rate: float  # as a decimal (e.g., 0.8 for 80%)

@dataclass
class VehicleDynamics:
    """Dataclass to store vehicle dynamics parameters."""
    mass_kg: float
    drag_coefficient: float
    frontal_area_m2: float
    rolling_resistance: float
    wheel_radius_m: float

class DualMotorAWDSimulator:
    """
    Simulates the performance of a dual motor AWD electric vehicle.
    
    Attributes:
        motor_front (MotorSpecs): Front motor specifications.
        motor_rear (MotorSpecs): Rear motor specifications.
        battery (BatterySpecs): Battery specifications.
        dynamics (VehicleDynamics): Vehicle dynamics parameters.
    """
    
    def __init__(
        self,
        motor_front: MotorSpecs,
        motor_rear: MotorSpecs,
        battery: BatterySpecs,
        dynamics: VehicleDynamics
    ):
        """Initialize the simulator with vehicle specifications."""
        self.motor_front = motor_front
        self.motor_rear = motor_rear
        self.battery = battery
        self.dynamics = dynamics
        
        # Constants
        self.AIR_DENSITY = 1.225  # kg/m^3
        self.GRAVITY = 9.81  # m/s^2
        
    def calculate_power_requirements(
        self,
        speed_mps: float,
        acceleration_mps2: float,
        grade_deg: float = 0.0
    ) -> Tuple[float, float]:
        """
        Calculate the total power required to maintain given speed and acceleration.
        
        Args:
            speed_mps: Vehicle speed in meters per second.
            acceleration_mps2: Vehicle acceleration in meters per second squared.
            grade_deg: Road grade in degrees (positive for uphill).
            
        Returns:
            Tuple of (total_power_w, battery_power_w) where:
                total_power_w: Total mechanical power required (Watts).
                battery_power_w: Battery power required accounting for motor efficiency (Watts).
        """
        try:
            # Convert grade to radians for calculation
            grade_rad = np.deg2rad(grade_deg)
            
            # Aerodynamic drag force
            drag_force = 0.5 * self.AIR_DENSITY * self.dynamics.drag_coefficient * \
                         self.dynamics.frontal_area_m2 * speed_mps**2
            
            # Rolling resistance force
            rolling_force = self.dynamics.rolling_resistance * self.dynamics.mass_kg * \
                           self.GRAVITY * np.cos(grade_rad)
            
            # Grade force
            grade_force = self.dynamics.mass_kg * self.GRAVITY * np.sin(grade_rad)
            
            # Acceleration force
            acceleration_force = self.dynamics.mass_kg * acceleration_mps2
            
            # Total force
            total_force = drag_force + rolling_force + grade_force + acceleration_force
            
            # Mechanical power required
            total_power_w = total_force * speed_mps
            
            # Battery power required (accounting for motor efficiency)
            # Assuming equal power distribution between front and rear motors
            front_power = total_power_w / 2 / self.motor_front.efficiency
            rear_power = total_power_w / 2 / self.motor_rear.efficiency
            battery_power_w = front_power + rear_power
            
            return total_power_w, battery_power_w
            
        except Exception as e:
            raise RuntimeError(f"Error calculating power requirements: {str(e)}")
    
    def simulate_acceleration(
        self,
        initial_speed_mps: float = 0.0,
        duration_sec: float = 10.0,
        time_step_sec: float = 0.1,
        max_speed_mps: Optional[float] = None,
        grade_deg: float = 0.0
    ) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Simulate vehicle acceleration over time.
        
        Args:
            initial_speed_mps: Initial speed in m/s (default 0).
            duration_sec: Duration of simulation in seconds (default 10).
            time_step_sec: Time step for simulation in seconds (default 0.1).
            max_speed_mps: Optional maximum speed limit in m/s.
            grade_deg: Road grade in degrees (default 0).
            
        Returns:
            Tuple of (time_array, speed_array, battery_power_array) numpy arrays.
        """
        try:
            # Initialize arrays
            steps = int(duration_sec / time_step_sec)
            time_array = np.linspace(0, duration_sec, steps)
            speed_array = np.zeros(steps)
            battery_power_array = np.zeros(steps)
            
            speed_array[0] = initial_speed_mps
            
            for i in range(1, steps):
                # Calculate available torque from both motors
                front_torque = min(
                    self.motor_front.max_torque_nm,
                    self.motor_front.max_power_kw * 1000 / (speed_array[i-1] + 0.001)
                )
                rear_torque = min(
                    self.motor_rear.max_torque_nm,
                    self.motor_rear.max_power_kw * 1000 / (speed_array[i-1] + 0.001)
                )
                
                total_torque = front_torque + rear_torque
                
                # Calculate acceleration (F = ma, F = torque / wheel_radius)
                acceleration = total_torque / self.dynamics.wheel_radius_m / self.dynamics.mass_kg
                
                # Update speed
                new_speed = speed_array[i-1] + acceleration * time_step_sec
                
                # Apply speed limit if specified
                if max_speed_mps is not None:
                    new_speed = min(new_speed, max_speed_mps)
                
                speed_array[i] = new_speed
                
                # Calculate power requirements
                _, battery_power = self.calculate_power_requirements(
                    speed=new_speed,
                    acceleration=acceleration,
                    grade_deg=grade_deg
                )
                battery_power_array[i] = battery_power
                
            return time_array, speed_array, battery_power_array
            
        except Exception as e:
            raise RuntimeError(f"Error during acceleration simulation: {str(e)}")
    
    def plot_simulation_results(
        self,
        time_array: np.ndarray,
        speed_array: np.ndarray,
        power_array: np.ndarray
    ) -> None:
        """Plot the simulation results."""
        try:
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
            
            # Speed plot
            ax1.plot(time_array, speed_array * 3.6)  # Convert to km/h for display
            ax1.set_xlabel('Time (s)')
            ax1.set_ylabel('Speed (km/h)')
            ax1.set_title('Vehicle Speed vs Time')
            ax1.grid(True)
            
            # Power plot
            ax2.plot(time_array, power_array / 1000)  # Convert to kW for display
            ax2.set_xlabel('Time (s)')
            ax2.set_ylabel('Battery Power (kW)')
            ax2.set_title('Battery Power vs Time')
            ax2.grid(True)
            
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            raise RuntimeError(f"Error plotting results: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Example specifications (similar to eControl SA models)
    front_motor = MotorSpecs(
        max_power_kw=150,
        max_torque_nm=250,
        efficiency=0.95
    )
    
    rear_motor = MotorSpecs(
        max_power_kw=150,
        max_torque_nm=250,
        efficiency=0.95
    )
    
    battery = BatterySpecs(
        capacity_kwh=75,
        voltage=400,
        max_discharge_rate=0.8
    )
    
    dynamics = VehicleDynamics(
        mass_kg=2000,
        drag_coefficient=0.24,
        frontal_area_m2=2.4,
        rolling_resistance=0.015,
        wheel_radius_m=0.35
    )
    
    # Create simulator
    simulator = DualMotorAWDSimulator(front_motor, rear_m
