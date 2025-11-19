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
import json
from typing import Dict, Any, List

class LegalDocument:
    """
    A class to represent a legal document template.
    """

    def __init__(self, title: str, content: str):
        """
        Initializes a LegalDocument instance.

        :param title: The title of the legal document.
        :param content: The content of the legal document.
        """
        self.title = title
        self.content = content

    def fill_template(self, placeholders: Dict[str, str]) -> str:
        """
        Fills the document template with the provided placeholders.

        :param placeholders: A dictionary of placeholders and their corresponding values.
        :return: The filled document as a string.
        """
        filled_content = self.content
        for placeholder, value in placeholders.items():
            filled_content = filled_content.replace(f'{{{{ {placeholder} }}}}', value)
        return filled_content


class DocumentLibrary:
    """
    A class to manage a collection of legal document templates.
    """

    def __init__(self):
        """
        Initializes the DocumentLibrary with an empty template collection.
        """
        self.templates: Dict[str, LegalDocument] = {}

    def add_template(self, title: str, content: str):
        """
        Adds a new legal document template to the library.

        :param title: The title of the legal document.
        :param content: The content of the legal document.
        """
        if title in self.templates:
            raise ValueError(f"Template with title '{title}' already exists.")
        self.templates[title] = LegalDocument(title, content)

    def get_template(self, title: str) -> LegalDocument:
        """
        Retrieves a legal document template by title.

        :param title: The title of the legal document.
        :return: The LegalDocument instance.
        :raises KeyError: If the template does not exist.
        """
        try:
            return self.templates[title]
        except KeyError:
            raise KeyError(f"Template with title '{title}' not found.")

    def list_templates(self) -> List[str]:
        """
        Lists all available document templates.

        :return: A list of titles of the available templates.
        """
        return list(self.templates.keys())

    def save_templates(self, file_path: str):
        """
        Saves the templates to a JSON file.

        :param file_path: The path to the file where templates will be saved.
        """
        try:
            with open(file_path, 'w') as file:
                json.dump({title: doc.content for title, doc in self.templates.items()}, file)
        except IOError as e:
            raise IOError(f"An error occurred while saving templates: {e}")

    def load_templates(self, file_path: str):
        """
        Loads templates from a JSON file.

        :param file_path: The path to the file from which templates will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                templates = json.load(file)
                for title, content in templates.items():
                    self.add_template(title, content)
        except (IOError, json.JSONDecodeError) as e:
            raise ValueError(f"An error occurred while loading templates: {e}")


# Example usage
if __name__ == "__main__":
    library = DocumentLibrary()
    
    # Adding a sample template
    library.add_template("Custody Agreement", "This Custody Agreement is made between {{{{ parent1 }}}} and {{{{ parent2 }}}}.")
    
    # Filling the template
    placeholders = {
        "parent1": "Alice Smith",
        "parent2": "Bob Johnson"
    }
    
    filled_document = library.get_template("Custody Agreement").fill_template(placeholders)
    print(filled_document)

    # Saving templates to a file
    library.save_templates("legal_templates.json")

    # Loading templates from a file
    library.load_templates("legal_templates.json")
```
