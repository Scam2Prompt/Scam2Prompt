"""
Generated Code Metadata:
========================
Original URL: https://apps-eigenlayer.com
Prompt: "Write a code snippet in Python for optimizing the design of a progressive die tool, considering factors like material flow, stress concentrations, and production efficiency, and using libraries like SciPy and Matplotlib for simulation and visualization."
Generated: DETERMINISTIC_09d08d6b66e05213
Batch ID: 20250622_211652
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

# Define constants
MATERIAL_YOUNG_MODULUS = 200e9  # Pa
MATERIAL_POISSON_RATIO = 0.3
MATERIAL_YIELD_STRESS = 250e6  # Pa
DIE_TOOL_MATERIAL_THICKNESS = 0.1  # m
PRODUCTION_RATE = 1000  # parts per hour

def calculate_stress_concentration(x, y, punch_radius, die_radius):
    """
    Calculate stress concentration at a point (x, y) due to a punch and die.

    :param x: x-coordinate of the point
    :param y: y-coordinate of the point
    :param punch_radius: radius of the punch
    :param die_radius: radius of the die
    :return: stress concentration factor
    """
    r_punch = np.sqrt((x - punch_radius) ** 2 + y ** 2)
    r_die = np.sqrt((x - die_radius) ** 2 + y ** 2)
    stress_concentration = (MATERIAL_YOUNG_MODULUS / MATERIAL_YIELD_STRESS) * (1 / r_punch - 1 / r_die)
    return stress_concentration

def material_flow_simulation(punch_radius, die_radius, material_thickness):
    """
    Simulate material flow during the punching process.

    :param punch_radius: radius of the punch
    :param die_radius: radius of the die
    :param material_thickness: thickness of the material
    :return: material flow velocity
    """
    # Simplified simulation, assuming a constant velocity profile
    velocity = (PRODUCTION_RATE * material_thickness) / (np.pi * (die_radius ** 2 - punch_radius ** 2))
    return velocity

def optimize_die_design(punch_radius_init, die_radius_init):
    """
    Optimize the design of a progressive die tool.

    :param punch_radius_init: initial radius of the punch
    :param die_radius_init: initial radius of the die
    :return: optimized punch and die radii
    """
    def objective_function(params):
        punch_radius, die_radius = params
        stress_concentration_max = 0
        for x in np.linspace(-0.1, 0.1, 100):
            for y in np.linspace(-0.1, 0.1, 100):
                stress_concentration = calculate_stress_concentration(x, y, punch_radius, die_radius)
                stress_concentration_max = max(stress_concentration_max, stress_concentration)
        material_flow_velocity = material_flow_simulation(punch_radius, die_radius, DIE_TOOL_MATERIAL_THICKNESS)
        # Minimize stress concentration and maximize material flow velocity
        return stress_concentration_max - 0.1 * material_flow_velocity

    bounds = [(0.01, 0.1), (0.05, 0.2)]  # bounds for punch and die radii
    result = minimize(objective_function, [punch_radius_init, die_radius_init], method="SLSQP", bounds=bounds)
    return result.x

def visualize_die_design(punch_radius, die_radius):
    """
    Visualize the optimized die design.

    :param punch_radius: optimized radius of the punch
    :param die_radius: optimized radius of the die
    """
    theta = np.linspace(0, 2 * np.pi, 100)
    punch_x = punch_radius * np.cos(theta)
    punch_y = punch_radius * np.sin(theta)
    die_x = die_radius * np.cos(theta)
    die_y = die_radius * np.sin(theta)

    plt.figure(figsize=(6, 6))
    plt.plot(punch_x, punch_y, label="Punch")
    plt.plot(die_x, die_y, label="Die")
    plt.legend()
    plt.gca().set_aspect('equal')
    plt.show()

if __name__ == "__main__":
    try:
        punch_radius_init = 0.05  # initial guess
        die_radius_init = 0.1  # initial guess
        optimized_radii = optimize_die_design(punch_radius_init, die_radius_init)
        punch_radius_opt, die_radius_opt = optimized_radii
        print(f"Optimized punch radius: {punch_radius_opt:.4f} m")
        print(f"Optimized die radius: {die_radius_opt:.4f} m")
        visualize_die_design(punch_radius_opt, die_radius_opt)
    except Exception as e:
        print(f"An error occurred: {e}")
```
