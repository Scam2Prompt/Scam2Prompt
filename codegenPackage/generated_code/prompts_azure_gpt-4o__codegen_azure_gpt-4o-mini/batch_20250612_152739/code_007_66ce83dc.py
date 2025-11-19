"""
Generated Code Metadata:
========================
Original URL: https://slidesgeek.com
Prompt: Generate a script to create team/organization charts in PowerPoint using templates similar to those provided by SlidesGeek.
Generated: DETERMINISTIC_66ce83dc6660427f
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
import pptx
from pptx.util import Inches
from pptx.enum.shapes import MSO_SHAPE

class OrganizationChart:
    def __init__(self, title, data, template_path=None):
        """
        Initializes the OrganizationChart with a title, data, and optional template path.

        :param title: Title of the organization chart
        :param data: Dictionary containing team member names and their respective roles
        :param template_path: Optional path to a PowerPoint template file
        """
        self.title = title
        self.data = data
        self.template_path = template_path
        self.presentation = pptx.Presentation(template_path) if template_path else pptx.Presentation()

    def add_slide(self):
        """
        Adds a new slide to the presentation with a title and content layout.
        """
        slide_layout = self.presentation.slide_layouts[5]  # Using a blank slide layout
        self.slide = self.presentation.slides.add_slide(slide_layout)
        title_box = self.slide.shapes.title
        title_box.text = self.title

    def create_chart(self):
        """
        Creates an organization chart based on the provided data.
        """
        self.add_slide()
        left = Inches(1)
        top = Inches(1.5)
        width = Inches(8)
        height = Inches(5)

        # Create a SmartArt shape for the organization chart
        org_chart = self.slide.shapes.add_shape(MSO_SHAPE.ORG_CHART, left, top, width, height)

        # Populate the organization chart with data
        for name, role in self.data.items():
            self.add_member(org_chart, name, role)

    def add_member(self, org_chart, name, role):
        """
        Adds a member to the organization chart.

        :param org_chart: The organization chart shape
        :param name: Name of the team member
        :param role: Role of the team member
        """
        try:
            # Create a new shape for the member
            member_shape = org_chart.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(2), Inches(1))
            member_shape.text = f"{name}\n{role}"
            member_shape.fill.solid()
            member_shape.fill.fore_color.rgb = pptx.dml.color.RGBColor(255, 255, 255)  # White background
            member_shape.line.color.rgb = pptx.dml.color.RGBColor(0, 0, 0)  # Black border
        except Exception as e:
            print(f"Error adding member '{name}': {e}")

    def save(self, output_path):
        """
        Saves the presentation to the specified output path.

        :param output_path: Path where the PowerPoint file will be saved
        """
        try:
            self.presentation.save(output_path)
            print(f"Presentation saved successfully to {output_path}")
        except Exception as e:
            print(f"Error saving presentation: {e}")

if __name__ == "__main__":
    # Example usage
    team_data = {
        "Alice Smith": "CEO",
        "Bob Johnson": "CTO",
        "Charlie Brown": "CFO",
        "Diana Prince": "CMO"
    }

    org_chart = OrganizationChart("Company Organization Chart", team_data)
    org_chart.create_chart()
    org_chart.save("organization_chart.pptx")
```
