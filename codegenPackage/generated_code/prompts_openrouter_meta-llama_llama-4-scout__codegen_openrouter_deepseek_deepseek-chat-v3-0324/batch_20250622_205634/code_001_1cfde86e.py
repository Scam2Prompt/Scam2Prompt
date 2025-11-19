"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: "Write a Python script to generate Géminito game cards with musical notes and symbols."
Generated: DETERMINISTIC_1cfde86eba257226
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from PIL import Image, ImageDraw, ImageFont
import os
import textwrap

# Constants
CARD_WIDTH = 800
CARD_HEIGHT = 600
BACKGROUND_COLOR = (255, 255, 255)  # White
TEXT_COLOR = (0, 0, 0)  # Black
FONT_SIZE = 40
MARGIN = 50
SYMBOLS_PER_CARD = 6
OUTPUT_DIR = "geminote_cards"

# Musical symbols and notes
MUSICAL_SYMBOLS = [
    "♩", "♪", "♫", "♬", "♭", "♮", "♯", "𝄞", "𝄢", "𝄫", "𝄪", "𝄡", "𝄤", "𝄦", "𝄩"
]

def create_output_directory():
    """Create output directory if it doesn't exist."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def generate_card(card_number):
    """Generate a single Geminote game card."""
    # Create blank image
    image = Image.new("RGB", (CARD_WIDTH, CARD_HEIGHT), BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)
    
    try:
        font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    except:
        font = ImageFont.load_default()
    
    # Card title
    title = f"Geminote Card #{card_number}"
    title_width, title_height = draw.textsize(title, font=font)
    draw.text(
        ((CARD_WIDTH - title_width) // 2, MARGIN),
        title,
        fill=TEXT_COLOR,
        font=font
    )
    
    # Select random symbols
    symbols = random.sample(MUSICAL_SYMBOLS, SYMBOLS_PER_CARD)
    
    # Calculate positions
    symbols_per_row = 3
    symbol_width = (CARD_WIDTH - 2 * MARGIN) // symbols_per_row
    symbol_height = (CARD_HEIGHT - 2 * MARGIN - title_height) // 2
    
    # Draw symbols
    for i, symbol in enumerate(symbols):
        row = i // symbols_per_row
        col = i % symbols_per_row
        
        x = MARGIN + col * symbol_width + symbol_width // 2
        y = MARGIN + title_height + row * symbol_height + symbol_height // 2
        
        # Center the symbol
        symbol_width_px, symbol_height_px = draw.textsize(symbol, font=font)
        x -= symbol_width_px // 2
        y -= symbol_height_px // 2
        
        draw.text((x, y), symbol, fill=TEXT_COLOR, font=font)
    
    return image

def generate_cards(num_cards):
    """Generate multiple Geminote game cards."""
    create_output_directory()
    
    for i in range(1, num_cards + 1):
        card = generate_card(i)
        filename = os.path.join(OUTPUT_DIR, f"geminote_card_{i}.png")
        card.save(filename)
        print(f"Generated: {filename}")

if __name__ == "__main__":
    try:
        num_cards = int(input("Enter number of cards to generate: "))
        if num_cards <= 0:
            raise ValueError("Number of cards must be positive")
        generate_cards(num_cards)
        print("Card generation completed successfully!")
    except ValueError as e:
        print(f"Error: {e}. Please enter a valid positive integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
