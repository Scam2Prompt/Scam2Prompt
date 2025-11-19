"""
Generated Code Metadata:
========================
Original URL: https://braindom.xyz
Prompt: Design a puzzle game using Python and suggest how to integrate Braindom-style challenges to improve logical reasoning and creative thinking.
Generated: DETERMINISTIC_a23d56b3cabafc9b
Batch ID: 20250622_212104
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
import time
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FONT_SIZE = 32

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Brain Teaser Puzzle Game")
clock = pygame.time.Clock()

# Font setup
font = pygame.font.SysFont('Arial', FONT_SIZE)

class PuzzleGame:
    def __init__(self):
        self.current_puzzle = 0
        self.score = 0
        self.puzzles = [
            self.puzzle_pattern_recognition,
            self.puzzle_math_riddle,
            self.puzzle_word_scramble,
            self.puzzle_logic_gate
        ]
        self.user_input = ""
        self.message = ""
        self.message_timer = 0

    def draw_text(self, text, x, y, color=WHITE):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        screen.blit(text_surface, text_rect)

    def show_message(self, msg, color=GREEN):
        self.message = msg
        self.message_timer = 120  # 2 seconds at 60 FPS

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                if event.key == K_RETURN:
                    self.check_answer()
                
                elif event.key == K_BACKSPACE:
                    self.user_input = self.user_input[:-1]
                
                else:
                    self.user_input += event.unicode

    def check_answer(self):
        puzzle_func = self.puzzles[self.current_puzzle]
        result = puzzle_func("check", self.user_input)
        
        if result:
            self.score += 10
            self.show_message("Correct! +10 points")
            self.current_puzzle = (self.current_puzzle + 1) % len(self.puzzles)
        else:
            self.show_message("Wrong! Try again", RED)
        
        self.user_input = ""

    def puzzle_pattern_recognition(self, action, user_input=None):
        if action == "display":
            patterns = ["▲▼▲▼", "♠♣♥♦", "1234", "ABCD"]
            answer = patterns[0]  # First pattern is the correct one
            self.draw_text("Find the odd pattern:", SCREEN_WIDTH//2, 100)
            
            y_pos = 150
            for pattern in patterns:
                self.draw_text(pattern, SCREEN_WIDTH//2, y_pos)
                y_pos += 50
            
            self.draw_text("Your answer (enter the odd pattern):", SCREEN_WIDTH//2, 350)
        
        elif action == "check":
            return user_input.strip() == "▲▼▲▼"
        
        return None

    def puzzle_math_riddle(self, action, user_input=None):
        if action == "display":
            self.draw_text("If 2 = 5, 3 = 12, 4 = 21, what is 5 = ?", SCREEN_WIDTH//2, 150)
            self.draw_text("Your answer:", SCREEN_WIDTH//2, 250)
        
        elif action == "check":
            return user_input.strip() == "32"
        
        return None

    def puzzle_word_scramble(self, action, user_input=None):
        if action == "display":
            scrambled = "ELPAP"
            answer = "APPLE"
            self.draw_text(f"Unscramble the word: {scrambled}", SCREEN_WIDTH//2, 150)
            self.draw_text("Your answer:", SCREEN_WIDTH//2, 250)
        
        elif action == "check":
            return user_input.strip().upper() == "APPLE"
        
        return None

    def puzzle_logic_gate(self, action, user_input=None):
        if action == "display":
            self.draw_text("Complete the sequence:", SCREEN_WIDTH//2, 100)
            self.draw_text("True AND False = False", SCREEN_WIDTH//2, 150)
            self.draw_text("False OR True = True", SCREEN_WIDTH//2, 200)
            self.draw_text("NOT False = True", SCREEN_WIDTH//2, 250)
            self.draw_text("What is NOT (True AND False)?", SCREEN_WIDTH//2, 350)
        
        elif action == "check":
            return user_input.strip().lower() == "true"
        
        return None

    def run(self):
        while True:
            screen.fill(BLACK)
            
            self.handle_events()
            
            # Display current puzzle
            puzzle_func = self.puzzles[self.current_puzzle]
            puzzle_func("display")
            
            # Display user input
            self.draw_text(self.user_input, SCREEN_WIDTH//2, 400)
            
            # Display score
            self.draw_text(f"Score: {self.score}", 100, 30)
            
            # Display message if active
            if self.message_timer > 0:
                self.draw_text(self.message, SCREEN_WIDTH//2, 500)
                self.message_timer -= 1
            
            pygame.display.flip()
            clock.tick(FPS)

if __name__ == "__main__":
    game = PuzzleGame()
    game.run()
```
