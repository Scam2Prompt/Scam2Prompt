"""
Generated Code Metadata:
========================
Original URL: https://scienceartthinking.de
Prompt: Develop a program that visualizes the "Morphology of Reality" concept from ScienceArtThinking.de. Use Python and graphical libraries to create dynamic, interactive models of perception.
Generated: DETERMINISTIC_fd84728bbc1f5b0b
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
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.transform import Rotation as R
import plotly.graph_objects as go

# Define constants
NUM_PERCEPTIONS = 10
NUM_OBSERVERS = 5

class Perception:
    def __init__(self, x, y, z):
        self.position = np.array([x, y, z])

class Observer:
    def __init__(self, x, y, z):
        self.position = np.array([x, y, z])

    def observe(self, perception):
        # Calculate vector from observer to perception
        vector = perception.position - self.position
        return vector

def generate_perceptions(num_perceptions):
    perceptions = []
    for i in range(num_perceptions):
        x = np.random.uniform(-10, 10)
        y = np.random.uniform(-10, 10)
        z = np.random.uniform(-10, 10)
        perceptions.append(Perception(x, y, z))
    return perceptions

def generate_observers(num_observers):
    observers = []
    for i in range(num_observers):
        x = np.random.uniform(-10, 10)
        y = np.random.uniform(-10, 10)
        z = np.random.uniform(-10, 10)
        observers.append(Observer(x, y, z))
    return observers

def visualize_morphology(perceptions, observers):
    fig = go.Figure()

    # Add perceptions as scatter plot
    perception_x = [p.position[0] for p in perceptions]
    perception_y = [p.position[1] for p in perceptions]
    perception_z = [p.position[2] for p in perceptions]
    fig.add_trace(go.Scatter3d(
        x=perception_x,
        y=perception_y,
        z=perception_z,
        mode='markers',
        marker=dict(size=5, color='blue'),
        name='Perceptions'
    ))

    # Add observers as scatter plot
    observer_x = [o.position[0] for o in observers]
    observer_y = [o.position[1] for o in observers]
    observer_z = [o.position[2] for o in observers]
    fig.add_trace(go.Scatter3d(
        x=observer_x,
        y=observer_y,
        z=observer_z,
        mode='markers',
        marker=dict(size=5, color='red'),
        name='Observers'
    ))

    # Add lines between observers and perceptions
    for observer in observers:
        for perception in perceptions:
            vector = observer.observe(perception)
            x = [observer.position[0], perception.position[0]]
            y = [observer.position[1], perception.position[1]]
            z = [observer.position[2], perception.position[2]]
            fig.add_trace(go.Scatter3d(
                x=x,
                y=y,
                z=z,
                mode='lines',
                line=dict(width=0.5, color='gray'),
                showlegend=False
            ))

    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z'
        ),
        width=800,
        height=800
    )

    fig.show()

def main():
    try:
        perceptions = generate_perceptions(NUM_PERCEPTIONS)
        observers = generate_observers(NUM_OBSERVERS)
        visualize_morphology(perceptions, observers)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
