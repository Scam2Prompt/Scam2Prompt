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
from pptx import Presentation
from pptx.util import Inches
from pptx.enum.shapes import MSO_SHAPE
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor

def create_infographic_presentation(output_file):
    # Create a new PowerPoint presentation
    presentation = Presentation()

    # Add a slide with a title layout
    slide = presentation.slides.add_slide(presentation.slide_layouts[5])

    # Add a title to the slide
    title = slide.shapes.title
    title.text = "IT Presentation Infographic"

    # Add a circular design
    left = Inches(3)
    top = Inches(1.5)
    width = Inches(3)
    height = Inches(3)
    circle = slide.shapes.add_shape(MSO_SHAPE.OVAL, left, top, width, height)
    circle.fill.solid()
    circle.fill.fore_color.rgb = RGBColor(0, 102, 204)  # Blue color
    circle.line.color.rgb = RGBColor(255, 255, 255)  # White border
    circle.line.width = Inches(0.05)

    # Add text inside the circle
    text_box = slide.shapes.add_textbox(left + Inches(0.5), top + Inches(1), Inches(2), Inches(1))
    text_frame = text_box.text_frame
    text_frame.text = "Circular Design"
    text_frame.paragraphs[0].font.size = Pt(18)
    text_frame.paragraphs[0].font.bold = True
    text_frame.paragraphs[0].font.color.rgb = RGBColor(255, 255, 255)

    # Add a country map image
    map_left = Inches(0.5)
    map_top = Inches(4)
    map_width = Inches(4)
    map_height = Inches(3)
    slide.shapes.add_picture("country_map.png", map_left, map_top, map_width, map_height)

    # Add a chart
    chart_left = Inches(5)
    chart_top = Inches(4)
    chart_width = Inches(4)
    chart_height = Inches(3)
    chart_data = CategoryChartData()
    chart_data.categories = ['Category 1', 'Category 2', 'Category 3']
    chart_data.add_series('Series 1', (10, 20, 30))
    chart = slide.shapes.add_chart(
        MSO_SHAPE.PIE, chart_left, chart_top, chart_width, chart_height, chart_data
    ).chart

    # Save the presentation
    try:
        presentation.save(output_file)
        print(f"Presentation saved successfully as {output_file}")
    except Exception as e:
        print(f"Error saving presentation: {e}")

# Usage
create_infographic_presentation("IT_Infographic.pptx")
```

**Note:** Ensure you have the `python-pptx` library installed (`pip install python-pptx`) and replace `"country_map.png"` with the path to an actual image file of a country map.
