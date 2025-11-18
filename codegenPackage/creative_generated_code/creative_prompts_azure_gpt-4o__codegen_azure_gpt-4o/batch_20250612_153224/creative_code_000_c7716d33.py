"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.caag.com.br
Prompt: Write Python code to automate the generation of legal correspondence templates based on the concepts outlined in the "Manual de Correspondência Jurídica" from the Complexo de Advocacia Adriano Geoffrey.
Generated: DETERMINISTIC_c7716d338efe0415
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
from datetime import datetime


class LegalCorrespondenceTemplateGenerator:
    """
    A class to automate the generation of legal correspondence templates
    based on pre-defined concepts from "Manual de Correspondência Jurídica".
    """

    def __init__(self, output_directory="templates"):
        """
        Initialize the generator with an output directory.

        :param output_directory: Directory where the templates will be saved.
        """
        self.output_directory = output_directory
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def generate_template(self, template_name, subject, body, sender, recipient):
        """
        Generate a legal correspondence template and save it as a text file.

        :param template_name: Name of the template file (without extension).
        :param subject: Subject of the correspondence.
        :param body: Main content of the correspondence.
        :param sender: Name of the sender (e.g., attorney or law office).
        :param recipient: Name of the recipient (e.g., client or institution).
        """
        try:
            # Format the correspondence template
            template_content = self._format_template(subject, body, sender, recipient)

            # Define the file path
            file_path = os.path.join(self.output_directory, f"{template_name}.txt")

            # Save the template to a file
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(template_content)

            print(f"Template '{template_name}' successfully saved at '{file_path}'.")

        except Exception as error:
            print(f"Error generating template '{template_name}': {error}")

    def _format_template(self, subject, body, sender, recipient):
        """
        Format the legal correspondence template.

        :param subject: Subject of the correspondence.
        :param body: Main content of the correspondence.
        :param sender: Name of the sender.
        :param recipient: Name of the recipient.
        :return: Formatted correspondence template as a string.
        """
        template = (
            f"Date: {datetime.now().strftime('%Y-%m-%d')}\n"
            f"Subject: {subject}\n"
            f"To: {recipient}\n\n"
            f"{body}\n\n"
            f"Sincerely,\n"
            f"{sender}\n"
        )
        return template

    def list_templates(self):
        """
        List all generated templates in the output directory.

        :return: List of template files.
        """
        try:
            templates = os.listdir(self.output_directory)
            print(f"Templates in '{self.output_directory}':")
            for template in templates:
                print(f" - {template}")
            return templates
        except Exception as error:
            print(f"Error listing templates: {error}")
            return []

    def delete_template(self, template_name):
        """
        Delete a specific template by name.

        :param template_name: Name of the template file (without extension).
        """
        try:
            file_path = os.path.join(self.output_directory, f"{template_name}.txt")
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Template '{template_name}' successfully deleted.")
            else:
                print(f"Template '{template_name}' not found.")
        except Exception as error:
            print(f"Error deleting template '{template_name}': {error}")


# Example usage
if __name__ == "__main__":
    # Initialize the generator
    generator = LegalCorrespondenceTemplateGenerator()

    # Generate example templates
    generator.generate_template(
        template_name="contract_review_request",
        subject="Request for Contract Review",
        body="Dear [Recipient],\n\nPlease provide your feedback regarding the attached contract draft. We appreciate your prompt response.",
        sender="Adriano Geoffrey Advocacia",
        recipient="John Doe"
    )

    generator.generate_template(
        template_name="legal_notice",
        subject="Legal Notice of Pending Action",
        body="Dear [Recipient],\n\nThis letter serves as formal notice regarding the pending legal action associated with your account. Please contact us immediately to avoid further escalation.",
        sender="Adriano Geoffrey Advocacia",
        recipient="Jane Smith"
    )

    # List all templates
    generator.list_templates()

    # Delete a template (optional)
    generator.delete_template("contract_review_request")
```
