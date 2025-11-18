"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pollux.ai
Prompt: Create a custom Omniverse Extension and publish it to GitHub, following Pollux.AI's guidelines for extension development.
Generated: DETERMINISTIC_77e9eabc070c3b8b
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries from Omniverse
import omni.ext
import omni.ui as ui
from pxr import Usd, UsdGeom

class MyCustomExtension(omni.ext.IExt):
    """Custom Omniverse Extension Example"""

    def on_startup(self, ext_id):
        """Called when the extension is loaded"""
        self._ext_id = ext_id
        self._window = None
        self._create_ui()

    def on_shutdown(self):
        """Called when the extension is unloaded"""
        if self._window:
            self._window.destroy()
            self._window = None

    def _create_ui(self):
        """Create the UI for the extension"""
        self._window = ui.Window("My Custom Extension", width=300, height=200)
        with self._window.frame:
            ui.Label("Hello, Welcome to My Custom Extension!")
            ui.Button("Add Cube", clicked_fn=self._add_cube)

    def _add_cube(self):
        """Add a cube to the stage when the button is pressed"""
        try:
            stage = Usd.Stage.Open("path/to/your/scene.usda")  # Specify the path to the USD stage
            if not stage:
                raise RuntimeError("Failed to open the stage")

            # Create a new cube at the origin
            cube = UsdGeom.Cube.Define(stage, '/MyCube')
            cube.CreateSizeAttr(2.0)  # Set cube size
            stage.GetRootLayer().Save()  # Save the changes to the stage

            ui.InfoMessage("Cube added successfully!", title="Success")
        except Exception as e:
            ui.ErrorMessage(f"Error adding cube: {str(e)}", title="Error")

# Register the extension
omni.ext.register_extension(MyCustomExtension)
```

### Instructions for Publishing to GitHub
1. Create a new repository on GitHub.
2. Add a README.md file with a brief description of your extension and usage instructions.
3. Place this script in the repository.
4. Commit your changes and push the repository to GitHub.

### Note
Make sure you have the appropriate permissions and paths set up to access and modify USD files in your Omniverse environment.
