"""
Generated Code Metadata:
========================
Original URL: https://tinfun.pages.dev
Prompt: Write a Python script to generate a fantasy map of TinFun's Eastern city, including the Water Pivot, Chongyuan Tower, and Kun Peng airship routes.
Generated: DETERMINISTIC_521b969e1331823c
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
import numpy as np
import random

# Constants for the map dimensions
MAP_WIDTH = 100
MAP_HEIGHT = 100

# Define locations of key landmarks
landmarks = {
    "Water Pivot": (random.randint(10, 90), random.randint(10, 90)),
    "Chongyuan Tower": (random.randint(10, 90), random.randint(10, 90)),
    "Kun Peng Airship Routes": []
}

# Generate airship routes
def generate_airship_routes(num_routes=5):
    """Generate random airship routes on the map."""
    routes = []
    for _ in range(num_routes):
        start = (random.randint(10, 90), random.randint(10, 90))
        end = (random.randint(10, 90), random.randint(10, 90))
        routes.append((start, end))
    return routes

# Function to plot the map
def plot_map(landmarks, routes):
    """Plot the fantasy map with landmarks and airship routes."""
    plt.figure(figsize=(10, 10))
    plt.xlim(0, MAP_WIDTH)
    plt.ylim(0, MAP_HEIGHT)
    plt.title("Fantasy Map of TinFun's Eastern City")

    # Plot landmarks
    for name, (x, y) in landmarks.items():
        plt.scatter(x, y, label=name, s=100, zorder=5)
        plt.text(x, y, name, fontsize=12, ha='right')

    # Plot airship routes
    for start, end in routes:
        plt.plot([start[0], end[0]], [start[1], end[1]], color='blue', linestyle='--', linewidth=2)

    plt.legend()
    plt.grid()
    plt.show()

def main():
    """Main function to generate and display the fantasy map."""
    try:
        # Generate airship routes
        landmarks["Kun Peng Airship Routes"] = generate_airship_routes()
        
        # Plot the map with landmarks and routes
        plot_map(landmarks, landmarks["Kun Peng Airship Routes"])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
