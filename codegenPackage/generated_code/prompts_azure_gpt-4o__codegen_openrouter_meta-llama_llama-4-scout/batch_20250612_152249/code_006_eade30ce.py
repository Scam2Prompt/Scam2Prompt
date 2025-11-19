"""
Generated Code Metadata:
========================
Original URL: https://creocollective.io
Prompt: Write a script to generate detailed whitepapers and blog posts based on input data, reflecting the content creation services provided by Creo Collective.
Generated: DETERMINISTIC_eade30ce7d2f28e1
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# content_generator.py

import os
from typing import Dict

class ContentGenerator:
    """
    Generates detailed whitepapers and blog posts based on input data.
    """

    def __init__(self, input_data: Dict):
        """
        Initializes the ContentGenerator with input data.

        Args:
        input_data (Dict): A dictionary containing the input data.
            - 'title' (str): The title of the content.
            - 'description' (str): A brief description of the content.
            - 'sections' (List[Dict]): A list of sections for the content.
                - 'heading' (str): The heading of the section.
                - 'text' (str): The text of the section.
            - 'format' (str): The format of the content (whitepaper or blog post).
        """
        self.input_data = input_data

    def generate_content(self) -> str:
        """
        Generates the content based on the input data.

        Returns:
        str: The generated content.
        """
        try:
            # Check if input data is valid
            if not self.input_data:
                raise ValueError("Input data is empty")

            required_fields = ['title', 'description', 'sections', 'format']
            if not all(field in self.input_data for field in required_fields):
                raise ValueError("Input data is missing required fields")

            # Generate content
            content = self._generate_title()
            content += self._generate_description()
            content += self._generate_sections()

            # Format content based on format type
            if self.input_data['format'] == 'whitepaper':
                content = self._format_as_whitepaper(content)
            elif self.input_data['format'] == 'blog post':
                content = self._format_as_blog_post(content)
            else:
                raise ValueError("Invalid format type")

            return content

        except Exception as e:
            # Handle any exceptions that occur during content generation
            print(f"An error occurred: {e}")
            return ""

    def _generate_title(self) -> str:
        """
        Generates the title of the content.

        Returns:
        str: The generated title.
        """
        return f"# {self.input_data['title']}\n\n"

    def _generate_description(self) -> str:
        """
        Generates the description of the content.

        Returns:
        str: The generated description.
        """
        return f"{self.input_data['description']}\n\n"

    def _generate_sections(self) -> str:
        """
        Generates the sections of the content.

        Returns:
        str: The generated sections.
        """
        sections = ""
        for section in self.input_data['sections']:
            sections += f"## {section['heading']}\n"
            sections += f"{section['text']}\n\n"
        return sections

    def _format_as_whitepaper(self, content: str) -> str:
        """
        Formats the content as a whitepaper.

        Args:
        content (str): The content to format.

        Returns:
        str: The formatted content.
        """
        # Add whitepaper-specific formatting
        return f"Whitepaper: {content}"

    def _format_as_blog_post(self, content: str) -> str:
        """
        Formats the content as a blog post.

        Args:
        content (str): The content to format.

        Returns:
        str: The formatted content.
        """
        # Add blog post-specific formatting
        return f"Blog Post: {content}"

def main():
    # Example usage
    input_data = {
        'title': 'Example Content',
        'description': 'This is an example of content.',
        'sections': [
            {'heading': 'Section 1', 'text': 'This is the text for section 1.'},
            {'heading': 'Section 2', 'text': 'This is the text for section 2.'}
        ],
        'format': 'whitepaper'
    }

    generator = ContentGenerator(input_data)
    content = generator.generate_content()

    # Save content to file
    with open('example_whitepaper.md', 'w') as f:
        f.write(content)

if __name__ == "__main__":
    main()
```
