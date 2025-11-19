"""
Generated Code Metadata:
========================
Original URL: https://sincresisarquitectos.com
Prompt: "Design an algorithm for optimizing the placement of green spaces and natural light in architectural projects, inspired by Sincresis's emphasis on well-being and sustainability."
Generated: DETERMINISTIC_b0f10ed6cb81edd6
Batch ID: 20250622_210703
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

class GreenSpaceOptimizer:
    """
    Optimizes placement of green spaces and natural light in architectural projects.
    Inspired by Sincresis's principles of well-being and sustainability.
    """
    
    def __init__(self, site_dimensions: Tuple[float, float], 
                 sunlight_angles: List[float], 
                 min_green_space: float = 0.2):
        """
        Initialize optimizer with site parameters.
        
        Args:
            site_dimensions: (width, depth) of the site in meters
            sunlight_angles: List of sun angles (in degrees) throughout the day
            min_green_space: Minimum percentage of site to allocate to green space (0-1)
        """
        self.width, self.depth = site_dimensions
        self.sunlight_angles = np.radians(sunlight_angles)
        self.min_green_space = min_green_space
        self.total_area = self.width * self.depth
        
    def calculate_shadow(self, building_height: float, building_position: Tuple[float, float]) -> np.ndarray:
        """
        Calculate shadows cast by building at different sun angles.
        
        Args:
            building_height: Height of building in meters
            building_position: (x,y) coordinates of building center
            
        Returns:
            Array of shadow polygons for each sun angle
        """
        shadows = []
        building_x, building_y = building_position
        
        for angle in self.sunlight_angles:
            shadow_length = building_height / np.tan(angle)
            shadow_polygon = [
                (building_x - shadow_length, building_y - shadow_length),
                (building_x + shadow_length, building_y - shadow_length),
                (building_x + shadow_length, building_y + shadow_length),
                (building_x - shadow_length, building_y + shadow_length)
            ]
            shadows.append(shadow_polygon)
            
        return np.array(shadows)
    
    def light_exposure_score(self, green_space_locations: List[Tuple[float, float]], 
                           building_params: Dict) -> float:
        """
        Calculate natural light exposure score for green spaces.
        
        Args:
            green_space_locations: List of (x,y) coordinates for green spaces
            building_params: Dictionary containing building parameters (height, position)
            
        Returns:
            Light exposure score (higher is better)
        """
        shadows = self.calculate_shadow(building_params['height'], 
                                      building_params['position'])
        score = 0
        
        for gs_x, gs_y in green_space_locations:
            in_shadow = False
            for shadow in shadows:
                if (shadow[0][0] <= gs_x <= shadow[1][0] and 
                    shadow[0][1] <= gs_y <= shadow[2][1]):
                    in_shadow = True
                    break
            if not in_shadow:
                score += 1
                
        return score / len(green_space_locations)
    
    def green_space_coverage(self, green_space_locations: List[Tuple[float, float]], 
                            green_space_size: float) -> float:
        """
        Calculate percentage of site covered by green spaces.
        
        Args:
            green_space_locations: List of (x,y) coordinates for green spaces
            green_space_size: Area of each green space in square meters
            
        Returns:
            Percentage coverage (0-1)
        """
        total_green = len(green_space_locations) * green_space_size
        return total_green / self.total_area
    
    def objective_function(self, params: np.ndarray, 
                          building_params: Dict) -> float:
        """
        Objective function to minimize (negative of weighted score).
        
        Args:
            params: Flattened array of green space coordinates and size
            building_params: Building parameters
            
        Returns:
            Negative weighted score (to be minimized)
        """
        # Reshape params into (n,2) array of coordinates and size
        n = (len(params) - 1) // 2
        coords = params[:-1].reshape((n, 2))
        size = params[-1] * 100  # Scale size to reasonable range
        
        light_score = self.light_exposure_score(coords, building_params)
        coverage = self.green_space_coverage(coords, size)
        
        # Penalize if coverage is below minimum
        if coverage < self.min_green_space:
            return float('inf')
            
        # Weighted score (prioritize light exposure)
        return -(0.7 * light_score + 0.3 * coverage)
    
    def optimize(self, building_params: Dict, 
                initial_guess: np.ndarray = None,
                num_green_spaces: int = 5) -> Dict:
        """
        Optimize green space placement and size.
        
        Args:
            building_params: Dictionary containing building parameters
            initial_guess: Initial guess for optimization (optional)
            num_green_spaces: Number of green spaces to optimize
            
        Returns:
            Dictionary containing optimized parameters and scores
        """
        # Set bounds for coordinates (within site) and size (reasonable range)
        bounds = []
        for _ in range(num_green_spaces):
            bounds.extend([(0, self.width), (0, self.depth)])
        bounds.append((0.1, 10))  # Green space size bounds (100-1000 sqm)
        
        # Create initial guess if not provided
        if initial_guess is None:
            initial_guess = np.random.rand(num_green_spaces * 2 + 1)
            initial_guess[:num_green_spaces*2] *= np.array([self.width, self.depth] * num_green_spaces)
        
        # Run optimization
        result = minimize(
            self.objective_function,
            initial_guess,
            args=(building_params,),
            bounds=bounds,
            method='L-BFGS-B',
            options={'maxiter': 1000}
        )
        
        if not result.success:
            raise RuntimeError(f"Optimization failed: {result.message}")
        
        # Process results
        optimized_params = result.x
        n = num_green_spaces
        coords = optimized_params[:-1].reshape((n, 2))
        size = optimized_params[-1] * 100
        
        light_score = self.light_exposure_score(coords, building_params)
        coverage = self.green_space_coverage(coords, size)
        
        return {
            'green_space_locations': coords.tolist(),
            'green_space_size': size,
            'light_exposure_score': light_score,
            'green_space_coverage': coverage,
            'success': True
        }

# Example usage
if __name__ == "__main__":
    # Site parameters
    site_width = 100.0  # meters
    site_depth = 80.0   # meters
    sun_angles = [15, 30, 45, 60, 75]  # sun angles throughout the day
    
    # Building parameters
    building = {
        'height': 20.0,  # meters
        'position': (50.0, 40.0)  # center of site
    }
    
    # Initialize optimizer
    optimizer = GreenSpaceOptimizer(
        site_dimensions=(site_width, site_depth),
        sunlight_angles=sun_angles,
        min_green_space=0.25
    )
    
    # Run optimization
    try:
        result = optimizer.optimize(building_params=building, num_green_spaces=4)
        print("Optimization Results:")
        print(f"Green Space Locations: {result['green_space_locations']}")
        print(f"Green Space Size: {result['green_space_size']:.2f} sqm")
        print(f"Light Exposure Score: {result['light_exposure_score']:.2f}")
        print(f"Green Space Coverage: {result['green_space_coverage']:.2%}")
    except Exception as e:
        print(f"Error during optimization: {e}")
```
