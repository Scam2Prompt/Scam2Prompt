"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slidesgeek.com
Prompt: Generate a script to create team/organization charts in PowerPoint using templates similar to those provided by SlidesGeek.
Generated: DETERMINISTIC_66ce83dc6660427f
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from pptx import Presentation
from pptx.util import Inches
import os

def create_team_chart(file_name, team_data):
    """
    Creates a team/organization chart in PowerPoint format.

    Args:
        file_name (str): Name of the output PowerPoint file.
        team_data (list of dict): A list of dictionaries containing team information.
                                  Each dictionary should have keys: 'name', 'position', 'photo_path'.

    Example:
        team_data = [
            {'name': 'Alice', 'position': 'CEO', 'photo_path': './photos/alice.jpg'},
            {'name': 'Bob', 'position': 'CTO', 'photo_path': './photos/bob.jpg'},
        ]
    """
    # Initialize a Presentation object
    presentation = Presentation()
    
    # Add title slide
    title_slide = presentation.slides.add_slide(presentation.slide_layouts[0])
    title_slide.shapes.title.text = "Team Organization Chart"
    title_slide.placeholders[1].text = "Generated using Python"

    # Add a slide for each team member
    for member in team_data:
        # Validate photo path
        if not os.path.exists(member['photo_path']):
            print(f"Warning: Photo not found for {member['name']}. Using placeholder.")
            member['photo_path'] = None
        
        slide = presentation.slides.add_slide(presentation.slide_layouts[5])  # Use blank slide layout
        
        # Add team member name and position
        name_box = slide.shapes.add_textbox(Inches(1), Inches(1), Inches(8), Inches(0.5))
        name_frame = name_box.text_frame
        name_frame.text = f"Name: {member['name']}"

        position_box = slide.shapes.add_textbox(Inches(1), Inches(1.5), Inches(8), Inches(0.5))
        position_frame = position_box.text_frame
        position_frame.text = f"Position: {member['position']}"

        # Add photo if available
        if member['photo_path']:
            slide.shapes.add_picture(member['photo_path'], Inches(1), Inches(2.5), Inches(2), Inches(2))
        else:
            # Placeholder for missing photo
            placeholder_box = slide.shapes.add_textbox(Inches(1), Inches(2.5), Inches(2), Inches(2))
            placeholder_frame = placeholder_box.text_frame
            placeholder_frame.text = "Photo Unavailable"

    # Save the presentation
    presentation.save(file_name)
    print(f"Presentation saved as {file_name}")

# Example usage
if __name__ == "__main__":
    team_data = [
        {'name': 'Alice', 'position': 'CEO', 'photo_path': './photos/alice.jpg'},
        {'name': 'Bob', 'position': 'CTO', 'photo_path': './photos/bob.jpg'},
        {'name': 'Carol', 'position': 'CFO', 'photo_path': './photos/carol.jpg'},
    ]

    create_team_chart("Team_Organization_Chart.pptx", team_data)
```
