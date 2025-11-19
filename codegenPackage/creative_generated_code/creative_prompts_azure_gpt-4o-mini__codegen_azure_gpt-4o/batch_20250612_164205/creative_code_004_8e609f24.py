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

def generate_health_doc(content, header_info, footer_info, output_file):
    """
    Generates a health information document with specified header and footer details.

    Args:
        content (str): The main content of the document.
        header_info (dict): Dictionary containing header details, e.g., {'title': 'Health Report', 'author': 'Dr. Smith'}.
        footer_info (dict): Dictionary containing footer details, e.g., {'organization': 'HealthCare Inc.', 'date': '2023-01-01'}.
        output_file (str): Path to the output file where the document will be saved.

    Returns:
        None
    """
    try:
        # Validate inputs
        if not isinstance(content, str):
            raise ValueError("Content must be a string.")
        if not isinstance(header_info, dict):
            raise ValueError("Header info must be a dictionary.")
        if not isinstance(footer_info, dict):
            raise ValueError("Footer info must be a dictionary.")
        if not isinstance(output_file, str):
            raise ValueError("Output file path must be a string.")

        # Construct the header
        header = f"Title: {header_info.get('title', 'Untitled')}\n"
        header += f"Author: {header_info.get('author', 'Unknown')}\n"
        header += "=" * 40 + "\n"

        # Construct the footer
        footer = "=" * 40 + "\n"
        footer += f"Organization: {footer_info.get('organization', 'Unknown')}\n"
        footer += f"Date: {footer_info.get('date', datetime.now().strftime('%Y-%m-%d'))}\n"

        # Combine all parts into the final document
        document = header + content + "\n" + footer

        # Write the document to the output file
        with open(output_file, 'w') as file:
            file.write(document)

        print(f"Document successfully written to {output_file}")

    except Exception as e:
        # Handle any errors gracefully
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    content = "This is the main content of the health information document.\nIt provides critical information about patient health and medical records."
    header_info = {
        'title': 'Health Information Document',
        'author': 'Dr. John Doe'
    }
    footer_info = {
        'organization': 'Wellness Center',
        'date': '2023-10-01'
    }
    output_file = "health_document.txt"

    generate_health_doc(content, header_info, footer_info, output_file)
```
