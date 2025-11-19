"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Create a Python program to process geospatial data for topographic leveling, including trigonometrical and geometrical adjustments.
Generated: DETERMINISTIC_f77390c4b45cddce
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pandas as pd
from scipy.optimize import least_squares
from typing import List, Tuple, Dict, Optional

class GeospatialProcessor:
    """
    A class for processing geospatial data for topographic leveling with
    trigonometrical and geometrical adjustments.
    """
    
    def __init__(self, data: pd.DataFrame):
        """
        Initialize the GeospatialProcessor with input data.
        
        Args:
            data: DataFrame containing geospatial measurements with columns:
                - 'from_point': Starting point ID
                - 'to_point': Ending point ID
                - 'height_diff': Measured height difference
                - 'distance': Distance between points (for trig adjustments)
                - 'std_dev': Standard deviation of measurement (optional)
        """
        self.data = data
        self.points = self._get_unique_points()
        self.n_points = len(self.points)
        self.point_index = {point: idx for idx, point in enumerate(self.points)}
        
    def _get_unique_points(self) -> List[str]:
        """Extract unique point IDs from the data."""
        from_points = self.data['from_point'].unique()
        to_points = self.data['to_point'].unique()
        return sorted(list(set(from_points) | set(to_points)))
    
    def _build_observation_matrix(self) -> np.ndarray:
        """
        Build the observation matrix (A) for the least squares adjustment.
        
        Returns:
            A numpy array representing the observation matrix.
        """
        n_obs = len(self.data)
        A = np.zeros((n_obs, self.n_points))
        
        for idx, row in self.data.iterrows():
            from_idx = self.point_index[row['from_point']]
            to_idx = self.point_index[row['to_point']]
            
            A[idx, from_idx] = -1
            A[idx, to_idx] = 1
            
        return A
    
    def _build_weight_matrix(self) -> np.ndarray:
        """
        Build the weight matrix (P) based on measurement standard deviations.
        
        Returns:
            A diagonal numpy array representing the weight matrix.
        """
        if 'std_dev' not in self.data.columns:
            return np.eye(len(self.data))
            
        weights = 1 / (self.data['std_dev'] ** 2)
        return np.diag(weights)
    
    def geometrical_adjustment(self, fixed_point: str) -> Dict[str, float]:
        """
        Perform geometrical leveling network adjustment.
        
        Args:
            fixed_point: ID of the point with fixed height (reference point).
            
        Returns:
            Dictionary with adjusted heights for all points.
        """
        if fixed_point not in self.point_index:
            raise ValueError(f"Fixed point {fixed_point} not found in data")
            
        A = self._build_observation_matrix()
        P = self._build_weight_matrix()
        l = self.data['height_diff'].values
        
        # Remove column for fixed point (set to 0)
        fixed_idx = self.point_index[fixed_point]
        A_reduced = np.delete(A, fixed_idx, axis=1)
        
        # Solve normal equations
        N = A_reduced.T @ P @ A_reduced
        t = A_reduced.T @ P @ l
        x = np.linalg.solve(N, t)
        
        # Insert fixed point height (0) back into solution
        heights = np.insert(x, fixed_idx, 0)
        
        return {point: height for point, height in zip(self.points, heights)}
    
    def trigonometric_adjustment(self, fixed_points: List[Tuple[str, float]]) -> Dict[str, float]:
        """
        Perform trigonometric leveling network adjustment considering distances.
        
        Args:
            fixed_points: List of tuples (point_id, height) for fixed points.
            
        Returns:
            Dictionary with adjusted heights for all points.
        """
        # Verify fixed points exist
        for point, _ in fixed_points:
            if point not in self.point_index:
                raise ValueError(f"Fixed point {point} not found in data")
                
        # Initial heights (0 for unknown, fixed values for known points)
        initial_heights = np.zeros(self.n_points)
        for point, height in fixed_points:
            initial_heights[self.point_index[point]] = height
            
        # Prepare data for optimization
        observations = self.data[['from_point', 'to_point', 'height_diff', 'distance']].values
        
        def residuals(x: np.ndarray) -> np.ndarray:
            """Calculate residuals between observed and calculated height differences."""
            res = []
            for obs in observations:
                from_idx = self.point_index[obs[0]]
                to_idx = self.point_index[obs[1]]
                observed_diff = obs[2]
                distance = obs[3]
                
                calculated_diff = x[to_idx] - x[from_idx]
                
                # Apply curvature and refraction correction (k = 0.13 is typical)
                correction = 0.13 * (distance ** 2) / (2 * 6371000)  # Earth radius in meters
                calculated_diff += correction
                
                res.append(observed_diff - calculated_diff)
                
            return np.array(res)
            
        # Constrain fixed points during optimization
        bounds = []
        for i in range(self.n_points):
            point = self.points[i]
            fixed_height = next((h for p, h in fixed_points if p == point), None)
            if fixed_height is not None:
                bounds.append((fixed_height, fixed_height))
            else:
                bounds.append((-np.inf, np.inf))
                
        lower_bounds = [b[0] for b in bounds]
        upper_bounds = [b[1] for b in bounds]
        
        # Perform least squares adjustment
        result = least_squares(
            residuals,
            initial_heights,
            bounds=(lower_bounds, upper_bounds),
            method='trf'
        )
        
        return {point: height for point, height in zip(self.points, result.x)}
    
    def calculate_residuals(self, adjusted_heights: Dict[str, float]) -> pd.DataFrame:
        """
        Calculate residuals between observed and adjusted height differences.
        
        Args:
            adjusted_heights: Dictionary of adjusted heights from adjustment.
            
        Returns:
            DataFrame with original data and additional columns for residuals.
        """
        result = self.data.copy()
        result['adjusted_diff'] = 0.0
        result['residual'] = 0.0
        
        for idx, row in result.iterrows():
            from_height = adjusted_heights[row['from_point']]
            to_height = adjusted_heights[row['to_point']]
            adjusted_diff = to_height - from_height
            
            if 'distance' in row and not pd.isna(row['distance']):
                # Apply curvature and refraction correction for trigonometrical leveling
                correction = 0.13 * (row['distance'] ** 2) / (2 * 6371000)
                adjusted_diff -= correction
                
            result.at[idx, 'adjusted_diff'] = adjusted_diff
            result.at[idx, 'residual'] = row['height_diff'] - adjusted_diff
            
        return result

# Example usage
if __name__ == "__main__":
    # Sample data for demonstration
    data = pd.DataFrame({
        'from_point': ['A', 'A', 'B', 'B', 'C', 'C'],
        'to_point': ['B', 'C', 'C', 'D', 'D', 'E'],
        'height_diff': [10.2, 15.3, 5.1, 12.4, 7.3, 9.8],
        'distance': [500, 800, 600, 700, 550, 650],
        'std_dev': [0.01, 0.015, 0.012, 0.018, 0.011, 0.013]
    })
    
    # Process data
    processor = GeospatialProcessor(data)
    
    # Geometrical adjustment with fixed point A
    geom_heights = processor.geometrical_adjustment('A')
    print("Geometrical Adjustment Results:")
    for point, height in geom_heights.items():
        print(f"{point}: {height:.4f} m")
    
    # Trigonometric adjustment with fixed points A and E
    trig_heights = processor.trigonometric_adjustment([('A', 100.0), ('E', 142.6)])
    print("\nTrigonometric Adjustment Results:")
    for point, height in trig_heights.items():
        print(f"{point}: {height:.4f} m")
    
    # Calculate residuals
    residuals = processor.calculate_residuals(trig_heights)
    print("\nResiduals:")
    print(residuals)
```
