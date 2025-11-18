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
import os
import json
from datetime import datetime

# Define the structure for blog metadata
BLOG_TEMPLATE = {
    "title": "",
    "author": "",
    "date": "",
    "tags": [],
    "summary": "",
}

# Function to generate metadata for the blog
def generate_metadata(title, author, tags, summary):
    """
    Generate metadata for the blog post.

    Args:
        title (str): The title of the blog post.
        author (str): The author of the blog post.
        tags (list): A list of tags for categorization.
        summary (str): A short summary of the blog.

    Returns:
        dict: A dictionary containing the metadata.
    """
    metadata = BLOG_TEMPLATE.copy()
    metadata["title"] = title
    metadata["author"] = author
    metadata["date"] = datetime.now().strftime("%Y-%m-%d")
    metadata["tags"] = tags
    metadata["summary"] = summary
    return metadata

# Function to create blog post file
def create_blog_post(directory, title, author, tags, summary, content):
    """
    Create a blog post file with metadata and content.

    Args:
        directory (str): The directory to save the blog post.
        title (str): The title of the blog post.
        author (str): The author of the blog post.
        tags (list): A list of tags for categorization.
        summary (str): A short summary of the blog.
        content (str): The main content of the blog post.

    Returns:
        None
    """
    try:
        # Generate metadata
        metadata = generate_metadata(title, author, tags, summary)

        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Create the file name (slugified title + date)
        sanitized_title = title.replace(" ", "-").lower()
        file_name = f"{metadata['date']}-{sanitized_title}.json"
        file_path = os.path.join(directory, file_name)

        # Prepare blog post data
        blog_post = {
            "metadata": metadata,
            "content": content
        }

        # Write the blog post to a JSON file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(blog_post, f, indent=4)

        print(f"Blog post created successfully: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Sample data
    blog_directory = "blogs"
    blog_title = "Exploring Eigenlabs"
    blog_author = "John Doe"
    blog_tags = ["technology", "Eigenlabs", "programming"]
    blog_summary = "A deep dive into the structure and features of Eigenlabs blogs."
    blog_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio."

    # Create the blog post
    create_blog_post(blog_directory, blog_title, blog_author, blog_tags, blog_summary, blog_content)
```
