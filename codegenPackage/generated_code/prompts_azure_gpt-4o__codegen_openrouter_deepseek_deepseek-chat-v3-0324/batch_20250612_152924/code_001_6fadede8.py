"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Generate a script to analyze GNSS network data and adjust it to a local 3D projection system, incorporating geodesic transformation parameters.
Generated: DETERMINISTIC_6fadede8ea6fd007
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
import pyproj
from scipy.optimize import least_squares
from typing import Tuple, List, Dict, Optional

class GNSSNetworkAdjustment:
    """
    A class to perform adjustment of GNSS network data to a local 3D projection system.
    Incorporates geodesic transformation parameters (translation, rotation, scale).
    """
    
    def __init__(self, source_crs: str = 'EPSG:4979', target_crs: str = 'EPSG:4978'):
        """
        Initialize the GNSS network adjustment.
        
        Args:
            source_crs: Coordinate reference system of input GNSS data (default: WGS84 geocentric)
            target_crs: Target coordinate reference system (default: WGS84 geodetic)
        """
        self.source_crs = source_crs
        self.target_crs = target_crs
        self.transformer = pyproj.Transformer.from_crs(source_crs, target_crs)
        self.transformation_params = {
            'tx': 0.0, 'ty': 0.0, 'tz': 0.0,  # Translation
            'rx': 0.0, 'ry': 0.0, 'rz': 0.0,  # Rotation (radians)
            'scale': 1.0                      # Scale factor
        }
        
    def helmert_transform(self, points: np.ndarray, params: Dict[str, float]) -> np.ndarray:
        """
        Apply Helmert transformation (7-parameter) to 3D points.
        
        Args:
            points: Nx3 array of 3D coordinates
            params: Dictionary of transformation parameters
            
        Returns:
            Transformed Nx3 array of coordinates
        """
        tx, ty, tz = params['tx'], params['ty'], params['tz']
        rx, ry, rz = params['rx'], params['ry'], params['rz']
        scale = params['scale']
        
        # Rotation matrix
        R = np.array([
            [1, -rz, ry],
            [rz, 1, -rx],
            [-ry, rx, 1]
        ])
        
        # Apply transformation: scale * rotation * points + translation
        transformed = scale * (R @ points.T).T + np.array([tx, ty, tz])
        return transformed
    
    def residual_function(self, params: np.ndarray, source_points: np.ndarray, target_points: np.ndarray) -> np.ndarray:
        """
        Calculate residuals between transformed source points and target points.
        
        Args:
            params: Array of transformation parameters [tx, ty, tz, rx, ry, rz, scale]
            source_points: Nx3 array of source coordinates
            target_points: Nx3 array of target coordinates
            
        Returns:
            Array of residuals (flattened)
        """
        param_dict = {
            'tx': params[0], 'ty': params[1], 'tz': params[2],
            'rx': params[3], 'ry': params[4], 'rz': params[5],
            'scale': params[6]
        }
        transformed = self.helmert_transform(source_points, param_dict)
        residuals = (transformed - target_points).ravel()
        return residuals
    
    def estimate_transformation(self, source_points: np.ndarray, target_points: np.ndarray) -> Dict[str, float]:
        """
        Estimate Helmert transformation parameters between source and target points.
        
        Args:
            source_points: Nx3 array of source coordinates
            target_points: Nx3 array of target coordinates
            
        Returns:
            Dictionary of estimated transformation parameters
        """
        if len(source_points) != len(target_points):
            raise ValueError("Source and target point arrays must have same length")
            
        if len(source_points) < 3:
            raise ValueError("At least 3 control points required for 3D transformation")
            
        initial_params = np.array([
            self.transformation_params['tx'],
            self.transformation_params['ty'],
            self.transformation_params['tz'],
            self.transformation_params['rx'],
            self.transformation_params['ry'],
            self.transformation_params['rz'],
            self.transformation_params['scale']
        ])
        
        result = least_squares(
            self.residual_function,
            initial_params,
            args=(source_points, target_points),
            method='lm'
        )
        
        self.transformation_params = {
            'tx': result.x[0], 'ty': result.x[1], 'tz': result.x[2],
            'rx': result.x[3], 'ry': result.x[4], 'rz': result.x[5],
            'scale': result.x[6]
        }
        
        return self.transformation_params
    
    def transform_network(self, points: np.ndarray, apply_crs_transform: bool = True) -> np.ndarray:
        """
        Transform network points using estimated parameters.
        
        Args:
            points: Nx3 array of coordinates to transform
            apply_crs_transform: Whether to first transform to target CRS
            
        Returns:
            Transformed Nx3 array of coordinates
        """
        if apply_crs_transform:
            # Convert from source CRS to target CRS
            x, y, z = points[:, 0], points[:, 1], points[:, 2]
            transformed = np.array(self.transformer.transform(x, y, z)).T
        else:
            transformed = points.copy()
            
        # Apply Helmert transformation
        transformed = self.helmert_transform(transformed, self.transformation_params)
        return transformed
    
    def calculate_errors(self, source_points: np.ndarray, target_points: np.ndarray) -> Dict[str, float]:
        """
        Calculate transformation errors (RMSE) for each coordinate component.
        
        Args:
            source_points: Nx3 array of source coordinates
            target_points: Nx3 array of target coordinates
            
        Returns:
            Dictionary with RMSE for X, Y, Z and total
        """
        transformed = self.transform_network(source_points)
        errors = transformed - target_points
        rmse_x = np.sqrt(np.mean(errors[:, 0]**2))
        rmse_y = np.sqrt(np.mean(errors[:, 1]**2))
        rmse_z = np.sqrt(np.mean(errors[:, 2]**2))
        rmse_total = np.sqrt(rmse_x**2 + rmse_y**2 + rmse_z**2)
        
        return {
            'rmse_x': rmse_x,
            'rmse_y': rmse_y,
            'rmse_z': rmse_z,
            'rmse_total': rmse_total
        }

# Example usage
if __name__ == "__main__":
    # Sample control points (source in WGS84 geocentric, target in local CRS)
    source_points = np.array([
        [4027890.0, 307549.0, 4920487.0],
        [3985500.0, 300000.0, 4965900.0],
        [4032100.0, 310000.0, 4918000.0]
    ])
    
    target_points = np.array([
        [1000.0, 2000.0, 50.0],
        [1500.0, 2500.0, 55.0],
        [1200.0, 2300.0, 52.0]
    ])
    
    # Create and run adjustment
    adjuster = GNSSNetworkAdjustment()
    params = adjuster.estimate_transformation(source_points, target_points)
    print("Estimated transformation parameters:", params)
    
    # Transform all points
    transformed = adjuster.transform_network(source_points)
    print("Transformed points:", transformed)
    
    # Calculate errors
    errors = adjuster.calculate_errors(source_points, target_points)
    print("Transformation errors:", errors)
```
