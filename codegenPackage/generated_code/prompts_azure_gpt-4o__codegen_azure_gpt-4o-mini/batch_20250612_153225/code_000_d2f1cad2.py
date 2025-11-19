"""
Generated Code Metadata:
========================
Original URL: https://klar-sehen.ch
Prompt: Write Python code to simulate a visual perception training exercise inspired by the holistic eye training methods described on the Klar Sehen website. Include features like dynamic visual stimuli and user interaction.
Generated: DETERMINISTIC_d2f1cad218e5c14e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)
STIMULUS_COLOR = (0, 0, 255)
STIMULUS_RADIUS = 30
FPS = 60

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Visual Perception Training Exercise")

# Function to generate random position for the stimulus
def get_random_position():
    x = random.randint(STIMULUS_RADIUS, SCREEN_WIDTH - STIMULUS_RADIUS)
    y = random.randint(STIMULUS_RADIUS, SCREEN_HEIGHT - STIMULUS_RADIUS)
    return x, y

# Main function to run the training exercise
def run_training():
    clock = pygame.time.Clock()
    stimulus_position = get_random_position()
    score = 0
    font = pygame.font.Font(None, 36)

    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                # Check if the stimulus was clicked
                if (mouse_x - stimulus_position[0]) ** 2 + (mouse_y - stimulus_position[1]) ** 2 <= STIMULUS_RADIUS ** 2:
                    score += 1
                    stimulus_position = get_random_position()  # Move stimulus to a new position

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)

        # Draw the stimulus
        pygame.draw.circle(screen, STIMULUS_COLOR, stimulus_position, STIMULUS_RADIUS)

        # Display the score
        score_text = font.render(f'Score: {score}', True, (0, 0, 0))
        screen.blit(score_text, (10, 10))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

# Entry point of the program
if __name__ == "__main__":
    try:
        run_training()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()
```
