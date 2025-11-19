"""
Generated Code Metadata:
========================
Original URL: https://agnelosfx.in
Prompt: Generate code to design a fireworks animation for a New Year’s Eve celebration, referencing the luxury event setups provided by Agnelo SFX.
Generated: DETERMINISTIC_985d40c498b8619d
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import tkinter as tk
import random
import math

# Constants
WIDTH, HEIGHT = 800, 600
FIREWORK_SIZE = 5
EXPLOSION_SIZE = 50

class Firework:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.exploded = False
        self.id = self.canvas.create_oval(self.x, self.y, self.x + FIREWORK_SIZE, self.y + FIREWORK_SIZE, fill='red')

    def update(self):
        if not self.exploded:
            self.y -= 5
            self.canvas.coords(self.id, self.x, self.y, self.x + FIREWORK_SIZE, self.y + FIREWORK_SIZE)
            if self.y < HEIGHT // 2:
                self.explode()

    def explode(self):
        self.exploded = True
        self.canvas.delete(self.id)
        for _ in range(100):
            x = self.x + random.uniform(-EXPLOSION_SIZE, EXPLOSION_SIZE)
            y = self.y + random.uniform(-EXPLOSION_SIZE, EXPLOSION_SIZE)
            angle = random.uniform(0, 2 * math.pi)
            velocity_x = math.cos(angle) * random.uniform(1, 5)
            velocity_y = math.sin(angle) * random.uniform(1, 5)
            self.canvas.create_oval(x, y, x + 2, y + 2, fill='gold', tags='particle')

        # Create particles
        self.particles = []
        for _ in range(100):
            particle_x = self.x
            particle_y = self.y
            angle = random.uniform(0, 2 * math.pi)
            velocity_x = math.cos(angle) * random.uniform(1, 5)
            velocity_y = math.sin(angle) * random.uniform(1, 5)
            self.particles.append([particle_x, particle_y, velocity_x, velocity_y])

        self.update_particles()

    def update_particles(self):
        for i, particle in enumerate(self.particles):
            self.particles[i][0] += particle[2]
            self.particles[i][1] += particle[3]
            self.particles[i][3] += 0.1  # gravity

            if self.particles[i][1] > HEIGHT:
                self.particles.pop(i)
            else:
                self.canvas.create_oval(self.particles[i][0], self.particles[i][1], 
                                        self.particles[i][0] + 2, self.particles[i][1] + 2, 
                                        fill='gold', tags='particle')

        if self.particles:
            self.canvas.after(16, self.update_particles)  # 60 FPS
        else:
            self.canvas.delete('particle')

class FireworksAnimation:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(self.root, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.fireworks = []

        for _ in range(10):
            x = random.randint(0, WIDTH)
            y = random.randint(HEIGHT // 2, HEIGHT)
            self.fireworks.append(Firework(self.canvas, x, y))

        self.update_fireworks()

    def update_fireworks(self):
        for firework in self.fireworks:
            firework.update()
            if firework.exploded and not firework.particles:
                x = random.randint(0, WIDTH)
                y = random.randint(HEIGHT // 2, HEIGHT)
                firework.__init__(self.canvas, x, y)

        self.root.after(16, self.update_fireworks)  # 60 FPS

if __name__ == "__main__":
    root = tk.Tk()
    root.title("New Year's Eve Fireworks")
    animation = FireworksAnimation(root)
    root.mainloop()
```
