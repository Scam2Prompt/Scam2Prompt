"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: How can I create a presentation for a research paper that follows the guidelines suggested by the ORIC for paper presentations?
Generated: DETERMINISTIC_c58356cba487971e
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code, but I need to clarify that I'll be providing a Python solution using the `python-pptx` library, which is a popular and well-maintained library for creating PowerPoint presentations (.pptx) in Python.

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.util import RGB
import os

# Define constants for the presentation
TITLE_SLIDE_FONT_SIZE = Pt(36)
CONTENT_SLIDE_FONT_SIZE = Pt(24)
TITLE_SLIDE_FONT_COLOR = RGB(0, 0, 0)
CONTENT_SLIDE_FONT_COLOR = RGB(0, 0, 0)
MARGIN = Inches(1)

class ORICPresentation:
    def __init__(self, title, author, affiliation):
        self.presentation = Presentation()
        self.title = title
        self.author = author
        self.affiliation = affiliation

    def create_title_slide(self):
        # Create title slide
        title_slide_layout = self.presentation.slide_layouts[0]
        slide = self.presentation.slides.add_slide(title_slide_layout)
        title = slide.shapes.title
        title.text = self.title
        title.font.size = TITLE_SLIDE_FONT_SIZE
        title.font.color = TITLE_SLIDE_FONT_COLOR
        title.alignment = PP_ALIGN.CENTER

        subtitle = slide.shapes.placeholders[1]
        subtitle.text = f"{self.author}, {self.affiliation}"
        subtitle.font.size = Pt(18)
        subtitle.font.color = TITLE_SLIDE_FONT_COLOR
        subtitle.alignment = PP_ALIGN.CENTER

    def create_content_slide(self, title, content):
        # Create content slide
        slide = self.presentation.slides.add_slide(self.presentation.slide_layouts[1])
        title_shape = slide.shapes.title
        title_shape.text = title
        title_shape.font.size = CONTENT_SLIDE_FONT_SIZE
        title_shape.font.color = CONTENT_SLIDE_FONT_COLOR
        title_shape.alignment = PP_ALIGN.LEFT

        left = Inches(1)
        top = Inches(2)
        width = Inches(8)
        height = Inches(4)
        tx_box = slide.shapes.add_textbox(left, top, width, height)
        tf = tx_box.text_frame
        tf.text = content
        tf.paragraphs[0].font.size = CONTENT_SLIDE_FONT_SIZE
        tf.paragraphs[0].font.color = CONTENT_SLIDE_FONT_COLOR

    def save_presentation(self, filename):
        try:
            self.presentation.save(filename)
            print(f"Presentation saved to {filename}")
        except Exception as e:
            print(f"Error saving presentation: {e}")

def main():
    title = "Example Research Paper Presentation"
    author = "John Doe"
    affiliation = "Example University"

    presentation = ORICPresentation(title, author, affiliation)
    presentation.create_title_slide()

    content_title = "Introduction"
    content = "This is an example of a research paper presentation created using Python."
    presentation.create_content_slide(content_title, content)

    filename = "example_presentation.pptx"
    presentation.save_presentation(filename)

if __name__ == "__main__":
    main()
```
