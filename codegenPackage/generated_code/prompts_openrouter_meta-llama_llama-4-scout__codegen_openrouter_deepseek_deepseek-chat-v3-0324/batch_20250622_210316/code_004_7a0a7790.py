"""
Generated Code Metadata:
========================
Original URL: https://slidesgeek.com
Prompt: "Design an organizational chart PPT template with a balanced scorecard and relationship diagrams for a business presentation."
Generated: DETERMINISTIC_7a0a7790b8ff34a9
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

def create_org_chart_template(output_file):
    """Create a PowerPoint template with organizational chart, balanced scorecard, and relationship diagrams."""
    
    # Create a presentation object
    prs = Presentation()
    
    # Slide layouts
    title_slide_layout = prs.slide_layouts[0]
    content_slide_layout = prs.slide_layouts[1]
    blank_slide_layout = prs.slide_layouts[6]
    
    # Add title slide
    slide = prs.slides.add_slide(title_slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = "Organizational Chart Template"
    subtitle.text = "With Balanced Scorecard & Relationship Diagrams"
    
    # Add organizational chart slide
    slide = prs.slides.add_slide(content_slide_layout)
    title = slide.shapes.title
    title.text = "Organizational Structure"
    
    # Add org chart shapes
    left = Inches(1)
    top = Inches(2)
    width = Inches(2)
    height = Inches(1)
    
    # CEO box
    ceo = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left + width, top, width, height)
    ceo.text = "CEO"
    ceo.fill.solid()
    ceo.fill.fore_color.rgb = RGBColor(0, 112, 192)
    ceo.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
    ceo.text_frame.paragraphs[0].font.bold = True
    
    # Department boxes
    departments = ["Finance", "Operations", "Marketing", "HR"]
    for i, dept in enumerate(departments):
        box = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left + (i * width), top + height + Inches(0.5), width, height)
        box.text = dept
        box.fill.solid()
        box.fill.fore_color.rgb = RGBColor(155, 194, 230)
        
        # Add connector
        connector = slide.shapes.add_connector(
            MSO_SHAPE.STRAIGHT_CONNECTOR_1,
            ceo.left + (ceo.width/2),
            ceo.top + ceo.height,
            box.left + (box.width/2),
            box.top
        )
    
    # Add balanced scorecard slide
    slide = prs.slides.add_slide(content_slide_layout)
    title = slide.shapes.title
    title.text = "Balanced Scorecard"
    
    # Create scorecard table
    rows = 5
    cols = 4
    left = Inches(1)
    top = Inches(2)
    width = Inches(8)
    height = Inches(4)
    
    table = slide.shapes.add_table(rows, cols, left, top, width, height).table
    
    # Set column widths
    for col in range(cols):
        table.columns[col].width = Inches(2)
    
    # Header row
    headers = ["Perspective", "Objectives", "Measures", "Targets"]
    for i, header in enumerate(headers):
        cell = table.cell(0, i)
        cell.text = header
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(0, 112, 192)
        cell.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
        cell.text_frame.paragraphs[0].font.bold = True
    
    # Perspective names
    perspectives = ["Financial", "Customer", "Internal Process", "Learning & Growth"]
    for i, perspective in enumerate(perspectives):
        cell = table.cell(i+1, 0)
        cell.text = perspective
        cell.fill.solid()
        cell.fill.fore_color.rgb = RGBColor(155, 194, 230)
    
    # Add relationship diagram slide
    slide = prs.slides.add_slide(blank_slide_layout)
    title = slide.shapes.add_textbox(Inches(1), Inches(0.5), Inches(8), Inches(1))
    title.text = "Relationship Diagram"
    title.text_frame.paragraphs[0].font.size = Pt(32)
    title.text_frame.paragraphs[0].font.bold = True
    
    # Add central circle
    center_x = Inches(5)
    center_y = Inches(3.5)
    radius = Inches(1.5)
    
    center = slide.shapes.add_shape(
        MSO_SHAPE.OVAL,
        center_x - radius,
        center_y - radius,
        radius * 2,
        radius * 2
    )
    center.text = "Core Business"
    center.fill.solid()
    center.fill.fore_color.rgb = RGBColor(0, 112, 192)
    center.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
    center.text_frame.paragraphs[0].font.bold = True
    
    # Add surrounding elements
    elements = ["Suppliers", "Customers", "Partners", "Competitors", "Regulators"]
    angles = [0, 72, 144, 216, 288]  # 72 degrees apart
    
    for i, (element, angle) in enumerate(zip(elements, angles)):
        # Calculate position
        rad = angle * (3.14159 / 180)
        x = center_x + Inches(2.5) * math.cos(rad)
        y = center_y + Inches(2.5) * math.sin(rad)
        
        # Add shape
        elem = slide.shapes.add_shape(
            MSO_SHAPE.ROUNDED_RECTANGLE,
            x - Inches(1),
            y - Inches(0.5),
            Inches(2),
            Inches(1)
        )
        elem.text = element
        elem.fill.solid()
        elem.fill.fore_color.rgb = RGBColor(155, 194, 230)
        
        # Add connector
        connector = slide.shapes.add_connector(
            MSO_SHAPE.CURVED_CONNECTOR_2,
            center_x,
            center_y,
            x,
            y
        )
    
    # Save the presentation
    prs.save(output_file)

# Example usage
if __name__ == "__main__":
    import math
    create_org_chart_template("organizational_chart_template.pptx")
```
