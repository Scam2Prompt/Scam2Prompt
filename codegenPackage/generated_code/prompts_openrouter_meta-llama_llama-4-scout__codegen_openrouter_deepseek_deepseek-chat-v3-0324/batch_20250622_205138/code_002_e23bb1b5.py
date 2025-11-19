"""
Generated Code Metadata:
========================
Original URL: https://cadv.io
Prompt: Generate code to implement intuitive game-style navigation for 3D CAD models, as seen in cadvio's interface.
Generated: DETERMINISTIC_e23bb1b53d856bdb
Batch ID: 20250622_205138
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import math
from typing import Tuple, Optional
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

class CADNavigation:
    """
    Intuitive 3D CAD model navigation system inspired by cadvio's interface.
    Handles mouse and keyboard inputs for rotation, panning, and zooming.
    """
    
    def __init__(self, window_size: Tuple[int, int] = (800, 600)):
        """
        Initialize the navigation system with default parameters.
        
        Args:
            window_size: Tuple of (width, height) for the viewport
        """
        pygame.init()
        pygame.display.set_mode(window_size, DOUBLEBUF|OPENGL)
        
        # Camera parameters
        self.camera_pos = np.array([0.0, 0.0, 5.0])
        self.camera_target = np.array([0.0, 0.0, 0.0])
        self.camera_up = np.array([0.0, 1.0, 0.0])
        
        # Navigation parameters
        self.zoom_speed = 0.1
        self.pan_speed = 0.01
        self.rotate_speed = 0.5
        
        # Mouse state
        self.last_mouse_pos = None
        self.is_rotating = False
        self.is_panning = False
        
        # Initialize OpenGL
        self._setup_gl()
    
    def _setup_gl(self):
        """Initialize OpenGL settings."""
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glClearColor(0.1, 0.1, 0.1, 1.0)
        
        # Set perspective
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (self.window_size[0]/self.window_size[1]), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
    
    @property
    def window_size(self) -> Tuple[int, int]:
        """Get current window size."""
        return pygame.display.get_surface().get_size()
    
    def handle_events(self):
        """Process all input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            
            self._handle_mouse_events(event)
            self._handle_keyboard_events(event)
        
        return True
    
    def _handle_mouse_events(self, event):
        """Process mouse events."""
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                self.is_rotating = True
                self.last_mouse_pos = pygame.mouse.get_pos()
            elif event.button == 3:  # Right click
                self.is_panning = True
                self.last_mouse_pos = pygame.mouse.get_pos()
            elif event.button == 4:  # Scroll up
                self.zoom(1)
            elif event.button == 5:  # Scroll down
                self.zoom(-1)
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.is_rotating = False
            elif event.button == 3:
                self.is_panning = False
        
        elif event.type == pygame.MOUSEMOTION:
            self._handle_mouse_motion()
    
    def _handle_mouse_motion(self):
        """Handle mouse movement for rotation and panning."""
        current_mouse_pos = pygame.mouse.get_pos()
        if self.last_mouse_pos is None:
            self.last_mouse_pos = current_mouse_pos
            return
        
        dx = current_mouse_pos[0] - self.last_mouse_pos[0]
        dy = current_mouse_pos[1] - self.last_mouse_pos[1]
        
        if self.is_rotating:
            self.rotate(dx, dy)
        elif self.is_panning:
            self.pan(dx, dy)
        
        self.last_mouse_pos = current_mouse_pos
    
    def _handle_keyboard_events(self, event):
        """Process keyboard events."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  # Reset view
                self.reset_view()
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                return False
        return True
    
    def rotate(self, dx: float, dy: float):
        """
        Rotate the view around the target point.
        
        Args:
            dx: Horizontal mouse movement
            dy: Vertical mouse movement
        """
        # Calculate rotation angles
        angle_x = dx * self.rotate_speed
        angle_y = dy * self.rotate_speed
        
        # Rotate camera position around target
        direction = self.camera_pos - self.camera_target
        distance = np.linalg.norm(direction)
        direction = direction / distance
        
        # Horizontal rotation (around world up vector)
        horizontal_axis = self.camera_up
        horizontal_rot = self._rotation_matrix(horizontal_axis, math.radians(angle_x))
        direction = np.dot(horizontal_rot[:3,:3], direction)
        
        # Vertical rotation (around camera right vector)
        right = np.cross(direction, self.camera_up)
        right = right / np.linalg.norm(right)
        vertical_rot = self._rotation_matrix(right, math.radians(angle_y))
        direction = np.dot(vertical_rot[:3,:3], direction)
        
        # Update camera position
        self.camera_pos = self.camera_target + direction * distance
    
    def pan(self, dx: float, dy: float):
        """
        Pan the view based on mouse movement.
        
        Args:
            dx: Horizontal mouse movement
            dy: Vertical mouse movement
        """
        # Calculate pan direction
        direction = self.camera_pos - self.camera_target
        distance = np.linalg.norm(direction)
        direction = direction / distance
        
        right = np.cross(direction, self.camera_up)
        right = right / np.linalg.norm(right)
        up = np.cross(right, direction)
        
        # Calculate pan amount
        pan_right = right * dx * self.pan_speed * distance
        pan_up = up * dy * self.pan_speed * distance
        
        # Update camera and target positions
        self.camera_pos += pan_right - pan_up
        self.camera_target += pan_right - pan_up
    
    def zoom(self, direction: int):
        """
        Zoom in/out the view.
        
        Args:
            direction: 1 for zoom in, -1 for zoom out
        """
        view_vector = self.camera_target - self.camera_pos
        distance = np.linalg.norm(view_vector)
        
        if distance > 0.1 or direction > 0:
            zoom_amount = direction * self.zoom_speed * distance
            self.camera_pos += view_vector * zoom_amount / distance
    
    def reset_view(self):
        """Reset the view to default position."""
        self.camera_pos = np.array([0.0, 0.0, 5.0])
        self.camera_target = np.array([0.0, 0.0, 0.0])
        self.camera_up = np.array([0.0, 1.0, 0.0])
    
    def _rotation_matrix(self, axis: np.ndarray, angle: float) -> np.ndarray:
        """
        Create a rotation matrix around an arbitrary axis.
        
        Args:
            axis: The axis to rotate around
            angle: Rotation angle in radians
            
        Returns:
            4x4 rotation matrix
        """
        axis = axis / np.linalg.norm(axis)
        c = math.cos(angle)
        s = math.sin(angle)
        t = 1 - c
        
        x, y, z = axis
        return np.array([
            [t*x*x + c,   t*x*y - s*z, t*x*z + s*y, 0],
            [t*x*y + s*z, t*y*y + c,   t*y*z - s*x, 0],
            [t*x*z - s*y, t*y*z + s*x, t*z*z + c,   0],
            [0,           0,           0,           1]
        ])
    
    def update_view(self):
        """Update the OpenGL view matrix based on camera parameters."""
        glLoadIdentity()
        gluLookAt(
            self.camera_pos[0], self.camera_pos[1], self.camera_pos[2],
            self.camera_target[0], self.camera_target[1], self.camera_target[2],
            self.camera_up[0], self.camera_up[1], self.camera_up[2]
        )
    
    def render(self):
        """Render the scene (to be overridden by user)."""
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        # Example: render a simple cube
        glBegin(GL_QUADS)
        glColor3f(1,
