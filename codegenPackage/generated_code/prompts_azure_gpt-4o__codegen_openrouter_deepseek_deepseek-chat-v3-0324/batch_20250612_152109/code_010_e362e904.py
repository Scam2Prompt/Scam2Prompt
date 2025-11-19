"""
Generated Code Metadata:
========================
Original URL: https://udizine.com
Prompt: Write code to optimize the placement of UDIZINE's SlatWall accessories for displaying a mix of clothing, shoes, and eyewear in a retail store.
Generated: DETERMINISTIC_e362e9047b2a70c9
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.optimize import linear_sum_assignment
from typing import List, Dict, Tuple

class SlatWallOptimizer:
    """
    Optimizes placement of UDIZINE's SlatWall accessories for retail displays.
    Handles clothing, shoes, and eyewear placement with constraints.
    """
    
    def __init__(self, wall_width: float, wall_height: float):
        """
        Initialize with wall dimensions in inches.
        
        Args:
            wall_width: Total width of available slat wall space
            wall_height: Total height of available slat wall space
        """
        self.wall_width = wall_width
        self.wall_height = wall_height
        self.accessories = []
        self.categories = {
            'clothing': {'weight': 0.5, 'min_height': 12},
            'shoes': {'weight': 0.3, 'min_height': 6},
            'eyewear': {'weight': 0.2, 'min_height': 4}
        }
        
    def add_accessory(self, name: str, category: str, width: float, height: float, 
                      priority: int = 1) -> None:
        """
        Add an accessory to be placed on the slat wall.
        
        Args:
            name: Identifier for the accessory
            category: Type of accessory (clothing/shoes/eyewear)
            width: Width of accessory in inches
            height: Height of accessory in inches
            priority: Placement priority (1-10, 10 being highest)
        """
        if category not in self.categories:
            raise ValueError(f"Invalid category. Must be one of {list(self.categories.keys())}")
            
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive numbers")
            
        if priority < 1 or priority > 10:
            raise ValueError("Priority must be between 1 and 10")
            
        self.accessories.append({
            'name': name,
            'category': category,
            'width': width,
            'height': height,
            'priority': priority,
            'area': width * height
        })
        
    def _calculate_cost_matrix(self) -> np.ndarray:
        """
        Create cost matrix for linear assignment problem.
        
        Returns:
            Numpy array representing cost matrix
        """
        num_accessories = len(self.accessories)
        cost_matrix = np.zeros((num_accessories, num_accessories))
        
        for i, acc in enumerate(self.accessories):
            for j in range(num_accessories):
                # Cost based on category weight, priority, and area utilization
                category_weight = self.categories[acc['category']]['weight']
                priority_factor = (11 - acc['priority']) / 10  # Higher priority = lower cost
                area_utilization = acc['area'] / (self.wall_width * self.wall_height)
                
                cost_matrix[i][j] = (
                    (1 - category_weight) * 0.5 + 
                    priority_factor * 0.3 + 
                    (1 - area_utilization) * 0.2
                )
                
        return cost_matrix
    
    def _validate_placement(self, positions: List[Tuple[float, float]]) -> bool:
        """
        Validate that all accessories fit within wall dimensions.
        
        Args:
            positions: List of (x, y) positions for accessories
            
        Returns:
            bool: True if all placements are valid
        """
        for i, (x, y) in enumerate(positions):
            acc = self.accessories[i]
            if (x + acc['width'] > self.wall_width or 
                y + acc['height'] > self.wall_height):
                return False
                
            # Check category-specific height constraints
            min_height = self.categories[acc['category']]['min_height']
            if y + acc['height'] > min_height:
                return False
                
        return True
    
    def optimize_placement(self) -> Dict[str, Tuple[float, float]]:
        """
        Optimize accessory placement using linear assignment algorithm.
        
        Returns:
            Dictionary mapping accessory names to (x, y) positions
        """
        if not self.accessories:
            return {}
            
        cost_matrix = self._calculate_cost_matrix()
        row_ind, col_ind = linear_sum_assignment(cost_matrix)
        
        # Generate potential positions
        positions = []
        x, y = 0, 0
        current_row_height = 0
        
        for i in col_ind:
            acc = self.accessories[i]
            
            # Check if accessory fits in current row
            if x + acc['width'] > self.wall_width:
                x = 0
                y += current_row_height
                current_row_height = 0
                
            positions.append((x, y))
            x += acc['width']
            current_row_height = max(current_row_height, acc['height'])
            
        # Validate the generated positions
        if not self._validate_placement(positions):
            raise RuntimeError("Could not find valid placement for given accessories")
            
        # Return results as name: position mapping
        return {
            self.accessories[i]['name']: positions[idx] 
            for idx, i in enumerate(col_ind)
        }
        
    def visualize_placement(self, placements: Dict[str, Tuple[float, float]]) -> None:
        """
        Simple ASCII visualization of the slat wall layout.
        
        Args:
            placements: Dictionary of accessory positions from optimize_placement()
        """
        wall_grid = [[' ' for _ in range(int(self.wall_width))] 
                    for _ in range(int(self.wall_height))]
        
        for name, (x, y) in placements.items():
            acc = next(a for a in self.accessories if a['name'] == name)
            x_start, y_start = int(x), int(y)
            x_end = min(int(x + acc['width']), int(self.wall_width))
            y_end = min(int(y + acc['height']), int(self.wall_height))
            
            for i in range(y_start, y_end):
                for j in range(x_start, x_end):
                    if i < len(wall_grid) and j < len(wall_grid[0]):
                        wall_grid[i][j] = name[0].upper()  # Use first letter as identifier
                        
        print("\nSlat Wall Layout:")
        print("+" + "-" * int(self.wall_width) + "+")
        for row in wall_grid:
            print("|" + "".join(row) + "|")
        print("+" + "-" * int(self.wall_width) + "+")


# Example usage
if __name__ == "__main__":
    optimizer = SlatWallOptimizer(wall_width=120, wall_height=72)  # 10ft x 6ft wall
    
    # Add accessories
    optimizer.add_accessory("Shirt_Rack", "clothing", 24, 18, priority=8)
    optimizer.add_accessory("Jean_Hook", "clothing", 12, 24, priority=7)
    optimizer.add_accessory("Shoe_Shelf", "shoes", 36, 12, priority=6)
    optimizer.add_accessory("Sneaker_Display", "shoes", 24, 8, priority=5)
    optimizer.add_accessory("Sunglass_Stand", "eyewear", 12, 6, priority=9)
    optimizer.add_accessory("Glasses_Case", "eyewear", 8, 4, priority=4)
    
    try:
        placements = optimizer.optimize_placement()
        print("Optimized Placements:")
        for name, pos in placements.items():
            print(f"{name}: Position (x={pos[0]}, y={pos[1]})")
            
        optimizer.visualize_placement(placements)
    except Exception as e:
        print(f"Optimization failed: {str(e)}")
```
