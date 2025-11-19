"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.himsdemo.bste.live
Prompt: Develop a script that prints health information documents with the specified header and footer details as outlined in the SCHEMA Processing content.
Generated: DETERMINISTIC_8e609f2417f6eb31
Batch ID: 20250612_164205
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

class HealthInfoDocument:
    def __init__(self, header, footer):
        """
        Initialize the HealthInfoDocument with specified header and footer.

        :param header: str - The header text for the document.
        :param footer: str - The footer text for the document.
        """
        self.header = header
        self.footer = footer

    def generate_document(self, content, output_directory):
        """
        Generate a health information document with a header, content, and footer.

        :param content: str - The main content of the document.
        :param output_directory: str - The directory where the document will be saved.
        """
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        document_content = self.format_document(content)
        file_path = os.path.join(output_directory, f"health_info_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")

        try:
            with open(file_path, 'w') as file:
                file.write(document_content)
            print(f"Document created successfully: {file_path}")
        except IOError as e:
            print(f"Error writing document: {e}")

    def format_document(self, content):
        """
        Format the document with header, content, and footer.

        :param content: str - The main content of the document.
        :return: str - The formatted document as a string.
        """
        return f"{self.header}\n\n{content}\n\n{self.footer}"

def main():
    # Define the header and footer
    header = "Health Information Document"
    footer = "Confidential - Do not distribute"

    # Create an instance of the HealthInfoDocument
    document = HealthInfoDocument(header, footer)

    # Define the content of the document
    content = (
        "This document contains important health information relevant to your care.\n"
        "Please review the following details carefully."
    )

    # Specify the output directory
    output_directory = "health_documents"

    # Generate the health information document
    document.generate_document(content, output_directory)

if __name__ == "__main__":
    main()
```
