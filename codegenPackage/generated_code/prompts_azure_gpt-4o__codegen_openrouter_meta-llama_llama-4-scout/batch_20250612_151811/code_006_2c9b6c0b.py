"""
Generated Code Metadata:
========================
Original URL: https://srhfoundation.ca
Prompt: Generate a Python script to categorize blog posts from SRH Life Foundation into predefined tags like "Technology," "Pets," and "Around The House" based on their content.
Generated: DETERMINISTIC_2c9b6c0bb953ca31
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import re
from typing import Dict, List

class BlogPostCategorizer:
    """
    A class used to categorize blog posts into predefined tags based on their content.

    Attributes:
    ----------
    tags : Dict[str, List[str]]
        A dictionary of predefined tags and their corresponding keywords.

    Methods:
    -------
    categorize(post_content: str) -> str
        Categorizes a blog post into a predefined tag based on its content.
    """

    def __init__(self):
        # Define predefined tags and their corresponding keywords
        self.tags = {
            "Technology": ["tech", "software", "programming", "coding", "app", "algorithm"],
            "Pets": ["pet", "dog", "cat", "animal", "wildlife", "conservation"],
            "Around The House": ["home", "house", "decor", "furniture", "renovation", "diy"]
        }

    def categorize(self, post_content: str) -> str:
        """
        Categorizes a blog post into a predefined tag based on its content.

        Args:
        ----
        post_content (str): The content of the blog post.

        Returns:
        -------
        str: The category of the blog post. If no match is found, returns "Uncategorized".
        """
        # Convert post content to lowercase for case-insensitive matching
        post_content = post_content.lower()

        # Iterate over each tag and its keywords
        for tag, keywords in self.tags.items():
            # Iterate over each keyword
            for keyword in keywords:
                # Use regular expression to search for the keyword in the post content
                if re.search(r'\b' + re.escape(keyword) + r'\b', post_content):
                    # If a match is found, return the tag
                    return tag

        # If no match is found, return "Uncategorized"
        return "Uncategorized"


def main():
    # Create an instance of the BlogPostCategorizer class
    categorizer = BlogPostCategorizer()

    # Example blog posts
    blog_posts = [
        {"title": "My Favorite Programming Languages", "content": "In this post, I'll discuss my favorite programming languages and why I love them."},
        {"title": "The Benefits of Having a Pet", "content": "Having a pet can bring numerous benefits to your mental and physical health."},
        {"title": "DIY Home Renovation on a Budget", "content": "In this post, I'll share some tips and tricks for renovating your home on a budget."},
        {"title": "Uncategorized Post", "content": "This post doesn't fit into any category."}
    ]

    # Categorize each blog post
    for blog_post in blog_posts:
        category = categorizer.categorize(blog_post["content"])
        print(f"Title: {blog_post['title']}, Category: {category}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
