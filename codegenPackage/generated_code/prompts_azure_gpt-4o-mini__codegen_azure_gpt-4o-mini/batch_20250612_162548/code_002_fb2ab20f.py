"""
Generated Code Metadata:
========================
Original URL: https://stethevent.org
Prompt: Can you provide code examples for creating perfectly looping animations in Python, as mentioned in the Stethevent projects?
Generated: DETERMINISTIC_fb2ab20f4a971e73
Batch ID: 20250612_162548
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

# Constants for screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Perfectly Looping Animation Example")

# Load images for animation frames
# Ensure you have 'frame1.png', 'frame2.png', ..., 'frameN.png' in the same directory
frames = []
frame_count = 5  # Number of frames in the animation
for i in range(1, frame_count + 1):
    try:
        frame = pygame.image.load(f'frame{i}.png').convert_alpha()
        frames.append(frame)
    except pygame.error as e:
        print(f"Error loading frame {i}: {e}")
        sys.exit(1)

# Animation settings
current_frame = 0
frame_delay = 100  # Delay in milliseconds between frames
last_update = pygame.time.get_ticks()

# Main loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation frame
    now = pygame.time.get_ticks()
    if now - last_update > frame_delay:
        current_frame = (current_frame + 1) % len(frames)  # Loop back to the first frame
        last_update = now

    # Clear the screen
    screen.fill((0, 0, 0))  # Fill with black

    # Draw the current frame
    screen.blit(frames[current_frame], (SCREEN_WIDTH // 2 - frames[current_frame].get_width() // 2,
                                         SCREEN_HEIGHT // 2 - frames[current_frame].get_height() // 2))

    # Update the display
    pygame.display.flip()

# Clean up and exit
pygame.quit()
sys.exit()
```
