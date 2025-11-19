"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Develop a gamified quiz in Python to teach the functions of computer keyboard keys, referencing the interactive informatics games on "Portal de Saltinho."
Generated: DETERMINISTIC_16702fe1234d0620
Batch ID: 20250612_153224
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
import random
from pygame.locals import *

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FONT_SIZE = 24
QUESTION_TIME = 10  # seconds

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Keyboard Keys Quiz Game')

# Fonts
font = pygame.font.SysFont('Arial', FONT_SIZE)
title_font = pygame.font.SysFont('Arial', FONT_SIZE * 2)

# Game states
MENU = 0
PLAYING = 1
GAME_OVER = 2
game_state = MENU

# Quiz data
questions = [
    {
        "question": "What is the function of the 'Enter' key?",
        "options": [
            "Move cursor to next line",
            "Delete text",
            "Insert space",
            "Open menu"
        ],
        "correct": 0,
        "key": K_RETURN
    },
    {
        "question": "What is the function of the 'Shift' key?",
        "options": [
            "Type uppercase letters",
            "Delete characters",
            "Move cursor",
            "Open settings"
        ],
        "correct": 0,
        "key": K_LSHIFT
    },
    {
        "question": "What is the function of the 'Backspace' key?",
        "options": [
            "Delete character to the left",
            "Delete character to the right",
            "Insert space",
            "Move cursor up"
        ],
        "correct": 0,
        "key": K_BACKSPACE
    },
    {
        "question": "What is the function of the 'Tab' key?",
        "options": [
            "Indent text or move to next field",
            "Delete text",
            "Insert special character",
            "Open new tab"
        ],
        "correct": 0,
        "key": K_TAB
    },
    {
        "question": "What is the function of the 'Caps Lock' key?",
        "options": [
            "Toggle uppercase letters",
            "Copy text",
            "Capitalize next letter",
            "Lock computer"
        ],
        "correct": 0,
        "key": K_CAPSLOCK
    }
]

# Game variables
current_question = 0
score = 0
time_left = QUESTION_TIME
clock = pygame.time.Clock()
start_time = 0
selected_option = None
feedback = None
feedback_time = 0

def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def draw_menu():
    screen.fill(BLUE)
    draw_text("Keyboard Keys Quiz", title_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
    draw_text("Learn about keyboard functions!", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text("Press SPACE to start", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3)

def draw_question():
    screen.fill(WHITE)
    question = questions[current_question]
    
    # Draw question
    draw_text(question["question"], font, BLACK, SCREEN_WIDTH // 2, 50)
    
    # Draw options
    for i, option in enumerate(question["options"]):
        color = BLACK
        if selected_option == i:
            color = GREEN if i == question["correct"] else RED
        draw_text(f"{i+1}. {option}", font, color, SCREEN_WIDTH // 2, 150 + i * 50)
    
    # Draw score and timer
    draw_text(f"Score: {score}", font, BLACK, 100, 30)
    draw_text(f"Time: {int(time_left)}s", font, BLACK, SCREEN_WIDTH - 100, 30)
    
    # Draw feedback if any
    if feedback:
        draw_text(feedback, font, GREEN if feedback == "Correct!" else RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50)

def draw_game_over():
    screen.fill(BLUE)
    draw_text("Game Over!", title_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
    draw_text(f"Final Score: {score}/{len(questions)}", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    draw_text("Press SPACE to play again", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3)

def check_answer(selected):
    global score, feedback, feedback_time, current_question, time_left
    
    question = questions[current_question]
    if selected == question["correct"]:
        score += 1
        feedback = "Correct!"
    else:
        feedback = "Incorrect!"
    
    feedback_time = pygame.time.get_ticks()
    current_question += 1
    
    if current_question >= len(questions):
        return True  # Game over
    else:
        time_left = QUESTION_TIME
        return False

def reset_game():
    global current_question, score, time_left, feedback, selected_option
    current_question = 0
    score = 0
    time_left = QUESTION_TIME
    feedback = None
    selected_option = None

# Main game loop
running = True
while running:
    current_time = pygame.time.get_ticks()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if game_state == MENU:
            if event.type == KEYDOWN and event.key == K_SPACE:
                game_state = PLAYING
                reset_game()
                start_time = current_time
        
        elif game_state == PLAYING:
            if event.type == KEYDOWN:
                question = questions[current_question]
                
                # Check if the pressed key matches the question's key
                if event.key == question["key"]:
                    selected_option = question["correct"]
                    if check_answer(selected_option):
                        game_state = GAME_OVER
                
                # Allow answering with number keys
                elif event.key == K_1:
                    selected_option = 0
                    if check_answer(selected_option):
                        game_state = GAME_OVER
                elif event.key == K_2 and len(question["options"]) > 1:
                    selected_option = 1
                    if check_answer(selected_option):
                        game_state = GAME_OVER
                elif event.key == K_3 and len(question["options"]) > 2:
                    selected_option = 2
                    if check_answer(selected_option):
                        game_state = GAME_OVER
                elif event.key == K_4 and len(question["options"]) > 3:
                    selected_option = 3
                    if check_answer(selected_option):
                        game_state = GAME_OVER
        
        elif game_state == GAME_OVER:
            if event.type == KEYDOWN and event.key == K_SPACE:
                game_state = MENU
    
    # Update game state
    if game_state == PLAYING:
        time_left = max(0, QUESTION_TIME - (current_time - start_time) / 1000)
        if time_left <= 0:
            if check_answer(-1):  # -1 means no answer selected
                game_state = GAME_OVER
        
        # Clear feedback after 1 second
        if feedback and current_time - feedback_time > 1000:
            feedback = None
            selected_option = None
    
    # Draw current screen
    if game_state == MENU:
        draw_menu()
    elif game_state == PLAYING:
        draw_question()
    elif game_state == GAME_OVER:
        draw_game_over()
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
```
