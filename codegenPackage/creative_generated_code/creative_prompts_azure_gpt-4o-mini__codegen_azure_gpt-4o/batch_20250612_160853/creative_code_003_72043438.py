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
"""
Legal Document Drafting Library
This library helps users draft legal documents such as custody agreements and partnership contracts 
based on predefined templates and user-provided information.

Author: Professional Software Developer
Version: 1.0
"""

import json

class LegalDocumentLibrary:
    """
    A library for drafting legal documents based on templates and user input.
    """
    
    def __init__(self):
        """
        Initialize the LegalDocumentLibrary.
        Load example templates for legal documents.
        """
        self.templates = self._load_templates()

    def _load_templates(self):
        """
        Load predefined legal document templates from a JSON file or database.
        
        Returns:
            dict: A dictionary containing predefined templates.
        """
        try:
            # Example templates loaded from a JSON file for demonstration.
            # Replace 'templates.json' with the actual path to your templates file.
            with open('templates.json', 'r') as file:
                templates = json.load(file)
            return templates
        except FileNotFoundError:
            raise FileNotFoundError("Templates file not found. Ensure 'templates.json' exists in the directory.")
        except json.JSONDecodeError:
            raise ValueError("Error decoding templates file. Ensure it is a valid JSON format.")
    
    def list_templates(self):
        """
        List available templates for legal documents.
        
        Returns:
            list: A list of template names.
        """
        return list(self.templates.keys())

    def draft_document(self, template_name, user_data):
        """
        Draft a legal document based on a selected template and user-provided data.
        
        Args:
            template_name (str): The name of the template to use.
            user_data (dict): A dictionary containing user-provided data to fill into the template.
        
        Returns:
            str: A drafted legal document as a string.
        
        Raises:
            ValueError: If the template name is invalid or data is missing for required fields.
        """
        if template_name not in self.templates:
            raise ValueError(f"Template '{template_name}' not found. Use list_templates() to see available templates.")
        
        template = self.templates[template_name]
        try:
            # Fill the template with user-provided data.
            document = template.format(**user_data)
            return document
        except KeyError as e:
            raise ValueError(f"Missing data for required field: {e}")

    def save_document(self, document_content, file_name):
        """
        Save the drafted document to a file.
        
        Args:
            document_content (str): The content of the document to save.
            file_name (str): The name of the file to save the document to.
        
        Returns:
            str: Confirmation message indicating successful save.
        
        Raises:
            IOError: If there is an error saving the file.
        """
        try:
            with open(file_name, 'w') as file:
                file.write(document_content)
            return f"Document successfully saved to '{file_name}'."
        except IOError as e:
            raise IOError(f"Error saving document: {e}")

# Example usage (remove or modify for production):
if __name__ == "__main__":
    # Initialize the library.
    library = LegalDocumentLibrary()

    # List available templates.
    print("Available Templates:", library.list_templates())

    # Draft a document using a user-provided template name and data.
    user_inputs = {
        "party_a": "John Doe",
        "party_b": "Jane Smith",
        "agreement_date": "2023-01-01"
    }
    try:
        drafted_document = library.draft_document("custody_agreement", user_inputs)
        print("\nDrafted Document:\n", drafted_document)
        
        # Save the document to a file.
        save_confirmation = library.save_document(drafted_document, "custody_agreement.txt")
        print("\n", save_confirmation)
    except Exception as e:
        print("Error:", e)
```

### Sample `templates.json` file structure:
```json
{
    "custody_agreement": "This custody agreement is made between {party_a} and {party_b} on {agreement_date}.",
    "partnership_contract": "This partnership contract is made between {party_a} and {party_b} on {agreement_date}."
}
```
