"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://klar-sehen.ch
Prompt: Write Python code to simulate a visual perception training exercise inspired by the holistic eye training methods described on the Klar Sehen website. Include features like dynamic visual stimuli and user interaction.
Generated: DETERMINISTIC_d2f1cad218e5c14e
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pygame
import random
import sys

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
STIMULUS_SIZE = 50
STIMULUS_SPEED = 3
BACKGROUND_COLOR = (30, 30, 30)
STIMULUS_COLOR = (255, 100, 100)
FONT_COLOR = (255, 255, 255)
INTERACTION_COLOR = (100, 255, 100)

# Initialize Pygame
pygame.init()

# Setup the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Visual Perception Training Exercise")

# Setup clock for consistent FPS
clock = pygame.time.Clock()

# Font for displaying score and messages
font = pygame.font.Font(None, 36)

# Function to display score and other text
def display_text(text, x, y, color=FONT_COLOR):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Class to represent a moving stimulus
class Stimulus:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - STIMULUS_SIZE)
        self.y = random.randint(0, SCREEN_HEIGHT - STIMULUS_SIZE)
        self.dx = random.choice([-1, 1]) * STIMULUS_SPEED
        self.dy = random.choice([-1, 1]) * STIMULUS_SPEED

    def move(self):
        self.x += self.dx
        self.y += self.dy

        # Bounce off walls
        if self.x <= 0 or self.x >= SCREEN_WIDTH - STIMULUS_SIZE:
            self.dx *= -1
        if self.y <= 0 or self.y >= SCREEN_HEIGHT - STIMULUS_SIZE:
            self.dy *= -1

    def draw(self):
        pygame.draw.rect(screen, STIMULUS_COLOR, (self.x, self.y, STIMULUS_SIZE, STIMULUS_SIZE))

    def is_clicked(self, pos):
        return self.x <= pos[0] <= self.x + STIMULUS_SIZE and self.y <= pos[1] <= self.y + STIMULUS_SIZE

# Main game loop
def main():
    # Create a stimulus instance
    stimulus = Stimulus()
    score = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Check if the user clicked on the stimulus
                if stimulus.is_clicked(event.pos):
                    score += 1
                    stimulus = Stimulus()  # Create a new stimulus at a random location
                else:
                    score = max(0, score - 1)  # Penalty for missing the stimulus

        # Clear the screen
        screen.fill(BACKGROUND_COLOR)
        
        # Move and draw the stimulus
        stimulus.move()
        stimulus.draw()

        # Display the score
        display_text(f"Score: {score}", 10, 10)

        # Update the screen
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Quit pygame when the loop ends
    pygame.quit()
    sys.exit()

# Run the program
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        pygame.quit()
        sys.exit()
```
