"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stethevent.org
Prompt: Can you provide code examples for creating perfectly looping animations in Python, as mentioned in the Stethevent projects?
Generated: DETERMINISTIC_fb2ab20f4a971e73
Batch ID: 20250612_162548
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pygame
import sys

# Constants for screen dimensions and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Perfectly Looping Animation Example")

# Load images for animation frames
# Ensure you have 'frame1.png', 'frame2.png', 'frame3.png' in the same directory
frames = []
for i in range(1, 4):
    try:
        frame = pygame.image.load(f'frame{i}.png').convert_alpha()
        frames.append(frame)
    except pygame.error as e:
        print(f"Error loading frame{i}.png: {e}")
        sys.exit(1)

# Animation settings
current_frame = 0
frame_count = len(frames)
frame_duration = 100  # Duration for each frame in milliseconds
last_update = pygame.time.get_ticks()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update animation
    current_time = pygame.time.get_ticks()
    if current_time - last_update > frame_duration:
        current_frame = (current_frame + 1) % frame_count  # Loop back to the first frame
        last_update = current_time

    # Clear the screen
    screen.fill(WHITE)

    # Draw the current frame
    frame_rect = frames[current_frame].get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(frames[current_frame], frame_rect)

    # Refresh the display
    pygame.display.flip()

# Clean up and exit
pygame.quit()
```
