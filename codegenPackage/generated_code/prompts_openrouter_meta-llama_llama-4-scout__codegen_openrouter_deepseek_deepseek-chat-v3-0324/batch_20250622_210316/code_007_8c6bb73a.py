"""
Generated Code Metadata:
========================
Original URL: https://slidesgeek.com
Prompt: "Create a circular design infographic template in PowerPoint format for an IT presentation with a country map and charts."
Generated: DETERMINISTIC_8c6bb73add702560
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
from pptx.chart.data import ChartData
from pptx.enum.chart import XL_CHART_TYPE
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN

def create_circular_infographic(output_path):
    """Create a PowerPoint presentation with a circular infographic design."""
    
    try:
        # Create a presentation object
        prs = pptx.Presentation()
        
        # Add a blank slide
        slide_layout = prs.slide_layouts[6]  # Blank slide layout
        slide = prs.slides.add_slide(slide_layout)
        
        # Set slide dimensions (16:9 aspect ratio)
        prs.slide_width = Inches(13.333)
        prs.slide_height = Inches(7.5)
        
        # Add background color
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(18, 34, 56)  # Dark blue
        
        # Add title
        title = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(12), Inches(1))
        title_frame = title.text_frame
        title_para = title_frame.add_paragraph()
        title_para.text = "IT Infrastructure Overview"
        title_para.font.size = Pt(36)
        title_para.font.color.rgb = RGBColor(255, 255, 255)  # White
        title_para.font.bold = True
        title_para.alignment = PP_ALIGN.LEFT
        
        # Create circular design elements
        center_x = prs.slide_width / 2
        center_y = prs.slide_height / 2
        radius = Inches(2.5)
        
        # Add outer circle
        outer_circle = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            center_x - radius, center_y - radius,
            radius * 2, radius * 2
        )
        outer_circle.fill.solid()
        outer_circle.fill.fore_color.rgb = RGBColor(0, 112, 192)  # Blue
        outer_circle.line.color.rgb = RGBColor(255, 255, 255)  # White
        outer_circle.line.width = Pt(2)
        
        # Add inner circle
        inner_radius = Inches(1.5)
        inner_circle = slide.shapes.add_shape(
            MSO_SHAPE.OVAL,
            center_x - inner_radius, center_y - inner_radius,
            inner_radius * 2, inner_radius * 2
        )
        inner_circle.fill.solid()
        inner_circle.fill.fore_color.rgb = RGBColor(31, 73, 125)  # Darker blue
        inner_circle.line.color.rgb = RGBColor(255, 255, 255)  # White
        inner_circle.line.width = Pt(2)
        
        # Add country map placeholder (would be replaced with actual map image)
        map_width = Inches(3)
        map_left = center_x - (map_width / 2)
        map_top = center_y - (map_width / 2)
        map_placeholder = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE,
            map_left, map_top,
            map_width, map_width
        )
        map_placeholder.fill.solid()
        map_placeholder.fill.fore_color.rgb = RGBColor(200, 200, 200)  # Light gray
        map_placeholder.line.color.rgb = RGBColor(150, 150, 150)  # Gray
        map_placeholder.line.width = Pt(1)
        
        # Add text to map placeholder
        map_text = map_placeholder.text_frame
        map_para = map_text.add_paragraph()
        map_para.text = "Country Map"
        map_para.font.size = Pt(14)
        map_para.font.color.rgb = RGBColor(0, 0, 0)  # Black
        map_para.alignment = PP_ALIGN.CENTER
        
        # Add data points around the circle
        data_points = [
            ("Servers", 85),
            ("Network", 92),
            ("Storage", 78),
            ("Security", 88),
            ("Cloud", 95)
        ]
        
        angle_step = 360 / len(data_points)
        current_angle = 0
        point_radius = Inches(0.5)
        
        for label, value in data_points:
            # Calculate position
            rad_angle = current_angle * (3.14159 / 180)
            x = center_x + (radius * 1.3) * math.cos(rad_angle)
            y = center_y + (radius * 1.3) * math.sin(rad_angle)
            
            # Add data point circle
            point = slide.shapes.add_shape(
                MSO_SHAPE.OVAL,
                x - point_radius, y - point_radius,
                point_radius * 2, point_radius * 2
            )
            point.fill.solid()
            point.fill.fore_color.rgb = RGBColor(255, 192, 0)  # Yellow
            point.line.color.rgb = RGBColor(255, 255, 255)  # White
            point.line.width = Pt(1.5)
            
            # Add value text
            value_text = point.text_frame
            value_para = value_text.add_paragraph()
            value_para.text = f"{value}%"
            value_para.font.size = Pt(14)
            value_para.font.color.rgb = RGBColor(0, 0, 0)  # Black
            value_para.alignment = PP_ALIGN.CENTER
            
            # Add label textbox
            label_left = x - Inches(1)
            label_top = y + point_radius
            label_box = slide.shapes.add_textbox(label_left, label_top, Inches(2), Inches(0.5))
            label_frame = label_box.text_frame
            label_para = label_frame.add_paragraph()
            label_para.text = label
            label_para.font.size = Pt(12)
            label_para.font.color.rgb = RGBColor(255, 255, 255)  # White
            label_para.alignment = PP_ALIGN.CENTER
            
            current_angle += angle_step
        
        # Add a pie chart
        chart_data = ChartData()
        chart_data.categories = ['Windows', 'Linux', 'MacOS', 'Other']
        chart_data.add_series('OS Distribution', [45, 40, 10, 5])
        
        chart_left = Inches(1)
        chart_top = Inches(4)
        chart_width = Inches(4)
        chart_height = Inches(3)
        
        chart = slide.shapes.add_chart(
            XL_CHART_TYPE.PIE, chart_left, chart_top, chart_width, chart_height, chart_data
        ).chart
        
        # Format chart
        chart.has_legend = True
        chart.legend.position = 'right'
        chart.plots[0].has_data_labels = True
        
        # Save the presentation
        prs.save(output_path)
        
    except Exception as e:
        print(f"Error creating PowerPoint: {str(e)}")
        raise

# Example usage
if __name__ == "__main__":
    import math
    create_circular_infographic("IT_Infographic_Template.pptx")
```
