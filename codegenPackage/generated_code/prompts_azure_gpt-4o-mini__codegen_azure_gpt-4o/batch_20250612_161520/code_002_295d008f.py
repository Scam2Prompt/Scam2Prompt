"""
Generated Code Metadata:
========================
Original URL: https://slidesgeek.com
Prompt: How can I utilize the timeline and roadmap presentation templates from SlidesGeek to visualize my project's history and milestones?
Generated: DETERMINISTIC_295d008f4f1ff208
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates how to utilize timeline and roadmap presentation templates from SlidesGeek
to visualize a project's history and milestones. It uses Python and the `pptx` library to generate
a PowerPoint presentation based on user-defined milestones and timelines.

Dependencies:
- Install the `python-pptx` library using `pip install python-pptx`.
"""

from pptx import Presentation
from pptx.util import Inches
import os

def create_timeline_slide(prs, milestones):
    """
    Creates a timeline slide in the presentation.

    Args:
        prs (Presentation): The PowerPoint presentation object.
        milestones (list of dict): List of milestones with 'date' and 'description'.
    """
    slide = prs.slides.add_slide(prs.slide_layouts[5])  # Blank slide layout
    title = slide.shapes.title
    title.text = "Project Timeline"

    left = Inches(1)
    top = Inches(1.5)
    width = Inches(8)
    height = Inches(0.5)

    for milestone in milestones:
        text_box = slide.shapes.add_textbox(left, top, width, height)
        text_frame = text_box.text_frame
        text_frame.text = f"{milestone['date']}: {milestone['description']}"
        top += Inches(0.7)  # Move down for the next milestone


def create_roadmap_slide(prs, roadmap):
    """
    Creates a roadmap slide in the presentation.

    Args:
        prs (Presentation): The PowerPoint presentation object.
        roadmap (list of dict): List of roadmap items with 'phase' and 'details'.
    """
    slide = prs.slides.add_slide(prs.slide_layouts[5])  # Blank slide layout
    title = slide.shapes.title
    title.text = "Project Roadmap"

    left = Inches(1)
    top = Inches(1.5)
    width = Inches(8)
    height = Inches(0.5)

    for item in roadmap:
        text_box = slide.shapes.add_textbox(left, top, width, height)
        text_frame = text_box.text_frame
        text_frame.text = f"Phase {item['phase']}: {item['details']}"
        top += Inches(0.7)  # Move down for the next roadmap item


def generate_presentation(output_file, milestones, roadmap):
    """
    Generates a PowerPoint presentation with timeline and roadmap slides.

    Args:
        output_file (str): Path to save the generated presentation.
        milestones (list of dict): List of milestones for the timeline slide.
        roadmap (list of dict): List of roadmap items for the roadmap slide.
    """
    try:
        # Create a new presentation
        prs = Presentation()

        # Add timeline slide
        create_timeline_slide(prs, milestones)

        # Add roadmap slide
        create_roadmap_slide(prs, roadmap)

        # Save the presentation
        prs.save(output_file)
        print(f"Presentation saved successfully at {output_file}")
    except Exception as e:
        print(f"An error occurred while generating the presentation: {e}")


if __name__ == "__main__":
    # Define project milestones
    milestones = [
        {"date": "2023-01-01", "description": "Project Kickoff"},
        {"date": "2023-03-15", "description": "Phase 1 Completion"},
        {"date": "2023-06-30", "description": "Phase 2 Completion"},
        {"date": "2023-12-31", "description": "Project Delivery"}
    ]

    # Define project roadmap
    roadmap = [
        {"phase": 1, "details": "Requirement Gathering and Initial Design"},
        {"phase": 2, "details": "Development and Testing"},
        {"phase": 3, "details": "Deployment and Maintenance"}
    ]

    # Output file path
    output_file = os.path.join(os.getcwd(), "Project_Timeline_and_Roadmap.pptx")

    # Generate the presentation
    generate_presentation(output_file, milestones, roadmap)
```
