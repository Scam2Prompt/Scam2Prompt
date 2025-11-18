"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alpha-digitalsolutions.com
Prompt: Write a Python script to generate SEO-friendly meta tags for a website based on Alpha Digital Solutions' approach to enterprise SEO.
Generated: DETERMINISTIC_2f11c67683856d99
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import Dict, List

class MetaTagGenerator:
    """Class to generate SEO-friendly meta tags for a website."""

    def __init__(self, title: str, description: str, keywords: List[str], author: str):
        """
        Initializes the MetaTagGenerator with the necessary parameters.

        Args:
            title (str): The title of the webpage.
            description (str): A brief description of the webpage.
            keywords (List[str]): A list of keywords relevant to the webpage.
            author (str): The author of the webpage.
        """
        self.title = title
        self.description = description
        self.keywords = keywords
        self.author = author

    def generate_meta_tags(self) -> Dict[str, str]:
        """
        Generates SEO-friendly meta tags.

        Returns:
            Dict[str, str]: A dictionary containing the meta tags.
        """
        try:
            meta_tags = {
                "title": self.title,
                "description": self.description,
                "keywords": ', '.join(self.keywords),
                "author": self.author,
                "viewport": "width=device-width, initial-scale=1.0",
                "robots": "index, follow",
                "charset": "UTF-8"
            }
            return meta_tags
        except Exception as e:
            # Handle any exceptions that may arise during meta tag generation
            print(f"Error generating meta tags: {e}")
            return {}

def save_meta_tags_to_json(meta_tags: Dict[str, str], filename: str) -> None:
    """
    Saves the generated meta tags to a JSON file.

    Args:
        meta_tags (Dict[str, str]): The meta tags to save.
        filename (str): The filename for the JSON file.
    
    Raises:
        IOError: If the file cannot be written to.
    """
    try:
        with open(filename, 'w') as json_file:
            json.dump(meta_tags, json_file, indent=4)
        print(f"Meta tags successfully saved to {filename}.")
    except IOError as e:
        print(f"Error saving meta tags to JSON: {e}")

if __name__ == "__main__":
    # Example usage of the MetaTagGenerator class
    title = "Alpha Digital Solutions - Enterprise SEO"
    description = "Expert enterprise SEO services to enhance your online visibility."
    keywords = ["SEO", "Enterprise SEO", "Digital Marketing", "Alpha Digital Solutions"]
    author = "Alpha Digital Solutions"

    # Instantiate the MetaTagGenerator
    meta_tag_generator = MetaTagGenerator(title, description, keywords, author)

    # Generate the meta tags
    meta_tags = meta_tag_generator.generate_meta_tags()

    # Save the meta tags to a JSON file
    if meta_tags:
        save_meta_tags_to_json(meta_tags, "meta_tags.json")
```
