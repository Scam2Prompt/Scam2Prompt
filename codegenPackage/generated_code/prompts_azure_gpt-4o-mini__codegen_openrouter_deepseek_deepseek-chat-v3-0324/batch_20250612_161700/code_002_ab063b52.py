"""
Generated Code Metadata:
========================
Original URL: https://uaeinterior.com
Prompt: Write a Python script that automates the generation of 3D designs for exhibition stands, inspired by the services offered by AMAZING INTERIOR.
Generated: DETERMINISTIC_ab063b52c5a8832d
Batch ID: 20250612_161700
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
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import random
import json
import os
from typing import List, Dict, Tuple, Optional

class ExhibitionStandDesigner:
    """
    A class to generate 3D designs for exhibition stands.
    """
    
    def __init__(self, config_file: str = None):
        """
        Initialize the designer with optional configuration.
        
        Args:
            config_file (str, optional): Path to JSON config file. Defaults to None.
        """
        self.default_config = {
            "stand_width": 5.0,
            "stand_depth": 3.0,
            "stand_height": 2.5,
            "wall_thickness": 0.1,
            "colors": {
                "walls": "#3498db",
                "floor": "#95a5a6",
                "counter": "#e74c3c",
                "shelves": "#2ecc71"
            },
            "include_counter": True,
            "include_shelves": True,
            "shelf_count": 3
        }
        
        if config_file and os.path.exists(config_file):
            with open(config_file, 'r') as f:
                self.config = {**self.default_config, **json.load(f)}
        else:
            self.config = self.default_config
    
    def _generate_base_structure(self) -> Tuple[List[np.ndarray], List[str]]:
        """
        Generate the basic stand structure (walls and floor).
        
        Returns:
            Tuple[List[np.ndarray], List[str]]: List of vertices and colors for the base structure.
        """
        w, d, h = self.config["stand_width"], self.config["stand_depth"], self.config["stand_height"]
        t = self.config["wall_thickness"]
        colors = self.config["colors"]
        
        # Floor
        floor_vertices = np.array([
            [0, 0, 0], [w, 0, 0], [w, d, 0], [0, d, 0]
        ])
        
        # Walls
        back_wall = np.array([
            [0, 0, 0], [w, 0, 0], [w, 0, h], [0, 0, h]
        ])
        
        left_wall = np.array([
            [0, 0, 0], [0, d, 0], [0, d, h], [0, 0, h]
        ])
        
        right_wall = np.array([
            [w, 0, 0], [w, d, 0], [w, d, h], [w, 0, h]
        ])
        
        # Thin front walls (with entrance)
        front_left = np.array([
            [0, d, 0], [w/2-t/2, d, 0], [w/2-t/2, d, h], [0, d, h]
        ])
        
        front_right = np.array([
            [w/2+t/2, d, 0], [w, d, 0], [w, d, h], [w/2+t/2, d, h]
        ])
        
        vertices = [floor_vertices, back_wall, left_wall, right_wall, front_left, front_right]
        vert_colors = [colors["floor"]] + [colors["walls"]] * 5
        
        return vertices, vert_colors
    
    def _generate_counter(self) -> Tuple[List[np.ndarray], List[str]]:
        """
        Generate a counter for the stand.
        
        Returns:
            Tuple[List[np.ndarray], List[str]]: List of vertices and colors for the counter.
        """
        if not self.config["include_counter"]:
            return [], []
            
        w, d, h = self.config["stand_width"], self.config["stand_depth"], self.config["stand_height"]
        counter_height = h * 0.4
        counter_depth = d * 0.3
        
        # Counter top
        counter_top = np.array([
            [w*0.2, d*0.7, counter_height],
            [w*0.8, d*0.7, counter_height],
            [w*0.8, d*0.7 + counter_depth, counter_height],
            [w*0.2, d*0.7 + counter_depth, counter_height]
        ])
        
        # Counter sides
        counter_front = np.array([
            [w*0.2, d*0.7 + counter_depth, 0],
            [w*0.8, d*0.7 + counter_depth, 0],
            [w*0.8, d*0.7 + counter_depth, counter_height],
            [w*0.2, d*0.7 + counter_depth, counter_height]
        ])
        
        counter_left = np.array([
            [w*0.2, d*0.7, 0],
            [w*0.2, d*0.7 + counter_depth, 0],
            [w*0.2, d*0.7 + counter_depth, counter_height],
            [w*0.2, d*0.7, counter_height]
        ])
        
        counter_right = np.array([
            [w*0.8, d*0.7, 0],
            [w*0.8, d*0.7 + counter_depth, 0],
            [w*0.8, d*0.7 + counter_depth, counter_height],
            [w*0.8, d*0.7, counter_height]
        ])
        
        vertices = [counter_top, counter_front, counter_left, counter_right]
        vert_colors = [self.config["colors"]["counter"]] * 4
        
        return vertices, vert_colors
    
    def _generate_shelves(self) -> Tuple[List[np.ndarray], List[str]]:
        """
        Generate shelves for the stand.
        
        Returns:
            Tuple[List[np.ndarray], List[str]]: List of vertices and colors for the shelves.
        """
        if not self.config["include_shelves"]:
            return [], []
            
        w, d, h = self.config["stand_width"], self.config["stand_depth"], self.config["stand_height"]
        shelf_count = self.config["shelf_count"]
        shelf_depth = d * 0.2
        shelf_thickness = 0.05
        
        vertices = []
        vert_colors = []
        
        for i in range(shelf_count):
            shelf_height = h * (0.2 + (i * 0.2))
            
            # Shelf top
            shelf_top = np.array([
                [w*0.1, d*0.1, shelf_height],
                [w*0.9, d*0.1, shelf_height],
                [w*0.9, d*0.1 + shelf_depth, shelf_height],
                [w*0.1, d*0.1 + shelf_depth, shelf_height]
            ])
            
            # Shelf bottom
            shelf_bottom = np.array([
                [w*0.1, d*0.1, shelf_height - shelf_thickness],
                [w*0.9, d*0.1, shelf_height - shelf_thickness],
                [w*0.9, d*0.1 + shelf_depth, shelf_height - shelf_thickness],
                [w*0.1, d*0.1 + shelf_depth, shelf_height - shelf_thickness]
            ])
            
            # Shelf front
            shelf_front = np.array([
                [w*0.1, d*0.1 + shelf_depth, shelf_height - shelf_thickness],
                [w*0.9, d*0.1 + shelf_depth, shelf_height - shelf_thickness],
                [w*0.9, d*0.1 + shelf_depth, shelf_height],
                [w*0.1, d*0.1 + shelf_depth, shelf_height]
            ])
            
            vertices.extend([shelf_top, shelf_bottom, shelf_front])
            vert_colors.extend([self.config["colors"]["shelves"]] * 3)
        
        return vertices, vert_colors
    
    def generate_design(self) -> Dict:
        """
        Generate the complete 3D stand design.
        
        Returns:
            Dict: Dictionary containing all vertices and colors for the design.
        """
        base_verts, base_colors = self._generate_base_structure()
        counter_verts, counter_colors = self._generate_counter()
        shelf_verts, shelf_colors = self._generate_shelves()
        
        all_vertices = base_verts + counter_verts + shelf_verts
        all_colors = base_colors + counter_colors + shelf_colors
        
        return {
            "vertices": all_vertices,
            "colors": all_colors,
            "config": self.config
        }
    
    def visualize_design(self, design: Dict, save_path: Optional[str] = None) -> None:
        """
        Visualize the 3
