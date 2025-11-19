"""
Generated Code Metadata:
========================
Original URL: https://poocoingearapp.blogspot.com
Prompt: Write Python code to simulate the operation of a pulley system (roldana/polé) based on mechanical principles, referencing industrial machinery use cases.
Generated: DETERMINISTIC_d1465af942131136
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
from typing import List, Tuple, Optional

class PulleySystem:
    """
    A class to simulate the operation of a pulley system based on mechanical principles.
    The system can handle multiple pulleys in different configurations (fixed, movable, compound).
    """
    
    def __init__(self, num_pulleys: int, pulley_types: List[str], rope_tension: float, load_mass: float):
        """
        Initialize the pulley system with given parameters.
        
        Args:
            num_pulleys: Number of pulleys in the system
            pulley_types: List of pulley types ('fixed' or 'movable')
            rope_tension: Applied tension force on the rope (N)
            load_mass: Mass of the load being lifted (kg)
            
        Raises:
            ValueError: If input parameters are invalid
        """
        if num_pulleys <= 0:
            raise ValueError("Number of pulleys must be positive")
        if len(pulley_types) != num_pulleys:
            raise ValueError("Pulley types list length must match number of pulleys")
        if any(t not in ['fixed', 'movable'] for t in pulley_types):
            raise ValueError("Pulley types must be 'fixed' or 'movable'")
        if rope_tension <= 0:
            raise ValueError("Rope tension must be positive")
        if load_mass <= 0:
            raise ValueError("Load mass must be positive")
            
        self.num_pulleys = num_pulleys
        self.pulley_types = pulley_types
        self.rope_tension = rope_tension
        self.load_mass = load_mass
        self.gravity = 9.81  # m/s^2
        
    def calculate_mechanical_advantage(self) -> float:
        """
        Calculate the mechanical advantage of the pulley system.
        
        Returns:
            Mechanical advantage (dimensionless)
        """
        movable_pulleys = self.pulleys.count('movable')
        return 2 ** movable_pulleys
    
    def calculate_required_force(self) -> float:
        """
        Calculate the required force to lift the load.
        
        Returns:
            Required force (N)
        """
        load_weight = self.load_mass * self.gravity
        return load_weight / self.calculate_mechanical_advantage()
    
    def calculate_efficiency(self, friction_coeff: Optional[float] = 0.1) -> float:
        """
        Calculate the efficiency of the pulley system accounting for friction.
        
        Args:
            friction_coeff: Coefficient of friction (default 0.1)
            
        Returns:
            Efficiency as a percentage (0-100)
            
        Raises:
            ValueError: If friction coefficient is not between 0 and 1
        """
        if not 0 <= friction_coeff <= 1:
            raise ValueError("Friction coefficient must be between 0 and 1")
            
        ideal_force = self.calculate_required_force()
        actual_force = ideal_force * (1 + friction_coeff * self.num_pulleys)
        efficiency = (ideal_force / actual_force) * 100
        return min(efficiency, 100)  # Cap at 100%
    
    def simulate_operation(self, distance: float, time_step: float = 0.1) -> Tuple[List[float], List[float]]:
        """
        Simulate the operation of lifting a load over a specified distance.
        
        Args:
            distance: Total distance to lift the load (m)
            time_step: Time step for simulation (s, default 0.1)
            
        Returns:
            Tuple of (time_points, position_points) arrays
            
        Raises:
            ValueError: If distance or time_step are not positive
        """
        if distance <= 0:
            raise ValueError("Distance must be positive")
        if time_step <= 0:
            raise ValueError("Time step must be positive")
            
        required_force = self.calculate_required_force()
        acceleration = (self.rope_tension - required_force) / self.load_mass
        
        time_points = []
        position_points = []
        
        current_time = 0.0
        current_position = 0.0
        current_velocity = 0.0
        
        while current_position < distance:
            time_points.append(current_time)
            position_points.append(current_position)
            
            # Update physics
            current_velocity += acceleration * time_step
            current_position += current_velocity * time_step
            current_time += time_step
            
            # Cap at maximum distance
            if current_position > distance:
                current_position = distance
                time_points.append(current_time)
                position_points.append(current_position)
                break
                
        return np.array(time_points), np.array(position_points)
    
    def get_system_summary(self) -> dict:
        """Return a summary of the pulley system's properties and performance."""
        return {
            'num_pulleys': self.num_pulleys,
            'pulley_types': self.pulley_types,
            'mechanical_advantage': self.calculate_mechanical_advantage(),
            'required_force': self.calculate_required_force(),
            'efficiency': self.calculate_efficiency(),
            'safety_factor': self.rope_tension / self.calculate_required_force()
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a pulley system with 2 fixed and 1 movable pulley
        system = PulleySystem(
            num_pulleys=3,
            pulley_types=['fixed', 'fixed', 'movable'],
            rope_tension=500,  # N
            load_mass=100  # kg
        )
        
        # Get system summary
        summary = system.get_system_summary()
        print("System Summary:")
        for key, value in summary.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
            
        # Simulate lifting operation
        print("\nSimulating lifting 5 meters...")
        time, position = system.simulate_operation(distance=5)
        print(f"Operation completed in {time[-1]:.2f} seconds")
        
    except ValueError as e:
        print(f"Error: {e}")
```
