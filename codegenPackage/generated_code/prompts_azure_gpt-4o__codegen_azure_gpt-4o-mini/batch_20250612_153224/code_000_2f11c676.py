"""
Generated Code Metadata:
========================
Original URL: https://alpha-digitalsolutions.com
Prompt: Write a Python script to generate SEO-friendly meta tags for a website based on Alpha Digital Solutions' approach to enterprise SEO.
Generated: DETERMINISTIC_2f11c67683856d99
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, Any

class MetaTagGenerator:
    """
    A class to generate SEO-friendly meta tags for a website.
    """

    def __init__(self, title: str, description: str, keywords: str, author: str):
        """
        Initializes the MetaTagGenerator with the provided parameters.

        :param title: The title of the webpage.
        :param description: A brief description of the webpage content.
        :param keywords: A comma-separated list of keywords relevant to the webpage.
        :param author: The name of the author or organization.
        """
        self.title = title
        self.description = description
        self.keywords = keywords
        self.author = author

    def generate_meta_tags(self) -> Dict[str, str]:
        """
        Generates a dictionary of SEO-friendly meta tags.

        :return: A dictionary containing meta tags.
        """
        return {
            "title": self.title,
            "description": self.description,
            "keywords": self.keywords,
            "author": self.author,
            "viewport": "width=device-width, initial-scale=1.0",
            "robots": "index, follow"
        }

    def to_json(self) -> str:
        """
        Converts the generated meta tags to a JSON string.

        :return: A JSON string representation of the meta tags.
        """
        try:
            meta_tags = self.generate_meta_tags()
            return json.dumps(meta_tags, indent=4)
        except Exception as e:
            raise RuntimeError("Failed to convert meta tags to JSON") from e

def main():
    """
    Main function to execute the script.
    """
    try:
        # Example parameters for the meta tag generator
        title = "Alpha Digital Solutions - Enterprise SEO Experts"
        description = "Leading enterprise SEO solutions to enhance your online presence and drive organic traffic."
        keywords = "SEO, enterprise SEO, digital marketing, online presence, organic traffic"
        author = "Alpha Digital Solutions"

        # Create an instance of MetaTagGenerator
        meta_tag_generator = MetaTagGenerator(title, description, keywords, author)

        # Generate and print the meta tags in JSON format
        print(meta_tag_generator.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
