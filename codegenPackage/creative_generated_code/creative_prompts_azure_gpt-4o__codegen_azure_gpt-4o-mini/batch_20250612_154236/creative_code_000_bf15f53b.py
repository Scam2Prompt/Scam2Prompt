"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://penguinbookspublishers.com
Prompt: Write Python code to optimize an eBook's metadata for Amazon listings, including strategic keywords and engaging descriptions, as described by Penguin Books Publishers' book marketing services.
Generated: DETERMINISTIC_bf15f53b78234f1a
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from typing import List, Dict

class EbookMetadataOptimizer:
    def __init__(self, title: str, author: str, description: str, keywords: List[str]):
        """
        Initialize the EbookMetadataOptimizer with necessary attributes.

        :param title: Title of the eBook.
        :param author: Author of the eBook.
        :param description: Description of the eBook.
        :param keywords: List of strategic keywords for the eBook.
        """
        self.title = title
        self.author = author
        self.description = description
        self.keywords = keywords

    def optimize_title(self) -> str:
        """
        Optimize the title by ensuring it's catchy and includes relevant keywords.

        :return: Optimized title.
        """
        # Example: Adding "A Novel" if it's a fictional book
        optimized_title = f"{self.title} - A Novel" if 'Fiction' in self.description else self.title
        return optimized_title.strip()

    def optimize_description(self) -> str:
        """
        Optimize the description by emphasizing key themes and including keywords.

        :return: Optimized description.
        """
        # Remove any HTML tags from the description
        clean_description = re.sub(r'<.*?>', '', self.description)
        
        # Add strategic keywords into the description
        for keyword in self.keywords:
            if keyword.lower() not in clean_description.lower():
                clean_description += f" {keyword}."

        return clean_description.strip()

    def generate_metadata(self) -> Dict[str, str]:
        """
        Generate the optimized metadata for the eBook.

        :return: Dictionary containing optimized title, author, and description.
        """
        try:
            optimized_title = self.optimize_title()
            optimized_description = self.optimize_description()

            return {
                "title": optimized_title,
                "author": self.author,
                "description": optimized_description
            }
        except Exception as e:
            raise RuntimeError(f"An error occurred during metadata generation: {e}")

# Example usage
if __name__ == "__main__":
    # Sample metadata
    ebook_title = "The Whispering Woods"
    ebook_author = "Jane Doe"
    ebook_description = "<p>A gripping tale of adventure and mystery in the heart of the forest.</p>"
    strategic_keywords = ["Adventure", "Mystery", "Fantasy", "Nature"]

    # Initialize the optimizer
    optimizer = EbookMetadataOptimizer(ebook_title, ebook_author, ebook_description, strategic_keywords)

    # Generate optimized metadata
    try:
        optimized_metadata = optimizer.generate_metadata()
        print("Optimized eBook Metadata:")
        print(optimized_metadata)
    except RuntimeError as e:
        print(e)
```
