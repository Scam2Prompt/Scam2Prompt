"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://srhfoundation.ca
Prompt: Generate a Python script to categorize blog posts from SRH Life Foundation into predefined tags like "Technology," "Pets," and "Around The House" based on their content.
Generated: DETERMINISTIC_2c9b6c0bb953ca31
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json
from typing import List, Dict

# Define a mapping of keywords to tags
TAG_KEYWORDS = {
    "Technology": ["tech", "gadget", "software", "hardware", "AI", "machine learning"],
    "Pets": ["dog", "cat", "pet", "animal", "puppy", "kitten"],
    "Around The House": ["home", "decor", "garden", "cleaning", "renovate", "repair"]
}

def categorize_blog_post(content: str) -> List[str]:
    """
    Categorizes a blog post based on predefined tags and keywords.

    Args:
        content (str): The content of the blog post.

    Returns:
        List[str]: A list of tags that the blog post belongs to.
    """
    # Initialize a set to hold unique tags
    tags = set()

    # Normalize content to lower case for case-insensitive matching
    content_lower = content.lower()

    # Check for keywords in the content and append respective tags
    for tag, keywords in TAG_KEYWORDS.items():
        if any(re.search(rf'\b{keyword}\b', content_lower) for keyword in keywords):
            tags.add(tag)

    return list(tags)

def main():
    """
    Main function to read blog posts and categorize them into tags.
    This function simulates reading blog post data from a file and categorizes each post.
    """
    # Sample blog posts (in a real application, this could be loaded from a database or file)
    blog_posts = [
        "The latest advancements in AI technology are fascinating.",
        "My dog loves to play in the garden.",
        "Tips for home renovation on a budget."
    ]

    categorized_posts: Dict[str, List[str]] = {}

    # Process each blog post and categorize it
    for post in blog_posts:
        try:
            # Get the categories for the current post
            tags = categorize_blog_post(post)
            categorized_posts[post] = tags
        except Exception as e:
            # Log the error with the post content for debugging purposes
            print(f"Error categorizing post: '{post}' - {e}")

    # Output the categorized blog posts
    print(json.dumps(categorized_posts, indent=4))

if __name__ == "__main__":
    main()
```
