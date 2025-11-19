"""
Generated Code Metadata:
========================
Original URL: https://www.pics3dstudio.com
Prompt: Generate a code snippet for a virtual reality application that showcases 360-degree views of architectural projects like the Mercedes-Benz AMG S 63 E 2025.
Generated: DETERMINISTIC_5d7cefd12c55a739
Batch ID: 20250612_160254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import sys
import pygame
import cv2
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Define a class for the VR application
class VR360Viewer:
    def __init__(self, texture_file):
        """
        Initialize the VR360Viewer with the texture file.
        :param texture_file: Path to the 360-degree image file.
        """
        self.texture_file = texture_file
        self.texture_id = None
        self.screen_width = 800
        self.screen_height = 600

    def load_texture(self):
        """
        Load the 360-degree image as a texture for OpenGL rendering.
        """
        try:
            # Load the image using OpenCV
            image = cv2.imread(self.texture_file)
            if image is None:
                raise FileNotFoundError(f"Image file '{self.texture_file}' not found.")
            
            # Convert the image from BGR to RGB format
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Flip the image vertically for OpenGL compatibility
            image = cv2.flip(image, 0)
            
            # Generate a texture ID
            self.texture_id = glGenTextures(1)
            
            # Bind the texture
            glBindTexture(GL_TEXTURE_2D, self.texture_id)
            
            # Set texture parameters
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
            
            # Upload the texture to the GPU
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, image.shape[1], image.shape[0], 0, GL_RGB, GL_UNSIGNED_BYTE, image)
        except Exception as e:
            print(f"Error loading texture: {e}")
            sys.exit(1)

    def draw_sphere(self):
        """
        Render a sphere with the 360-degree texture applied.
        """
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        quadric = gluNewQuadric()
        gluQuadricTexture(quadric, GL_TRUE)
        gluSphere(quadric, 5, 100, 100)
        gluDeleteQuadric(quadric)
        glDisable(GL_TEXTURE_2D)

    def run(self):
        """
        Run the VR application.
        """
        try:
            # Initialize Pygame and OpenGL
            pygame.init()
            pygame.display.set_mode((self.screen_width, self.screen_height), DOUBLEBUF | OPENGL)
            gluPerspective(90, (self.screen_width / self.screen_height), 0.1, 50.0)
            glTranslatef(0.0, 0.0, -10)
            
            # Load the texture
            self.load_texture()
            
            # Main application loop
            running = True
            while running:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                    elif event.type == KEYDOWN and event.key == K_ESCAPE:
                        running = False
                
                # Handle mouse movement for camera rotation
                mouse_rel = pygame.mouse.get_rel()
                glRotatef(mouse_rel[0] * 0.1, 0, 1, 0)
                glRotatef(-mouse_rel[1] * 0.1, 1, 0, 0)
                
                # Clear the screen and render the sphere
                glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
                self.draw_sphere()
                pygame.display.flip()
            
            # Cleanup
            pygame.quit()
        except Exception as e:
            print(f"Error running VR application: {e}")
            sys.exit(1)

# Main entry point
if __name__ == "__main__":
    # Path to the 360-degree image file
    texture_file = "mercedes_benz_amg_s63_2025_360.jpg"
    
    # Check if the file exists
    if not os.path.exists(texture_file):
        print(f"Error: File '{texture_file}' not found.")
        sys.exit(1)
    
    # Create and run the VR viewer
    viewer = VR360Viewer(texture_file)
    viewer.run()
```
