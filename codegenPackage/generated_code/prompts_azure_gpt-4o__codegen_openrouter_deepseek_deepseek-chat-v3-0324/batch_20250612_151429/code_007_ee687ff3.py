"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Generate a Python script to optimize space utilization in interior design projects, inspired by SOM Civil Engineers' interior designing and contracting services.
Generated: DETERMINISTIC_ee687ff33eefedcf
Batch ID: 20250612_151429
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
from typing import List, Tuple, Dict, Optional
import json
import logging
from dataclasses import dataclass

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class Furniture:
    """Class representing a piece of furniture."""
    name: str
    width: float
    depth: float
    height: float
    quantity: int = 1
    fixed_position: bool = False
    x: Optional[float] = None
    y: Optional[float] = None

@dataclass
class Room:
    """Class representing a room with dimensions and furniture."""
    width: float
    depth: float
    height: float
    furniture: List[Furniture]
    door_positions: List[Tuple[float, float]] = None
    window_positions: List[Tuple[float, float]] = None

class SpaceOptimizer:
    """Optimizes furniture placement in a room for maximum space utilization."""
    
    def __init__(self, room: Room):
        self.room = room
        self.validate_inputs()
        
    def validate_inputs(self) -> None:
        """Validate room and furniture dimensions."""
        if self.room.width <= 0 or self.room.depth <= 0 or self.room.height <= 0:
            raise ValueError("Room dimensions must be positive")
            
        for item in self.room.furniture:
            if item.width <= 0 or item.depth <= 0 or item.height <= 0:
                raise ValueError(f"Furniture {item.name} has invalid dimensions")
            if item.height > self.room.height:
                logger.warning(f"Furniture {item.name} is taller than room height")
    
    def calculate_total_furniture_area(self) -> float:
        """Calculate total area occupied by all furniture pieces."""
        total_area = 0.0
        for item in self.room.furniture:
            total_area += (item.width * item.depth) * item.quantity
        return total_area
    
    def calculate_room_area(self) -> float:
        """Calculate total area of the room."""
        return self.room.width * self.room.depth
    
    def space_utilization_ratio(self) -> float:
        """Calculate current space utilization ratio."""
        return self.calculate_total_furniture_area() / self.calculate_room_area()
    
    def furniture_collision(self, x: np.ndarray) -> float:
        """Calculate collision penalty between furniture items."""
        penalty = 0.0
        n = len(self.room.furniture)
        
        for i in range(n):
            if self.room.furniture[i].fixed_position:
                continue
                
            xi, yi = x[2*i], x[2*i+1]
            wi, di = self.room.furniture[i].width, self.room.furniture[i].depth
            
            # Check room boundaries
            if xi < 0 or yi < 0 or xi + wi > self.room.width or yi + di > self.room.depth:
                penalty += 1000  # Large penalty for out-of-bounds
            
            # Check other furniture
            for j in range(i+1, n):
                xj, yj = x[2*j], x[2*j+1]
                wj, dj = self.room.furniture[j].width, self.room.furniture[j].depth
                
                # Check for overlap
                if not (xi + wi <= xj or xj + wj <= xi or yi + di <= yj or yj + dj <= yi):
                    penalty += 1000  # Large penalty for collisions
        
        return penalty
    
    def optimize_layout(self) -> Dict:
        """Optimize furniture layout to maximize space utilization."""
        try:
            # Initial positions (center of room for non-fixed items)
            x0 = []
            for item in self.room.furniture:
                if item.fixed_position:
                    x0.extend([item.x, item.y])
                else:
                    x0.extend([
                        (self.room.width - item.width) / 2,
                        (self.room.depth - item.depth) / 2
                    ])
            
            x0 = np.array(x0)
            
            # Define objective function (minimize unused space + collisions)
            def objective(x):
                # Calculate unused space (negative of space utilization)
                unused_space = 1 - self.space_utilization_ratio()
                # Add collision penalty
                return unused_space + self.furniture_collision(x)
            
            # Run optimization
            result = minimize(
                objective,
                x0,
                method='L-BFGS-B',
                options={'maxiter': 1000, 'disp': True}
            )
            
            if not result.success:
                logger.warning("Optimization did not converge successfully")
            
            # Update furniture positions with optimized values
            optimized_positions = {}
            for i, item in enumerate(self.room.furniture):
                if not item.fixed_position:
                    item.x = result.x[2*i]
                    item.y = result.x[2*i+1]
                optimized_positions[item.name] = (item.x, item.y)
            
            return {
                'success': result.success,
                'message': result.message,
                'optimized_positions': optimized_positions,
                'space_utilization': self.space_utilization_ratio(),
                'total_furniture_area': self.calculate_total_furniture_area(),
                'room_area': self.calculate_room_area()
            }
            
        except Exception as e:
            logger.error(f"Error during optimization: {str(e)}")
            raise
    
    def visualize_layout(self) -> None:
        """Simple ASCII visualization of the room layout."""
        try:
            room_width = int(self.room.width)
            room_depth = int(self.room.depth)
            
            # Create empty room grid
            grid = [['.' for _ in range(room_width)] for _ in range(room_depth)]
            
            # Mark walls
            for i in range(room_depth):
                grid[i][0] = '|'
                grid[i][-1] = '|'
            for j in range(room_width):
                grid[0][j] = '-'
                grid[-1][j] = '-'
            
            # Place furniture
            for item in self.room.furniture:
                if item.x is None or item.y is None:
                    continue
                    
                x_start = int(item.x)
                y_start = int(item.y)
                x_end = min(x_start + int(item.width), room_width - 1)
                y_end = min(y_start + int(item.depth), room_depth - 1)
                
                for i in range(y_start, y_end):
                    for j in range(x_start, x_end):
                        if 0 <= i < room_depth and 0 <= j < room_width:
                            grid[i][j] = item.name[0].upper()  # First letter of furniture name
            
            # Print the grid
            print("\nRoom Layout:")
            for row in grid:
                print(' '.join(row))
            print(f"\nSpace Utilization: {self.space_utilization_ratio()*100:.2f}%")
            
        except Exception as e:
            logger.error(f"Error during visualization: {str(e)}")

def load_config(config_file: str) -> Room:
    """Load room configuration from JSON file."""
    try:
        with open(config_file, 'r') as f:
            data = json.load(f)
            
        furniture = [
            Furniture(
                name=item['name'],
                width=item['width'],
                depth=item['depth'],
                height=item['height'],
                quantity=item.get('quantity', 1),
                fixed_position=item.get('fixed_position', False),
                x=item.get('x'),
                y=item.get('y')
            ) for item in data['furniture']
        ]
        
        return Room(
            width=data['room']['width'],
            depth=data['room']['depth'],
            height=data['room']['height'],
            furniture=furniture,
            door_positions=data.get('door_positions'),
            window_positions=data.get('window_positions')
        )
        
    except Exception as e:
        logger.error(f"Error loading config: {str(e)}")
        raise

def main():
    """Main function to demonstrate space optimization."""
    try:
        # Example usage
        room = Room(
            width=10,
            depth=8,
            height=3,
            furniture=[
                Furniture(name="desk", width=1.5, depth=0.8, height=0.7, quantity=2),
                Furniture(name="chair", width=0.5, depth=0.5, height=0.9, quantity=4),
                Furniture(name="sofa", width=2.0, depth=1.0, height=0.8, quantity=1),
                Furniture(name="bookshelf", width=1.0, depth=0.3, height=2.0, quantity=1, fixed_position=True, x=
