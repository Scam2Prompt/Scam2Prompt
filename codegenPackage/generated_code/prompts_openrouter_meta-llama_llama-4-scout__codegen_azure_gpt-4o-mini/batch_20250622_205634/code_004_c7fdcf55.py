"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: "Develop a simple game using a library like Pygame to play a digital version of Géminito."
Generated: DETERMINISTIC_c7fdcf550ebe6491
Batch ID: 20250622_205634
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
FPS = 60
CARD_WIDTH = 100
CARD_HEIGHT = 150
NUM_CARDS = 12  # Total number of cards (6 pairs)
CARD_BACK_COLOR = (0, 128, 255)
CARD_FRONT_COLOR = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Géminito Game")

# Card class to represent each card in the game
class Card:
    def __init__(self, value):
        self.value = value
        self.is_flipped = False

    def draw(self, x, y):
        if self.is_flipped:
            pygame.draw.rect(screen, CARD_FRONT_COLOR, (x, y, CARD_WIDTH, CARD_HEIGHT))
            font = pygame.font.Font(None, 74)
            text = font.render(str(self.value), True, (0, 0, 0))
            screen.blit(text, (x + CARD_WIDTH // 4, y + CARD_HEIGHT // 4))
        else:
            pygame.draw.rect(screen, CARD_BACK_COLOR, (x, y, CARD_WIDTH, CARD_HEIGHT))

# Function to create and shuffle cards
def create_cards():
    values = list(range(1, NUM_CARDS // 2 + 1)) * 2
    random.shuffle(values)
    return [Card(value) for value in values]

# Main game function
def main():
    clock = pygame.time.Clock()
    cards = create_cards()
    flipped_cards = []
    matched_pairs = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_x, mouse_y = event.pos
                card_x = mouse_x // CARD_WIDTH
                card_y = mouse_y // CARD_HEIGHT
                card_index = card_y * (SCREEN_WIDTH // CARD_WIDTH) + card_x

                if 0 <= card_index < NUM_CARDS and not cards[card_index].is_flipped:
                    cards[card_index].is_flipped = True
                    flipped_cards.append(card_index)

                    # Check for a match
                    if len(flipped_cards) == 2:
                        pygame.display.flip()
                        pygame.time.wait(1000)  # Wait for a second to show the cards
                        if cards[flipped_cards[0]].value == cards[flipped_cards[1]].value:
                            matched_pairs += 1
                        else:
                            cards[flipped_cards[0]].is_flipped = False
                            cards[flipped_cards[1]].is_flipped = False
                        flipped_cards.clear()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the cards
        for index, card in enumerate(cards):
            x = (index % (SCREEN_WIDTH // CARD_WIDTH)) * CARD_WIDTH
            y = (index // (SCREEN_WIDTH // CARD_WIDTH)) * CARD_HEIGHT
            card.draw(x, y)

        # Check for game over
        if matched_pairs == NUM_CARDS // 2:
            game_over = True

        pygame.display.flip()
        clock.tick(FPS)

    # Display game over message
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over!", True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)

    pygame.quit()

if __name__ == "__main__":
    main()
```
