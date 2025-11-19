"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Generate code to simulate the performance of Penske Racing Shocks as the suspension link between a racecar chassis and the track surface.
Generated: DETERMINISTIC_34459097a5760497
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Constants
M = 1500  # Mass of the car in kg
K_spring = 100000  # Spring constant of the shock in N/m
C_damping = 5000  # Damping coefficient of the shock in Ns/m
K_tire = 200000  # Spring constant of the tire in N/m
C_tire_damping = 1000  # Damping coefficient of the tire in Ns/m

# Initial conditions
x0_chassis = 0.1  # Initial displacement of the chassis from equilibrium in m
x0_tire = 0  # Initial displacement of the tire from equilibrium in m
v0_chassis = 0  # Initial velocity of the chassis in m/s
v0_tire = 0  # Initial velocity of the tire in m/s

# Time points
t = np.linspace(0, 10, 1000)

# Equations of motion
def equations_of_motion(state, t, M, K_spring, C_damping, K_tire, C_tire_damping):
    x_chassis, v_chassis, x_tire, v_tire = state
    
    # Calculate the force from the shock
    F_shock = -K_spring * (x_chassis - x_tire) - C_damping * (v_chassis - v_tire)
    
    # Calculate the force from the tire
    F_tire = -K_tire * x_tire - C_tire_damping * v_tire
    
    # Calculate the acceleration of the chassis and tire
    a_chassis = F_shock / M
    a_tire = (F_shock - F_tire) / (M / 10)  # assume 1/10 of the mass is unsprung
    
    return [v_chassis, a_chassis, v_tire, a_tire]

# Solve ODE
state0 = [x0_chassis, v0_chassis, x0_tire, v0_tire]
solution = odeint(equations_of_motion, state0, t, args=(M, K_spring, C_damping, K_tire, C_tire_damping))

# Plot results
plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.plot(t, solution[:, 0], label='Chassis displacement')
plt.plot(t, solution[:, 2], label='Tire displacement')
plt.xlabel('Time [s]')
plt.ylabel('Displacement [m]')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(t, solution[:, 1], label='Chassis velocity')
plt.plot(t, solution[:, 3], label='Tire velocity')
plt.xlabel('Time [s]')
plt.ylabel('Velocity [m/s]')
plt.legend()

plt.tight_layout()
plt.show()
```
