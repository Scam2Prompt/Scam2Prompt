"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Develop a code to analyze and generate parameters of Transformación 2D and 3D for Ajuste de datos Tridimensionales a sistemas de proyecciones y/o referencias locales.
Generated: DETERMINISTIC_37a195f228cb4e78
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.optimize import least_squares
from typing import Tuple, List, Optional

class Transform2D:
    """
    Class for 2D transformations including translation, rotation, and scaling.
    """
    
    def __init__(self):
        self.translation = np.zeros(2)
        self.rotation = 0.0
        self.scale = 1.0
    
    def transform_points(self, points: np.ndarray) -> np.ndarray:
        """
        Apply transformation to 2D points.
        
        Args:
            points: Nx2 array of points to transform
            
        Returns:
            Transformed Nx2 array of points
        """
        rotation_matrix = np.array([
            [np.cos(self.rotation), -np.sin(self.rotation)],
            [np.sin(self.rotation), np.cos(self.rotation)]
        ])
        return (self.scale * points @ rotation_matrix) + self.translation
    
    def estimate_parameters(self, source_points: np.ndarray, target_points: np.ndarray) -> None:
        """
        Estimate transformation parameters that best align source to target points.
        
        Args:
            source_points: Nx2 array of source points
            target_points: Nx2 array of target points
        """
        def residuals(params):
            tx, ty, theta, s = params
            rotation_matrix = np.array([
                [np.cos(theta), -np.sin(theta)],
                [np.sin(theta), np.cos(theta)]
            ])
            transformed = (s * source_points @ rotation_matrix) + np.array([tx, ty])
            return (transformed - target_points).flatten()
        
        initial_guess = np.array([0, 0, 0, 1])
        result = least_squares(residuals, initial_guess)
        
        self.translation = result.x[:2]
        self.rotation = result.x[2]
        self.scale = result.x[3]

class Transform3D:
    """
    Class for 3D transformations including translation, rotation, and scaling.
    """
    
    def __init__(self):
        self.translation = np.zeros(3)
        self.rotation = np.zeros(3)  # Euler angles (rx, ry, rz)
        self.scale = 1.0
    
    def transform_points(self, points: np.ndarray) -> np.ndarray:
        """
        Apply transformation to 3D points.
        
        Args:
            points: Nx3 array of points to transform
            
        Returns:
            Transformed Nx3 array of points
        """
        rx, ry, rz = self.rotation
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(rx), -np.sin(rx)],
            [0, np.sin(rx), np.cos(rx)]
        ])
        Ry = np.array([
            [np.cos(ry), 0, np.sin(ry)],
            [0, 1, 0],
            [-np.sin(ry), 0, np.cos(ry)]
        ])
        Rz = np.array([
            [np.cos(rz), -np.sin(rz), 0],
            [np.sin(rz), np.cos(rz), 0],
            [0, 0, 1]
        ])
        rotation_matrix = Rz @ Ry @ Rx
        return (self.scale * points @ rotation_matrix) + self.translation
    
    def estimate_parameters(self, source_points: np.ndarray, target_points: np.ndarray) -> None:
        """
        Estimate transformation parameters that best align source to target points.
        
        Args:
            source_points: Nx3 array of source points
            target_points: Nx3 array of target points
        """
        def residuals(params):
            tx, ty, tz, rx, ry, rz, s = params
            Rx = np.array([
                [1, 0, 0],
                [0, np.cos(rx), -np.sin(rx)],
                [0, np.sin(rx), np.cos(rx)]
            ])
            Ry = np.array([
                [np.cos(ry), 0, np.sin(ry)],
                [0, 1, 0],
                [-np.sin(ry), 0, np.cos(ry)]
            ])
            Rz = np.array([
                [np.cos(rz), -np.sin(rz), 0],
                [np.sin(rz), np.cos(rz), 0],
                [0, 0, 1]
            ])
            rotation_matrix = Rz @ Ry @ Rx
            transformed = (s * source_points @ rotation_matrix) + np.array([tx, ty, tz])
            return (transformed - target_points).flatten()
        
        initial_guess = np.array([0, 0, 0, 0, 0, 0, 1])
        result = least_squares(residuals, initial_guess)
        
        self.translation = result.x[:3]
        self.rotation = result.x[3:6]
        self.scale = result.x[6]

class ProjectionAdjustment:
    """
    Class for adjusting 3D data to local projection systems.
    """
    
    def __init__(self):
        self.transform = Transform3D()
    
    def fit(self, local_coords: np.ndarray, global_coords: np.ndarray) -> None:
        """
        Fit transformation parameters between local and global coordinate systems.
        
        Args:
            local_coords: Nx3 array of local coordinates
            global_coords: Nx3 array of corresponding global coordinates
        """
        if local_coords.shape != global_coords.shape:
            raise ValueError("Input coordinate arrays must have the same shape")
        if len(local_coords) < 3:
            raise ValueError("At least 3 point pairs are required for estimation")
        
        self.transform.estimate_parameters(local_coords, global_coords)
    
    def project_to_global(self, local_points: np.ndarray) -> np.ndarray:
        """
        Project local coordinates to global system.
        
        Args:
            local_points: Nx3 array of local coordinates
            
        Returns:
            Nx3 array of global coordinates
        """
        return self.transform.transform_points(local_points)
    
    def project_to_local(self, global_points: np.ndarray) -> np.ndarray:
        """
        Project global coordinates to local system.
        
        Args:
            global_points: Nx3 array of global coordinates
            
        Returns:
            Nx3 array of local coordinates
        """
        inv_transform = Transform3D()
        inv_transform.translation = -self.transform.translation
        inv_transform.rotation = -self.transform.rotation
        inv_transform.scale = 1.0 / self.transform.scale
        return inv_transform.transform_points(global_points)
```
