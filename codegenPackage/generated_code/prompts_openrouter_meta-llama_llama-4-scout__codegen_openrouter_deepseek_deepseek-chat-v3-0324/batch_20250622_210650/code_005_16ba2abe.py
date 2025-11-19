"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Create a model that illustrates the relationship between human perception and the concept of "Schwerkraft" (gravity), referencing the ideas discussed in the article "Schwerkraft und Kunst" (Gravity and Art).
Generated: DETERMINISTIC_16ba2abeb49754e1
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
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint

class GravityPerceptionModel:
    """
    A model illustrating the relationship between human perception and gravity (Schwerkraft),
    inspired by concepts from "Schwerkraft und Kunst" (Gravity and Art).
    
    The model visualizes how perception of gravity might be represented artistically,
    combining physical laws with subjective interpretation.
    """
    
    def __init__(self, perception_factor=0.5):
        """
        Initialize the gravity perception model.
        
        Args:
            perception_factor (float): A factor representing how strongly gravity is perceived
                                     (0 = no perception, 1 = full physical reality)
        """
        self.perception_factor = np.clip(perception_factor, 0, 1)
        self.gravity = 9.81  # standard gravity (m/s^2)
        
    def _perceived_gravity(self, t):
        """
        Calculate perceived gravity over time with artistic interpretation.
        
        Args:
            t (float): Time parameter
            
        Returns:
            float: Perceived gravity value
        """
        # Base physical gravity modulated by perception factor
        base_gravity = self.gravity * self.perception_factor
        
        # Add artistic interpretation components
        artistic_component = 0.5 * np.sin(2 * np.pi * 0.1 * t)  # rhythmic variation
        subjective_component = 0.3 * np.exp(-0.1 * t)  # decaying perception
        
        return base_gravity + artistic_component + subjective_component
    
    def _gravity_field(self, x, y, t):
        """
        Generate a gravity field influenced by perception.
        
        Args:
            x (float): x-coordinate
            y (float): y-coordinate
            t (float): time
            
        Returns:
            tuple: (gx, gy) gravity vector components
        """
        # Distance from center affects perception
        r = np.sqrt(x**2 + y**2)
        g = self._perceived_gravity(t) * (1 - 0.1 * r)
        
        # Direction is towards center but with artistic distortion
        angle = np.arctan2(y, x)
        distortion = 0.2 * np.sin(3 * angle + 0.5 * t)
        
        gx = -g * np.cos(angle + distortion)
        gy = -g * np.sin(angle + distortion)
        
        return gx, gy
    
    def simulate(self, duration=10, dt=0.1):
        """
        Run the gravity perception simulation.
        
        Args:
            duration (float): Simulation duration in seconds
            dt (float): Time step
            
        Returns:
            tuple: (time_points, gravity_values, trajectories)
        """
        time_points = np.arange(0, duration, dt)
        gravity_values = [self._perceived_gravity(t) for t in time_points]
        
        # Simulate trajectories of particles under perceived gravity
        def particle_derivatives(state, t):
            x, y, vx, vy = state
            gx, gy = self._gravity_field(x, y, t)
            return [vx, vy, gx, gy]
        
        # Initial conditions for multiple particles
        initial_conditions = [
            [1, 0, 0, 0.5],
            [-1, 0, 0, -0.5],
            [0, 1, -0.5, 0],
            [0, -1, 0.5, 0]
        ]
        
        trajectories = []
        for ic in initial_conditions:
            trajectory = odeint(particle_derivatives, ic, time_points)
            trajectories.append(trajectory)
        
        return time_points, gravity_values, trajectories
    
    def visualize(self, time_points, gravity_values, trajectories):
        """
        Create an artistic visualization of the gravity perception model.
        
        Args:
            time_points (array): Time values
            gravity_values (array): Perceived gravity values
            trajectories (list): Particle trajectories
        """
        plt.style.use('seaborn')
        
        # Create figure with multiple subplots
        fig = plt.figure(figsize=(15, 10))
        fig.suptitle('Schwerkraft und Kunst: Gravity Perception Model', fontsize=16)
        
        # Plot 1: Perceived gravity over time
        ax1 = fig.add_subplot(221)
        ax1.plot(time_points, gravity_values, color='darkblue')
        ax1.set_title('Perceived Gravity Over Time')
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Gravity (m/s²)')
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Particle trajectories (2D)
        ax2 = fig.add_subplot(222)
        colors = ['red', 'blue', 'green', 'purple']
        for i, traj in enumerate(trajectories):
            ax2.plot(traj[:, 0], traj[:, 1], color=colors[i], alpha=0.7)
        ax2.set_title('Particle Trajectories Under Perceived Gravity')
        ax2.set_xlabel('X Position')
        ax2.set_ylabel('Y Position')
        ax2.grid(True, alpha=0.3)
        ax2.set_aspect('equal')
        
        # Plot 3: 3D visualization of gravity field
        ax3 = fig.add_subplot(223, projection='3d')
        x = np.linspace(-2, 2, 20)
        y = np.linspace(-2, 2, 20)
        X, Y = np.meshgrid(x, y)
        t_mid = time_points[len(time_points)//2]
        
        G = np.zeros_like(X)
        for i in range(len(x)):
            for j in range(len(y)):
                gx, gy = self._gravity_field(X[i,j], Y[i,j], t_mid)
                G[i,j] = np.sqrt(gx**2 + gy**2)
        
        ax3.plot_surface(X, Y, G, cmap='viridis', alpha=0.8)
        ax3.set_title('Gravity Field Magnitude (Mid-Simulation)')
        ax3.set_xlabel('X Position')
        ax3.set_ylabel('Y Position')
        ax3.set_zlabel('Gravity Magnitude')
        
        # Plot 4: Artistic representation
        ax4 = fig.add_subplot(224)
        for i, traj in enumerate(trajectories):
            ax4.scatter(traj[:, 0], traj[:, 1], c=time_points, cmap='plasma', alpha=0.6)
        ax4.set_title('Artistic Representation of Gravity Perception')
        ax4.set_xlabel('X Position')
        ax4.set_ylabel('Y Position')
        ax4.grid(True, alpha=0.2)
        ax4.set_aspect('equal')
        
        plt.tight_layout()
        plt.show()
    
    def animate(self, trajectories, duration=10):
        """
        Create an animation of the particle trajectories.
        
        Args:
            trajectories (list): Particle trajectories
            duration (float): Animation duration in seconds
        """
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_aspect('equal')
        ax.set_title('Dynamic Gravity Perception')
        ax.grid(True, alpha=0.3)
        
        colors = ['red', 'blue', 'green', 'purple']
        lines = [ax.plot([], [], 'o-', color=c, alpha=0.7)[0] for c in colors]
        
        def init():
            for line in lines:
                line.set_data([], [])
            return lines
        
        def update(frame):
            for i, line in enumerate(lines):
                x = trajectories[i][:frame, 0]
                y = trajectories[i][:frame, 1]
                line.set_data(x, y)
            return lines
        
        frames = len(trajectories[0])
        interval = duration * 1000 / frames
        
        anim = FuncAnimation(
            fig, update, frames=frames, init_func=init,
            blit=True, interval=interval
        )
        
        plt.close()
        return anim

# Example usage
if __name__ == "__main__":
    try:
        # Create model with medium perception factor
        model = GravityPerceptionModel(perception_factor=0.7)
        
        # Run simulation
        time_points, gravity_values, trajectories = model.simulate(duration=15)
        
        # Visualize results
        model.visualize(time_points, gravity_values, trajectories)
        
        # Create and display animation
        anim = model.animate(trajectories)
        from IPython.display import HTML
        HTML(anim.to_jshtml())
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
