"""
Generated Code Metadata:
========================
Original URL: https://pollux.ai
Prompt: Explain how to use NVIDIA's Omniverse Code to build a custom extension for simulating physical interactions in a digital twin environment as outlined on Pollux.AI.
Generated: DETERMINISTIC_895dcb93c76981a4
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# NVIDIA Omniverse Code for Custom Extension: Physical Interactions in Digital Twin Environment

import omni
import numpy as np
from pxr import Usd, UsdPhysics, UsdGeom

# Define the extension class
class PhysicalInteractionsExtension:
    def __init__(self, stage):
        """
        Initialize the extension with a USD stage.

        :param stage: The USD stage to work with.
        """
        self.stage = stage
        self.physics_api = UsdPhysics.PhysicsAPI(stage)

    def create_physical_interaction(self, prim_path, mass, friction):
        """
        Create a physical interaction for a prim.

        :param prim_path: The path to the prim.
        :param mass: The mass of the prim.
        :param friction: The friction coefficient of the prim.
        """
        # Get the prim
        prim = self.stage.GetPrimAtPath(prim_path)
        if not prim:
            raise ValueError(f"Prim not found at path: {prim_path}")

        # Create a rigid body API
        rigid_body_api = UsdPhysics.RigidBodyAPI(prim)

        # Set the mass and friction
        rigid_body_api.CreateMassAttr(mass)
        rigid_body_api.CreateFrictionAttr(friction)

    def simulate_physics(self):
        """
        Simulate physics on the stage.
        """
        # Get the physics scene
        physics_scene = self.physics_api.GetPhysicsScene()

        # Simulate physics
        physics_scene.Simulate(1.0 / 60.0)  # 1/60th of a second

# Example usage
if __name__ == "__main__":
    # Initialize the Omniverse client
    omni.client.init()

    # Open a USD stage
    stage = Usd.Stage.Open("example.usd")

    # Create an extension instance
    extension = PhysicalInteractionsExtension(stage)

    # Create a physical interaction for a prim
    extension.create_physical_interaction("/hello", 1.0, 0.5)

    # Simulate physics
    extension.simulate_physics()

    # Save the stage
    stage.GetRootLayer().Export("example.usd")

    # Clean up
    omni.client.shutdown()
```
