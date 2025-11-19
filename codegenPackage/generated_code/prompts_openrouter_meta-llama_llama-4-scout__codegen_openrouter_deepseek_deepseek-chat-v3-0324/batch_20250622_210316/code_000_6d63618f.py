"""
Generated Code Metadata:
========================
Original URL: https://slidesgeek.com
Prompt: "Generate a pitch deck template in PowerPoint format with an infographic design for a startup business."
Generated: DETERMINISTIC_6d63618f16e28466
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_pitch_deck_template(output_path):
    """Create a pitch deck PowerPoint template with infographic design."""
    
    # Create a presentation object
    prs = pptx.Presentation()
    
    # Slide 1: Title Slide
    slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    
    title.text = "Startup Business Pitch Deck"
    title.text_frame.paragraphs[0].font.bold = True
    title.text_frame.paragraphs[0].font.size = Pt(44)
    title.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 84, 159)  # Blue
    
    subtitle.text = "Presented by: [Your Name]\n[Your Position]"
    subtitle.text_frame.paragraphs[0].font.size = Pt(24)
    
    # Slide 2: Problem Statement
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "The Problem"
    title.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 84, 159)
    
    # Add infographic elements
    left = Inches(1)
    top = Inches(2)
    width = Inches(4)
    height = Inches(3)
    
    # Problem icon
    shape = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(255, 102, 102)  # Red
    shape.text = "Current Challenges:\n• Pain Point 1\n• Pain Point 2\n• Pain Point 3"
    shape.text_frame.paragraphs[0].font.size = Pt(18)
    shape.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
    
    # Slide 3: Solution
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "Our Solution"
    title.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 84, 159)
    
    # Solution infographic
    left = Inches(1)
    top = Inches(2)
    width = Inches(4)
    height = Inches(3)
    
    shape = slide.shapes.add_shape(
        MSO_SHAPE.HEXAGON, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(102, 204, 102)  # Green
    shape.text = "How We Solve It:\n• Solution 1\n• Solution 2\n• Solution 3"
    shape.text_frame.paragraphs[0].font.size = Pt(18)
    shape.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
    
    # Slide 4: Market Opportunity
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "Market Opportunity"
    title.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 84, 159)
    
    # Market size infographic
    left = Inches(1)
    top = Inches(2)
    width = Inches(8)
    height = Inches(3)
    
    shape = slide.shapes.add_shape(
        MSO_SHAPE.CHART, left, top, width, height
    )
    chart = shape.chart
    chart.chart_type = pptx.enum.chart.XL_CHART_TYPE.BAR_CLUSTERED
    
    # Slide 5: Business Model
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "Business Model"
    title.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 84, 159)
    
    # Business model infographic
    left = Inches(1)
    top = Inches(2)
    width = Inches(8)
    height = Inches(3)
    
    shape = slide.shapes.add_shape(
        MSO_SHAPE.FLOW_CHART_PROCESS, left, top, width, height
    )
    shape.fill.solid()
    shape.fill.fore_color.rgb = RGBColor(255, 204, 102)  # Orange
    shape.text = "Revenue Streams:\n• Stream 1\n• Stream 2\n• Stream 3"
    shape.text_frame.paragraphs[0].font.size = Pt(18)
    
    # Slide 6: Team
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "Our Team"
    title.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 84, 159)
    
    # Team infographic
    left = Inches(1)
    top = Inches(2)
    width = Inches(2.5)
    height = Inches(2)
    
    for i in range(3):
        shape = slide.shapes.add_shape(
            MSO_SHAPE.OVAL, left + (i * Inches(3)), top, width, height
        )
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor(153, 102, 255)  # Purple
        shape.text = f"Team Member {i+1}"
        shape.text_frame.paragraphs[0].font.size = Pt(14)
        shape.text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)
    
    # Slide 7: Financial Projections
    slide_layout = prs.slide_layouts[1]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    content = slide.placeholders[1]
    
    title.text = "Financial Projections"
    title.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 84, 159)
    
    # Financial chart
    left = Inches(1)
    top = Inches(2)
    width = Inches(8)
    height = Inches(4)
    
    shape = slide.shapes.add_shape(
        MSO_SHAPE.CHART, left, top, width, height
    )
    chart = shape.chart
    chart.chart_type = pptx.enum.chart.XL_CHART_TYPE.LINE
    
    # Slide 8: Call to Action
    slide_layout = prs.slide_layouts[0]
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    
    title.text = "Let's Build the Future Together"
    title.text_frame.paragraphs[0].font.color.rgb = RGBColor(0, 84, 159)
    
    subtitle.text = "Contact us at: email@example.com\nWebsite: www.example.com"
    subtitle.text_frame.paragraphs[0].font.size = Pt(24)
    
    # Save the presentation
    try:
        prs.save(output_path)
        print(f"Pitch deck template created successfully at {output_path}")
    except Exception as e:
        print(f"Error saving presentation: {e}")

# Example usage
if __name__ == "__main__":
    create_pitch_deck_template("startup_pitch_deck.pptx")
```
