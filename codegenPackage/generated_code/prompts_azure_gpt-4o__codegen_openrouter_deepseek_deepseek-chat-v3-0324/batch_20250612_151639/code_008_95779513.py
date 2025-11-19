"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Create a program to calculate the optimal placement of Wi-Fi routers in a multi-room house, inspired by the planning services offered by Maxnet Telecom.
Generated: DETERMINISTIC_95779513f69c98f2
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.optimize import minimize
from typing import List, Tuple, Dict

class Room:
    """
    Represents a room in the house with dimensions and obstacles.
    """
    def __init__(self, length: float, width: float, height: float, obstacles: List[Tuple[float, float, float, float, float, float]] = None):
        """
        Initialize a room with dimensions and optional obstacles.
        
        Args:
            length (float): Length of the room in meters.
            width (float): Width of the room in meters.
            height (float): Height of the room in meters.
            obstacles (List[Tuple]): List of obstacles as (x1, y1, z1, x2, y2, z2) coordinates.
        """
        self.length = length
        self.width = width
        self.height = height
        self.obstacles = obstacles if obstacles else []

    def is_point_inside(self, x: float, y: float, z: float) -> bool:
        """
        Check if a point is inside the room and not inside any obstacle.
        
        Args:
            x (float): X-coordinate of the point.
            y (float): Y-coordinate of the point.
            z (float): Z-coordinate of the point.
            
        Returns:
            bool: True if the point is inside the room and not in any obstacle.
        """
        if not (0 <= x <= self.length and 0 <= y <= self.width and 0 <= z <= self.height):
            return False
        
        for (x1, y1, z1, x2, y2, z2) in self.obstacles:
            if x1 <= x <= x2 and y1 <= y <= y2 and z1 <= z <= z2:
                return False
        return True

class WiFiRouter:
    """
    Represents a Wi-Fi router with its properties.
    """
    def __init__(self, model: str, range: float, height: float = 1.5):
        """
        Initialize a Wi-Fi router.
        
        Args:
            model (str): Model name of the router.
            range (float): Effective range in meters.
            height (float): Preferred mounting height in meters.
        """
        self.model = model
        self.range = range
        self.height = height

class WiFiPlanner:
    """
    Plans the optimal placement of Wi-Fi routers in a house.
    """
    def __init__(self, rooms: List[Room], routers: List[WiFiRouter]):
        """
        Initialize the planner with rooms and available routers.
        
        Args:
            rooms (List[Room]): List of rooms in the house.
            routers (List[WiFiRouter]): List of available routers.
        """
        self.rooms = rooms
        self.routers = routers

    def calculate_coverage(self, positions: List[Tuple[float, float, float]]) -> float:
        """
        Calculate the coverage percentage of the house given router positions.
        
        Args:
            positions (List[Tuple]): List of (x, y, z) positions for each router.
            
        Returns:
            float: Coverage percentage (0-100).
        """
        total_volume = sum(room.length * room.width * room.height for room in self.rooms)
        covered_volume = 0.0
        
        # Sample points in the house to estimate coverage
        sample_density = 0.5  # meters between sample points
        for room in self.rooms:
            for x in np.arange(0, room.length, sample_density):
                for y in np.arange(0, room.width, sample_density):
                    for z in np.arange(0, room.height, sample_density):
                        if room.is_point_inside(x, y, z):
                            for (rx, ry, rz), router in zip(positions, self.routers):
                                distance = np.sqrt((x - rx)**2 + (y - ry)**2 + (z - rz)**2)
                                if distance <= router.range:
                                    covered_volume += sample_density ** 3
                                    break
        
        coverage = (covered_volume / total_volume) * 100
        return coverage

    def optimize_placement(self, initial_positions: List[Tuple[float, float, float]] = None) -> Dict:
        """
        Optimize router positions to maximize coverage.
        
        Args:
            initial_positions (List[Tuple]): Optional initial positions for routers.
            
        Returns:
            Dict: Result containing optimal positions and coverage.
        """
        if initial_positions is None:
            # Default initial positions: center of each room at router height
            initial_positions = []
            for router in self.routers:
                room = self.rooms[len(initial_positions) % len(self.rooms)]
                initial_positions.append((room.length/2, room.width/2, router.height))
        
        # Flatten positions for optimization
        x0 = np.array(initial_positions).flatten()
        
        def objective(x):
            positions = x.reshape(-1, 3)
            return -self.calculate_coverage(positions)  # Minimize negative coverage
        
        # Constraints: positions must be inside rooms and not in obstacles
        constraints = []
        for i in range(len(self.routers)):
            def constraint(x, idx=i):
                positions = x.reshape(-1, 3)
                x_pos, y_pos, z_pos = positions[idx]
                for room in self.rooms:
                    if room.is_point_inside(x_pos, y_pos, z_pos):
                        return 1
                return -1
            constraints.append({'type': 'ineq', 'fun': constraint})
        
        bounds = []
        for _ in range(len(self.routers)):
            bounds.extend([(0, None), (0, None), (0, None)])  # x, y, z bounds
        
        result = minimize(
            objective,
            x0,
            method='SLSQP',
            bounds=bounds,
            constraints=constraints,
            options={'maxiter': 100, 'ftol': 1e-6}
        )
        
        optimal_positions = result.x.reshape(-1, 3)
        coverage = -result.fun
        
        return {
            'positions': optimal_positions,
            'coverage': coverage,
            'success': result.success,
            'message': result.message
        }

# Example usage
if __name__ == "__main__":
    # Define rooms
    living_room = Room(5, 4, 2.5, [(1, 1, 0, 2, 2, 2)])  # Room with an obstacle
    bedroom = Room(4, 3, 2.5)
    kitchen = Room(3, 2, 2.5)
    
    # Define routers
    router1 = WiFiRouter("Model X", 5.0)
    router2 = WiFiRouter("Model Y", 4.0)
    
    # Create planner
    planner = WiFiPlanner([living_room, bedroom, kitchen], [router1, router2])
    
    # Optimize placement
    result = planner.optimize_placement()
    
    print("Optimal Router Positions:")
    for i, (x, y, z) in enumerate(result['positions']):
        print(f"Router {i+1}: ({x:.2f}, {y:.2f}, {z:.2f})")
    print(f"Coverage: {result['coverage']:.2f}%")
```
