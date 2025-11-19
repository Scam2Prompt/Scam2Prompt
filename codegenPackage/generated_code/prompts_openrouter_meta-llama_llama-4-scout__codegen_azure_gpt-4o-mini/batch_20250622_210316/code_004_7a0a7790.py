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
import pptx
from pptx.util import Inches
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.shapes import MSO_SHAPE_TYPE

def create_presentation():
    """Create a PowerPoint presentation with an organizational chart and balanced scorecard."""
    # Create a presentation object
    prs = pptx.Presentation()

    # Add a title slide
    slide_layout = prs.slide_layouts[0]  # 0 is the layout for title slide
    slide = prs.slides.add_slide(slide_layout)
    title = slide.shapes.title
    subtitle = slide.placeholders[1]
    title.text = "Organizational Chart & Balanced Scorecard"
    subtitle.text = "Business Presentation"

    # Add a slide for the organizational chart
    add_organizational_chart_slide(prs)

    # Add a slide for the balanced scorecard
    add_balanced_scorecard_slide(prs)

    # Save the presentation
    prs.save('organizational_chart_and_balanced_scorecard.pptx')

def add_organizational_chart_slide(prs):
    """Add a slide containing an organizational chart."""
    slide_layout = prs.slide_layouts[5]  # 5 is a blank layout
    slide = prs.slides.add_slide(slide_layout)

    # Add a title for the organizational chart
    title = slide.shapes.title
    title.text = "Organizational Chart"

    # Create a simple organizational chart using shapes
    # Define positions for the chart
    positions = [
        ("CEO", 0.5, 0.1),
        ("Manager 1", 0.2, 0.3),
        ("Manager 2", 0.8, 0.3),
        ("Employee 1", 0.1, 0.5),
        ("Employee 2", 0.3, 0.5),
        ("Employee 3", 0.7, 0.5),
        ("Employee 4", 0.9, 0.5),
    ]

    # Create shapes for each position
    for position in positions:
        add_shape(slide, position[0], position[1], position[2])

def add_shape(slide, text, x, y):
    """Add a shape to the slide."""
    left = Inches(x)
    top = Inches(y)
    width = Inches(1.5)
    height = Inches(0.5)
    
    # Create a rounded rectangle shape
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.text = text

def add_balanced_scorecard_slide(prs):
    """Add a slide containing a balanced scorecard."""
    slide_layout = prs.slide_layouts[5]  # 5 is a blank layout
    slide = prs.slides.add_slide(slide_layout)

    # Add a title for the balanced scorecard
    title = slide.shapes.title
    title.text = "Balanced Scorecard"

    # Define the categories of the balanced scorecard
    categories = ["Financial", "Customer", "Internal Processes", "Learning & Growth"]
    metrics = [
        "Revenue Growth\nProfit Margin",
        "Customer Satisfaction\nMarket Share",
        "Process Efficiency\nQuality Control",
        "Employee Training\nInnovation Rate"
    ]

    # Create a table for the balanced scorecard
    rows, cols = len(categories) + 1, 2
    left = Inches(1)
    top = Inches(1.5)
    width = Inches(8)
    height = Inches(2)

    table = slide.shapes.add_table(rows, cols, left, top, width, height).table

    # Set column widths
    table.columns[0].width = Inches(4)
    table.columns[1].width = Inches(4)

    # Set the header row
    table.cell(0, 0).text = "Perspective"
    table.cell(0, 1).text = "Metrics"

    # Fill in the table with categories and metrics
    for i, category in enumerate(categories):
        table.cell(i + 1, 0).text = category
        table.cell(i + 1, 1).text = metrics[i]

if __name__ == "__main__":
    try:
        create_presentation()
        print("Presentation created successfully: 'organizational_chart_and_balanced_scorecard.pptx'")
    except Exception as e:
        print(f"An error occurred: {e}")
```
