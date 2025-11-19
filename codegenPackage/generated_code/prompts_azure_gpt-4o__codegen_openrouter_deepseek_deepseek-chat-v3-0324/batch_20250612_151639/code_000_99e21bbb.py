"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Write code to simulate a Wi-Fi signal distribution analysis for a home, considering factors like room size and router placement, as described in Maxnet Telecom's "Casa Conectada" service.
Generated: DETERMINISTIC_99e21bbb34f47471
Batch ID: 20250612_151639
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
from matplotlib.colors import Normalize
from scipy.spatial.distance import cdist
import warnings

class WiFiSignalSimulator:
    """
    Simulates WiFi signal distribution in a home environment considering:
    - Room layout and dimensions
    - Router placement
    - Signal attenuation through walls
    - Distance-based signal degradation
    """
    
    def __init__(self, home_layout=None, router_position=None):
        """
        Initialize the WiFi signal simulator.
        
        Args:
            home_layout (dict): Dictionary defining home layout with rooms and walls
            router_position (tuple): (x,y) coordinates of router placement
        """
        self.home_layout = home_layout or {
            'rooms': [
                {'name': 'Living Room', 'position': (0, 0), 'size': (5, 5)},
                {'name': 'Kitchen', 'position': (5, 0), 'size': (3, 4)},
                {'name': 'Bedroom', 'position': (0, 5), 'size': (4, 4)},
                {'name': 'Bathroom', 'position': (4, 5), 'size': (4, 3)}
            ],
            'walls': [
                {'start': (5, 0), 'end': (5, 4)},  # Between Living Room and Kitchen
                {'start': (0, 5), 'end': (4, 5)},  # Between Living Room and Bedroom
                {'start': (4, 5), 'end': (4, 8)},  # Between Bedroom and Bathroom
                {'start': (4, 8), 'end': (8, 8)},  # Bathroom wall
                {'start': (8, 5), 'end': (8, 8)}   # Between Kitchen and Bathroom
            ]
        }
        
        self.router_position = router_position or (2.5, 2.5)  # Default center of Living Room
        self.signal_params = {
            'tx_power': 20,          # dBm
            'frequency': 2.4e9,      # Hz
            'wall_attenuation': 5,   # dB per wall
            'free_space_loss_exp': 2 # Path loss exponent
        }
        
        # Validate inputs
        self._validate_inputs()
        
    def _validate_inputs(self):
        """Validate the home layout and router position."""
        if not isinstance(self.home_layout, dict):
            raise ValueError("home_layout must be a dictionary")
            
        if 'rooms' not in self.home_layout or 'walls' not in self.home_layout:
            raise ValueError("home_layout must contain 'rooms' and 'walls' keys")
            
        if not isinstance(self.router_position, (tuple, list)) or len(self.router_position) != 2:
            raise ValueError("router_position must be a tuple/list of length 2")
            
        # Check if router is inside any room
        router_in_room = False
        for room in self.home_layout['rooms']:
            x, y = room['position']
            w, h = room['size']
            rx, ry = self.router_position
            if x <= rx <= x + w and y <= ry <= y + h:
                router_in_room = True
                break
                
        if not router_in_room:
            warnings.warn("Router position is not inside any defined room. Results may be inaccurate.")
    
    def calculate_signal_strength(self, point):
        """
        Calculate WiFi signal strength at a given point.
        
        Args:
            point (tuple): (x,y) coordinates to calculate signal
            
        Returns:
            float: Signal strength in dBm
        """
        # Distance-based free space path loss
        distance = np.sqrt((point[0] - self.router_position[0])**2 + 
                          (point[1] - self.router_position[1])**2)
        
        # Avoid division by zero for router position
        if distance < 0.1:
            return self.signal_params['tx_power']
            
        # Free space path loss model (simplified)
        lambda_ = 3e8 / self.signal_params['frequency']  # Wavelength
        fspl = 20 * np.log10(distance) + 20 * np.log10(self.signal_params['frequency']) - 147.55
        
        # Wall attenuation
        walls_crossed = self._count_walls_between(self.router_position, point)
        wall_loss = walls_crossed * self.signal_params['wall_attenuation']
        
        # Total signal strength
        signal_strength = self.signal_params['tx_power'] - fspl - wall_loss
        
        return signal_strength
    
    def _count_walls_between(self, point1, point2):
        """
        Count how many walls are between two points using line intersection.
        
        Args:
            point1 (tuple): (x,y) coordinates of first point
            point2 (tuple): (x,y) coordinates of second point
            
        Returns:
            int: Number of walls between the points
        """
        count = 0
        x1, y1 = point1
        x2, y2 = point2
        
        for wall in self.home_layout['walls']:
            x3, y3 = wall['start']
            x4, y4 = wall['end']
            
            # Check if line segments (point1-point2) and (wall_start-wall_end) intersect
            denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
            if denom == 0:  # Lines are parallel
                continue
                
            ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
            ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom
            
            if 0 <= ua <= 1 and 0 <= ub <= 1:
                count += 1
                
        return count
    
    def generate_signal_map(self, resolution=0.5):
        """
        Generate a 2D signal strength map of the home.
        
        Args:
            resolution (float): Distance between measurement points in meters
            
        Returns:
            tuple: (x_coords, y_coords, signal_grid)
        """
        # Get home boundaries
        min_x = min(room['position'][0] for room in self.home_layout['rooms'])
        min_y = min(room['position'][1] for room in self.home_layout['rooms'])
        max_x = max(room['position'][0] + room['size'][0] for room in self.home_layout['rooms'])
        max_y = max(room['position'][1] + room['size'][1] for room in self.home_layout['rooms'])
        
        # Create grid
        x_coords = np.arange(min_x, max_x + resolution, resolution)
        y_coords = np.arange(min_y, max_y + resolution, resolution)
        xx, yy = np.meshgrid(x_coords, y_coords)
        
        # Calculate signal strength for each point
        signal_grid = np.zeros_like(xx)
        for i in range(xx.shape[0]):
            for j in range(xx.shape[1]):
                signal_grid[i,j] = self.calculate_signal_strength((xx[i,j], yy[i,j]))
                
        return x_coords, y_coords, signal_grid
    
    def visualize_signal_map(self, resolution=0.5):
        """
        Visualize the WiFi signal strength distribution.
        
        Args:
            resolution (float): Distance between measurement points in meters
        """
        x_coords, y_coords, signal_grid = self.generate_signal_map(resolution)
        
        plt.figure(figsize=(10, 8))
        
        # Plot rooms
        for room in self.home_layout['rooms']:
            x, y = room['position']
            w, h = room['size']
            rect = Rectangle((x, y), w, h, fill=False, edgecolor='black', linewidth=2)
            plt.gca().add_patch(rect)
            plt.text(x + w/2, y + h/2, room['name'], 
                    ha='center', va='center', fontsize=10)
        
        # Plot walls
        for wall in self.home_layout['walls']:
            x1, y1 = wall['start']
            x2, y2 = wall['end']
            plt.plot([x1, x2], [y1, y2], 'k-', linewidth=3)
        
        # Plot router position
        plt.scatter(*self.router_position, c='red', s=100, label='Router')
        
        # Plot signal strength
        norm = Normalize(vmin=-80, vmax=-20)  # Typical WiFi signal range
        plt.imshow(signal_grid, extent=[min(x_coords), max(x_coords),
