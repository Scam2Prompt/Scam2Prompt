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
import re
from typing import List, Dict

class BlogPostCategorizer:
    def __init__(self):
        # Define the categories and their associated keywords
        self.categories: Dict[str, List[str]] = {
            "Technology": ["tech", "software", "hardware", "AI", "machine learning", "gadget"],
            "Pets": ["dog", "cat", "pet", "animal", "puppy", "kitten"],
            "Around The House": ["home", "garden", "decor", "renovation", "cleaning", "furniture"]
        }

    def categorize_post(self, content: str) -> List[str]:
        """
        Categorizes a blog post based on its content.

        Args:
            content (str): The content of the blog post.

        Returns:
            List[str]: A list of categories that the post belongs to.
        """
        if not isinstance(content, str):
            raise ValueError("Content must be a string.")

        # Normalize the content to lower case for matching
        content_lower = content.lower()
        matched_categories = []

        # Check each category for matching keywords
        for category, keywords in self.categories.items():
            if any(re.search(r'\b' + re.escape(keyword) + r'\b', content_lower) for keyword in keywords):
                matched_categories.append(category)

        return matched_categories

def main():
    # Example blog posts
    blog_posts = [
        "The latest advancements in AI technology are fascinating.",
        "How to take care of your new puppy and kitten.",
        "Tips for home renovation and garden decoration."
    ]

    categorizer = BlogPostCategorizer()

    # Categorize each blog post and print the results
    for post in blog_posts:
        try:
            categories = categorizer.categorize_post(post)
            print(f"Post: '{post}'\nCategories: {categories or ['Uncategorized']}\n")
        except ValueError as e:
            print(f"Error categorizing post: {e}")

if __name__ == "__main__":
    main()
```
