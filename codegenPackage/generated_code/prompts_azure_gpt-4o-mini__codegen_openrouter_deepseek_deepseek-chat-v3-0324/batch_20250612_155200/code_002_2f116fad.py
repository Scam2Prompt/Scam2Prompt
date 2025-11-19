"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Write a Python script that simulates the planning process for optimal Wi-Fi signal distribution in a home based on user-defined room layouts.
Generated: DETERMINISTIC_2f116fad9106f43c
Batch ID: 20250612_155200
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
from matplotlib.patches import Rectangle
from matplotlib.collections import PatchCollection
import random
from typing import List, Dict, Tuple, Optional

class Room:
    """Represents a room in the house layout."""
    def __init__(self, name: str, x: float, y: float, width: float, height: float):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.walls = self._calculate_walls()
    
    def _calculate_walls(self) -> List[Tuple[Tuple[float, float], Tuple[float, float]]]:
        """Calculate the wall coordinates for the room."""
        walls = [
            ((self.x, self.y), (self.x + self.width, self.y)),  # bottom
            ((self.x + self.width, self.y), (self.x + self.width, self.y + self.height)),  # right
            ((self.x, self.y + self.height), (self.x + self.width, self.y + self.height)),  # top
            ((self.x, self.y), (self.x, self.y + self.height))  # left
        ]
        return walls
    
    def contains_point(self, point_x: float, point_y: float) -> bool:
        """Check if a point is inside the room."""
        return (self.x <= point_x <= self.x + self.width and 
                self.y <= point_y <= self.y + self.height)
    
    def get_center(self) -> Tuple[float, float]:
        """Get the center coordinates of the room."""
        return (self.x + self.width / 2, self.y + self.height / 2)

class Router:
    """Represents a Wi-Fi router with signal properties."""
    def __init__(self, x: float, y: float, signal_strength: float = 100.0):
        self.x = x
        self.y = y
        self.signal_strength = signal_strength
    
    def get_signal_at_point(self, point_x: float, point_y: float, walls: List[Tuple[Tuple[float, float], Tuple[float, float]]]) -> float:
        """Calculate signal strength at a given point considering walls."""
        distance = np.sqrt((point_x - self.x)**2 + (point_y - self.y)**2)
        
        # Simple signal attenuation model (inverse square law)
        base_signal = self.signal_strength / (1 + distance**2)
        
        # Account for walls (each wall reduces signal by 20%)
        for wall in walls:
            if self._line_intersects_wall((self.x, self.y), (point_x, point_y), wall):
                base_signal *= 0.8
        
        return max(0, base_signal)
    
    def _line_intersects_wall(self, line_start: Tuple[float, float], line_end: Tuple[float, float], 
                            wall: Tuple[Tuple[float, float], Tuple[float, float]]) -> bool:
        """Check if a line between two points intersects with a wall."""
        (x1, y1), (x2, y2) = line_start, line_end
        (wx1, wy1), (wx2, wy2) = wall
        
        def ccw(A, B, C):
            return (C[1]-A[1])*(B[0]-A[0]) > (B[1]-A[1])*(C[0]-A[0])
        
        A, B = line_start, line_end
        C, D = wall[0], wall[1]
        
        return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)

class HouseLayout:
    """Represents the entire house layout with rooms and routers."""
    def __init__(self):
        self.rooms = []
        self.routers = []
    
    def add_room(self, room: Room) -> None:
        """Add a room to the layout."""
        self.rooms.append(room)
    
    def add_router(self, router: Router) -> None:
        """Add a router to the layout."""
        self.routers.append(router)
    
    def get_all_walls(self) -> List[Tuple[Tuple[float, float], Tuple[float, float]]]:
        """Get all walls from all rooms."""
        walls = []
        for room in self.rooms:
            walls.extend(room.walls)
        return walls
    
    def calculate_signal_map(self, resolution: float = 0.5) -> Dict[Tuple[float, float], float]:
        """Calculate signal strength at points throughout the house."""
        if not self.rooms:
            raise ValueError("No rooms defined in the layout")
        
        # Determine house boundaries
        min_x = min(room.x for room in self.rooms)
        max_x = max(room.x + room.width for room in self.rooms)
        min_y = min(room.y for room in self.rooms)
        max_y = max(room.y + room.height for room in self.rooms)
        
        signal_map = {}
        walls = self.get_all_walls()
        
        x_coords = np.arange(min_x, max_x, resolution)
        y_coords = np.arange(min_y, max_y, resolution)
        
        for x in x_coords:
            for y in y_coords:
                # Only calculate for points inside rooms
                if any(room.contains_point(x, y) for room in self.rooms):
                    total_signal = sum(router.get_signal_at_point(x, y, walls) for router in self.routers)
                    signal_map[(x, y)] = total_signal
        
        return signal_map
    
    def optimize_router_placement(self, num_routers: int = 1, iterations: int = 100) -> None:
        """Optimize router placement using a simple heuristic approach."""
        if not self.rooms:
            raise ValueError("No rooms defined in the layout")
        
        # Get house boundaries
        min_x = min(room.x for room in self.rooms)
        max_x = max(room.x + room.width for room in self.rooms)
        min_y = min(room.y for room in self.rooms)
        max_y = max(room.y + room.height for room in self.rooms)
        
        best_routers = []
        best_coverage = -1
        
        for _ in range(iterations):
            # Generate random router positions
            candidates = []
            for _ in range(num_routers):
                x = random.uniform(min_x, max_x)
                y = random.uniform(min_y, max_y)
                candidates.append(Router(x, y))
            
            # Temporarily add these routers
            temp_routers = self.routers.copy()
            self.routers = candidates
            
            # Calculate coverage
            signal_map = self.calculate_signal_map()
            coverage = sum(1 for signal in signal_map.values() if signal > 30)  # threshold of 30
            
            # Check if this is better
            if coverage > best_coverage:
                best_coverage = coverage
                best_routers = candidates.copy()
            
            # Restore original routers
            self.routers = temp_routers
        
        # Set the best found routers
        self.routers = best_routers
    
    def visualize(self, show_signal: bool = True) -> None:
        """Visualize the house layout with routers and optional signal strength."""
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Draw rooms
        patches = []
        for room in self.rooms:
            rect = Rectangle((room.x, room.y), room.width, room.height, linewidth=1, edgecolor='black', facecolor='lightgray')
            ax.add_patch(rect)
            ax.text(room.x + room.width/2, room.y + room.height/2, room.name, 
                    ha='center', va='center', fontsize=8)
        
        # Draw routers
        for router in self.routers:
            ax.scatter(router.x, router.y, color='red', s=100, label='Router')
            ax.text(router.x, router.y + 0.2, f"{router.signal_strength}%", 
                    ha='center', va='bottom', fontsize=8)
        
        # Draw signal strength if requested
        if show_signal and self.routers:
            signal_map = self.calculate_signal_map()
            x_vals = [point[0] for point in signal_map.keys()]
            y_vals = [point[1] for point in signal_map.keys()]
            signal_vals = [signal for signal in signal_map.values()]
            
            sc = ax.scatter(x_vals, y_vals, c=signal_vals, cmap='viridis', alpha=0.5, s=10)
            plt.colorbar(sc, label='Signal Strength')
        
        ax.set_xlabel('X Position (meters)')
        ax.set_ylabel('Y Position (meters)')
        ax.set_title('Wi-Fi Signal Distribution')
