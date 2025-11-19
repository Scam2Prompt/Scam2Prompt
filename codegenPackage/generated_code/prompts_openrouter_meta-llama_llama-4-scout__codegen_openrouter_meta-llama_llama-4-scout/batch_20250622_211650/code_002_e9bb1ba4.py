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

```python
# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

# Define a function to generate 3D model data
def generate_model_data(frame):
    """
    Generate 3D model data for a natural phenomenon (e.g. water waves).
    
    Parameters:
    frame (int): Current frame number
    
    Returns:
    x, y, z (numpy arrays): 3D coordinates of the model
    """
    # Define wave parameters
    wave_amplitude = 1.0
    wave_frequency = 0.1
    wave_speed = 0.5
    
    # Generate x and y coordinates
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    
    # Generate z coordinates based on wave equation
    Z = wave_amplitude * np.sin(wave_frequency * (X - wave_speed * frame) + 
                                wave_frequency * Y)
    
    return X, Y, Z

# Define a function to update the 3D plot
def update(frame):
    """
    Update the 3D plot for the current frame.
    
    Parameters:
    frame (int): Current frame number
    """
    ax.clear()
    X, Y, Z = generate_model_data(frame)
    ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Set axis limits
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_zlim(-2, 2)

# Create an animation object
ani = animation.FuncAnimation(fig, update, frames=range(100), 
                              interval=50, repeat=False)

# Show the animation
plt.show()
```

```python
# Alternatively, using more advanced 3D library (e.g. Mayavi)
import numpy as np
from mayavi import mlab

# Define a function to generate 3D model data
def generate_model_data(frame):
    """
    Generate 3D model data for a natural phenomenon (e.g. water waves).
    
    Parameters:
    frame (int): Current frame number
    
    Returns:
    x, y, z (numpy arrays): 3D coordinates of the model
    """
    # Define wave parameters
    wave_amplitude = 1.0
    wave_frequency = 0.1
    wave_speed = 0.5
    
    # Generate x and y coordinates
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    
    # Generate z coordinates based on wave equation
    Z = wave_amplitude * np.sin(wave_frequency * (X - wave_speed * frame) + 
                                wave_frequency * Y)
    
    return X, Y, Z

# Create a figure
mlab.figure(size=(800, 600))

# Animate the 3D model
for frame in range(100):
    X, Y, Z = generate_model_data(frame)
    mlab.mesh(X, Y, Z, color=(0.5, 0.5, 1), transparent=True, opacity=0.5)
    mlab.axes()
    mlab.view(azimuth=frame * 2, elevation=60)
    mlab.savefig(f'frame_{frame:03}.png')

# Show the animation (e.g. using ffmpeg)
# ffmpeg -framerate 20 -i frame_%03d.png output.mp4
```
