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
import pygame
import sys
import math
from pygame.locals import *

class VR360Viewer:
    def __init__(self, image_paths):
        """
        Initialize the VR 360-degree viewer with a list of 360-degree images.
        
        Args:
            image_paths (list): List of paths to 360-degree images for different views
        """
        pygame.init()
        self.screen_width, self.screen_height = 1280, 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Architectural VR 360° Viewer - Mercedes-Benz AMG S 63 E 2025')
        
        self.clock = pygame.time.Clock()
        self.fps = 60
        
        # Load 360-degree images
        self.images = []
        try:
            for path in image_paths:
                img = pygame.image.load(path).convert()
                self.images.append(pygame.transform.scale(img, (self.screen_width, self.screen_height)))
        except pygame.error as e:
            print(f"Error loading images: {e}")
            sys.exit(1)
            
        self.current_image_index = 0
        self.current_image = self.images[self.current_image_index]
        
        # VR viewing parameters
        self.yaw = 0  # Horizontal rotation
        self.pitch = 0  # Vertical rotation
        self.rotation_speed = 2  # Degrees per frame
        self.zoom = 1.0
        self.zoom_speed = 0.05
        
        # UI elements
        self.font = pygame.font.SysFont('Arial', 24)
        
    def handle_events(self):
        """Handle user input events."""
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == K_RIGHT:
                    self.current_image_index = (self.current_image_index + 1) % len(self.images)
                    self.current_image = self.images[self.current_image_index]
                elif event.key == K_LEFT:
                    self.current_image_index = (self.current_image_index - 1) % len(self.images)
                    self.current_image = self.images[self.current_image_index]
                elif event.key == K_r:  # Reset view
                    self.yaw = 0
                    self.pitch = 0
                    self.zoom = 1.0
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 4:  # Mouse wheel up
                    self.zoom = min(2.0, self.zoom + self.zoom_speed)
                elif event.button == 5:  # Mouse wheel down
                    self.zoom = max(0.5, self.zoom - self.zoom_speed)
        
        # Handle mouse movement for rotation
        if pygame.mouse.get_pressed()[0]:  # Left mouse button
            rel_x, rel_y = pygame.mouse.get_rel()
            self.yaw -= rel_x * 0.2
            self.pitch -= rel_y * 0.2
            self.pitch = max(-90, min(90, self.pitch))  # Clamp pitch
        else:
            pygame.mouse.get_rel()  # Reset relative movement
            
        # Handle keyboard rotation
        keys = pygame.key.get_pressed()
        if keys[K_a]:
            self.yaw -= self.rotation_speed
        if keys[K_d]:
            self.yaw += self.rotation_speed
        if keys[K_w]:
            self.pitch -= self.rotation_speed
            self.pitch = max(-90, self.pitch)
        if keys[K_s]:
            self.pitch += self.rotation_speed
            self.pitch = min(90, self.pitch)
    
    def render_scene(self):
        """Render the 360-degree view with current rotation and zoom."""
        # Create a surface for the rendered view
        render_surface = pygame.Surface((self.screen_width, self.screen_height))
        
        # Calculate visible portion based on yaw and pitch
        yaw_rad = math.radians(self.yaw)
        pitch_rad = math.radians(self.pitch)
        
        # Calculate the visible rectangle (simplified projection)
        visible_width = int(self.screen_width / self.zoom)
        visible_height = int(self.screen_height / self.zoom)
        
        # Calculate source rectangle position
        src_x = (self.yaw / 360) * self.current_image.get_width()
        src_x %= self.current_image.get_width()  # Wrap around
        
        src_y = (self.pitch / 180) * (self.current_image.get_height() - visible_height) / 2 + \
                (self.current_image.get_height() - visible_height) / 2
        src_y = max(0, min(self.current_image.get_height() - visible_height, src_y))
        
        # Blit the visible portion
        src_rect = pygame.Rect(int(src_x), int(src_y), visible_width, visible_height)
        render_surface.blit(self.current_image, (0, 0), src_rect)
        
        # Scale to simulate zoom
        if self.zoom != 1.0:
            render_surface = pygame.transform.scale(
                render_surface, 
                (self.screen_width, self.screen_height)
            )
        
        # Draw to screen
        self.screen.blit(render_surface, (0, 0))
        
        # Draw UI
        self.draw_ui()
        
        pygame.display.flip()
    
    def draw_ui(self):
        """Draw user interface elements."""
        # View information
        info_text = f"View: {self.current_image_index + 1}/{len(self.images)} | " \
                   f"Yaw: {self.yaw:.1f}° | Pitch: {self.pitch:.1f}° | Zoom: {self.zoom:.1f}x"
        text_surface = self.font.render(info_text, True, (255, 255, 255))
        self.screen.blit(text_surface, (10, 10))
        
        # Controls hint
        controls_text = "Controls: WASD/Mouse to rotate | Wheel to zoom | Arrows to change view | R to reset"
        controls_surface = self.font.render(controls_text, True, (255, 255, 255))
        self.screen.blit(controls_surface, (10, self.screen_height - 30))
    
    def run(self):
        """Main application loop."""
        pygame.mouse.set_visible(True)
        
        while True:
            self.handle_events()
            self.render_scene()
            self.clock.tick(self.fps)

if __name__ == "__main__":
    # Example usage with placeholder image paths
    image_paths = [
        "assets/mercedes_amg_s63e_2025_exterior.jpg",
        "assets/mercedes_amg_s63e_2025_interior.jpg",
        "assets/mercedes_amg_s63e_2025_dashboard.jpg"
    ]
    
    try:
        viewer = VR360Viewer(image_paths)
        viewer.run()
    except Exception as e:
        print(f"Error: {e}")
        pygame.quit()
        sys.exit(1)
```
