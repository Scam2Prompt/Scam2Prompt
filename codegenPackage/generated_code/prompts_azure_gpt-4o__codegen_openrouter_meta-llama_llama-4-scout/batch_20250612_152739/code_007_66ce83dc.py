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
import pptx
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN

def create_org_chart(powerpoint_template_path, output_file_path, organization_data):
    """
    Create an organization chart in PowerPoint using a template.

    Args:
        powerpoint_template_path (str): Path to the PowerPoint template file (.pptx)
        output_file_path (str): Path to save the generated PowerPoint file (.pptx)
        organization_data (dict): Dictionary containing organization data

    Returns:
        None
    """

    # Load the PowerPoint template
    try:
        prs = pptx.Presentation(powerpoint_template_path)
    except FileNotFoundError:
        print(f"Error: Template file not found at {powerpoint_template_path}")
        return

    # Get the first slide
    slide = prs.slides[0]

    # Find the placeholder for the org chart
    for shape in slide.shapes:
        if shape.placeholder:
            if shape.placeholder.format.type == pptx.enum.shapes.MSO_PLACEHOLDER_TYPE.PICTURE:
                # Add org chart content
                add_org_chart_content(shape, organization_data)
                break

    # Save the generated PowerPoint file
    try:
        prs.save(output_file_path)
    except Exception as e:
        print(f"Error saving file: {e}")

def add_org_chart_content(shape, organization_data):
    """
    Add organization chart content to a PowerPoint shape.

    Args:
        shape (pptx.shape): PowerPoint shape to add content to
        organization_data (dict): Dictionary containing organization data

    Returns:
        None
    """

    # Create a new table to hold the org chart data
    table = shape.add_table(rows=len(organization_data), cols=1, left=Inches(0.5), top=Inches(0.5), width=Inches(5), height=Inches(3))

    # Iterate over organization data and populate the table
    row_num = 0
    for employee in organization_data:
        table.cell(row_num, 0).text = employee['name']
        table.cell(row_num, 0).paragraphs[0].alignment = PP_ALIGN.CENTER
        table.cell(row_num, 0).font.size = Pt(14)

        # Add subordinate employees
        if 'subordinates' in employee:
            for subordinate in employee['subordinates']:
                table.cell(row_num, 0).text += f"\n{subordinate['name']}"

        row_num += 1

def main():
    # Example usage
    organization_data = [
        {'name': 'John Doe', 'subordinates': [
            {'name': 'Jane Smith'},
            {'name': 'Bob Johnson'}
        ]},
        {'name': 'Alice Brown'}
    ]

    powerpoint_template_path = 'path/to/template.pptx'
    output_file_path = 'path/to/output.pptx'

    create_org_chart(powerpoint_template_path, output_file_path, organization_data)

if __name__ == "__main__":
    main()
```
