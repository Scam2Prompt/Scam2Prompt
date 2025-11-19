"""
Generated Code Metadata:
========================
Original URL: https://www.pics3dstudio.com
Prompt: Generate code to integrate a virtual reality viewer for showcasing 3D architectural designs, inspired by the visualization approach used in "La Estancia De Cafayate House 2024" on PICS3DStudio.
Generated: DETERMINISTIC_c620995bff0a8751
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
import json
import numpy as np
import pyglet
from pyglet.gl import *
from pyglet.window import key
import trimesh
from trimesh.viewer import SceneViewer

class VRViewer:
    """
    Virtual Reality Viewer for 3D architectural designs.
    """
    
    def __init__(self, model_path, config_path=None):
        """
        Initialize the VR viewer with a 3D model.
        
        Args:
            model_path (str): Path to the 3D model file (supported formats: .obj, .glb, .ply)
            config_path (str, optional): Path to configuration file for viewer settings
        """
        self.model_path = model_path
        self.config_path = config_path
        self.window = None
        self.scene = None
        self.config = {
            'background_color': [0.1, 0.1, 0.1, 1.0],
            'light_intensity': 1.0,
            'movement_speed': 0.5,
            'rotation_speed': 0.01,
            'vr_mode': False
        }
        
        self._load_config()
        self._load_model()
        
    def _load_config(self):
        """Load configuration from file if provided."""
        if self.config_path and os.path.exists(self.config_path):
            try:
                with open(self.config_path, 'r') as f:
                    user_config = json.load(f)
                    self.config.update(user_config)
            except Exception as e:
                print(f"Warning: Could not load config file. Using defaults. Error: {e}")
    
    def _load_model(self):
        """Load the 3D model from file."""
        try:
            self.scene = trimesh.load(self.model_path)
            if not isinstance(self.scene, trimesh.Scene):
                self.scene = trimesh.Scene(self.scene)
            print(f"Successfully loaded model: {self.model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
            sys.exit(1)
    
    def _setup_lighting(self):
        """Set up lighting for the scene."""
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, (GLfloat * 4)(1.0, 1.0, 1.0, 0.0))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (GLfloat * 4)(1.0, 1.0, 1.0, 1.0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (GLfloat * 4)(0.1, 0.1, 0.1, 1.0))
        glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
        glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
        glLightf(GL_LIGHT0, GL_QUADRATIC_ATTENUATION, 0.01)
    
    def run(self):
        """Run the VR viewer."""
        try:
            # Initialize the window
            self.window = pyglet.window.Window(
                width=1280,
                height=720,
                caption="Architectural VR Viewer",
                resizable=True,
                vsync=True
            )
            
            # Set up OpenGL context
            glClearColor(*self.config['background_color'])
            glEnable(GL_DEPTH_TEST)
            glEnable(GL_CULL_FACE)
            glCullFace(GL_BACK)
            
            self._setup_lighting()
            
            # Set up camera
            camera = trimesh.scene.Camera(
                resolution=(self.window.width, self.window.height),
                fov=(60.0, 60.0)
            )
            
            # Create scene viewer
            self.viewer = SceneViewer(
                scene=self.scene,
                start_loop=False,
                window=self.window,
                callback=self._update,
                camera=camera
            )
            
            # Set up event handlers
            self.window.on_key_press = self._on_key_press
            self.window.on_resize = self._on_resize
            
            # Start the main loop
            pyglet.app.run()
            
        except Exception as e:
            print(f"Error running viewer: {e}")
            sys.exit(1)
    
    def _update(self, dt):
        """Update function called every frame."""
        pass
    
    def _on_key_press(self, symbol, modifiers):
        """Handle keyboard input."""
        if symbol == key.ESCAPE:
            self.window.close()
        elif symbol == key.SPACE:
            self.config['vr_mode'] = not self.config['vr_mode']
            print(f"VR Mode: {'ON' if self.config['vr_mode'] else 'OFF'}")
    
    def _on_resize(self, width, height):
        """Handle window resize."""
        glViewport(0, 0, width, height)
        self.viewer.camera.resolution = (width, height)
    
    def export_view(self, output_path):
        """
        Export the current view as an image.
        
        Args:
            output_path (str): Path to save the image
        """
        try:
            image = self.viewer.render()
            image.save(output_path)
            print(f"View exported to: {output_path}")
        except Exception as e:
            print(f"Error exporting view: {e}")

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) < 2:
        print("Usage: python vr_viewer.py <model_path> [config_path]")
        sys.exit(1)
    
    model_path = sys.argv[1]
    config_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    viewer = VRViewer(model_path, config_path)
    viewer.run()
```
