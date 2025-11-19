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
import os
import json
from datetime import datetime
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN

def load_slidesgeek_template(template_path):
    """
    Load a SlidesGeek PowerPoint template file.
    
    Args:
        template_path (str): Path to the PowerPoint template file.
        
    Returns:
        Presentation: PowerPoint presentation object.
    """
    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Template file not found at {template_path}")
    
    return Presentation(template_path)

def create_timeline_slide(prs, title, milestones):
    """
    Create a timeline slide using a template layout.
    
    Args:
        prs (Presentation): PowerPoint presentation object.
        title (str): Title for the timeline slide.
        milestones (list): List of milestone dictionaries with 'date', 'title', 'description'.
    """
    # Use the first slide layout that matches our needs (adjust index as needed)
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    
    # Set slide title
    title_placeholder = slide.shapes.title
    title_placeholder.text = title
    
    # Add timeline content
    left = Inches(1)
    top = Inches(2)
    width = Inches(8)
    height = Inches(4)
    
    # Create a text box for the timeline
    textbox = slide.shapes.add_textbox(left, top, width, height)
    tf = textbox.text_frame
    
    # Format timeline entries
    for milestone in milestones:
        date_str = milestone['date'].strftime("%b %Y") if isinstance(milestone['date'], datetime) else milestone['date']
        
        p = tf.add_paragraph()
        p.text = f"{date_str}: {milestone['title']}"
        p.level = 0
        p.font.bold = True
        p.font.size = Pt(14)
        p.font.color.rgb = RGBColor(59, 89, 152)  # Blue color
        
        p = tf.add_paragraph()
        p.text = milestone['description']
        p.level = 1
        p.font.size = Pt(12)
        p.space_after = Pt(12)

def create_roadmap_slide(prs, title, phases):
    """
    Create a roadmap slide with phases and milestones.
    
    Args:
        prs (Presentation): PowerPoint presentation object.
        title (str): Title for the roadmap slide.
        phases (list): List of phase dictionaries with 'name', 'start', 'end', 'milestones'.
    """
    # Use a different slide layout for roadmap
    slide_layout = prs.slide_layouts[2]
    slide = prs.slides.add_slide(slide_layout)
    
    # Set slide title
    title_placeholder = slide.shapes.title
    title_placeholder.text = title
    
    # Add roadmap content
    left = Inches(1)
    top = Inches(1.5)
    width = Inches(8)
    height = Inches(5)
    
    # Create a text box for the roadmap
    textbox = slide.shapes.add_textbox(left, top, width, height)
    tf = textbox.text_frame
    
    for phase in phases:
        # Add phase header
        p = tf.add_paragraph()
        p.text = phase['name']
        p.level = 0
        p.font.bold = True
        p.font.size = Pt(16)
        p.font.color.rgb = RGBColor(31, 73, 125)  # Dark blue
        
        # Add phase timeline
        start_str = phase['start'].strftime("%b %Y") if isinstance(phase['start'], datetime) else phase['start']
        end_str = phase['end'].strftime("%b %Y") if isinstance(phase['end'], datetime) else phase['end']
        
        p = tf.add_paragraph()
        p.text = f"{start_str} - {end_str}"
        p.level = 1
        p.font.italic = True
        p.font.size = Pt(12)
        
        # Add milestones
        for milestone in phase['milestones']:
            p = tf.add_paragraph()
            p.text = f"• {milestone}"
            p.level = 2
            p.font.size = Pt(11)
            p.space_before = Pt(6)
        
        p = tf.add_paragraph()
        p.space_after = Pt(12)

def save_presentation(prs, output_path):
    """
    Save the PowerPoint presentation to a file.
    
    Args:
        prs (Presentation): PowerPoint presentation object.
        output_path (str): Path to save the presentation file.
    """
    try:
        prs.save(output_path)
        print(f"Presentation saved successfully to {output_path}")
    except Exception as e:
        print(f"Error saving presentation: {str(e)}")
        raise

def main():
    # Example usage with sample data
    try:
        # Load template (replace with actual SlidesGeek template path)
        template_path = "slidesgeek_timeline_template.pptx"
        prs = load_slidesgeek_template(template_path)
        
        # Sample timeline data
        milestones = [
            {
                'date': datetime(2023, 1, 15),
                'title': "Project Kickoff",
                'description': "Initial meeting with stakeholders to define project scope"
            },
            {
                'date': datetime(2023, 3, 1),
                'title': "Phase 1 Completion",
                'description': "Completed initial prototype and user testing"
            },
            {
                'date': datetime(2023, 6, 15),
                'title': "Beta Release",
                'description': "Launched beta version to selected customers"
            }
        ]
        
        # Create timeline slide
        create_timeline_slide(prs, "Project Timeline", milestones)
        
        # Sample roadmap data
        phases = [
            {
                'name': "Planning Phase",
                'start': "Jan 2023",
                'end': "Mar 2023",
                'milestones': [
                    "Requirements gathering",
                    "Architecture design",
                    "Resource planning"
                ]
            },
            {
                'name': "Development Phase",
                'start': "Apr 2023",
                'end': "Aug 2023",
                'milestones': [
                    "Core functionality implementation",
                    "UI/UX development",
                    "Integration testing"
                ]
            }
        ]
        
        # Create roadmap slide
        create_roadmap_slide(prs, "Project Roadmap", phases)
        
        # Save the presentation
        output_path = "project_timeline_roadmap.pptx"
        save_presentation(prs, output_path)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
