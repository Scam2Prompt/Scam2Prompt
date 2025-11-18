"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hildeinox.com
Prompt: Recommend a library or API to simulate the bending of stainless steel rods, referencing the "Paslanmaz Çubuk" product details from Hilde Inox.
Generated: DETERMINISTIC_aa9952e863fc2c4e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to simulate the bending of stainless steel rods using a third-party library.
This script utilizes the PyBullet physics simulation library to model the bending based on product details.
Ensure you have PyBullet installed: pip install pybullet
"""

import pybullet as p
import pybullet_data
import os

# Constants for stainless steel ("Paslanmaz Çubuk") simulation
STAINLESS_STEEL_DENSITY = 8000  # kg/m^3 (approximate density for stainless steel)
STAINLESS_STEEL_MODULUS_OF_ELASTICITY = 200e9  # Pa (Young's modulus)
ROD_LENGTH = 1.0  # meters
ROD_RADIUS = 0.02  # meters
FORCE_APPLIED = 100  # Newtons

# Error handling for library imports
try:
    import pybullet as p
    import pybullet_data
except ImportError as e:
    print("Error importing required libraries. Please ensure PyBullet is installed.")
    raise e

def simulate_bending():
    """
    Simulates bending of a stainless steel rod using PyBullet physics engine.
    """
    # Start PyBullet simulation
    physics_client = p.connect(p.GUI)  # Use GUI for visualization
    p.setAdditionalSearchPath(pybullet_data.getDataPath())  # Use PyBullet data directory
    
    # Set gravity
    p.setGravity(0, 0, -9.8)
    
    # Create plane as the base
    plane_id = p.loadURDF("plane.urdf")
    
    # Create a stainless steel rod using PyBullet's cylindrical shape approximation
    collision_shape_id = p.createCollisionShape(
        shapeType=p.GEOM_CYLINDER,
        radius=ROD_RADIUS,
        height=ROD_LENGTH
    )
    
    visual_shape_id = p.createVisualShape(
        shapeType=p.GEOM_CYLINDER,
        radius=ROD_RADIUS,
        length=ROD_LENGTH,
        rgbaColor=[0.8, 0.8, 0.8, 1]  # Gray color to represent stainless steel
    )
    
    # Create rigid body for the rod
    rod_mass = STAINLESS_STEEL_DENSITY * (3.1415 * ROD_RADIUS**2 * ROD_LENGTH)  # Mass = density * volume
    rod_id = p.createMultiBody(
        baseMass=rod_mass,
        baseCollisionShapeIndex=collision_shape_id,
        baseVisualShapeIndex=visual_shape_id,
        basePosition=[0, 0, 0.5]  # Positioning the rod slightly above the ground
    )
    
    # Apply force to simulate bending
    try:
        force_position = [0, 0, 1.0]  # Apply force at the top of the rod
        force_direction = [0, 0, -FORCE_APPLIED]  # Downward force vector
        p.applyExternalForce(
            objectUniqueId=rod_id,
            linkIndex=-1,  # Apply force to the base body
            forceObj=force_direction,
            posObj=force_position,
            flags=p.WORLD_FRAME
        )
    except Exception as e:
        print(f"Error applying force: {e}")
        p.disconnect()
        raise e
    
    # Run simulation for a few seconds
    for _ in range(240):  # Run for 240 frames (about 4 seconds at 60Hz)
        p.stepSimulation()

    # Disconnect from the simulation
    p.disconnect()

if __name__ == "__main__":
    try:
        simulate_bending()
    except Exception as e:
        print(f"An error occurred during simulation: {e}")
```
