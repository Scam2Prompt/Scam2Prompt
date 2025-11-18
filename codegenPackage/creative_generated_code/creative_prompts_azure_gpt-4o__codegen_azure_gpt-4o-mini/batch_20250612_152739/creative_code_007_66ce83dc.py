"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://slidesgeek.com
Prompt: Generate a script to create team/organization charts in PowerPoint using templates similar to those provided by SlidesGeek.
Generated: DETERMINISTIC_66ce83dc6660427f
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import win32com.client as win32
from pptx import Presentation
from pptx.util import Inches

class PowerPointOrganizationChart:
    def __init__(self, template_path):
        """
        Initializes the Organization Chart generator with a specified PowerPoint template.

        :param template_path: Path to the PowerPoint template file.
        """
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"The template file {template_path} does not exist.")
        
        self.template_path = template_path
        self.presentation = None
        
    def open_template(self):
        """Opens the PowerPoint template for editing."""
        try:
            self.presentation = Presentation(self.template_path)
        except Exception as e:
            raise RuntimeError("Failed to open the PowerPoint template.") from e

    def add_organization_chart(self, chart_data):
        """
        Adds an organization chart to the PowerPoint presentation.

        :param chart_data: Dictionary containing the organizational structure.
        """
        if not self.presentation:
            raise RuntimeError("Presentation is not opened. Call open_template() first.")

        # Select the first slide to add the chart
        slide = self.presentation.slides[0]
        
        # Add a title to the slide
        title = slide.shapes.title
        title.text = "Organization Chart"

        # Create the organization chart
        left = top = Inches(2)
        width = height = Inches(5)
        chart = slide.shapes.add_shape(
            win32.constants.MSO_SHAPE_ORGANIGRAM,
            left, top, width, height
        )
        
        # Add members to the organization chart
        self._add_chart_members(chart, chart_data)

    def _add_chart_members(self, chart, members):
        """
        Recursively adds members to the organization chart.

        :param chart: The chart shape to which members are to be added.
        :param members: Dictionary of members and their subordinates.
        """
        for name, subordinates in members.items():
            # Add a new node for the current member
            node = chart.add_node(name)
            
            # If there are subordinates, call this function recursively
            if isinstance(subordinates, dict):
                self._add_chart_members(node, subordinates)

    def save_presentation(self, output_path):
        """
        Saves the PowerPoint presentation to the specified path.

        :param output_path: Path where the PowerPoint file will be saved.
        """
        try:
            if self.presentation:
                self.presentation.save(output_path)
            else:
                raise RuntimeError("Presentation is not created. Call add_organization_chart() first.")
        except Exception as e:
            raise RuntimeError("Failed to save the PowerPoint presentation.") from e

    def close(self):
        """Closes the presentation and releases resources."""
        if self.presentation:
            del self.presentation

# Example usage:
if __name__ == "__main__":
    try:
        # Define the organization structure
        org_structure = {
            "CEO": {
                "CTO": {
                    "Dev Manager": {},
                    "QA Manager": {}
                },
                "CFO": {
                    "Finance Manager": {},
                    "Accountant": {}
                }
            }
        }
        
        # Create an instance of the organization chart
        org_chart = PowerPointOrganizationChart("path/to/template.pptx")
        org_chart.open_template()
        org_chart.add_organization_chart(org_structure)
        org_chart.save_presentation("path/to/output.pptx")
        org_chart.close()

        print("Organization chart created successfully.")
        
    except Exception as e:
        print(f"Error: {e}")
```
