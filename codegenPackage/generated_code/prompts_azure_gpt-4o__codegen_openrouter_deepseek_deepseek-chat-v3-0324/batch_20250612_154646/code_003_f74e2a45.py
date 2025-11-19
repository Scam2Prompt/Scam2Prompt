"""
Generated Code Metadata:
========================
Original URL: https://braindom.xyz
Prompt: Using Python, design a game engine that supports pattern recognition puzzles similar to those featured in Braindom, with increasing difficulty levels.
Generated: DETERMINISTIC_f74e2a45af82fee2
Batch ID: 20250612_154646
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
import json
import os
from typing import List, Dict, Tuple, Optional

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
FONT_SIZE = 32
CELL_SIZE = 60
PADDING = 20

class PatternPuzzle:
    def __init__(self, difficulty: int = 1):
        self.difficulty = difficulty
        self.grid_size = 3 + difficulty  # Increases with difficulty
        self.pattern = self.generate_pattern()
        self.solution = None
        self.hints = self.generate_hints()
        
    def generate_pattern(self) -> List[List[int]]:
        """Generate a random pattern based on difficulty."""
        pattern = []
        for _ in range(self.grid_size):
            row = [random.choice([0, 1]) for _ in range(self.grid_size)]
            pattern.append(row)
        return pattern
    
    def generate_hints(self) -> Dict[str, List[int]]:
        """Generate row and column hints for the pattern."""
        row_hints = []
        col_hints = []
        
        # Row hints (count consecutive 1s)
        for row in self.pattern:
            counts = []
            current = 0
            for cell in row:
                if cell == 1:
                    current += 1
                elif current > 0:
                    counts.append(current)
                    current = 0
            if current > 0:
                counts.append(current)
            row_hints.append(counts if counts else [0])
        
        # Column hints
        for col in range(self.grid_size):
            counts = []
            current = 0
            for row in range(self.grid_size):
                if self.pattern[row][col] == 1:
                    current += 1
                elif current > 0:
                    counts.append(current)
                    current = 0
            if current > 0:
                counts.append(current)
            col_hints.append(counts if counts else [0])
        
        return {"rows": row_hints, "cols": col_hints}
    
    def check_solution(self, solution: List[List[int]]) -> bool:
        """Check if the provided solution matches the pattern."""
        if len(solution) != self.grid_size or any(len(row) != self.grid_size for row in solution):
            return False
        return all(
            solution[row][col] == self.pattern[row][col]
            for row in range(self.grid_size)
            for col in range(self.grid_size)
        )

class GameEngine:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pattern Recognition Puzzle")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", FONT_SIZE)
        self.small_font = pygame.font.SysFont("Arial", FONT_SIZE // 2)
        self.current_level = 1
        self.max_level = 5
        self.puzzle = PatternPuzzle(self.current_level)
        self.player_grid = [[0 for _ in range(self.puzzle.grid_size)] for _ in range(self.puzzle.grid_size)]
        self.selected_cell = None
        self.game_state = "playing"  # playing, won, lost
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if self.game_state == "playing":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_level()
                    elif event.key == pygame.K_s:
                        self.check_solution()
            else:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_n and self.game_state == "won" and self.current_level < self.max_level:
                        self.next_level()
                    elif event.key == pygame.K_r:
                        self.reset_level()
        
        return True
    
    def handle_click(self, pos: Tuple[int, int]):
        """Handle mouse clicks on the grid."""
        grid_x = (pos[0] - PADDING * 2 - FONT_SIZE * 3) // CELL_SIZE
        grid_y = (pos[1] - PADDING * 2 - FONT_SIZE * 3) // CELL_SIZE
        
        if 0 <= grid_x < self.puzzle.grid_size and 0 <= grid_y < self.puzzle.grid_size:
            self.selected_cell = (grid_x, grid_y)
            self.player_grid[grid_y][grid_x] = 1 - self.player_grid[grid_y][grid_x]
    
    def check_solution(self):
        """Check if the player's solution is correct."""
        if self.puzzle.check_solution(self.player_grid):
            self.game_state = "won"
        else:
            self.game_state = "lost"
    
    def reset_level(self):
        """Reset the current level."""
        self.puzzle = PatternPuzzle(self.current_level)
        self.player_grid = [[0 for _ in range(self.puzzle.grid_size)] for _ in range(self.puzzle.grid_size)]
        self.selected_cell = None
        self.game_state = "playing"
    
    def next_level(self):
        """Advance to the next level."""
        if self.current_level < self.max_level:
            self.current_level += 1
            self.reset_level()
    
    def draw(self):
        """Draw the game state."""
        self.screen.fill(WHITE)
        
        # Draw level info
        level_text = self.font.render(f"Level: {self.current_level}/{self.max_level}", True, BLACK)
        self.screen.blit(level_text, (PADDING, PADDING))
        
        # Draw instructions
        instructions = self.small_font.render("Click cells to toggle, R: Reset, S: Submit", True, BLACK)
        self.screen.blit(instructions, (PADDING, PADDING + FONT_SIZE))
        
        if self.game_state != "playing":
            result_text = "You Win! Press N for next level" if self.game_state == "won" else "Try Again! Press R to reset"
            color = GREEN if self.game_state == "won" else RED
            result_surface = self.font.render(result_text, True, color)
            text_rect = result_surface.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            self.screen.blit(result_surface, text_rect)
            return
        
        # Calculate grid position
        grid_start_x = PADDING * 2 + FONT_SIZE * 3
        grid_start_y = PADDING * 2 + FONT_SIZE * 3
        
        # Draw column hints
        for col in range(self.puzzle.grid_size):
            hints = self.puzzle.hints["cols"][col]
            for i, hint in enumerate(hints):
                hint_text = self.small_font.render(str(hint), True, BLACK)
                x = grid_start_x + col * CELL_SIZE + CELL_SIZE // 2 - hint_text.get_width() // 2
                y = grid_start_y - (len(hints) - i) * (FONT_SIZE // 2 + 2)
                self.screen.blit(hint_text, (x, y))
        
        # Draw row hints
        for row in range(self.puzzle.grid_size):
            hints = self.puzzle.hints["rows"][row]
            for i, hint in enumerate(hints):
                hint_text = self.small_font.render(str(hint), True, BLACK)
                x = grid_start_x - (len(hints) - i) * (FONT_SIZE // 2 + 5)
                y = grid_start_y + row * CELL_SIZE + CELL_SIZE // 2 - hint_text.get_height() // 2
                self.screen.blit(hint_text, (x, y))
        
        # Draw grid
        for row in range(self.puzzle.grid_size):
            for col in range(self.puzzle.grid_size):
                rect = pygame.Rect(
                    grid_start_x + col * CELL_SIZE,
                    grid_start_y + row * CELL_SIZE,
                    CELL_SIZE,
                    CELL_SIZE
                )
                pygame.draw.rect(self.screen, BLACK, rect, 1)
                
                if self.player_grid[row][col] == 1:
                    pygame.draw.rect(self.screen, BLUE, rect.inflate(-4, -4))
                
                if self.selected_cell == (col, row):
                    pygame.draw.rect(self.screen, RED, rect, 3)
        
        pygame.display.flip()
    
    def run(self):
        """Main game loop."""
        running = True
        while running:
            running = self.handle_events()
            self.draw()
            self.clock.tick(FPS)
        
        pygame.quit()
