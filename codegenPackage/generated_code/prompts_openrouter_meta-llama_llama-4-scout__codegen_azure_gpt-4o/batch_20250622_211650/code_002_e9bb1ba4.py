"""
Generated Code Metadata:
========================
Original URL: https://structurefilms.com
Prompt: "Write code to animate a 3D model of a natural phenomenon for an educational film."
Generated: DETERMINISTIC_e9bb1ba442738b77
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python script using the `matplotlib` library for animating a 3D model of a natural phenomenon (e.g., a tornado). This code is clean, well-documented, and production-ready.

```python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Function to generate tornado-like 3D coordinates
def generate_tornado_data(num_points=500, height=10, radius=5):
    """
    Generate 3D coordinates for a tornado-like structure.

    Parameters:
        num_points (int): Number of points in the tornado.
        height (float): Height of the tornado.
        radius (float): Maximum radius of the tornado.

    Returns:
        x, y, z (numpy arrays): 3D coordinates of the tornado.
    """
    z = np.linspace(0, height, num_points)  # Vertical axis
    theta = np.linspace(0, 4 * np.pi, num_points)  # Spiral angle
    r = np.linspace(0, radius, num_points)  # Radius decreases with height
    x = r * np.cos(theta)  # X coordinates
    y = r * np.sin(theta)  # Y coordinates
    return x, y, z

# Initialize tornado data
num_points = 500
x, y, z = generate_tornado_data(num_points=num_points)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-6, 6])
ax.set_ylim([-6, 6])
ax.set_zlim([0, 10])
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Tornado Animation')

# Scatter plot for tornado points
scatter = ax.scatter(x, y, z, c=z, cmap='viridis', s=10)

# Animation function
def update(frame):
    """
    Update function for the animation.

    Parameters:
        frame (int): Current frame number.

    Returns:
        scatter (matplotlib object): Updated scatter plot.
    """
    # Rotate the tornado by modifying the theta values
    theta = np.linspace(0, 4 * np.pi, num_points) + frame * 0.1
    x = np.linspace(0, 5, num_points) * np.cos(theta)
    y = np.linspace(0, 5, num_points) * np.sin(theta)
    scatter._offsets3d = (x, y, z)  # Update scatter plot coordinates
    return scatter,

# Create animation
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=False)

# Error handling for saving the animation
try:
    ani.save('tornado_animation.mp4', writer='ffmpeg', fps=30)
    print("Animation saved successfully as 'tornado_animation.mp4'.")
except Exception as e:
    print(f"Error saving animation: {e}")

# Display the animation
plt.show()
```

This code animates a 3D tornado-like structure, rotates it over time, and saves the animation as an MP4 file. It includes error handling for saving the animation and follows best practices for readability and maintainability.
