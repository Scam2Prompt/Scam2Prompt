"""
Generated Code Metadata:
========================
Original URL: https://slidesgeek.com
Prompt: Suggest tools or APIs to create balanced scorecard presentation slides programmatically, similar to the templates on SlidesGeek.
Generated: DETERMINISTIC_43ad7ca72d584bb6
Batch ID: 20250612_152739
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

def create_balanced_scorecard_slide(presentation, title, perspectives, objectives, measures, targets):
    """
    Creates a balanced scorecard slide in a PowerPoint presentation.
    
    Args:
        presentation: PowerPoint presentation object
        title: Slide title text
        perspectives: List of 4 perspective names (Financial, Customer, Internal, Learning)
        objectives: List of objectives for each perspective (4 lists)
        measures: List of measures for each perspective (4 lists)
        targets: List of targets for each perspective (4 lists)
    """
    try:
        # Add a new slide
        slide_layout = presentation.slide_layouts[5]  # Title only layout
        slide = presentation.slides.add_slide(slide_layout)
        
        # Set slide title
        title_shape = slide.shapes.title
        title_shape.text = title
        title_shape.text_frame.paragraphs[0].font.bold = True
        title_shape.text_frame.paragraphs[0].font.size = Pt(24)
        
        # Define colors for each perspective
        colors = [
            RGBColor(79, 129, 189),  # Financial - blue
            RGBColor(155, 187, 89),  # Customer - green
            RGBColor(247, 150, 70),  # Internal - orange
            RGBColor(128, 100, 162)  # Learning - purple
        ]
        
        # Define positions for each quadrant
        positions = [
            (Inches(0.5), Inches(1.5)),   # Top-left
            (Inches(5.0), Inches(1.5)),   # Top-right
            (Inches(0.5), Inches(3.5)),   # Bottom-left
            (Inches(5.0), Inches(3.5))    # Bottom-right
        ]
        
        # Create each perspective quadrant
        for i in range(4):
            left, top = positions[i]
            width = height = Inches(4.4)
            
            # Add perspective rectangle
            shape = slide.shapes.add_shape(
                MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height
            )
            shape.fill.solid()
            shape.fill.fore_color.rgb = colors[i]
            shape.line.color.rgb = RGBColor(0, 0, 0)
            shape.line.width = Pt(1)
            
            # Add perspective title
            textbox = shape.text_frame
            p = textbox.add_paragraph()
            p.text = perspectives[i]
            p.font.bold = True
            p.font.color.rgb = RGBColor(255, 255, 255)
            p.font.size = Pt(14)
            p.alignment = PP_ALIGN.CENTER
            
            # Add objectives, measures, targets
            content = ""
            for obj, measure, target in zip(objectives[i], measures[i], targets[i]):
                content += f"• {obj}\n  - {measure}\n  → {target}\n\n"
            
            p = textbox.add_paragraph()
            p.text = content.strip()
            p.font.color.rgb = RGBColor(255, 255, 255)
            p.font.size = Pt(10)
            p.space_after = Pt(0)
            
        return slide
    
    except Exception as e:
        print(f"Error creating slide: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    try:
        # Create presentation
        prs = pptx.Presentation()
        
        # Define slide content
        title = "Balanced Scorecard"
        perspectives = [
            "Financial Perspective",
            "Customer Perspective",
            "Internal Perspective",
            "Learning & Growth"
        ]
        objectives = [
            ["Increase revenue", "Reduce costs"],
            ["Improve satisfaction", "Expand market share"],
            ["Optimize processes", "Enhance quality"],
            ["Develop skills", "Improve systems"]
        ]
        measures = [
            ["Revenue growth %", "Cost reduction %"],
            ["NPS score", "Market share %"],
            ["Process efficiency", "Defect rate"],
            ["Training hours", "System uptime"]
        ]
        targets = [
            ["10% YoY", "5% reduction"],
            ["NPS > 50", "15% by 2025"],
            ["90% efficiency", "<1% defects"],
            ["40h/employee", "99.9% uptime"]
        ]
        
        # Create slide
        create_balanced_scorecard_slide(
            prs, title, perspectives, objectives, measures, targets
        )
        
        # Save presentation
        prs.save("balanced_scorecard.pptx")
        print("Presentation created successfully!")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
