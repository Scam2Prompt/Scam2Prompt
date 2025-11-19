"""
Generated Code Metadata:
========================
Original URL: https://editorialcontra.com
Prompt: "Design a book cover for a new edition of 'SING BACKWARDS AND WEEP' by Mark Lanegan, incorporating elements that reflect the memoir's themes and tone."
Generated: DETERMINISTIC_c2aec00c1ab76ec4
Batch ID: 20250622_211241
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
import colorsys

def create_book_cover(title, author, background_color, text_color, image_path):
    """
    Creates a book cover with the given title, author, background color, text color, and image.

    Args:
        title (str): The title of the book.
        author (str): The author of the book.
        background_color (tuple): The RGB values of the background color.
        text_color (tuple): The RGB values of the text color.
        image_path (str): The path to the image file.

    Returns:
        Image: The created book cover image.
    """

    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Resize the image to fit the book cover
            img = img.resize((500, 700))

            # Create a new image with the background color
            cover = Image.new('RGB', (500, 700), background_color)

            # Paste the image onto the cover
            cover.paste(img, (0, 0))

            # Set the font and font size
            font = ImageFont.truetype('arial.ttf', 40)

            # Draw the title and author onto the cover
            draw = ImageDraw.Draw(cover)
            draw.text((20, 20), title, font=font, fill=text_color)
            draw.text((20, 600), author, font=font, fill=text_color)

            # Calculate a darker shade of the text color for the subtitle
            h, s, v = colorsys.rgb_to_hsv(text_color[0] / 255, text_color[1] / 255, text_color[2] / 255)
            v *= 0.7
            subtitle_color = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(h, s, v))
            subtitle_font = ImageFont.truetype('arial.ttf', 20)
            draw.text((20, 80), "'SING BACKWARDS AND WEEP'", font=subtitle_font, fill=subtitle_color)

            return cover

    except FileNotFoundError:
        print("The image file was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    title = "'SING BACKWARDS AND WEEP"
    author = "Mark Lanegan"
    background_color = (35, 35, 35)  # Dark gray
    text_color = (255, 255, 255)  # White
    image_path = 'memoir_image.jpg'  # Replace with the actual image path

    cover = create_book_cover(title, author, background_color, text_color, image_path)

    if cover:
        cover.save('book_cover.png')

if __name__ == "__main__":
    main()
```
