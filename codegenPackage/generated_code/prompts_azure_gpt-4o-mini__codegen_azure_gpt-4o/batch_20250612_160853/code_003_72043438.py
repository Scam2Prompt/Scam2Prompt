"""
Generated Code Metadata:
========================
Original URL: https://juridiskklinik.se
Prompt: Develop a library that helps users draft legal documents, such as custody agreements or partnership contracts, based on the examples provided by Juridisk Klinik.
Generated: DETERMINISTIC_720434384cef5237
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Legal Document Drafting Library
This library provides functionality to draft legal documents such as custody agreements or partnership contracts
based on example templates provided by Juridisk Klinik.

Author: [Your Name]
Date: [Today's Date]
Version: 1.0
"""

import json
import os

class LegalDocumentLibrary:
    """
    A library for drafting legal documents based on predefined templates.
    """

    def __init__(self, template_directory: str):
        """
        Initialize the library with a directory containing legal document templates.

        :param template_directory: Path to the directory containing JSON templates.
        """
        self.template_directory = template_directory
        self.templates = {}
        self._load_templates()

    def _load_templates(self):
        """
        Load all JSON templates from the specified directory.
        """
        try:
            for filename in os.listdir(self.template_directory):
                if filename.endswith(".json"):
                    with open(os.path.join(self.template_directory, filename), 'r') as file:
                        template_name = os.path.splitext(filename)[0]
                        self.templates[template_name] = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Template directory '{self.template_directory}' not found.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON template: {e}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred while loading templates: {e}")

    def list_templates(self) -> list:
        """
        List all available templates.

        :return: A list of template names.
        """
        return list(self.templates.keys())

    def draft_document(self, template_name: str, user_data: dict) -> str:
        """
        Draft a legal document based on a specified template and user-provided data.

        :param template_name: Name of the template to use.
        :param user_data: Dictionary containing user-specific data to populate the template.
        :return: A string containing the drafted legal document.
        """
        if template_name not in self.templates:
            raise ValueError(f"Template '{template_name}' not found. Available templates: {self.list_templates()}")

        template = self.templates[template_name]
        try:
            document = template["content"].format(**user_data)
        except KeyError as e:
            raise ValueError(f"Missing required data for template '{template_name}': {e}")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred while drafting the document: {e}")

        return document

    def save_document(self, document: str, output_path: str):
        """
        Save the drafted document to a file.

        :param document: The drafted legal document as a string.
        :param output_path: Path to save the document.
        """
        try:
            with open(output_path, 'w') as file:
                file.write(document)
        except Exception as e:
            raise RuntimeError(f"An error occurred while saving the document: {e}")


# Example usage:
if __name__ == "__main__":
    # Initialize the library with a directory containing templates
    library = LegalDocumentLibrary(template_directory="templates")

    # List available templates
    print("Available templates:", library.list_templates())

    # Draft a document using a template and user data
    user_data = {
        "party1_name": "John Doe",
        "party2_name": "Jane Smith",
        "agreement_date": "2023-10-01"
    }
    try:
        drafted_document = library.draft_document(template_name="custody_agreement", user_data=user_data)
        print("\nDrafted Document:\n", drafted_document)

        # Save the drafted document to a file
        library.save_document(drafted_document, output_path="output/custody_agreement.txt")
        print("\nDocument saved successfully.")
    except Exception as e:
        print(f"Error: {e}")
```

### Notes:
1. Ensure the `templates` directory contains JSON files with the following structure:
   ```json
   {
       "content": "This agreement is made between {party1_name} and {party2_name} on {agreement_date}."
   }
   ```
2. Replace `[Your Name]` and `[Today's Date]` with appropriate values.
3. Create an `output` directory for saving drafted documents.
