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

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

class VisualPerceptionTrainer:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Visual Perception Training")
        self.clock = pygame.time.Clock()
        self.running = True
        self.stimuli_size = 50
        self.stimuli_color = RED
        self.stimuli_x = random.randint(0, WINDOW_WIDTH - self.stimuli_size)
        self.stimuli_y = random.randint(0, WINDOW_HEIGHT - self.stimuli_size)
        self.user_score = 0
        self.total_attempts = 0

    def run(self):
        while self.running:
            self.handle_events()
            self.draw_stimuli()
            self.update_score()
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.check_user_response(event.pos)

    def draw_stimuli(self):
        self.window.fill(WHITE)
        pygame.draw.rect(self.window, self.stimuli_color, (self.stimuli_x, self.stimuli_y, self.stimuli_size, self.stimuli_size))
        font = pygame.font.Font(None, 36)
        text = font.render(f"Score: {self.user_score}/{self.total_attempts}", 1, (0, 0, 0))
        self.window.blit(text, (10, 10))

    def update_score(self):
        if random.random() < 0.05:
            self.stimuli_x = random.randint(0, WINDOW_WIDTH - self.stimuli_size)
            self.stimuli_y = random.randint(0, WINDOW_HEIGHT - self.stimuli_size)
            self.stimuli_color = random.choice([RED, GREEN])

    def check_user_response(self, pos):
        self.total_attempts += 1
        if ((self.stimuli_x < pos[0] < self.stimuli_x + self.stimuli_size) and 
            (self.stimuli_y < pos[1] < self.stimuli_y + self.stimuli_size)):
            self.user_score += 1
            print("Correct!")
        else:
            print(f"Incorrect. Target was at ({self.stimuli_x}, {self.stimuli_y})")

if __name__ == "__main__":
    trainer = VisualPerceptionTrainer()
    trainer.run()
```
