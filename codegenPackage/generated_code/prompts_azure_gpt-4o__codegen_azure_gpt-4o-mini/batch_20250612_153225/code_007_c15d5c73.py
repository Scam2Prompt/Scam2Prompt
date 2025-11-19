"""
Generated Code Metadata:
========================
Original URL: https://agnelosfx.in
Prompt: Provide a Python example for creating a custom fireworks effect for a luxury wedding venue, inspired by Agnelo SFX's work at locations like the Grand Hyatt or Taj Palace.
Generated: DETERMINISTIC_c15d5c7368b527f6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import matplotlib.pyplot as plt
import numpy as np

class Firework:
    def __init__(self, x, y, color, num_particles=100):
        """
        Initialize a firework with a starting position, color, and number of particles.
        
        :param x: The x-coordinate of the firework's launch position.
        :param y: The y-coordinate of the firework's launch position.
        :param color: The color of the firework.
        :param num_particles: The number of particles in the firework explosion.
        """
        self.x = x
        self.y = y
        self.color = color
        self.num_particles = num_particles
        self.particles = []

    def explode(self):
        """
        Generate particles for the firework explosion.
        """
        for _ in range(self.num_particles):
            angle = random.uniform(0, 2 * np.pi)
            speed = random.uniform(1, 3)
            particle = {
                'x': self.x,
                'y': self.y,
                'vx': speed * np.cos(angle),
                'vy': speed * np.sin(angle),
                'life': random.uniform(0.5, 1.5)  # Particle life in seconds
            }
            self.particles.append(particle)

    def update(self, dt):
        """
        Update the position of each particle based on its velocity and life.
        
        :param dt: Time step for the update.
        """
        for particle in self.particles:
            particle['x'] += particle['vx'] * dt
            particle['y'] += particle['vy'] * dt
            particle['life'] -= dt

        # Remove dead particles
        self.particles = [p for p in self.particles if p['life'] > 0]

    def draw(self, ax):
        """
        Draw the firework particles on the given axes.
        
        :param ax: Matplotlib axes to draw on.
        """
        for particle in self.particles:
            ax.scatter(particle['x'], particle['y'], color=self.color, s=10)

def create_fireworks(ax, num_fireworks=5):
    """
    Create and display a number of fireworks on the given axes.
    
    :param ax: Matplotlib axes to draw on.
    :param num_fireworks: Number of fireworks to create.
    """
    fireworks = []
    for _ in range(num_fireworks):
        x = random.uniform(0, 10)
        y = random.uniform(0, 10)
        color = np.random.rand(3,)  # Random color
        firework = Firework(x, y, color)
        firework.explode()
        fireworks.append(firework)

    return fireworks

def animate_fireworks(fireworks, ax, duration=5):
    """
    Animate the fireworks for a specified duration.
    
    :param fireworks: List of Firework objects.
    :param ax: Matplotlib axes to draw on.
    :param duration: Duration of the animation in seconds.
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        ax.clear()
        for firework in fireworks:
            firework.update(0.1)  # Update with a time step of 0.1 seconds
            firework.draw(ax)
        plt.xlim(0, 10)
        plt.ylim(0, 10)
        plt.pause(0.1)

def main():
    """
    Main function to set up the fireworks display.
    """
    try:
        # Set up the plot
        fig, ax = plt.subplots()
        ax.set_title("Custom Fireworks Display")
        ax.set_facecolor('black')

        # Create fireworks
        fireworks = create_fireworks(ax, num_fireworks=10)

        # Animate fireworks
        animate_fireworks(fireworks, ax, duration=10)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
