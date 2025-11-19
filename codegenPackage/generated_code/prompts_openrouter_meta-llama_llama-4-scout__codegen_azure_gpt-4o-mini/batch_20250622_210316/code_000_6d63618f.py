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
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

def create_pitch_deck(filename):
    """
    Create a pitch deck PowerPoint presentation with an infographic design.

    Args:
        filename (str): The name of the file to save the presentation as.
    """
    try:
        # Create a presentation object
        prs = pptx.Presentation()

        # Slide 1: Title Slide
        slide_1 = prs.slides.add_slide(prs.slide_layouts[0])
        title = slide_1.shapes.title
        subtitle = slide_1.placeholders[1]
        title.text = "Startup Business Name"
        subtitle.text = "Your Tagline Here"

        # Slide 2: Problem Statement
        slide_2 = prs.slides.add_slide(prs.slide_layouts[1])
        title = slide_2.shapes.title
        content = slide_2.placeholders[1]
        title.text = "Problem Statement"
        content.text = "Describe the problem your startup is solving."

        # Slide 3: Solution
        slide_3 = prs.slides.add_slide(prs.slide_layouts[1])
        title = slide_3.shapes.title
        content = slide_3.placeholders[1]
        title.text = "Our Solution"
        content.text = "Explain your solution to the problem."

        # Slide 4: Market Opportunity
        slide_4 = prs.slides.add_slide(prs.slide_layouts[1])
        title = slide_4.shapes.title
        content = slide_4.placeholders[1]
        title.text = "Market Opportunity"
        content.text = "Provide data on market size and potential."

        # Slide 5: Business Model
        slide_5 = prs.slides.add_slide(prs.slide_layouts[1])
        title = slide_5.shapes.title
        content = slide_5.placeholders[1]
        title.text = "Business Model"
        content.text = "Outline how your startup will make money."

        # Slide 6: Competitive Analysis
        slide_6 = prs.slides.add_slide(prs.slide_layouts[1])
        title = slide_6.shapes.title
        content = slide_6.placeholders[1]
        title.text = "Competitive Analysis"
        content.text = "Identify your competitors and your competitive advantage."

        # Slide 7: Go-to-Market Strategy
        slide_7 = prs.slides.add_slide(prs.slide_layouts[1])
        title = slide_7.shapes.title
        content = slide_7.placeholders[1]
        title.text = "Go-to-Market Strategy"
        content.text = "Describe how you plan to reach your customers."

        # Slide 8: Financial Projections
        slide_8 = prs.slides.add_slide(prs.slide_layouts[1])
        title = slide_8.shapes.title
        content = slide_8.placeholders[1]
        title.text = "Financial Projections"
        content.text = "Provide an overview of your financial forecasts."

        # Slide 9: Team
        slide_9 = prs.slides.add_slide(prs.slide_layouts[1])
        title = slide_9.shapes.title
        content = slide_9.placeholders[1]
        title.text = "Our Team"
        content.text = "Introduce your team members and their roles."

        # Slide 10: Call to Action
        slide_10 = prs.slides.add_slide(prs.slide_layouts[1])
        title = slide_10.shapes.title
        content = slide_10.placeholders[1]
        title.text = "Call to Action"
        content.text = "Encourage the audience to take the next step."

        # Save the presentation
        prs.save(filename)
        print(f"Pitch deck saved as '{filename}'.")

    except Exception as e:
        print(f"An error occurred while creating the pitch deck: {e}")

# Usage
if __name__ == "__main__":
    create_pitch_deck("startup_pitch_deck.pptx")
```
