"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ev-io.now.sh
Prompt: Write code to display FPS and ping statistics in a multiplayer game interface, similar to the performance metrics shown in ev.io.
Generated: DETERMINISTIC_e48bc3421c100aef
Batch ID: 20250612_151354
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pygame
import time
import random


class PerformanceMetrics:
    def __init__(self):
        """Initialize the performance metrics class."""
        self.fps = 0
        self.ping = 0

    def update_metrics(self):
        """Update the FPS and ping with simulated values."""
        # Simulate FPS calculation
        self.fps = int(1 / (time.time() - self.last_frame_time))
        self.last_frame_time = time.time()
        
        # Simulating a ping value between 20ms and 150ms
        self.ping = random.randint(20, 150)

    def draw(self, surface):
        """Render the FPS and ping metrics on the given surface."""
        # Define font and colors
        font = pygame.font.Font(None, 36)
        white = (255, 255, 255)

        # Render FPS and Ping text
        fps_text = font.render(f"FPS: {self.fps}", True, white)
        ping_text = font.render(f"Ping: {self.ping} ms", True, white)

        # Blit the text onto the surface
        surface.blit(fps_text, (10, 10))
        surface.blit(ping_text, (10, 50))


def main():
    """Main function to run the game interface."""
    # Initialize Pygame
    pygame.init()

    # Set up display
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game Performance Metrics")

    # Performance metrics instance
    metrics = PerformanceMetrics()
    metrics.last_frame_time = time.time()

    # Main loop flag and clock
    running = True
    clock = pygame.time.Clock()

    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update performance metrics
        metrics.update_metrics()

        # Fill the screen with black
        screen.fill((0, 0, 0))

        # Draw performance metrics
        metrics.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate to 60 FPS
        clock.tick(60)

    # Clean up and exit
    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
