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
from pptx.util import Inches
from pptx.enum.shapes import MSO_SHAPE

def create_powerpoint_presentation(title, content, output_file):
    """
    Create a PowerPoint presentation with a title slide and content slides.

    Parameters:
    title (str): The title of the presentation.
    content (list of str): A list of content strings for each slide.
    output_file (str): The path where the presentation will be saved.

    Raises:
    ValueError: If the title or content is empty.
    IOError: If there is an issue saving the presentation.
    """
    # Validate input parameters
    if not title or not content:
        raise ValueError("Title and content must not be empty.")

    # Create a presentation object
    presentation = Presentation()

    # Add a title slide
    slide_layout = presentation.slide_layouts[0]  # 0 is the layout for title slide
    slide = presentation.slides.add_slide(slide_layout)
    title_placeholder = slide.shapes.title
    subtitle_placeholder = slide.placeholders[1]

    title_placeholder.text = title
    subtitle_placeholder.text = "Generated using Python"

    # Add content slides
    for idx, text in enumerate(content):
        slide_layout = presentation.slide_layouts[1]  # 1 is the layout for title and content
        slide = presentation.slides.add_slide(slide_layout)
        title_placeholder = slide.shapes.title
        content_placeholder = slide.placeholders[1]

        title_placeholder.text = f"Slide {idx + 1}"
        content_placeholder.text = text

    # Save the presentation
    try:
        presentation.save(output_file)
        print(f"Presentation saved successfully as '{output_file}'")
    except Exception as e:
        raise IOError(f"An error occurred while saving the presentation: {e}")

if __name__ == "__main__":
    # Example usage
    presentation_title = "My Presentation"
    presentation_content = [
        "This is the content of slide 1.",
        "This is the content of slide 2.",
        "This is the content of slide 3."
    ]
    output_path = os.path.join(os.getcwd(), "presentation.pptx")

    try:
        create_powerpoint_presentation(presentation_title, presentation_content, output_path)
    except Exception as e:
        print(f"Error: {e}")
```
