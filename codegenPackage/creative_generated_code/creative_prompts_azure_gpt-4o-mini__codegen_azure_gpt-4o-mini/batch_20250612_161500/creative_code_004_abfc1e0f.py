"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://disneypinnac.blogspot.com
Prompt: Suggest a library for creating interactive Disney-themed games and provide a sample code to get started.
Generated: DETERMINISTIC_abfc1e0f73083885
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import pygame

# Initialize the pygame
pygame.init()

# Constants for the screen dimensions and colors
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)

# Create the main game class
class DisneyGame:
    def __init__(self):
        """Initialize the game and create a window."""
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Disney-Themed Interactive Game")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        """Main loop of the game."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        """Handle user input events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Update game logic - placeholder for game updates."""
        pass  # Game logic updates would go here

    def draw(self):
        """Draw everything on the screen."""
        self.screen.fill(WHITE)  # Clear screen with white background
        self.draw_title()        # Draw the game title
        pygame.display.flip()    # Update the display

    def draw_title(self):
        """Draw the game title on the screen."""
        font = pygame.font.Font(None, 74)
        text = font.render("Disney Adventure!", True, (0, 0, 0))  # Black color
        text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        self.screen.blit(text, text_rect)

    def cleanup(self):
        """Cleanup resources before quitting the game."""
        pygame.quit()

# Entry point of the game
if __name__ == "__main__":
    game = DisneyGame()
    try:
        game.run()
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        game.cleanup()
```

### Note:
Make sure to have the `pygame` library installed before running the code:
```bash
pip install pygame
```
