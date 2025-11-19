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
import random

# Constants
WIDTH, HEIGHT = 800, 600
PARTICLE_SIZE = 2
PARTICLE_COLOR = 'red'
PARTICLE_COUNT = 100

class Particle:
    """Represents a single pyrotechnic particle."""
    
    def __init__(self):
        self.x = random.uniform(0, WIDTH)
        self.y = HEIGHT
        self.vel_x = random.uniform(-2, 2)
        self.vel_y = random.uniform(-5, -1)

    def update(self):
        """Updates particle position and velocity."""
        
        self.x += self.vel_x
        self.y += self.vel_y
        self.vel_y += 0.1  # gravity

    def draw(self, ax):
        """Draws the particle on the given axis."""
        
        ax.plot(self.x, self.y, marker='o', markersize=PARTICLE_SIZE, color=PARTICLE_COLOR)

class Pyrotechnics:
    """Simulates pyrotechnics using particles."""
    
    def __init__(self):
        self.particles = [Particle() for _ in range(PARTICLE_COUNT)]

    def update(self):
        """Updates all particles."""
        
        for particle in self.particles:
            particle.update()
            if particle.y > HEIGHT or particle.x < 0 or particle.x > WIDTH:
                particle.x = random.uniform(0, WIDTH)
                particle.y = HEIGHT
                particle.vel_x = random.uniform(-2, 2)
                particle.vel_y = random.uniform(-5, -1)

    def draw(self, ax):
        """Draws all particles on the given axis."""
        
        ax.clear()
        ax.set_xlim(0, WIDTH)
        ax.set_ylim(0, HEIGHT)
        for particle in self.particles:
            particle.draw(ax)

def main():
    try:
        fig, ax = plt.subplots()
        pyrotechnics = Pyrotechnics()

        def animate(i):
            pyrotechnics.update()
            pyrotechnics.draw(ax)

        ani = animation.FuncAnimation(fig, animate, interval=20)
        plt.show()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
