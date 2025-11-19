"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sif.com.bo
Prompt: Write a function that automates the legal documentation process for property and vehicle liens, referencing the services provided by SIF.
Generated: DETERMINISTIC_a3264758f9be19fe
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import os

class LiensDocumentAutomation:
    """
    A class to automate the creation of legal documentation for property and vehicle liens.
    It provides methods to generate lien documents based on the provided information.
    """

    def __init__(self, template_path):
        """
        Initializes the LiensDocumentAutomation class with a path to the document template.

        Args:
            template_path (str): The file path to the document template.
        """
        if not os.path.isfile(template_path):
            raise FileNotFoundError(f"Template file not found at: {template_path}")
        self.template_path = template_path

    def generate_document(self, lien_type, owner_name, property_details, lien_amount):
        """
        Generates a lien document based on the provided information.

        Args:
            lien_type (str): The type of lien ('property' or 'vehicle').
            owner_name (str): The name of the lien owner.
            property_details (str): Details of the property or vehicle.
            lien_amount (float): The amount of the lien.

        Returns:
            str: The path to the generated lien document.
        """
        # Validate inputs
        if lien_type not in ['property', 'vehicle']:
            raise ValueError("Invalid lien type. Must be 'property' or 'vehicle'.")
        if not isinstance(lien_amount, (int, float)) or lien_amount <= 0:
            raise ValueError("Invalid lien amount. It must be a positive number.")

        # Create the lien document
        document_content = self._prepare_document_content(lien_type, owner_name, property_details, lien_amount)
        document_path = self._save_document(document_content)

        return document_path

    def _prepare_document_content(self, lien_type, owner_name, property_details, lien_amount):
        """
        Prepares the content of the lien document based on the provided information.

        Args:
            lien_type (str): The type of lien.
            owner_name (str): The name of the lien owner.
            property_details (str): Details of the property or vehicle.
            lien_amount (float): The amount of the lien.

        Returns:
            str: The formatted document content.
        """
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        return (f"LIEN DOCUMENT\n"
                f"Date: {current_date}\n"
                f"Type of Lien: {lien_type.capitalize()}\n"
                f"Owner Name: {owner_name}\n"
                f"Details: {property_details}\n"
                f"Lien Amount: ${lien_amount:.2f}\n"
                f"\nThis document serves as a formal notice of lien.")

    def _save_document(self, content):
        """
        Saves the generated document content to a file.

        Args:
            content (str): The content to save in the document.

        Returns:
            str: The path to the saved document.
        """
        document_filename = f"lien_document_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        document_path = os.path.join(os.getcwd(), document_filename)

        with open(document_path, 'w') as file:
            file.write(content)

        return document_path

# Example usage
if __name__ == "__main__":
    try:
        lien_automation = LiensDocumentAutomation(template_path="template.txt")
        document_path = lien_automation.generate_document(
            lien_type='property',
            owner_name='John Doe',
            property_details='123 Main St, Anytown, USA',
            lien_amount=15000.00
        )
        print(f"Lien document created successfully: {document_path}")
    except Exception as e:
        print(f"Error: {e}")
```
