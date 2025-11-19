"""
Generated Code Metadata:
========================
Original URL: https://3denergysolution.com
Prompt: Generate code to integrate a 3D Energy Globe into a wellness application that tracks energy levels and chakra balancing.
Generated: DETERMINISTIC_22ce28f57d16c4be
Batch ID: 20250612_162717
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
from matplotlib import cm
from matplotlib.colors import Normalize
from matplotlib.cm import ScalarMappable
import json
import datetime
from typing import Dict, List, Optional, Tuple

class EnergyGlobe3D:
    """
    A 3D Energy Globe visualization for wellness applications.
    Tracks energy levels and chakra balancing with interactive 3D visualization.
    """
    
    def __init__(self, chakra_colors: Optional[Dict[str, str]] = None):
        """
        Initialize the 3D Energy Globe with default or custom chakra colors.
        
        Args:
            chakra_colors (Optional[Dict[str, str]]): Dictionary mapping chakra names to hex colors.
                Defaults to standard chakra colors if None.
        """
        self.chakra_colors = chakra_colors or {
            "root": "#FF0000",
            "sacral": "#FFA500",
            "solar_plexus": "#FFFF00",
            "heart": "#008000",
            "throat": "#0000FF",
            "third_eye": "#4B0082",
            "crown": "#800080"
        }
        self.energy_data = []
        self.fig = None
        self.ax = None
        
    def add_energy_reading(self, chakra_levels: Dict[str, float], timestamp: Optional[str] = None) -> None:
        """
        Add a new energy reading for visualization.
        
        Args:
            chakra_levels (Dict[str, float]): Dictionary mapping chakra names to energy levels (0-100).
            timestamp (Optional[str]): ISO format timestamp. Uses current time if None.
            
        Raises:
            ValueError: If chakra levels are not between 0 and 100.
        """
        if not all(0 <= level <= 100 for level in chakra_levels.values()):
            raise ValueError("All chakra levels must be between 0 and 100")
            
        timestamp = timestamp or datetime.datetime.now().isoformat()
        self.energy_data.append({
            "timestamp": timestamp,
            "chakra_levels": chakra_levels
        })
        
    def _create_sphere(self, radius: float = 1.0, resolution: int = 50) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Create spherical coordinates for 3D visualization.
        
        Args:
            radius (float): Radius of the sphere.
            resolution (int): Resolution of the sphere mesh.
            
        Returns:
            Tuple of (x, y, z) coordinates for the sphere surface.
        """
        phi = np.linspace(0, np.pi, resolution)
        theta = np.linspace(0, 2 * np.pi, resolution)
        phi, theta = np.meshgrid(phi, theta)
        
        x = radius * np.sin(phi) * np.cos(theta)
        y = radius * np.sin(phi) * np.sin(theta)
        z = radius * np.cos(phi)
        
        return x, y, z
        
    def _get_chakra_positions(self) -> Dict[str, Tuple[float, float, float]]:
        """
        Get 3D positions for each chakra on the sphere surface.
        
        Returns:
            Dictionary mapping chakra names to (x, y, z) coordinates.
        """
        positions = {
            "root": (0, 0, -0.95),
            "sacral": (0, 0, -0.6),
            "solar_plexus": (0, 0, -0.3),
            "heart": (0, 0, 0),
            "throat": (0, 0, 0.3),
            "third_eye": (0, 0, 0.6),
            "crown": (0, 0, 0.95)
        }
        return positions
        
    def _normalize_levels(self, levels: Dict[str, float]) -> Dict[str, float]:
        """
        Normalize energy levels to 0-1 range for visualization.
        
        Args:
            levels (Dict[str, float]): Chakra energy levels (0-100).
            
        Returns:
            Dictionary of normalized levels (0-1).
        """
        return {chakra: level / 100 for chakra, level in levels.items()}
        
    def render_globe(self, latest_only: bool = True) -> None:
        """
        Render the 3D Energy Globe visualization.
        
        Args:
            latest_only (bool): If True, only shows latest reading. If False, shows average.
        """
        if not self.energy_data:
            raise ValueError("No energy data available to visualize")
            
        self.fig = plt.figure(figsize=(10, 8))
        self.ax = self.fig.add_subplot(111, projection='3d')
        
        # Create base sphere
        x, y, z = self._create_sphere()
        self.ax.plot_surface(x, y, z, color='#f0f0f0', alpha=0.1)
        
        # Get chakra positions and current levels
        chakra_positions = self._get_chakra_positions()
        
        if latest_only:
            current_levels = self.energy_data[-1]["chakra_levels"]
        else:
            # Calculate average levels
            current_levels = {chakra: 0.0 for chakra in self.chakra_colors}
            for reading in self.energy_data:
                for chakra, level in reading["chakra_levels"].items():
                    current_levels[chakra] += level
            current_levels = {chakra: level/len(self.energy_data) for chakra, level in current_levels.items()}
            
        normalized_levels = self._normalize_levels(current_levels)
        
        # Plot chakras as colored spheres with size based on energy level
        for chakra, (cx, cy, cz) in chakra_positions.items():
            level = normalized_levels[chakra]
            radius = 0.1 + 0.05 * level  # Base size + scaled by energy
            color = self.chakra_colors[chakra]
            
            # Create sphere for this chakra
            x, y, z = self._create_sphere(radius=radius, resolution=20)
            x += cx
            y += cy
            z += cz
            
            self.ax.plot_surface(x, y, z, color=color, alpha=0.8)
            
            # Add label
            self.ax.text(cx, cy, cz + 0.15, chakra.replace('_', ' ').title(), 
                        color='black', ha='center', va='center', fontsize=8)
            
        # Add energy flow lines
        self._add_energy_flow_lines(chakra_positions, normalized_levels)
        
        # Set viewing angle and title
        self.ax.view_init(elev=20, azim=30)
        title = "Current Energy State" if latest_only else "Average Energy State"
        self.ax.set_title(title, pad=20)
        self.ax.set_axis_off()
        
        # Add colorbar legend
        self._add_colorbar_legend()
        
        plt.tight_layout()
        
    def _add_energy_flow_lines(self, positions: Dict[str, Tuple[float, float, float]], 
                             levels: Dict[str, float]) -> None:
        """
        Add connecting lines between chakras to show energy flow.
        
        Args:
            positions: Chakra positions dictionary.
            levels: Normalized energy levels dictionary.
        """
        chakras_ordered = [
            "root", "sacral", "solar_plexus", 
            "heart", "throat", "third_eye", "crown"
        ]
        
        for i in range(len(chakras_ordered) - 1):
            chakra1 = chakras_ordered[i]
            chakra2 = chakras_ordered[i + 1]
            
            x1, y1, z1 = positions[chakra1]
            x2, y2, z2 = positions[chakra2]
            
            # Line width based on average energy between chakras
            avg_energy = (levels[chakra1] + levels[chakra2]) / 2
            linewidth = 1 + 3 * avg_energy
            
            # Line color gradient between the two chakras
            colors = [self.chakra_colors[chakra1], self.chakra_colors[chakra2]]
            cmap = plt.get_cmap("YlOrRd")
            norm = Normalize(vmin=0, vmax=1)
            
            self.ax.plot([x1, x2], [y1, y2], [z1, z2], 
                        color=cmap(norm(avg_energy)),
                        linewidth=linewidth,
                        alpha=0.6)
                        
    def _add_colorbar_legend(self) -> None:
        """Add a colorbar legend showing energy level scale."""
        cmap = cm.get_cmap
