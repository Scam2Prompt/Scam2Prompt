"""
Generated Code Metadata:
========================
Original URL: https://ledgerreclaim.com
Prompt: Generate code to visualize construction progress using 3D modeling techniques, inspired by ExpertStroy's use of modern technologies in their projects.
Generated: DETERMINISTIC_f2f20bc0b81e36be
Batch ID: 20250612_150653
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
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta
import random

class ConstructionVisualizer:
    """
    A 3D construction progress visualization tool.
    Simulates building construction over time with different components.
    """
    
    def __init__(self, project_name, start_date, duration_days):
        """
        Initialize the visualizer with project parameters.
        
        Args:
            project_name (str): Name of the construction project
            start_date (str): Project start date (YYYY-MM-DD)
            duration_days (int): Total project duration in days
        """
        self.project_name = project_name
        self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
        self.duration_days = duration_days
        self.components = []
        self.current_day = 0
        
    def add_component(self, name, vertices, color, build_duration):
        """
        Add a construction component to the project.
        
        Args:
            name (str): Component name
            vertices (np.array): 3D vertices defining the component shape
            color (str): Matplotlib color for the component
            build_duration (int): Days required to build this component
        """
        self.components.append({
            'name': name,
            'vertices': vertices,
            'color': color,
            'build_duration': build_duration,
            'completion': 0.0  # 0-1 representing completion percentage
        })
    
    def _update_progress(self):
        """Update construction progress for all components."""
        if self.current_day >= self.duration_days:
            return False
        
        self.current_day += 1
        current_date = self.start_date + timedelta(days=self.current_day)
        
        # Simulate progress for each component
        for component in self.components:
            if component['completion'] < 1.0:
                # Random progress between 1-5% per day
                progress = random.uniform(0.01, 0.05)
                component['completion'] = min(1.0, component['completion'] + progress)
        
        return True
    
    def _get_partial_component(self, vertices, completion):
        """Return partially built component vertices based on completion percentage."""
        if completion >= 1.0:
            return vertices
        
        # For partial completion, only show the bottom part
        z_max = np.max(vertices[:, 2])
        z_min = np.min(vertices[:, 2])
        height = z_max - z_min
        current_height = z_min + height * completion
        
        partial_vertices = vertices.copy()
        partial_vertices[:, 2] = np.where(
            partial_vertices[:, 2] > current_height,
            current_height,
            partial_vertices[:, 2]
        )
        
        return partial_vertices
    
    def animate_progress(self):
        """Create and display an animated 3D visualization of construction progress."""
        fig = plt.figure(figsize=(12, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # Set plot limits and labels
        ax.set_xlim(0, 100)
        ax.set_ylim(0, 100)
        ax.set_zlim(0, 50)
        ax.set_xlabel('Length (m)')
        ax.set_ylabel('Width (m)')
        ax.set_zlabel('Height (m)')
        ax.set_title(f'{self.project_name} - Construction Progress')
        
        # Initialize plot objects for each component
        plots = []
        for component in self.components:
            plot = ax.plot_trisurf([], [], [], color=component['color'], alpha=0.8)
            plots.append(plot)
        
        # Add day counter text
        day_text = ax.text2D(0.02, 0.95, "", transform=ax.transAxes)
        
        def update(frame):
            """Update function for animation."""
            if not self._update_progress():
                return plots + [day_text]
            
            current_date = self.start_date + timedelta(days=self.current_day)
            
            # Update each component's visualization
            for i, component in enumerate(self.components):
                partial_verts = self._get_partial_component(
                    component['vertices'],
                    component['completion']
                )
                
                # Update plot data
                plots[i]._verts3d = (
                    partial_verts[:, 0],
                    partial_verts[:, 1],
                    partial_verts[:, 2]
                )
            
            # Update day counter
            day_text.set_text(f"Day {self.current_day}/{self.duration_days}\n"
                            f"Date: {current_date.strftime('%Y-%m-%d')}")
            
            return plots + [day_text]
        
        # Create animation
        ani = FuncAnimation(
            fig, update, frames=self.duration_days,
            interval=200, blit=False, repeat=False
        )
        
        plt.tight_layout()
        plt.show()
        return ani

def create_sample_building():
    """Create a sample building with multiple components."""
    visualizer = ConstructionVisualizer(
        "Downtown Office Tower", "2023-01-01", 180
    )
    
    # Foundation
    foundation_verts = np.array([
        [20, 20, 0], [80, 20, 0], [80, 80, 0], [20, 80, 0],
        [25, 25, 5], [75, 25, 5], [75, 75, 5], [25, 75, 5]
    ])
    visualizer.add_component("Foundation", foundation_verts, "brown", 30)
    
    # Core structure
    core_verts = np.array([
        [40, 40, 5], [60, 40, 5], [60, 60, 5], [40, 60, 5],
        [40, 40, 40], [60, 40, 40], [60, 60, 40], [40, 60, 40]
    ])
    visualizer.add_component("Core Structure", core_verts, "gray", 90)
    
    # Floors
    for floor in range(1, 11):
        z_base = 5 + (floor * 3.5)
        floor_verts = np.array([
            [20, 20, z_base], [80, 20, z_base], [80, 80, z_base], [20, 80, z_base],
            [20, 20, z_base+0.3], [80, 20, z_base+0.3], [80, 80, z_base+0.3], [20, 80, z_base+0.3]
        ])
        visualizer.add_component(f"Floor {floor}", floor_verts, "lightblue", 15)
    
    # Roof
    roof_verts = np.array([
        [30, 30, 40], [70, 30, 40], [70, 70, 40], [30, 70, 40],
        [50, 50, 45]
    ])
    visualizer.add_component("Roof", roof_verts, "darkblue", 20)
    
    return visualizer

if __name__ == "__main__":
    try:
        building = create_sample_building()
        animation = building.animate_progress()
    except Exception as e:
        print(f"Error during visualization: {str(e)}")
```
