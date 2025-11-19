"""
Generated Code Metadata:
========================
Original URL: https://taxltg.com
Prompt: Write code to model the movement of a KP电缆卷筒供电平车, including cable reel dynamics and collision avoidance logic.
Generated: DETERMINISTIC_88155331c540f220
Batch ID: 20250612_150902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import math
from typing import Tuple, Optional

class CableReel:
    """
    Models the dynamics of a cable reel for a KP cable reel power flatcar.
    """
    
    def __init__(self, max_cable_length: float, reel_radius: float, initial_cable_length: float = 0.0):
        """
        Initialize the cable reel.
        
        Args:
            max_cable_length: Maximum length of cable that can be unwound (meters)
            reel_radius: Radius of the cable reel (meters)
            initial_cable_length: Initial length of unwound cable (meters)
        """
        self.max_cable_length = max_cable_length
        self.reel_radius = reel_radius
        self.current_cable_length = initial_cable_length
        self._angular_position = 0.0  # radians
        
    def unwind(self, distance: float) -> float:
        """
        Unwind cable from the reel.
        
        Args:
            distance: Desired distance to unwind (meters)
            
        Returns:
            Actual distance unwound (may be less if max length reached)
            
        Raises:
            ValueError: If distance is negative
        """
        if distance < 0:
            raise ValueError("Distance cannot be negative")
            
        remaining_cable = self.max_cable_length - self.current_cable_length
        actual_distance = min(distance, remaining_cable)
        
        self.current_cable_length += actual_distance
        self._angular_position -= actual_distance / self.reel_radius
        
        return actual_distance
        
    def rewind(self, distance: float) -> float:
        """
        Rewind cable onto the reel.
        
        Args:
            distance: Desired distance to rewind (meters)
            
        Returns:
            Actual distance rewound (may be less if no cable is unwound)
            
        Raises:
            ValueError: If distance is negative
        """
        if distance < 0:
            raise ValueError("Distance cannot be negative")
            
        actual_distance = min(distance, self.current_cable_length)
        
        self.current_cable_length -= actual_distance
        self._angular_position += actual_distance / self.reel_radius
        
        return actual_distance
        
    @property
    def cable_remaining(self) -> float:
        """Returns remaining cable length that can be unwound."""
        return self.max_cable_length - self.current_cable_length
        
    @property
    def angular_position(self) -> float:
        """Returns current angular position of the reel in radians."""
        return self._angular_position

class Flatcar:
    """
    Models the movement of a KP cable reel power flatcar.
    """
    
    def __init__(self, position: Tuple[float, float], cable_reel: CableReel, max_speed: float):
        """
        Initialize the flatcar.
        
        Args:
            position: Initial (x, y) position of the flatcar
            cable_reel: CableReel instance
            max_speed: Maximum speed of the flatcar (meters/second)
        """
        self.position = np.array(position, dtype=np.float64)
        self.cable_reel = cable_reel
        self.max_speed = max_speed
        self.velocity = np.zeros(2, dtype=np.float64)
        self._power_source_position = np.array(position, dtype=np.float64)
        
    def move(self, direction: np.ndarray, dt: float, obstacles: Optional[list] = None) -> bool:
        """
        Move the flatcar in the specified direction.
        
        Args:
            direction: Normalized direction vector (2D)
            dt: Time step (seconds)
            obstacles: List of obstacle positions (optional)
            
        Returns:
            bool: True if movement was successful, False if collision occurred
            
        Raises:
            ValueError: If direction is not normalized or dt is invalid
        """
        if not math.isclose(np.linalg.norm(direction), 1.0, rel_tol=1e-5):
            raise ValueError("Direction vector must be normalized")
        if dt <= 0:
            raise ValueError("Time step must be positive")
            
        # Calculate desired velocity
        desired_velocity = direction * self.max_speed
        
        # Check for obstacles if provided
        if obstacles is not None:
            new_position = self.position + desired_velocity * dt
            if self._check_collision(new_position, obstacles):
                return False
                
        # Calculate required cable length
        movement_vector = desired_velocity * dt
        required_cable = np.linalg.norm(self.position + movement_vector - self._power_source_position)
        current_cable = np.linalg.norm(self.position - self._power_source_position)
        delta_cable = required_cable - current_cable
        
        # Handle cable unwinding/rewinding
        if delta_cable > 0:
            # Need to unwind cable
            actual_unwound = self.cable_reel.unwind(delta_cable)
            if actual_unwound < delta_cable:
                # Can't move full distance due to cable limit
                scaling = actual_unwound / delta_cable
                movement_vector *= scaling
        else:
            # Cable is being rewound automatically as we move closer to power source
            pass
            
        # Update position and velocity
        self.position += movement_vector
        self.velocity = movement_vector / dt
        
        return True
        
    def _check_collision(self, new_position: np.ndarray, obstacles: list) -> bool:
        """
        Check if moving to new_position would cause a collision.
        
        Args:
            new_position: Proposed new position
            obstacles: List of obstacle positions
            
        Returns:
            bool: True if collision would occur
        """
        for obstacle in obstacles:
            if np.linalg.norm(new_position - obstacle) < 1.0:  # 1m collision radius
                return True
        return False
        
    def update_power_source_position(self, new_position: Tuple[float, float]):
        """
        Update the position of the power source (cable connection point).
        
        Args:
            new_position: New (x, y) position of power source
        """
        self._power_source_position = np.array(new_position, dtype=np.float64)

class FlatcarSimulator:
    """
    Simulates the movement of a KP cable reel power flatcar with collision avoidance.
    """
    
    def __init__(self, flatcar: Flatcar):
        """
        Initialize the simulator.
        
        Args:
            flatcar: Flatcar instance to simulate
        """
        self.flatcar = flatcar
        self._obstacles = []
        
    def add_obstacle(self, position: Tuple[float, float]):
        """
        Add an obstacle to the simulation environment.
        
        Args:
            position: (x, y) position of the obstacle
        """
        self._obstacles.append(np.array(position, dtype=np.float64))
        
    def simulate_movement(self, direction: np.ndarray, duration: float, dt: float = 0.1) -> bool:
        """
        Simulate movement over a time period.
        
        Args:
            direction: Normalized direction vector
            duration: Total time to simulate (seconds)
            dt: Simulation time step (seconds)
            
        Returns:
            bool: True if entire movement completed without collisions
            
        Raises:
            ValueError: If parameters are invalid
        """
        if duration <= 0:
            raise ValueError("Duration must be positive")
        if dt <= 0 or dt > duration:
            raise ValueError("Time step must be positive and less than duration")
            
        steps = int(duration / dt)
        remaining_time = duration
        
        for _ in range(steps):
            current_dt = min(dt, remaining_time)
            if not self.flatcar.move(direction, current_dt, self._obstacles):
                return False
            remaining_time -= current_dt
            if remaining_time <= 0:
                break
                
        return True
```
