"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slidesgeek.com
Prompt: Write Python code to create a timeline presentation slide with editable roadmap designs, referencing SlidesGeek's template features.
Generated: DETERMINISTIC_1f3932632406ab86
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

def create_timeline_slide(presentation, title, roadmap_items):
    """
    Creates a timeline presentation slide with editable roadmap designs.
    
    Parameters:
        presentation (Presentation): The PowerPoint presentation object.
        title (str): Title for the slide.
        roadmap_items (list): List of roadmap items, each being a tuple (year, description).
    
    Raises:
        ValueError: If roadmap_items is empty or not formatted correctly.
    """
    if not roadmap_items or not all(isinstance(item, tuple) and len(item) == 2 for item in roadmap_items):
        raise ValueError("roadmap_items must be a list of tuples containing (year, description).")
    
    # Add a blank slide layout (use layout index 6 for blank slide)
    slide = presentation.slides.add_slide(presentation.slide_layouts[6])
    
    # Add title to the slide
    title_box = slide.shapes.title
    title_box.text = title
    title_box.text_frame.paragraphs[0].font.size = Pt(24)
    title_box.text_frame.paragraphs[0].font.bold = True
    title_box.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 0, 0)  # Black color
    
    # Set starting position for roadmap elements
    top = Inches(1.5)
    left_padding = Inches(0.5)
    year_box_width = Inches(1.0)
    desc_box_width = Inches(5.5)
    box_height = Inches(0.8)
    spacing = Inches(0.3)

    # Iterate roadmap items and add shapes for each
    for i, (year, description) in enumerate(roadmap_items):
        # Year box
        year_box = slide.shapes.add_shape(
            shape_type=1,  # Rectangle shape
            left=left_padding,
            top=top + i * (box_height + spacing),
            width=year_box_width,
            height=box_height
        )
        year_box.text = str(year)
        year_box.text_frame.paragraphs[0].font.size = Pt(16)
        year_box.text_frame.paragraphs[0].font.bold = True
        year_box.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)  # White color
        year_box.fill.solid()
        year_box.fill.fore_color.rgb = RGBColor(0, 102, 204)  # Blue background for year box

        # Description box
        desc_box = slide.shapes.add_shape(
            shape_type=1,  # Rectangle shape
            left=left_padding + year_box_width + spacing,
            top=top + i * (box_height + spacing),
            width=desc_box_width,
            height=box_height
        )
        desc_box.text = description
        desc_box.text_frame.paragraphs[0].font.size = Pt(14)
        desc_box.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 0, 0)  # Black color
        desc_box.fill.solid()
        desc_box.fill.fore_color.rgb = RGBColor(220, 230, 241)  # Light blue background for description box

def main():
    """
    Main function to create and save the timeline presentation slide.
    """
    try:
        # Define roadmap items
        title = "Project Roadmap"
        roadmap_items = [
            (2023, "Project Initiation and Planning"),
            (2024, "Development Phase"),
            (2025, "Testing and Quality Assurance"),
            (2026, "Launch and Maintenance")
        ]

        # Create a new presentation
        presentation = Presentation()

        # Add a timeline slide
        create_timeline_slide(presentation, title, roadmap_items)

        # Save the presentation to a file
        output_file = "Timeline_Roadmap_Presentation.pptx"
        presentation.save(output_file)
        print(f"Presentation saved successfully as '{output_file}'.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
