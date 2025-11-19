"""
Generated Code Metadata:
========================
Original URL: https://fernandez3d.com
Prompt: Develop a code example that demonstrates how to implement a user interface for visualizing architectural projects in 3D, focusing on user experience and comfort in space perception.
Generated: DETERMINISTIC_7eb55aa74108d92a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
import numpy as np
import pyglet
from pyglet.gl import *
from pyglet.window import key
from pyglet import graphics
from pyglet.math import Mat4, Vec3

class ArchitecturalVisualizer:
    """
    3D Architectural Project Visualizer with focus on user experience and space perception.
    """
    
    def __init__(self, width=1280, height=720):
        """
        Initialize the visualizer window and 3D environment.
        """
        self.window = pyglet.window.Window(width, height, caption="Architectural 3D Visualizer", resizable=True)
        self.width = width
        self.height = height
        
        # Camera parameters
        self.camera_pos = Vec3(0, 0, 5)
        self.camera_target = Vec3(0, 0, 0)
        self.camera_up = Vec3(0, 1, 0)
        self.camera_speed = 0.1
        self.rotation_speed = 0.5
        
        # Projection matrix
        self.projection = Mat4.perspective_projection(45, width/height, 0.1, 100)
        
        # Sample architectural elements (walls, floor, etc.)
        self.arch_elements = []
        self._setup_scene()
        
        # UI elements
        self._setup_ui()
        
        # Event handlers
        self.window.push_handlers(
            self,
            on_draw=self.on_draw,
            on_resize=self.on_resize,
            on_key_press=self.on_key_press
        )
    
    def _setup_scene(self):
        """Create sample architectural elements for visualization."""
        try:
            # Floor
            floor_vertices = [
                -5, 0, -5, 0.8, 0.8, 0.8,
                -5, 0, 5, 0.8, 0.8, 0.8,
                5, 0, 5, 0.8, 0.8, 0.8,
                5, 0, -5, 0.8, 0.8, 0.8
            ]
            floor_indices = [0, 1, 2, 0, 2, 3]
            self.arch_elements.append((
                graphics.vertex_list_indexed(4, floor_indices, 
                    ('v3f/static', floor_vertices[:4*3]),
                    ('c3f/static', floor_vertices[4*3:])
                ),
                GL_TRIANGLES
            ))
            
            # Walls
            wall_vertices = [
                -3, 0, -3, 0.9, 0.7, 0.5,
                -3, 2, -3, 0.9, 0.7, 0.5,
                3, 2, -3, 0.9, 0.7, 0.5,
                3, 0, -3, 0.9, 0.7, 0.5
            ]
            wall_indices = [0, 1, 2, 0, 2, 3]
            self.arch_elements.append((
                graphics.vertex_list_indexed(4, wall_indices,
                    ('v3f/static', wall_vertices[:4*3]),
                    ('c3f/static', wall_vertices[4*3:])
                ),
                GL_TRIANGLES
            ))
            
        except Exception as e:
            print(f"Error setting up scene: {e}")
            sys.exit(1)
    
    def _setup_ui(self):
        """Initialize UI elements for better user experience."""
        try:
            self.ui_batch = pyglet.graphics.Batch()
            self.ui_labels = [
                pyglet.text.Label('WASD: Move | QE: Up/Down | Arrow Keys: Look Around',
                                font_size=12,
                                x=10, y=10,
                                batch=self.ui_batch)
            ]
        except Exception as e:
            print(f"Error setting up UI: {e}")
            sys.exit(1)
    
    def on_draw(self):
        """Render the scene."""
        try:
            self.window.clear()
            
            # Set up view matrix
            view = Mat4.look_at(self.camera_pos, self.camera_target, self.camera_up)
            
            # Apply projection and view
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glLoadMatrixf(self.projection)
            
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            glLoadMatrixf(view)
            
            # Enable depth testing
            glEnable(GL_DEPTH_TEST)
            
            # Draw architectural elements
            for element, mode in self.arch_elements:
                element.draw(mode)
            
            # Draw UI
            glDisable(GL_DEPTH_TEST)
            self.ui_batch.draw()
            glEnable(GL_DEPTH_TEST)
            
        except Exception as e:
            print(f"Error during rendering: {e}")
    
    def on_resize(self, width, height):
        """Handle window resize events."""
        try:
            self.width = width
            self.height = height
            glViewport(0, 0, width, height)
            self.projection = Mat4.perspective_projection(45, width/height, 0.1, 100)
        except Exception as e:
            print(f"Error during resize: {e}")
    
    def on_key_press(self, symbol, modifiers):
        """Handle keyboard input for camera movement."""
        try:
            forward = (self.camera_target - self.camera_pos).normalize()
            right = forward.cross(self.camera_up).normalize()
            
            if symbol == key.W:
                self.camera_pos += forward * self.camera_speed
                self.camera_target += forward * self.camera_speed
            elif symbol == key.S:
                self.camera_pos -= forward * self.camera_speed
                self.camera_target -= forward * self.camera_speed
            elif symbol == key.A:
                self.camera_pos -= right * self.camera_speed
                self.camera_target -= right * self.camera_speed
            elif symbol == key.D:
                self.camera_pos += right * self.camera_speed
                self.camera_target += right * self.camera_speed
            elif symbol == key.Q:
                self.camera_pos += self.camera_up * self.camera_speed
                self.camera_target += self.camera_up * self.camera_speed
            elif symbol == key.E:
                self.camera_pos -= self.camera_up * self.camera_speed
                self.camera_target -= self.camera_up * self.camera_speed
            elif symbol == key.LEFT:
                self._rotate_camera(-self.rotation_speed, 0)
            elif symbol == key.RIGHT:
                self._rotate_camera(self.rotation_speed, 0)
            elif symbol == key.UP:
                self._rotate_camera(0, self.rotation_speed)
            elif symbol == key.DOWN:
                self._rotate_camera(0, -self.rotation_speed)
        except Exception as e:
            print(f"Error handling key press: {e}")
    
    def _rotate_camera(self, yaw, pitch):
        """Rotate the camera around the target point."""
        try:
            # Calculate direction from camera to target
            direction = self.camera_target - self.camera_pos
            
            # Create rotation matrices
            if yaw != 0:
                rot_yaw = Mat4.from_rotation(yaw, self.camera_up)
                direction = rot_yaw @ direction
            if pitch != 0:
                right = direction.cross(self.camera_up).normalize()
                rot_pitch = Mat4.from_rotation(pitch, right)
                direction = rot_pitch @ direction
            
            # Update camera target
            self.camera_target = self.camera_pos + direction
        except Exception as e:
            print(f"Error rotating camera: {e}")
    
    def run(self):
        """Start the application."""
        try:
            pyglet.app.run()
        except Exception as e:
            print(f"Error running application: {e}")
            sys.exit(1)

if __name__ == "__main__":
    visualizer = ArchitecturalVisualizer()
    visualizer.run()
```
