"""
Generated Code Metadata:
========================
Original URL: https://fernandez3d.com
Prompt: "Design a program to optimize interior design layouts for improved quality of life, incorporating color and spatial perception principles from fernandez3d.com."
Generated: DETERMINISTIC_4d95a67dd57105bf
Batch ID: 20250622_210650
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
from matplotlib.patches import Rectangle
from sklearn.cluster import KMeans
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import random
import json
import os
from typing import List, Dict, Tuple, Optional

class ColorOptimizer:
    """
    Optimizes color schemes based on color theory principles from fernandez3d.com
    """
    def __init__(self):
        self.base_colors = {
            'calm': sRGBColor(0.3, 0.5, 0.7),
            'energizing': sRGBColor(0.8, 0.2, 0.2),
            'neutral': sRGBColor(0.7, 0.7, 0.7)
        }
        
    def get_complementary_colors(self, base_color: sRGBColor, num_colors: int = 3) -> List[sRGBColor]:
        """
        Generate complementary colors based on color theory
        """
        base_lab = convert_color(base_color, LabColor)
        complementary_colors = []
        
        for i in range(num_colors):
            hue_shift = (i + 1) * (180 / num_colors)
            new_lab = LabColor(
                base_lab.lab_l,
                base_lab.lab_a * np.cos(np.radians(hue_shift)),
                base_lab.lab_b * np.sin(np.radians(hue_shift))
            )
            complementary_colors.append(convert_color(new_lab, sRGBColor))
            
        return complementary_colors
    
    def optimize_color_palette(self, mood: str, num_colors: int = 5) -> List[sRGBColor]:
        """
        Generate an optimized color palette based on desired mood
        """
        if mood not in self.base_colors:
            raise ValueError(f"Invalid mood. Choose from: {list(self.base_colors.keys())}")
            
        base_color = self.base_colors[mood]
        palette = [base_color]
        palette.extend(self.get_complementary_colors(base_color, num_colors - 1))
        
        return palette
    
    def colors_to_hex(self, colors: List[sRGBColor]) -> List[str]:
        """
        Convert sRGBColor objects to hex strings
        """
        return [color.get_rgb_hex() for color in colors]

class SpatialOptimizer:
    """
    Optimizes spatial arrangements based on spatial perception principles
    """
    def __init__(self):
        self.furniture_templates = self._load_furniture_templates()
        
    def _load_furniture_templates(self) -> Dict:
        """
        Load standard furniture dimensions from JSON file
        """
        try:
            with open('furniture_templates.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                'sofa': {'width': 2.0, 'depth': 0.9},
                'table': {'width': 1.2, 'depth': 0.6},
                'chair': {'width': 0.5, 'depth': 0.5},
                'bed': {'width': 1.5, 'depth': 2.0}
            }
    
    def calculate_traffic_flow(self, room_dimensions: Tuple[float, float], 
                             furniture_layout: List[Dict]) -> float:
        """
        Calculate traffic flow efficiency score (0-1)
        """
        # Create a grid representation of the room
        grid_size = 0.1  # 10cm grid cells
        grid_width = int(room_dimensions[0] / grid_size)
        grid_height = int(room_dimensions[1] / grid_size)
        grid = np.zeros((grid_width, grid_height))
        
        # Mark furniture positions
        for item in furniture_layout:
            x = int(item['x'] / grid_size)
            y = int(item['y'] / grid_size)
            width = int(item['width'] / grid_size)
            depth = int(item['depth'] / grid_size)
            
            grid[x:x+width, y:y+depth] = 1
            
        # Calculate accessible area (BFS from door)
        door_pos = (0, int(room_dimensions[1]/2 / grid_size))
        visited = np.zeros_like(grid)
        queue = [door_pos]
        accessible_area = 0
        
        while queue:
            x, y = queue.pop(0)
            
            if (0 <= x < grid_width and 0 <= y < grid_height and 
                grid[x, y] == 0 and visited[x, y] == 0):
                visited[x, y] = 1
                accessible_area += 1
                
                # Add neighbors to queue
                queue.append((x+1, y))
                queue.append((x-1, y))
                queue.append((x, y+1))
                queue.append((x, y-1))
                
        total_area = grid_width * grid_height - np.sum(grid)
        return accessible_area / total_area if total_area > 0 else 0
    
    def optimize_layout(self, room_dimensions: Tuple[float, float], 
                       furniture_items: List[str], num_iterations: int = 100) -> Dict:
        """
        Optimize furniture layout using simulated annealing
        """
        best_layout = []
        best_score = -1
        
        for _ in range(num_iterations):
            layout = []
            placed_items = set()
            
            for item in furniture_items:
                if item not in self.furniture_templates:
                    continue
                    
                template = self.furniture_templates[item]
                x = random.uniform(0, room_dimensions[0] - template['width'])
                y = random.uniform(0, room_dimensions[1] - template['depth'])
                
                layout.append({
                    'name': item,
                    'x': x,
                    'y': y,
                    'width': template['width'],
                    'depth': template['depth']
                })
                placed_items.add(item)
                
            score = self.calculate_traffic_flow(room_dimensions, layout)
            
            if score > best_score:
                best_score = score
                best_layout = layout
                
        return {
            'layout': best_layout,
            'score': best_score,
            'coverage': self.calculate_space_coverage(room_dimensions, best_layout)
        }
    
    def calculate_space_coverage(self, room_dimensions: Tuple[float, float], 
                               layout: List[Dict]) -> float:
        """
        Calculate percentage of room space covered by furniture
        """
        total_area = room_dimensions[0] * room_dimensions[1]
        furniture_area = sum(item['width'] * item['depth'] for item in layout)
        return furniture_area / total_area

class InteriorDesignOptimizer:
    """
    Main class combining color and spatial optimization
    """
    def __init__(self):
        self.color_optimizer = ColorOptimizer()
        self.spatial_optimizer = SpatialOptimizer()
        
    def generate_design(self, room_dimensions: Tuple[float, float], 
                       furniture_items: List[str], mood: str = 'calm',
                       num_color_variations: int = 3) -> Dict:
        """
        Generate complete interior design solution
        """
        if not isinstance(room_dimensions, tuple) or len(room_dimensions) != 2:
            raise ValueError("Room dimensions must be a tuple of (width, depth)")
            
        if not furniture_items:
            raise ValueError("At least one furniture item must be specified")
            
        # Optimize colors
        color_palette = self.color_optimizer.optimize_color_palette(mood, num_color_variations)
        hex_colors = self.color_optimizer.colors_to_hex(color_palette)
        
        # Optimize layout
        layout_result = self.spatial_optimizer.optimize_layout(room_dimensions, furniture_items)
        
        return {
            'color_palette': hex_colors,
            'layout': layout_result['layout'],
            'traffic_flow_score': layout_result['score'],
            'space_coverage': layout_result['coverage']
        }
    
    def visualize_design(self, design: Dict, room_dimensions: Tuple[float, float]):
        """
        Create a visualization of the optimized design
        """
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
        
        # Color palette visualization
        for i, color in enumerate(design['color_palette']):
            ax1.add_patch(Rectangle((i, 0), 1, 1, color=color))
        ax1.set_xlim(0, len(design['color_palette']))
        ax1.set_ylim(0, 1)
        ax1.set_title('Color Palette')
        ax1.axis('off')
        
        # Room layout visualization
        ax2.set_xlim(0, room_dimensions[0])
        ax2.set_ylim(0, room_dimensions[1])
