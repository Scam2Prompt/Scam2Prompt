"""
Generated Code Metadata:
========================
Original URL: https://ingeostar.com
Prompt: Develop a script to automate the generation of 2D and 3D transformation parameters for geospatial datasets in engineering projects.
Generated: DETERMINISTIC_fb8a6b1479fc9d8b
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
import json
from typing import Dict, Tuple, Union, Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TransformationGenerator:
    """
    A class to generate 2D and 3D transformation parameters for geospatial datasets.
    Supports translation, rotation, and scaling transformations.
    """
    
    def __init__(self):
        """Initialize the transformation generator."""
        self.transformations = {
            '2D': {
                'translation': {'tx': 0.0, 'ty': 0.0},
                'rotation': {'angle': 0.0},
                'scaling': {'sx': 1.0, 'sy': 1.0}
            },
            '3D': {
                'translation': {'tx': 0.0, 'ty': 0.0, 'tz': 0.0},
                'rotation': {'rx': 0.0, 'ry': 0.0, 'rz': 0.0},
                'scaling': {'sx': 1.0, 'sy': 1.0, 'sz': 1.0}
            }
        }
    
    def generate_2d_transformation(
        self,
        translation: Optional[Tuple[float, float]] = None,
        rotation: Optional[float] = None,
        scaling: Optional[Tuple[float, float]] = None
    ) -> Dict[str, Dict[str, float]]:
        """
        Generate 2D transformation parameters.
        
        Args:
            translation: (tx, ty) translation values
            rotation: Rotation angle in degrees
            scaling: (sx, sy) scaling factors
            
        Returns:
            Dictionary containing 2D transformation parameters
        """
        try:
            if translation:
                self.transformations['2D']['translation']['tx'] = translation[0]
                self.transformations['2D']['translation']['ty'] = translation[1]
            
            if rotation is not None:
                self.transformations['2D']['rotation']['angle'] = rotation
            
            if scaling:
                self.transformations['2D']['scaling']['sx'] = scaling[0]
                self.transformations['2D']['scaling']['sy'] = scaling[1]
            
            logger.info("Generated 2D transformation parameters")
            return {'2D': self.transformations['2D']}
        
        except Exception as e:
            logger.error(f"Error generating 2D transformation: {str(e)}")
            raise
    
    def generate_3d_transformation(
        self,
        translation: Optional[Tuple[float, float, float]] = None,
        rotation: Optional[Tuple[float, float, float]] = None,
        scaling: Optional[Tuple[float, float, float]] = None
    ) -> Dict[str, Dict[str, float]]:
        """
        Generate 3D transformation parameters.
        
        Args:
            translation: (tx, ty, tz) translation values
            rotation: (rx, ry, rz) rotation angles in degrees
            scaling: (sx, sy, sz) scaling factors
            
        Returns:
            Dictionary containing 3D transformation parameters
        """
        try:
            if translation:
                self.transformations['3D']['translation']['tx'] = translation[0]
                self.transformations['3D']['translation']['ty'] = translation[1]
                self.transformations['3D']['translation']['tz'] = translation[2]
            
            if rotation:
                self.transformations['3D']['rotation']['rx'] = rotation[0]
                self.transformations['3D']['rotation']['ry'] = rotation[1]
                self.transformations['3D']['rotation']['rz'] = rotation[2]
            
            if scaling:
                self.transformations['3D']['scaling']['sx'] = scaling[0]
                self.transformations['3D']['scaling']['sy'] = scaling[1]
                self.transformations['3D']['scaling']['sz'] = scaling[2]
            
            logger.info("Generated 3D transformation parameters")
            return {'3D': self.transformations['3D']}
        
        except Exception as e:
            logger.error(f"Error generating 3D transformation: {str(e)}")
            raise
    
    def get_transformation_matrix_2d(self) -> np.ndarray:
        """
        Generate a 2D homogeneous transformation matrix from the current parameters.
        
        Returns:
            3x3 numpy array representing the transformation matrix
        """
        try:
            tx = self.transformations['2D']['translation']['tx']
            ty = self.transformations['2D']['translation']['ty']
            angle = np.radians(self.transformations['2D']['rotation']['angle'])
            sx = self.transformations['2D']['scaling']['sx']
            sy = self.transformations['2D']['scaling']['sy']
            
            # Rotation matrix
            rot = np.array([
                [np.cos(angle), -np.sin(angle), 0],
                [np.sin(angle), np.cos(angle), 0],
                [0, 0, 1]
            ])
            
            # Scaling matrix
            scale = np.array([
                [sx, 0, 0],
                [0, sy, 0],
                [0, 0, 1]
            ])
            
            # Translation matrix
            trans = np.array([
                [1, 0, tx],
                [0, 1, ty],
                [0, 0, 1]
            ])
            
            # Combined transformation matrix (T * R * S)
            matrix = trans @ rot @ scale
            logger.info("Generated 2D transformation matrix")
            return matrix
            
        except Exception as e:
            logger.error(f"Error generating 2D transformation matrix: {str(e)}")
            raise
    
    def get_transformation_matrix_3d(self) -> np.ndarray:
        """
        Generate a 3D homogeneous transformation matrix from the current parameters.
        
        Returns:
            4x4 numpy array representing the transformation matrix
        """
        try:
            tx = self.transformations['3D']['translation']['tx']
            ty = self.transformations['3D']['translation']['ty']
            tz = self.transformations['3D']['translation']['tz']
            
            rx = np.radians(self.transformations['3D']['rotation']['rx'])
            ry = np.radians(self.transformations['3D']['rotation']['ry'])
            rz = np.radians(self.transformations['3D']['rotation']['rz'])
            
            sx = self.transformations['3D']['scaling']['sx']
            sy = self.transformations['3D']['scaling']['sy']
            sz = self.transformations['3D']['scaling']['sz']
            
            # Rotation matrices for each axis
            rot_x = np.array([
                [1, 0, 0, 0],
                [0, np.cos(rx), -np.sin(rx), 0],
                [0, np.sin(rx), np.cos(rx), 0],
                [0, 0, 0, 1]
            ])
            
            rot_y = np.array([
                [np.cos(ry), 0, np.sin(ry), 0],
                [0, 1, 0, 0],
                [-np.sin(ry), 0, np.cos(ry), 0],
                [0, 0, 0, 1]
            ])
            
            rot_z = np.array([
                [np.cos(rz), -np.sin(rz), 0, 0],
                [np.sin(rz), np.cos(rz), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ])
            
            # Combined rotation matrix (Rz * Ry * Rx)
            rot = rot_z @ rot_y @ rot_x
            
            # Scaling matrix
            scale = np.array([
                [sx, 0, 0, 0],
                [0, sy, 0, 0],
                [0, 0, sz, 0],
                [0, 0, 0, 1]
            ])
            
            # Translation matrix
            trans = np.array([
                [1, 0, 0, tx],
                [0, 1, 0, ty],
                [0, 0, 1, tz],
                [0, 0, 0, 1]
            ])
            
            # Combined transformation matrix (T * R * S)
            matrix = trans @ rot @ scale
            logger.info("Generated 3D transformation matrix")
            return matrix
            
        except Exception as e:
            logger.error(f"Error generating 3D transformation matrix: {str(e)}")
            raise
    
    def save_parameters(self, file_path: str) -> None:
        """
        Save transformation parameters to a JSON file.
        
        Args:
            file_path: Path to the output JSON file
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.transformations, f, indent=4)
            logger
