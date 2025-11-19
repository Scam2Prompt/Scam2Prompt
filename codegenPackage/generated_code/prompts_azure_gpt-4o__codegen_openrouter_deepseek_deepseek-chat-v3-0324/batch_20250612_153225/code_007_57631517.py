"""
Generated Code Metadata:
========================
Original URL: https://kallimos.com
Prompt: Write code to visualize a Kallimos neighborhood layout, including clustered homes, shared green spaces, and community centers, using a library like Matplotlib or Plotly.
Generated: DETERMINISTIC_5763151778dc250c
Batch ID: 20250612_153225
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
from matplotlib.patches import Circle, Rectangle, Polygon
from matplotlib.collections import PatchCollection
import random

def generate_kallimos_layout(num_homes=50, num_clusters=5, num_community_centers=2):
    """
    Generate a visualization of a Kallimos neighborhood layout.
    
    Args:
        num_homes (int): Number of homes in the neighborhood
        num_clusters (int): Number of home clusters
        num_community_centers (int): Number of community centers
        
    Returns:
        matplotlib.figure.Figure: The generated figure
    """
    fig, ax = plt.subplots(figsize=(12, 12))
    ax.set_aspect('equal')
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis('off')
    ax.set_title('Kallimos Neighborhood Layout', fontsize=16, pad=20)
    
    # Generate cluster centers
    cluster_centers = np.random.uniform(20, 80, size=(num_clusters, 2))
    
    # Generate homes around cluster centers
    home_patches = []
    homes_per_cluster = num_homes // num_clusters
    
    for center in cluster_centers:
        # Add some variation to cluster size
        cluster_radius = random.uniform(8, 15)
        
        # Generate homes in circular patterns around center
        for _ in range(homes_per_cluster):
            angle = random.uniform(0, 2*np.pi)
            distance = random.uniform(0, cluster_radius)
            x = center[0] + distance * np.cos(angle)
            y = center[1] + distance * np.sin(angle)
            
            # Small variation in home sizes
            home_size = random.uniform(1.5, 2.5)
            home_patches.append(Rectangle((x, y), home_size, home_size, color='#6b8ba4'))
    
    # Generate green spaces between clusters
    green_patches = []
    for i in range(num_clusters):
        for j in range(i+1, num_clusters):
            # Create green space between clusters
            midpoint = (cluster_centers[i] + cluster_centers[j]) / 2
            size = np.linalg.norm(cluster_centers[i] - cluster_centers[j]) * 0.6
            
            # Random shape for green space
            if random.random() > 0.5:
                green_patches.append(Circle(midpoint, size/2, color='#7cba92'))
            else:
                # Create irregular polygon
                vertices = []
                for _ in range(5):
                    angle = random.uniform(0, 2*np.pi)
                    r = size/2 * random.uniform(0.7, 1.3)
                    vertices.append([midpoint[0] + r*np.cos(angle), midpoint[1] + r*np.sin(angle)])
                green_patches.append(Polygon(vertices, color='#7cba92'))
    
    # Generate community centers
    community_patches = []
    for _ in range(num_community_centers):
        x = random.uniform(20, 80)
        y = random.uniform(20, 80)
        size = random.uniform(8, 12)
        community_patches.append(Rectangle((x, y), size, size, color='#d35f5f'))
    
    # Add all patches to the plot
    ax.add_collection(PatchCollection(home_patches, match_original=True))
    ax.add_collection(PatchCollection(green_patches, match_original=True))
    ax.add_collection(PatchCollection(community_patches, match_original=True))
    
    # Add paths connecting clusters and centers
    for center in cluster_centers:
        for comm in community_patches:
