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
# Import necessary libraries
from PIL import Image, ImageDraw, ImageFont

def create_book_cover(title, author, output_file):
    """
    Creates a sample book cover design inspired by Penguin Books Publishers.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.
        output_file (str): The file path to save the generated book cover.

    Returns:
        None
    """
    try:
        # Define cover dimensions (in pixels)
        width, height = 600, 900

        # Create a blank image with white background
        cover = Image.new("RGB", (width, height), "white")
        draw = ImageDraw.Draw(cover)

        # Define colors and fonts
        background_color = "#F4A261"  # Warm orange background
        accent_color = "#264653"      # Dark blue accent
        text_color = "#FFFFFF"        # White text
        font_title = ImageFont.truetype("arial.ttf", 40)  # Title font
        font_author = ImageFont.truetype("arial.ttf", 30)  # Author font

        # Draw background rectangle
        draw.rectangle([0, 0, width, height], fill=background_color)

        # Draw accent rectangle at the bottom
        accent_height = 150
        draw.rectangle([0, height - accent_height, width, height], fill=accent_color)

        # Add book title
        title_width, title_height = draw.textsize(title, font=font_title)
        title_x = (width - title_width) // 2
        title_y = (height - accent_height - title_height) // 2
        draw.text((title_x, title_y), title, fill=text_color, font=font_title)

        # Add author name
        author_width, author_height = draw.textsize(author, font=font_author)
        author_x = (width - author_width) // 2
        author_y = height - accent_height + (accent_height - author_height) // 2
        draw.text((author_x, author_y), author, fill=text_color, font=font_author)

        # Save the book cover to the specified file
        cover.save(output_file)
        print(f"Book cover saved to {output_file}")

    except Exception as e:
        print(f"An error occurred while creating the book cover: {e}")

# Example usage
if __name__ == "__main__":
    create_book_cover(
        title="The Great Adventure",
        author="John Doe",
        output_file="book_cover.png"
    )
```
