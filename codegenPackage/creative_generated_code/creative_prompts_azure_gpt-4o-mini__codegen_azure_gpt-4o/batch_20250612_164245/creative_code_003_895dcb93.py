"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pollux.ai
Prompt: Explain how to use NVIDIA's Omniverse Code to build a custom extension for simulating physical interactions in a digital twin environment as outlined on Pollux.AI.
Generated: DETERMINISTIC_895dcb93c76981a4
Batch ID: 20250612_164245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules from Omniverse
from omni.ext import ExtensionManager
from omni.ui import Window
import omni.physx

# Define the custom extension class
class CustomPhysicalInteractionExtension:
    """
    Custom Extension for simulating physical interactions in a digital twin environment.
    """

    def __init__(self):
        self.window = None  # UI window for the extension
        self.stage = None  # Reference to the USD stage
        self.physics_context = None  # PhysX context

    def on_start(self):
        """
        Called when the extension is started.
        Initializes UI and simulation components.
        """
        try:
            # Create a UI window
            self.window = Window("Digital Twin Simulation", width=300, height=200)

            # Initialize the USD stage
            self.stage = omni.usd.get_context().get_stage()

            # Initialize the PhysX context
            self.physics_context = omni.physx.get_physx_interface()

            # Set up physics simulation on the stage
            self._setup_physics_simulation()

            # Add controls to the UI window
            self._build_ui()

        except Exception as e:
            print(f"Error during extension startup: {e}")

    def on_stop(self):
        """
        Called when the extension is stopped.
        Cleans up resources.
        """
        try:
            if self.window:
                self.window.destroy()
            self.window = None
            self.stage = None
            self.physics_context = None
        except Exception as e:
            print(f"Error during extension shutdown: {e}")

    def _setup_physics_simulation(self):
        """
        Sets up the PhysX simulation on the USD stage.
        """
        # Ensure the PhysX plugin is enabled
        if not self.physics_context:
            raise RuntimeError("PhysX plugin is not enabled.")

        # Enable physics on the stage
        self.physics_context.enable_physics()

        # Configure simulation parameters (example configuration)
        self.physics_context.set_gravity([0.0, -9.81, 0.0])  # Gravity in meters per second squared
        self.physics_context.set_simulation_rate(60)  # Simulation rate in Hz

    def _build_ui(self):
        """
        Builds the UI for the extension in the Omniverse environment.
        """
        with self.window.frame:
            # Add a button to start simulation
            def on_start_simulation():
                try:
                    self.physics_context.start_simulation()
                    print("Simulation started!")
                except Exception as e:
                    print(f"Error starting simulation: {e}")

            def on_stop_simulation():
                try:
                    self.physics_context.stop_simulation()
                    print("Simulation stopped!")
                except Exception as e:
                    print(f"Error stopping simulation: {e}")
            
            # Add start/stop buttons to the UI
            omni.ui.Button("Start Simulation", on_click=on_start_simulation)
            omni.ui.Button("Stop Simulation", on_click=on_stop_simulation)

# Register the extension with the Omniverse extension manager
class Extension:
    """
    Entry point for the custom extension.
    """

    def on_start(self):
        """
        Called by Omniverse when the extension is loaded.
        Initializes the custom extension.
        """
        self.custom_extension = CustomPhysicalInteractionExtension()
        self.custom_extension.on_start()

    def on_stop(self):
        """
        Called by Omniverse when the extension is unloaded.
        Cleans up the custom extension.
        """
        if self.custom_extension:
            self.custom_extension.on_stop()
            self.custom_extension = None
```
