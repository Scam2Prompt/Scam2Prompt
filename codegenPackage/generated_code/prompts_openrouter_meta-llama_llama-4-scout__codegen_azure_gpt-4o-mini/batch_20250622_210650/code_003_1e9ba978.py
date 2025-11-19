"""
Generated Code Metadata:
========================
Original URL: https://agnelosfx.in
Prompt: "Generate a code snippet for simulating pyrotechnics using Python libraries."
Generated: DETERMINISTIC_1e9ba978477ab027
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
import matplotlib.animation as animation

class Firework:
    def __init__(self, x, y, color, num_particles=100):
        """
        Initialize a firework with a starting position, color, and number of particles.

        :param x: Initial x-coordinate of the firework
        :param y: Initial y-coordinate of the firework
        :param color: Color of the firework particles
        :param num_particles: Number of particles in the firework explosion
        """
        self.x = x
        self.y = y
        self.color = color
        self.num_particles = num_particles
        self.particles = self._create_particles()

    def _create_particles(self):
        """
        Create particles for the firework explosion.

        :return: A list of particle positions and velocities
        """
        angles = np.random.uniform(0, 2 * np.pi, self.num_particles)
        speeds = np.random.uniform(1, 3, self.num_particles)
        particles = []
        for angle, speed in zip(angles, speeds):
            vx = speed * np.cos(angle)
            vy = speed * np.sin(angle)
            particles.append({'pos': np.array([self.x, self.y]), 'vel': np.array([vx, vy])})
        return particles

    def update(self):
        """
        Update the position of each particle based on its velocity.
        """
        for particle in self.particles:
            particle['pos'] += particle['vel']

def init():
    """
    Initialize the background of the animation.
    """
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    return []

def update(frame):
    """
    Update the animation for each frame.

    :param frame: Current frame number
    :return: List of artists to be drawn
    """
    ax.clear()
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)

    # Create a new firework at a random position
    firework = Firework(np.random.uniform(1, 9), np.random.uniform(1, 9), color='red')
    firework.update()

    # Draw particles
    for particle in firework.particles:
        ax.plot(particle['pos'][0], particle['pos'][1], 'o', color=firework.color)

    return []

# Set up the figure and axis
fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, init_func=init, frames=100, interval=50, blit=True)

# Show the animation
plt.show()
```
