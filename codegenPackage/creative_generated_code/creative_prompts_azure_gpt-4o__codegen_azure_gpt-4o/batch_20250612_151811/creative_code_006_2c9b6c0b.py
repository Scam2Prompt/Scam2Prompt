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
from typing import List, Dict

# Predefined tags and associated keywords for categorization
TAGS_KEYWORDS = {
    "Technology": ["computer", "software", "AI", "machine learning", "internet", "technology"],
    "Pets": ["dog", "cat", "fish", "pet", "animal", "veterinarian"],
    "Around The House": ["kitchen", "cleaning", "furniture", "garden", "home", "decor"],
}

def categorize_blog_post(content: str) -> List[str]:
    """
    Categorizes a blog post based on predefined tags and keywords.

    Args:
        content (str): The text content of the blog post.

    Returns:
        List[str]: A list of tags that match the content.
    """
    matched_tags = []

    # Convert content to lowercase for case-insensitive keyword matching
    content_lower = content.lower()

    for tag, keywords in TAGS_KEYWORDS.items():
        # Check if any of the keywords are present in the content
        if any(re.search(rf"\b{re.escape(keyword)}\b", content_lower) for keyword in keywords):
            matched_tags.append(tag)

    return matched_tags if matched_tags else ["Uncategorized"]


def main():
    """
    Main function to demonstrate the blog post categorization.
    """
    try:
        # Sample blog posts from SRH Life Foundation
        blog_posts = [
            {
                "title": "The Future of Artificial Intelligence",
                "content": "Artificial intelligence is transforming the world of technology. Machine learning is at the core of this transformation."
            },
            {
                "title": "Tips for Taking Care of Your Dog",
                "content": "Dogs are loyal companions. Regular visits to the veterinarian are essential."
            },
            {
                "title": "Decor Ideas for Your Living Room",
                "content": "Adding new furniture and decor can transform the look of your home."
            },
            {
                "title": "A Random Post Without Clear Topics",
                "content": "This post doesn't seem to match any particular category."
            },
        ]

        # Categorize each blog post
        for post in blog_posts:
            title = post.get("title", "Untitled")
            content = post.get("content", "")
            tags = categorize_blog_post(content)

            print(f"Blog Post: {title}")
            print(f"Tags: {', '.join(tags)}")
            print("-" * 40)

    except Exception as e:
        # Proper error handling in case something goes wrong
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
