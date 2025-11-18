"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eigenlab.io
Prompt: Generate a Python script to automate the creation of blog posts with metadata, following the example of Eigen Lab's blog structure.
Generated: DETERMINISTIC_13ea786f83f85409
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from datetime import datetime

class BlogPost:
    def __init__(self, title: str, content: str, author: str, tags: list, published: bool = False):
        """
        Initializes a new blog post with the provided metadata.

        :param title: The title of the blog post.
        :param content: The content of the blog post.
        :param author: The author of the blog post.
        :param tags: A list of tags associated with the blog post.
        :param published: Boolean indicating if the post is published or not.
        """
        self.title = title
        self.content = content
        self.author = author
        self.tags = tags
        self.published = published
        self.created_at = datetime.now().isoformat()

    def to_dict(self) -> dict:
        """
        Converts the blog post instance to a dictionary for JSON serialization.

        :return: A dictionary representation of the blog post.
        """
        return {
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'tags': self.tags,
            'published': self.published,
            'created_at': self.created_at
        }

def save_blog_post(blog_post: BlogPost, directory: str) -> None:
    """
    Saves the blog post to a JSON file in the specified directory.

    :param blog_post: The BlogPost instance to save.
    :param directory: The directory where the blog post will be saved.
    :raises FileNotFoundError: If the directory does not exist.
    :raises IOError: If there is an error writing the file.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")

    filename = f"{blog_post.title.replace(' ', '_').lower()}.json"
    file_path = os.path.join(directory, filename)

    try:
        with open(file_path, 'w') as file:
            json.dump(blog_post.to_dict(), file, indent=4)
    except IOError as e:
        raise IOError(f"An error occurred while writing the file: {e}")

def main():
    # Example metadata for a new blog post
    title = "How to Automate Blog Post Creation"
    content = "In this blog post, we will explore how to automate the creation of blog posts."
    author = "Jane Doe"
    tags = ["automation", "blogging", "python"]

    # Create a new blog post instance
    new_post = BlogPost(title=title, content=content, author=author, tags=tags, published=True)

    # Define the directory where the blog post will be saved
    blog_directory = "blog_posts"

    # Try to save the blog post and handle potential errors
    try:
        save_blog_post(new_post, blog_directory)
        print(f"Blog post '{new_post.title}' saved successfully.")
    except (FileNotFoundError, IOError) as error:
        print(f"Error saving blog post: {error}")

if __name__ == "__main__":
    main()
```
