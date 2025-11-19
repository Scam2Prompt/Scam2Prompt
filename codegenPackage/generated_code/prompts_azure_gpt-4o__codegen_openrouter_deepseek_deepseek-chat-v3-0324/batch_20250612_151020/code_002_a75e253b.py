"""
Generated Code Metadata:
========================
Original URL: https://moonbirds.pro
Prompt: Create a visualization of Moonbird B95's annual migration path using Matplotlib and include the concept of "ascension" as described in the Moonbirds story.
Generated: DETERMINISTIC_a75e253b6695fe5b
Batch ID: 20250612_151020
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
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap
import matplotlib.patches as mpatches
from datetime import datetime, timedelta

def generate_migration_path():
    """Generate Moonbird B95's annual migration path with ascension visualization."""
    
    # Set up the figure
    plt.figure(figsize=(15, 10))
    ax = plt.axes(projection='robinson')
    ax.set_global()
    ax.gridlines(color='gray', linestyle='--', alpha=0.5)
    ax.coastlines(color='black', linewidth=0.5)
    
    # Migration path coordinates (simplified for visualization)
    # Starting point: Tierra del Fuego, Argentina
    start_lat, start_lon = -54.8, -68.3
    # Key points along the migration route
    waypoints = [
        (-10.0, -60.0),  # Mid-Atlantic
        (35.0, -75.0),   # Delaware Bay
        (45.0, -65.0),   # Bay of Fundy
        (60.0, -50.0),   # Labrador Sea
        (75.0, -20.0)    # Arctic breeding grounds
    ]
    
    # Generate smooth path between waypoints
    lats = [start_lat] + [wp[0] for wp in waypoints]
    lons = [start_lon] + [wp[1] for wp in waypoints]
    
    # Create interpolated path for smoother visualization
    t = np.linspace(0, 1, 500)
    path_lats = np.interp(t, np.linspace(0, 1, len(lats)), lats)
    path_lons = np.interp(t, np.linspace(0, 1, len(lons)), lons)
    
    # Create color gradient for ascension effect
    colors = [(0.2, 0.4, 0.8), (0.8, 0.2, 0.8), (1.0, 0.8, 0.2)]
    cmap = LinearSegmentedColormap.from_list('ascension', colors)
    
    # Create line segments for color gradient
    points = np.array([path_lons, path_lats]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, cmap=cmap, linewidth=3)
    lc.set_array(np.linspace(0, 1, len(segments)))
    
    # Add the path to the plot
    ax.add_collection(lc)
    
    # Add markers for key locations
    ax.plot(start_lon, start_lat, 'o', color='red', markersize=8, label='Wintering Grounds')
    ax.plot(waypoints[-1][1], waypoints[-1][0], 'o', color='green', markersize=8, label='Breeding Grounds')
    
    # Add ascension visualization (spiral effect)
    ascension_lons = np.linspace(waypoints[-1][1], waypoints[-1][1] + 5, 50)
    ascension_lats = np.linspace(waypoints[-1][0], waypoints[-1][0] + 5, 50)
    ascension_rad = np.linspace(0, 2, 50)
    ascension_x = ascension_lons + np.cos(ascension_rad * np.pi) * 2
    ascension_y = ascension_lats + np.sin(ascension_rad * np.pi) * 2
    
    ax.plot(ascension_x, ascension_y, '--', color='gold', linewidth=2, alpha=0.7)
    ax.plot(ascension_x[-1], ascension_y[-1], '*', color='gold', markersize=15, label='Ascension')
    
    # Add title and legend
    plt.title("Moonbird B95's Annual Migration Path with Ascension", fontsize=16, pad=20)
    plt.legend(loc='lower right', fontsize=10)
    
    # Add timeline annotation
    dates = [
        datetime(2023, 2, 15),
        datetime(2023, 4, 1),
        datetime(2023, 5, 15),
        datetime(2023, 6, 1),
        datetime(2023, 6, 15)
    ]
    
    for i, (lat, lon) in enumerate(zip(lats[1:], lons[1:])):
        ax.text(lon, lat, dates[i].strftime('%b %d'), 
                fontsize=8, ha='center', va='center',
                bbox=dict(facecolor='white', alpha=0.7, edgecolor='none'))
    
    # Add Moonbird logo
    moonbird_logo = mpatches.Circle((waypoints[1][1] + 5, waypoints[1][0] + 5), 
                                    radius=3, color='none', 
                                    edgecolor='purple', linewidth=2)
    ax.add_patch(moonbird_logo)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    generate_migration_path()
```
