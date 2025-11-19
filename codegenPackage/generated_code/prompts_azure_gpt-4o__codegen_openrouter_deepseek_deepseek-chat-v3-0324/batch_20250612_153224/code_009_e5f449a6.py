"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: Create a Python script to design a modular kitchen layout, ensuring it can be completed within a tight deadline, inspired by Nyiku Design's testimonial about completing a kitchen set renovation on time.
Generated: DETERMINISTIC_e5f449a6390b474c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Modular Kitchen Layout Designer

This script helps design a modular kitchen layout with constraints to ensure timely completion.
Inspired by Nyiku Design's efficient kitchen renovation approach.

Features:
- Modular unit placement
- Deadline tracking
- Space optimization
- Error handling for invalid configurations
"""

import datetime
from enum import Enum
from typing import List, Dict, Optional, Tuple


class KitchenUnitType(Enum):
    """Types of modular kitchen units available"""
    BASE_CABINET = "Base Cabinet"
    WALL_CABINET = "Wall Cabinet"
    CORNER_UNIT = "Corner Unit"
    SINK = "Sink"
    COOKTOP = "Cooktop"
    ISLAND = "Island"
    DRAWER = "Drawer"
    TALL_UNIT = "Tall Unit"


class KitchenUnit:
    """Represents a single modular kitchen unit"""
    
    def __init__(self, unit_type: KitchenUnitType, width: float, depth: float, height: float):
        """
        Initialize a kitchen unit with dimensions
        
        Args:
            unit_type: Type of the kitchen unit
            width: Width in meters
            depth: Depth in meters
            height: Height in meters
        """
        self.unit_type = unit_type
        self.width = width
        self.depth = depth
        self.height = height
        self.position = None  # Will be set during layout
        
    def __str__(self):
        return f"{self.unit_type.value} ({self.width}m x {self.depth}m x {self.height}m)"


class KitchenLayout:
    """Manages the layout of a modular kitchen with deadline constraints"""
    
    def __init__(self, room_width: float, room_depth: float, deadline: datetime.date):
        """
        Initialize kitchen layout with room dimensions and deadline
        
        Args:
            room_width: Total width of kitchen area in meters
            room_depth: Total depth of kitchen area in meters
            deadline: Project completion deadline
        """
        if room_width <= 0 or room_depth <= 0:
            raise ValueError("Room dimensions must be positive")
            
        if deadline < datetime.date.today():
            raise ValueError("Deadline must be in the future")
            
        self.room_width = room_width
        self.room_depth = room_depth
        self.deadline = deadline
        self.units: List[KitchenUnit] = []
        self.work_triangle = None  # (sink, cooktop, refrigerator positions)
        
    def add_unit(self, unit: KitchenUnit, x: float, y: float) -> bool:
        """
        Add a unit to the layout at specified coordinates
        
        Args:
            unit: KitchenUnit to add
            x: X coordinate (left position)
            y: Y coordinate (bottom position)
            
        Returns:
            bool: True if unit was successfully placed, False if it overlaps or exceeds room dimensions
        """
        # Check if unit fits within room dimensions
        if (x < 0 or y < 0 or 
            x + unit.width > self.room_width or 
            y + unit.depth > self.room_depth):
            return False
            
        # Check for overlaps with existing units
        for existing_unit in self.units:
            ex, ey = existing_unit.position
            if (x < ex + existing_unit.width and
                x + unit.width > ex and
                y < ey + existing_unit.depth and
                y + unit.depth > ey):
                return False
                
        unit.position = (x, y)
        self.units.append(unit)
        return True
        
    def calculate_work_triangle(self) -> Optional[Tuple[Tuple[float, float], ...]]:
        """
        Calculate the work triangle between sink, cooktop, and refrigerator
        
        Returns:
            Tuple of positions (sink, cooktop, refrigerator) or None if not all components are placed
        """
        sink = None
        cooktop = None
        refrigerator = None
        
        for unit in self.units:
            if unit.unit_type == KitchenUnitType.SINK:
                sink = unit.position
            elif unit.unit_type == KitchenUnitType.COOKTOP:
                cooktop = unit.position
            elif unit.unit_type == KitchenUnitType.TALL_UNIT:  # Assuming tall unit is refrigerator
                refrigerator = unit.position
                
        if sink and cooktop and refrigerator:
            self.work_triangle = (sink, cooktop, refrigerator)
            return self.work_triangle
        return None
        
    def check_deadline_feasibility(self, days_needed: int) -> bool:
        """
        Check if the project can be completed before the deadline
        
        Args:
            days_needed: Estimated days required to complete the project
            
        Returns:
            bool: True if project can be completed before deadline, False otherwise
        """
        today = datetime.date.today()
        days_remaining = (self.deadline - today).days
        return days_remaining >= days_needed
        
    def optimize_layout(self, max_iterations: int = 100) -> bool:
        """
        Attempt to optimize the layout by rearranging units
        
        Args:
            max_iterations: Maximum attempts to optimize
            
        Returns:
            bool: True if optimization improved the layout, False otherwise
        """
        # Simple optimization: try to minimize work triangle perimeter
        original_triangle = self.calculate_work_triangle()
        if not original_triangle:
            return False
            
        original_perimeter = self._calculate_triangle_perimeter(original_triangle)
        improved = False
        
        for _ in range(max_iterations):
            # Create a temporary shuffled list of units
            import random
            temp_units = self.units.copy()
            random.shuffle(temp_units)
            
            # Try to place units in new positions
            temp_layout = KitchenLayout(self.room_width, self.room_depth, self.deadline)
            placed_all = True
            
            for unit in temp_units:
                # Try random positions
                for __ in range(10):  # Try 10 random positions per unit
                    x = random.uniform(0, self.room_width - unit.width)
                    y = random.uniform(0, self.room_depth - unit.depth)
                    if temp_layout.add_unit(unit, x, y):
                        break
                else:
                    placed_all = False
                    break
                    
            if not placed_all:
                continue
                
            new_triangle = temp_layout.calculate_work_triangle()
            if new_triangle:
                new_perimeter = self._calculate_triangle_perimeter(new_triangle)
                if new_perimeter < original_perimeter:
                    self.units = temp_layout.units
                    original_perimeter = new_perimeter
                    improved = True
                    
        return improved
        
    def _calculate_triangle_perimeter(self, triangle: Tuple[Tuple[float, float], ...]) -> float:
        """Calculate perimeter of work triangle"""
        a, b, c = triangle
        def distance(p1, p2):
            return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
        return distance(a, b) + distance(b, c) + distance(c, a)
        
    def visualize(self):
        """Generate a simple ASCII visualization of the kitchen layout"""
        print(f"\nKitchen Layout (Room: {self.room_width}m x {self.room_depth}m)")
        print(f"Deadline: {self.deadline} ({self._days_remaining()} days remaining)")
        print("\nLegend:")
        print("B - Base Cabinet  W - Wall Cabinet  C - Corner Unit")
        print("S - Sink          T - Cooktop       I - Island")
        print("D - Drawer        U - Tall Unit")
        
        # Create a grid for visualization
        grid_size = 20
        grid = [[' ' for _ in range(grid_size)] for _ in range(grid_size)]
        
        # Map unit types to symbols
        unit_symbols = {
            KitchenUnitType.BASE_CABINET: 'B',
            KitchenUnitType.WALL_CABINET: 'W',
            KitchenUnitType.CORNER_UNIT: 'C',
            KitchenUnitType.SINK: 'S',
            KitchenUnitType.COOKTOP: 'T',
            KitchenUnitType.ISLAND: 'I',
            KitchenUnitType.DRAWER: 'D',
            KitchenUnitType.TALL_UNIT: 'U'
        }
        
        # Place units on grid
        for unit in self.units:
            if unit.position:
                x, y = unit.position
                # Scale positions to grid
                grid_x = min(int(x / self.room_width * grid_size), grid_size - 1)
                grid_y = min(int(y / self.room_depth * grid_size), grid_size - 1)
                grid[grid_y][grid_x] = unit_symbols.get(unit.unit_type, '?')
        
        # Print grid
        print("\nTop View:")
        print("+" + "-" * grid_size + "+")
        for row in reversed(grid):  # Reverse to show bottom at bottom
            print("|" + "".join(row) + "|")
        print("+" + "-" * grid_size + "+")
        
        # Print work triangle info if available
