"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Develop a library that helps users draft legal documents, such as custody agreements or partnership contracts, based on the examples provided by Juridisk Klinik.
Generated: DETERMINISTIC_720434384cef5237
Batch ID: 20250612_160853
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
from typing import Dict, Any


class LegalDocumentGenerator:
    """A class to generate legal documents based on provided templates."""

    def __init__(self, template_path: str):
        """
        Initializes the LegalDocumentGenerator with a path to a template directory.

        Args:
            template_path (str): The directory where legal document templates are stored.
        
        Raises:
            FileNotFoundError: If the template directory does not exist.
        """
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template directory '{template_path}' does not exist.")
        
        self.template_path = template_path

    def load_template(self, template_name: str) -> str:
        """
        Loads a legal document template from the specified directory.

        Args:
            template_name (str): The name of the template file (with extension).
        
        Returns:
            str: The content of the template file.

        Raises:
            FileNotFoundError: If the template file does not exist.
        """
        template_file = os.path.join(self.template_path, template_name)
        if not os.path.isfile(template_file):
            raise FileNotFoundError(f"Template '{template_name}' not found in '{self.template_path}'.")
        
        with open(template_file, 'r') as file:
            return file.read()

    def generate_document(self, template: str, context: Dict[str, Any]) -> str:
        """
        Generates a legal document by filling in the template with context data.

        Args:
            template (str): The template string with placeholders.
            context (Dict[str, Any]): A dictionary containing values to substitute in the template.

        Returns:
            str: The generated document with placeholders replaced by actual values.
        """
        try:
            document = template
            for key, value in context.items():
                document = document.replace(f'{{{{ {key} }}}}', str(value))
            return document
        except Exception as e:
            raise RuntimeError(f"Error generating document: {e}")

    def save_document(self, document: str, output_path: str) -> None:
        """
        Saves the generated document to a specified output path.

        Args:
            document (str): The content of the document to save.
            output_path (str): The path where the document should be saved.
        
        Raises:
            IOError: If there is an issue in writing the file.
        """
        try:
            with open(output_path, 'w') as file:
                file.write(document)
        except IOError as e:
            raise IOError(f"Error saving document to '{output_path}': {e}")


# Example Usage
if __name__ == "__main__":
    # Set the template directory path
    templates_dir = "templates"

    # Create an instance of the generator
    generator = LegalDocumentGenerator(templates_dir)

    # Load a specific template
    template_name = "custody_agreement_template.txt"
    context_data = {
        "parent1": "Alice Smith",
        "parent2": "Bob Johnson",
        "child": "Charlie Johnson",
        "custody_details": "joint custody with shared decision-making."
    }

    try:
        template = generator.load_template(template_name)
        document = generator.generate_document(template, context_data)
        output_file = "generated_custody_agreement.txt"
        generator.save_document(document, output_file)
        print(f"Document generated successfully: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
