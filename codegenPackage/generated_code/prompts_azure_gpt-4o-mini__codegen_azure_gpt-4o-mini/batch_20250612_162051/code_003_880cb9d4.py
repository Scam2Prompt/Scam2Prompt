"""
Generated Code Metadata:
========================
Original URL: https://www.caag.com.br
Prompt: Develop a library function that assists in generating customized legal documents, referencing the diverse areas of law mentioned by the Complexo de Advocacia.
Generated: DETERMINISTIC_880cb9d495ba0b03
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from jinja2 import Environment, FileSystemLoader, Template
from typing import Dict, Any

class LegalDocumentGenerator:
    """
    A class to generate customized legal documents based on templates.
    """

    def __init__(self, template_dir: str):
        """
        Initializes the LegalDocumentGenerator with the specified template directory.

        :param template_dir: Directory where the document templates are stored.
        """
        if not os.path.exists(template_dir):
            raise ValueError(f"Template directory '{template_dir}' does not exist.")
        
        self.template_dir = template_dir
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def generate_document(self, template_name: str, context: Dict[str, Any]) -> str:
        """
        Generates a legal document from a specified template and context.

        :param template_name: The name of the template file to use (e.g., 'contract_template.txt').
        :param context: A dictionary containing the variables to be replaced in the template.
        :return: The rendered document as a string.
        """
        try:
            template = self.env.get_template(template_name)
            document = template.render(context)
            return document
        except Exception as e:
            raise RuntimeError(f"Error generating document: {e}")

# Example usage:
if __name__ == "__main__":
    # Define the path to the templates directory
    templates_path = "path/to/legal/templates"

    # Create an instance of the LegalDocumentGenerator
    generator = LegalDocumentGenerator(templates_path)

    # Define the context for the document
    context = {
        'client_name': 'John Doe',
        'contract_date': '2023-10-01',
        'services': 'Legal Consultation',
        'fee': '500.00'
    }

    # Generate the document
    try:
        document = generator.generate_document('contract_template.txt', context)
        print(document)
    except RuntimeError as e:
        print(e)
```

**Note:** Ensure that you have the `jinja2` library installed in your environment. You can install it using `pip install jinja2`. Also, create a directory with the appropriate legal document templates for this code to function correctly.
