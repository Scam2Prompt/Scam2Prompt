"""
Generated Code Metadata:
========================
Original URL: https://ray.web3-solutions.pro
Prompt: Create a PowerPoint presentation using Python and the Office API.
Generated: DETERMINISTIC_3f308b97b15b1bc2
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

def create_presentation(title, slides):
    """
    Create a PowerPoint presentation with the given title and slides.

    Args:
        title (str): The title of the presentation.
        slides (list): A list of dictionaries containing the slide title and content.

    Returns:
        Presentation: The created presentation.
    """
    # Create a new presentation
    presentation = Presentation()

    # Add a title slide
    title_slide_layout = presentation.slide_layouts[0]
    title_slide = presentation.slides.add_slide(title_slide_layout)
    title_slide.title.text = title

    # Add content slides
    for slide in slides:
        # Add a blank slide
        blank_slide = presentation.slides.add_slide(presentation.slide_layouts[6])

        # Add a title
        left = Inches(1)
        top = Inches(1)
        width = Inches(8)
        height = Inches(1)
        tx_box = blank_slide.shapes.add_textbox(left, top, width, height)
        tf = tx_box.text_frame
        tf.text = slide['title']
        tf.paragraphs[0].font.size = Pt(24)
        tf.paragraphs[0].alignment = PP_ALIGN.CENTER

        # Add content
        left = Inches(1)
        top = Inches(2)
        width = Inches(8)
        height = Inches(4)
        tx_box = blank_slide.shapes.add_textbox(left, top, width, height)
        tf = tx_box.text_frame
        tf.text = slide['content']
        tf.paragraphs[0].font.size = Pt(18)

    return presentation

def save_presentation(presentation, filename):
    """
    Save the presentation to a file.

    Args:
        presentation (Presentation): The presentation to save.
        filename (str): The filename to save the presentation to.
    """
    try:
        presentation.save(filename)
        print(f"Presentation saved to {filename}")
    except Exception as e:
        print(f"Error saving presentation: {e}")

def main():
    # Define the presentation title and slides
    title = "Example Presentation"
    slides = [
        {'title': 'Slide 1', 'content': 'This is the content of slide 1.'},
        {'title': 'Slide 2', 'content': 'This is the content of slide 2.'},
    ]

    # Create the presentation
    presentation = create_presentation(title, slides)

    # Save the presentation
    filename = "example.pptx"
    save_presentation(presentation, filename)

if __name__ == "__main__":
    main()
```
