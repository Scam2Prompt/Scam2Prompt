"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Write code to create a virtual walkthrough of a residential home, incorporating Linea 7’s design principles of spatial connectivity and material complexion.
Generated: DETERMINISTIC_164ac4b758342269
Batch ID: 20250612_145615
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

# Initialize Pygame
pygame.init()

# Constants for the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
BROWN = (139, 69, 19)
LIGHT_BROWN = (210, 180, 140)

# Define a class for the Room
class Room:
    def __init__(self, name, rect, color):
        """
        Initialize a room with a name, position, and color.
        
        :param name: Name of the room
        :param rect: Pygame Rect object defining the room's position and size
        :param color: Color of the room
        """
        self.name = name
        self.rect = rect
        self.color = color

    def draw(self, surface):
        """
        Draw the room on the given surface.
        
        :param surface: The Pygame surface to draw on
        """
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.name, True, WHITE)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

# Define a class for the Walkthrough
class Walkthrough:
    def __init__(self):
        """
        Initialize the walkthrough with a list of rooms.
        """
        self.rooms = [
            Room("Living Room", pygame.Rect(50, 50, 300, 200), LIGHT_BROWN),
            Room("Kitchen", pygame.Rect(400, 50, 300, 200), BROWN),
            Room("Bedroom", pygame.Rect(50, 300, 300, 200), GREY),
            Room("Bathroom", pygame.Rect(400, 300, 300, 200), LIGHT_BROWN)
        ]

    def draw(self, surface):
        """
        Draw all rooms in the walkthrough on the given surface.
        
        :param surface: The Pygame surface to draw on
        """
        for room in self.rooms:
            room.draw(surface)

def main():
    """
    Main function to run the virtual walkthrough.
    """
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Virtual Home Walkthrough")

    # Create a walkthrough instance
    walkthrough = Walkthrough()

    # Main loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Fill the background
        screen.fill(WHITE)

        # Draw the walkthrough
        walkthrough.draw(screen)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
```
