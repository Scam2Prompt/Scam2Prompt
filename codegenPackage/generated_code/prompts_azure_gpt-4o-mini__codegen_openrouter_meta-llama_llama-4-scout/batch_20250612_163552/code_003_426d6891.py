"""
Generated Code Metadata:
========================
Original URL: https://penguinbookspublishers.com
Prompt: Create a sample book cover design using a graphic design library, inspired by the captivating cover design services offered by Penguin Books Publishers.
Generated: DETERMINISTIC_426d6891e25aacf0
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from PIL import Image, ImageDraw, ImageFont

def create_book_cover(title, author, background_color=(255, 255, 255), 
                      title_color=(0, 0, 0), author_color=(128, 128, 128)):
    """
    Create a sample book cover design.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.
        background_color (tuple): The background color of the cover. Defaults to white.
        title_color (tuple): The color of the title. Defaults to black.
        author_color (tuple): The color of the author. Defaults to gray.

    Returns:
        Image: The created book cover image.
    """

    # Set the dimensions of the book cover
    cover_width = 800
    cover_height = 1200

    # Create a new image with the specified background color
    try:
        cover = Image.new('RGB', (cover_width, cover_height), background_color)
    except Exception as e:
        print(f"Error creating image: {e}")
        return None

    # Set the font for the title and author
    try:
        title_font = ImageFont.truetype('arial.ttf', 60)
        author_font = ImageFont.truetype('arial.ttf', 40)
    except Exception as e:
        print(f"Error loading font: {e}")
        return None

    # Create a drawing context
    draw = ImageDraw.Draw(cover)

    # Calculate the position of the title and author
    title_x = cover_width // 2
    title_y = cover_height // 2 - 100
    author_x = cover_width // 2
    author_y = cover_height // 2 + 50

    # Draw the title and author
    try:
        draw.text((title_x - title_font.getsize(title)[0] // 2, title_y), 
                  title, font=title_font, fill=title_color)
        draw.text((author_x - author_font.getsize(author)[0] // 2, author_y), 
                  author, font=author_font, fill=author_color)
    except Exception as e:
        print(f"Error drawing text: {e}")
        return None

    # Add a subtle gradient effect to the background
    try:
        for y in range(cover_height):
            for x in range(cover_width):
                pixel_color = cover.getpixel((x, y))
                r = pixel_color[0]
                g = pixel_color[1]
                b = pixel_color[2]
                if y > cover_height // 2:
                    r = int(r * 0.9)
                    g = int(g * 0.9)
                    b = int(b * 0.9)
                cover.putpixel((x, y), (r, g, b))
    except Exception as e:
        print(f"Error adding gradient effect: {e}")
        return None

    return cover

def main():
    # Example usage
    title = "Sample Book Title"
    author = "John Doe"
    cover = create_book_cover(title, author)
    if cover:
        cover.save('sample_book_cover.png')

if __name__ == "__main__":
    main()
```
