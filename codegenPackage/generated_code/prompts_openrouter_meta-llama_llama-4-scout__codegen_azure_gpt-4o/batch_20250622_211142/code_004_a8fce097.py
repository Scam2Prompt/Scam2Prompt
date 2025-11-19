"""
Generated Code Metadata:
========================
Original URL: https://hamster-k.com
Prompt: Create a simple game using a game development library, incorporating elements like mining, earning tasks, and time-limited events, similar to Hamster Kombat.
Generated: DETERMINISTIC_a8fce0972ff8efac
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
FONT_SIZE = 32
MINING_REWARD = 10
TASK_REWARD = 20
EVENT_DURATION = 10  # seconds
EVENT_REWARD = 50

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mining and Task Game")

# Initialize font
font = pygame.font.Font(None, FONT_SIZE)

# Game variables
player_score = 0
event_active = False
event_start_time = None

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Function to display text on the screen
def display_text(text, x, y, color=WHITE):
    """Render and display text on the screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Function to handle mining action
def mine():
    """Simulate mining action and reward the player."""
    global player_score
    player_score += MINING_REWARD

# Function to handle task completion
def complete_task():
    """Simulate task completion and reward the player."""
    global player_score
    player_score += TASK_REWARD

# Function to handle time-limited event
def start_event():
    """Start a time-limited event."""
    global event_active, event_start_time
    event_active = True
    event_start_time = time.time()

def end_event():
    """End the time-limited event and reward the player."""
    global event_active, player_score
    event_active = False
    player_score += EVENT_REWARD

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:  # Press 'M' to mine
                mine()
            elif event.key == pygame.K_t:  # Press 'T' to complete a task
                complete_task()
            elif event.key == pygame.K_e:  # Press 'E' to start an event
                if not event_active:
                    start_event()

    # Update game state
    if event_active:
        elapsed_time = time.time() - event_start_time
        if elapsed_time >= EVENT_DURATION:
            end_event()

    # Draw everything
    screen.fill(BLACK)  # Clear screen
    display_text(f"Score: {player_score}", 10, 10)
    if event_active:
        display_text("Event Active!", SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2, RED)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
```
