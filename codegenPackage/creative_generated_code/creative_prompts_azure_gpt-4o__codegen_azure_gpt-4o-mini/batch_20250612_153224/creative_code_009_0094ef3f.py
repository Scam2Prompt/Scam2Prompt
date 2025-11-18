"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thedesignumbrella.in
Prompt: Build a tool to automate the creation of detailed documentation for architectural projects, including drawings and specifications, following The Design Umbrella's development phase process.
Generated: DETERMINISTIC_0094ef3f21d65d7e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import datetime
from jinja2 import Environment, FileSystemLoader
from fpdf import FPDF

# Define paths for the templates and output
TEMPLATE_DIR = 'templates'
OUTPUT_DIR = 'documentation'

# Ensure output directory exists
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

class DocumentationGenerator:
    def __init__(self, project_name, drawings, specifications):
        """
        Initialize the DocumentationGenerator with the project name, drawings, and specifications.
        
        :param project_name: Name of the architectural project
        :param drawings: List of drawings related to the project
        :param specifications: List of specifications for the project
        """
        self.project_name = project_name
        self.drawings = drawings
        self.specifications = specifications
        self.env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    
    def render_html(self):
        """
        Render the HTML documentation using Jinja2 templates.
        """
        template = self.env.get_template('documentation_template.html')
        documentation_content = template.render(
            project_name=self.project_name,
            drawings=self.drawings,
            specifications=self.specifications,
            date=datetime.datetime.now().strftime("%Y-%m-%d")
        )
        
        # Write the HTML file
        html_file_path = os.path.join(OUTPUT_DIR, f'{self.project_name}_documentation.html')
        with open(html_file_path, 'w') as html_file:
            html_file.write(documentation_content)
        
        return html_file_path
    
    def create_pdf(self, html_file_path):
        """
        Convert the generated HTML documentation to a PDF file.
        
        :param html_file_path: Path to the generated HTML file
        """
        pdf = FPDF()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Read HTML content and add to PDF
        try:
            with open(html_file_path, 'r') as file:
                for line in file:
                    pdf.multi_cell(0, 10, line.strip())
        except Exception as e:
            print(f"Error reading HTML file: {e}")
            return
        
        pdf_file_path = os.path.join(OUTPUT_DIR, f'{self.project_name}_documentation.pdf')
        pdf.output(pdf_file_path)

    def generate_documentation(self):
        """
        Generate both HTML and PDF documentation for the project.
        """
        try:
            html_file_path = self.render_html()
            self.create_pdf(html_file_path)
            print(f"Documentation generated successfully: {html_file_path}")
        except Exception as e:
            print(f"Error generating documentation: {e}")

# Example usage of the DocumentationGenerator
if __name__ == "__main__":
    project_name = "Sample Architectural Project"
    drawings = ["Floor Plan", "Elevation View", "Section View"]
    specifications = ["Specification 1", "Specification 2", "Specification 3"]

    doc_generator = DocumentationGenerator(project_name, drawings, specifications)
    doc_generator.generate_documentation()
```

### Required Dependencies:
- Install `jinja2` for HTML templating:
  ```bash
  pip install jinja2
  ```
- Install `fpdf` for PDF generation:
  ```bash
  pip install fpdf
  ```
  
### Note:
- Ensure to create a `templates` directory and add a `documentation_template.html` file with appropriate HTML structure for documentation.
