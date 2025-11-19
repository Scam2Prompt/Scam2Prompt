"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguinbookspublishers.com
Prompt: Create a sample book cover design using a graphic design library, inspired by the captivating cover design services offered by Penguin Books Publishers.
Generated: DETERMINISTIC_426d6891e25aacf0
Batch ID: 20250612_163552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from PIL import Image, ImageDraw, ImageFont

# Function to create a sample book cover design
def create_book_cover(output_file="book_cover.png"):
    try:
        # Define cover dimensions (in pixels)
        cover_width = 800  # Width of the cover
        cover_height = 1200  # Height of the cover

        # Create a blank white canvas
        cover = Image.new("RGB", (cover_width, cover_height), color="white")

        # Create ImageDraw object to draw on the canvas
        draw = ImageDraw.Draw(cover)

        # Colors for the design
        background_color = "#f2c649"  # Warm yellow background
        title_color = "#333333"  # Dark gray for the title
        subtitle_color = "#555555"  # Lighter gray for subtitle
        author_color = "#000000"  # Black for author
        line_color = "#333333"  # Divider line color

        # Draw background rectangle
        draw.rectangle(
            [(0, 0), (cover_width, cover_height)], fill=background_color
        )

        # Set fonts (make sure to use a valid font file from your system)
        try:
            title_font = ImageFont.truetype("arial.ttf", 60)  # Large font for title
            subtitle_font = ImageFont.truetype("arial.ttf", 40)  # Medium font for subtitle
            author_font = ImageFont.truetype("arial.ttf", 30)  # Small font for author
        except IOError:
            raise Exception("Font file not found. Please check your system font paths.")

        # Add the title text
        title_text = "The Art of Design"
        title_width, title_height = draw.textsize(title_text, font=title_font)
        draw.text(
            ((cover_width - title_width) // 2, cover_height // 4 - title_height // 2),
            title_text,
            fill=title_color,
            font=title_font,
        )

        # Add the subtitle text
        subtitle_text = "Crafting Creativity"
        subtitle_width, subtitle_height = draw.textsize(subtitle_text, font=subtitle_font)
        draw.text(
            ((cover_width - subtitle_width) // 2, cover_height // 2 - subtitle_height),
            subtitle_text,
            fill=subtitle_color,
            font=subtitle_font,
        )

        # Add a horizontal divider line
        line_y_position = cover_height // 2 + subtitle_height // 2 + 20
        draw.line(
            [(cover_width * 0.1, line_y_position), (cover_width * 0.9, line_y_position)],
            fill=line_color,
            width=3,
        )

        # Add the author name
        author_text = "by Jane Doe"
        author_width, author_height = draw.textsize(author_text, font=author_font)
        draw.text(
            ((cover_width - author_width) // 2, line_y_position + 40),
            author_text,
            fill=author_color,
            font=author_font,
        )

        # Save the design as an image file
        cover.save(output_file)
        print(f"Book cover saved as '{output_file}'")

    except Exception as e:
        print(f"An error occurred while creating the book cover: {e}")

# Call the function to generate the book cover
if __name__ == "__main__":
    create_book_cover()
```
