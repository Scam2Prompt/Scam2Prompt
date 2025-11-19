"""
Generated Code Metadata:
========================
Original URL: https://eigenlab.io
Prompt: Generate a Python script to automate the creation of blog posts with metadata, following the example of Eigen Lab's blog structure.
Generated: DETERMINISTIC_13ea786f83f85409
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime

class BlogPost:
    """
    A class to represent a blog post with metadata.
    """

    def __init__(self, title, content, author, tags):
        """
        Initializes a new blog post with the given title, content, author, and tags.

        :param title: Title of the blog post
        :param content: Content of the blog post
        :param author: Author of the blog post
        :param tags: List of tags associated with the blog post
        """
        self.title = title
        self.content = content
        self.author = author
        self.tags = tags
        self.date_created = datetime.now().isoformat()
        self.metadata = {
            "title": self.title,
            "author": self.author,
            "date_created": self.date_created,
            "tags": self.tags
        }

    def save_to_file(self, directory):
        """
        Saves the blog post content and metadata to a markdown file.

        :param directory: Directory where the blog post will be saved
        """
        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Create a filename based on the title
        filename = f"{self.title.replace(' ', '_').lower()}.md"
        file_path = os.path.join(directory, filename)

        # Write the content and metadata to the file
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                # Write metadata in JSON format
                json.dump(self.metadata, file, indent=4)
                file.write("\n\n")  # Add space between metadata and content
                file.write(self.content)
            print(f"Blog post '{self.title}' saved successfully at '{file_path}'")
        except IOError as e:
            print(f"Error saving blog post '{self.title}': {e}")

def create_blog_post(title, content, author, tags, directory='blog_posts'):
    """
    Creates a blog post and saves it to the specified directory.

    :param title: Title of the blog post
    :param content: Content of the blog post
    :param author: Author of the blog post
    :param tags: List of tags associated with the blog post
    :param directory: Directory where the blog post will be saved
    """
    post = BlogPost(title, content, author, tags)
    post.save_to_file(directory)

if __name__ == "__main__":
    # Example usage
    blog_title = "Understanding Eigenvalues and Eigenvectors"
    blog_content = """
    Eigenvalues and eigenvectors are fundamental concepts in linear algebra...
    """
    blog_author = "Jane Doe"
    blog_tags = ["linear algebra", "mathematics", "eigenvalues", "eigenvectors"]

    create_blog_post(blog_title, blog_content, blog_author, blog_tags)
```
