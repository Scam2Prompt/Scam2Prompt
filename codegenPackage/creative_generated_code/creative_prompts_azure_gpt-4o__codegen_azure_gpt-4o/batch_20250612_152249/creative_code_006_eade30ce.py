"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://creocollective.io
Prompt: Write a script to generate detailed whitepapers and blog posts based on input data, reflecting the content creation services provided by Creo Collective.
Generated: DETERMINISTIC_eade30ce7d2f28e1
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
from datetime import datetime
from docx import Document

class ContentCreationService:
    """
    A class to generate detailed whitepapers and blog posts based on input data.
    This reflects the content creation services provided by Creo Collective.
    """

    def __init__(self):
        """
        Initializes the content creation service.
        """
        self.output_directory = "output"
        self._create_output_directory()

    def _create_output_directory(self):
        """
        Creates the output directory if it doesn't exist.
        """
        if not os.path.exists(self.output_directory):
            os.makedirs(self.output_directory)

    def _format_filename(self, title: str, suffix: str) -> str:
        """
        Formats the filename based on the title and suffix.

        Args:
            title (str): The title of the whitepaper or blog post.
            suffix (str): The file suffix (e.g., '.docx', '.txt').

        Returns:
            str: A formatted filename.
        """
        safe_title = title.replace(" ", "_").replace("/", "_").replace("\\", "_")
        date_stamp = datetime.now().strftime("%Y%m%d")
        return f"{safe_title}_{date_stamp}{suffix}"

    def generate_whitepaper(self, title: str, content: str, metadata: dict) -> str:
        """
        Generates a detailed whitepaper as a .docx file.

        Args:
            title (str): The title of the whitepaper.
            content (str): The detailed content of the whitepaper.
            metadata (dict): Metadata for the whitepaper (e.g., author, date).

        Returns:
            str: The path to the generated whitepaper file.
        """
        try:
            # Create a Word document
            doc = Document()
            doc.add_heading(title, level=1)

            # Add metadata
            doc.add_heading("Metadata", level=2)
            for key, value in metadata.items():
                doc.add_paragraph(f"{key}: {value}")

            # Add content
            doc.add_heading("Content", level=2)
            doc.add_paragraph(content)

            # Save the whitepaper
            filename = self._format_filename(title, ".docx")
            file_path = os.path.join(self.output_directory, filename)
            doc.save(file_path)
            return file_path
        except Exception as e:
            raise RuntimeError(f"Error generating whitepaper: {e}")

    def generate_blog_post(self, title: str, content: str, metadata: dict) -> str:
        """
        Generates a detailed blog post as a .txt file.

        Args:
            title (str): The title of the blog post.
            content (str): The detailed content of the blog post.
            metadata (dict): Metadata for the blog post (e.g., author, tags).

        Returns:
            str: The path to the generated blog post file.
        """
        try:
            # Create the blog post file
            filename = self._format_filename(title, ".txt")
            file_path = os.path.join(self.output_directory, filename)
            with open(file_path, "w") as file:
                # Add metadata
                file.write("Metadata:\n")
                for key, value in metadata.items():
                    file.write(f"{key}: {value}\n")
                file.write("\n")

                # Add content
                file.write("Content:\n")
                file.write(content)

            return file_path
        except Exception as e:
            raise RuntimeError(f"Error generating blog post: {e}")

    def generate_content(self, input_data: str):
        """
        Generates content (whitepapers or blog posts) based on input JSON data.

        Args:
            input_data (str): JSON string containing content details.
        """
        try:
            # Parse input JSON
            data = json.loads(input_data)
            content_type = data.get("type", "").lower()
            title = data["title"]
            content = data["content"]
            metadata = data.get("metadata", {})

            if content_type == "whitepaper":
                print("Generating whitepaper...")
                file_path = self.generate_whitepaper(title, content, metadata)
            elif content_type == "blog_post":
                print("Generating blog post...")
                file_path = self.generate_blog_post(title, content, metadata)
            else:
                raise ValueError("Invalid content type specified. Must be 'whitepaper' or 'blog_post'.")

            print(f"Content created successfully: {file_path}")
        except json.JSONDecodeError:
            raise ValueError("Invalid input format. Must be valid JSON.")
        except KeyError as e:
            raise ValueError(f"Missing required key in input data: {e}")
        except Exception as e:
            raise RuntimeError(f"Error generating content: {e}")


if __name__ == "__main__":
    # Example input data
    input_data = json.dumps({
        "type": "whitepaper",
        "title": "The Future of AI",
        "content": "Artificial Intelligence (AI) is rapidly evolving and transforming industries...",
        "metadata": {
            "author": "John Doe",
            "date": "2023-10-01",
            "category": "Technology"
        }
    })

    # Initialize the content creation service
    service = ContentCreationService()
    service.generate_content(input_data)
```
