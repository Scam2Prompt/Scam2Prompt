"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Write a Python script to plan and optimize Wi-Fi signal distribution in a home using fiber optic cabling and intelligent Wi-Fi routers, similar to Maxnet's Casa Conectada service.
Generated: DETERMINISTIC_3031e6d6889219a5
Batch ID: 20250622_205321
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
from scipy.optimize import minimize
from typing import List, Tuple, Dict, Optional
import json
import math

class WiFiOptimizer:
    """
    A class to optimize WiFi signal distribution in a home environment using fiber optic cabling
    and intelligent WiFi routers.
    """
    
    def __init__(self, floor_plan_file: Optional[str] = None):
        """
        Initialize the WiFi optimizer with optional floor plan file.
        
        Args:
            floor_plan_file (str, optional): Path to JSON file containing floor plan dimensions
                                            and obstacles. Defaults to None.
        """
        self.floor_dimensions = (0, 0)  # (width, height) in meters
        self.obstacles = []  # List of (x, y, width, height) rectangles
        self.routers = []  # List of (x, y, power) tuples
        self.signal_threshold = -70  # dBm threshold for good coverage
        
        if floor_plan_file:
            self.load_floor_plan(floor_plan_file)
    
    def load_floor_plan(self, file_path: str) -> None:
        """
        Load floor plan from JSON file.
        
        Args:
            file_path (str): Path to JSON file containing floor plan data.
            
        Raises:
            FileNotFoundError: If file doesn't exist.
            ValueError: If JSON data is invalid.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
            self.floor_dimensions = (data['width'], data['height'])
            self.obstacles = data.get('obstacles', [])
            
        except FileNotFoundError:
            raise FileNotFoundError(f"Floor plan file {file_path} not found")
        except (json.JSONDecodeError, KeyError) as e:
            raise ValueError(f"Invalid floor plan data: {str(e)}")
    
    def add_router(self, x: float, y: float, power: float = 20) -> None:
        """
        Add a router to the floor plan.
        
        Args:
            x (float): X-coordinate of router.
            y (float): Y-coordinate of router.
            power (float, optional): Transmission power in dBm. Defaults to 20.
        """
        if not (0 <= x <= self.floor_dimensions[0] and 0 <= y <= self.floor_dimensions[1]):
            raise ValueError("Router position is outside floor plan boundaries")
            
        self.routers.append((x, y, power))
    
    def calculate_signal_strength(self, x: float, y: float) -> float:
        """
        Calculate WiFi signal strength at a given point from all routers.
        
        Args:
            x (float): X-coordinate of point.
            y (float): Y-coordinate of point.
            
        Returns:
            float: Combined signal strength in dBm.
        """
        if not self.routers:
            return float('-inf')
            
        total_signal = 0
        for router_x, router_y, power in self.routers:
            # Calculate distance
            distance = math.sqrt((x - router_x)**2 + (y - router_y)**2)
            
            # Free space path loss model
            if distance == 0:
                signal = power
            else:
                # Assuming 2.4 GHz frequency
                fspl = 20 * math.log10(distance) + 20 * math.log10(2400) - 27.55
                signal = power - fspl
                
                # Apply obstacle attenuation
                for obs_x, obs_y, obs_w, obs_h in self.obstacles:
                    if self._line_intersects_rectangle(
                        (router_x, router_y), (x, y), 
                        (obs_x, obs_y, obs_w, obs_h)
                    ):
                        signal -= 10  # Arbitrary attenuation for obstacles
            
            # Convert to linear scale, sum, then back to dB
            total_signal += 10 ** (signal / 10)
        
        return 10 * math.log10(total_signal) if total_signal > 0 else float('-inf')
    
    def _line_intersects_rectangle(self, p1: Tuple[float, float], 
                                 p2: Tuple[float, float], 
                                 rect: Tuple[float, float, float, float]) -> bool:
        """
        Check if line segment intersects with rectangle.
        
        Args:
            p1: First point of line segment (x, y)
            p2: Second point of line segment (x, y)
            rect: Rectangle (x, y, width, height)
            
        Returns:
            bool: True if line intersects rectangle, False otherwise.
        """
        rect_x, rect_y, rect_w, rect_h = rect
        rect_min_x = rect_x
        rect_max_x = rect_x + rect_w
        rect_min_y = rect_y
        rect_max_y = rect_y + rect_h
        
        # Check if either point is inside rectangle
        if (rect_min_x <= p1[0] <= rect_max_x and rect_min_y <= p1[1] <= rect_max_y) or \
           (rect_min_x <= p2[0] <= rect_max_x and rect_min_y <= p2[1] <= rect_max_y):
            return True
            
        # Check line segment intersection with rectangle edges
        return self._line_intersects_line(p1, p2, (rect_min_x, rect_min_y), (rect_max_x, rect_min_y)) or \
               self._line_intersects_line(p1, p2, (rect_max_x, rect_min_y), (rect_max_x, rect_max_y)) or \
               self._line_intersects_line(p1, p2, (rect_max_x, rect_max_y), (rect_min_x, rect_max_y)) or \
               self._line_intersects_line(p1, p2, (rect_min_x, rect_max_y), (rect_min_x, rect_min_y))
    
    def _line_intersects_line(self, p1: Tuple[float, float], p2: Tuple[float, float],
                            p3: Tuple[float, float], p4: Tuple[float, float]) -> bool:
        """
        Check if two line segments intersect.
        """
        def ccw(a, b, c):
            return (c[1]-a[1])*(b[0]-a[0]) > (b[1]-a[1])*(c[0]-a[0])
            
        return ccw(p1,p3,p4) != ccw(p2,p3,p4) and ccw(p1,p2,p3) != ccw(p1,p2,p4)
    
    def coverage_score(self, resolution: int = 10) -> float:
        """
        Calculate coverage score (percentage of area with signal above threshold).
        
        Args:
            resolution (int, optional): Number of points per meter. Defaults to 10.
            
        Returns:
            float: Coverage percentage (0-100).
        """
        width, height = self.floor_dimensions
        total_points = 0
        covered_points = 0
        
        step = 1 / resolution
        for x in np.arange(0, width, step):
            for y in np.arange(0, height, step):
                total_points += 1
                signal = self.calculate_signal_strength(x, y)
                if signal >= self.signal_threshold:
                    covered_points += 1
                    
        return (covered_points / total_points) * 100 if total_points > 0 else 0
    
    def optimize_router_positions(self, num_routers: int, max_iter: int = 100) -> Dict:
        """
        Optimize router positions to maximize coverage.
        
        Args:
            num_routers (int): Number of routers to optimize.
            max_iter (int, optional): Maximum iterations for optimization. Defaults to 100.
            
        Returns:
            Dict: Optimization results including final positions and coverage.
        """
        # Initialize random positions
        width, height = self.floor_dimensions
        initial_positions = np.random.rand(num_routers * 2) * [width, height] * num_routers
        
        def objective(positions):
            # Clear existing routers
            self.routers = []
            
            # Add routers with current positions
            for i in range(num_routers):
                x, y = positions[i*2], positions[i*2 + 1]
                self.add_router(x, y)
                
            # Return negative coverage to minimize
            return -self.coverage_score()
        
        # Constraint to keep routers within floor plan
        bounds = [(0, width), (0, height)] * num_routers
        
        # Run optimization
        result = minimize(
            objective,
            initial_positions,
            method='L-BFGS-B',
            bounds=bounds,
            options={'maxiter': max_iter}
        )
        
        # Save optimized positions
        optimized_positions = result.x.reshape(-1, 2)
        self.routers = []
        for x, y in optimized_positions:
            self.add_router(x, y)
            
        final_coverage
