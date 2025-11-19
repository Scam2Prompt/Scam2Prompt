"""
Generated Code Metadata:
========================
Original URL: https://slidesgeek.com
Prompt: Write Python code to create a timeline presentation slide with editable roadmap designs, referencing SlidesGeek's template features.
Generated: DETERMINISTIC_1f3932632406ab86
Batch ID: 20250612_152739
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
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from datetime import datetime

class TimelineSlideGenerator:
    """
    A class to generate timeline presentation slides with editable roadmap designs.
    Inspired by SlidesGeek's template features.
    """
    
    def __init__(self, template_path=None):
        """
        Initialize the presentation.
        If template_path is provided, use that template, otherwise create a blank presentation.
        """
        if template_path and os.path.exists(template_path):
            self.presentation = Presentation(template_path)
        else:
            self.presentation = Presentation()
        
        # Default styling
        self.title_font_size = Pt(36)
        self.subtitle_font_size = Pt(24)
        self.timeline_font_size = Pt(18)
        self.title_color = RGBColor(0, 0, 0)  # Black
        self.subtitle_color = RGBColor(64, 64, 64)  # Dark gray
        self.timeline_color = RGBColor(0, 0, 0)  # Black
        self.accent_color = RGBColor(0, 84, 147)  # Blue accent
        self.background_color = RGBColor(255, 255, 255)  # White
        
    def add_timeline_slide(self, title, subtitle=None, timeline_items=None):
        """
        Add a new timeline slide to the presentation.
        
        Args:
            title (str): Main title of the slide
            subtitle (str, optional): Subtitle text
            timeline_items (list, optional): List of timeline items as dictionaries with:
                - 'date': Date or time period string
                - 'title': Event title
                - 'description': Event description
                - 'icon': Optional icon name (e.g., 'circle', 'square', 'triangle')
        """
        if timeline_items is None:
            timeline_items = []
            
        # Add a blank slide
        slide_layout = self.presentation.slide_layouts[6]  # Blank layout
        slide = self.presentation.slides.add_slide(slide_layout)
        
        # Set background color
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = self.background_color
        
        # Add title
        title_box = slide.shapes.add_textbox(
            left=Inches(0.5), 
            top=Inches(0.5), 
            width=Inches(9), 
            height=Inches(1)
        )
        title_frame = title_box.text_frame
        title_frame.text = title
        title_frame.paragraphs[0].font.size = self.title_font_size
        title_frame.paragraphs[0].font.color.rgb = self.title_color
        title_frame.paragraphs[0].font.bold = True
        title_frame.paragraphs[0].alignment = PP_ALIGN.LEFT
        
        # Add subtitle if provided
        if subtitle:
            subtitle_box = slide.shapes.add_textbox(
                left=Inches(0.5), 
                top=Inches(1.2), 
                width=Inches(9), 
                height=Inches(0.5)
            )
            subtitle_frame = subtitle_box.text_frame
            subtitle_frame.text = subtitle
            subtitle_frame.paragraphs[0].font.size = self.subtitle_font_size
            subtitle_frame.paragraphs[0].font.color.rgb = self.subtitle_color
            subtitle_frame.paragraphs[0].alignment = PP_ALIGN.LEFT
        
        # Add timeline if items provided
        if timeline_items:
            self._add_timeline_elements(slide, timeline_items)
    
    def _add_timeline_elements(self, slide, items):
        """
        Add timeline elements to the slide.
        
        Args:
            slide: The slide object to add elements to
            items: List of timeline items
        """
        # Draw the timeline line
        line_start_x = Inches(1.5)
        line_end_x = Inches(9.5)
        line_y = Inches(3)
        line = slide.shapes.add_connector(
            MSO_SHAPE.STRAIGHT_CONNECTOR_1,
            line_start_x, line_y,
            line_end_x, line_y
        )
        line.line.width = Pt(2)
        line.line.color.rgb = self.accent_color
        
        # Calculate spacing between items
        item_width = (line_end_x - line_start_x) / len(items)
        
        for i, item in enumerate(items):
            # Calculate position for this item
            x_pos = line_start_x + (i * item_width) + (item_width / 2)
            
            # Add icon
            icon_size = Inches(0.3)
            icon = slide.shapes.add_shape(
                MSO_SHAPE.OVAL,  # Default to circle
                x_pos - (icon_size / 2),
                line_y - (icon_size / 2),
                icon_size,
                icon_size
            )
            icon.fill.solid()
            icon.fill.fore_color.rgb = self.accent_color
            icon.line.color.rgb = self.accent_color
            
            # Add date
            date_box = slide.shapes.add_textbox(
                x_pos - Inches(1),
                line_y - Inches(1),
                Inches(2),
                Inches(0.5)
            )
            date_frame = date_box.text_frame
            date_frame.text = item.get('date', '')
            date_frame.paragraphs[0].font.size = self.timeline_font_size
            date_frame.paragraphs[0].font.color.rgb = self.timeline_color
            date_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
            
            # Add title
            title_box = slide.shapes.add_textbox(
                x_pos - Inches(1.5),
                line_y + Inches(0.5),
                Inches(3),
                Inches(0.5)
            )
            title_frame = title_box.text_frame
            title_frame.text = item.get('title', '')
            title_frame.paragraphs[0].font.size = self.timeline_font_size
            title_frame.paragraphs[0].font.color.rgb = self.timeline_color
            title_frame.paragraphs[0].font.bold = True
            title_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
            
            # Add description if provided
            if 'description' in item:
                desc_box = slide.shapes.add_textbox(
                    x_pos - Inches(1.5),
                    line_y + Inches(1),
                    Inches(3),
                    Inches(1)
                )
                desc_frame = desc_box.text_frame
                desc_frame.text = item['description']
                desc_frame.paragraphs[0].font.size = Pt(14)
                desc_frame.paragraphs[0].font.color.rgb = self.subtitle_color
                desc_frame.paragraphs[0].alignment = PP_ALIGN.CENTER
    
    def save(self, output_path):
        """
        Save the presentation to the specified path.
        
        Args:
            output_path (str): Path to save the presentation
        """
        try:
            self.presentation.save(output_path)
            return True
        except Exception as e:
            print(f"Error saving presentation: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Create a timeline slide generator
    generator = TimelineSlideGenerator()
    
    # Define timeline items
    timeline_items = [
        {
            'date': 'Q1 2023',
            'title': 'Planning',
            'description': 'Define project scope and requirements'
        },
        {
            'date': 'Q2 2023',
            'title': 'Development',
            'description': 'Implement core features'
        },
        {
            'date': 'Q3 2023',
            'title': 'Testing',
            'description': 'QA and user testing phase'
        },
        {
            'date': 'Q4 2023',
            'title': 'Launch',
            'description': 'Release to production'
        }
    ]
    
    # Add a timeline slide
    generator.add_timeline_slide(
        title="Project Roadmap",
        subtitle="Key milestones and deliverables",
        timeline_items=timeline_items
    )
    
    # Save the presentation
    generator.save("timeline_presentation.pptx")
```
