"""
Generated Code Metadata:
========================
Original URL: https://epicpinterestfail.com
Prompt: Generate code to filter blog posts by tags such as "Dental," "Surgery," and "Health" and display them in a user-friendly interface.
Generated: DETERMINISTIC_5481b3a3e7ee2ba2
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blog_post_filter.py

from typing import List, Dict

class BlogPost:
    """Represents a blog post with a title, content, and tags."""

    def __init__(self, title: str, content: str, tags: List[str]):
        """
        Initializes a BlogPost object.

        Args:
            title (str): The title of the blog post.
            content (str): The content of the blog post.
            tags (List[str]): A list of tags associated with the blog post.
        """
        self.title = title
        self.content = content
        self.tags = tags

class BlogPostFilter:
    """Filters blog posts by tags and displays them in a user-friendly interface."""

    def __init__(self, blog_posts: List[BlogPost]):
        """
        Initializes a BlogPostFilter object.

        Args:
            blog_posts (List[BlogPost]): A list of BlogPost objects.
        """
        self.blog_posts = blog_posts

    def filter_by_tag(self, tag: str) -> List[BlogPost]:
        """
        Filters blog posts by a specific tag.

        Args:
            tag (str): The tag to filter by.

        Returns:
            List[BlogPost]: A list of BlogPost objects that match the specified tag.
        """
        return [post for post in self.blog_posts if tag in post.tags]

    def display_blog_posts(self, blog_posts: List[BlogPost]) -> None:
        """
        Displays a list of blog posts in a user-friendly interface.

        Args:
            blog_posts (List[BlogPost]): A list of BlogPost objects to display.
        """
        if not blog_posts:
            print("No blog posts found.")
            return

        for i, post in enumerate(blog_posts, start=1):
            print(f"**{i}. {post.title}**")
            print(f"Tags: {', '.join(post.tags)}")
            print(post.content)
            print("------------------------")

def main() -> None:
    # Create sample blog posts
    blog_posts = [
        BlogPost("Dental Care Tips", "Regular brushing and flossing are essential for good oral health.", ["Dental", "Health"]),
        BlogPost("Surgery Recovery", "It's essential to follow your doctor's instructions after surgery.", ["Surgery", "Health"]),
        BlogPost("The Importance of Flossing", "Flossing helps prevent gum disease and bad breath.", ["Dental", "Health"]),
        BlogPost("Types of Dental Surgery", "There are several types of dental surgery, including root canals and extractions.", ["Dental", "Surgery"]),
    ]

    # Create a BlogPostFilter object
    filter = BlogPostFilter(blog_posts)

    # Display available tags
    available_tags = set(tag for post in blog_posts for tag in post.tags)
    print("Available tags:")
    for i, tag in enumerate(available_tags, start=1):
        print(f"{i}. {tag}")

    # Get user input
    while True:
        try:
            choice = int(input("Enter the number of a tag to filter by, or 0 to exit: "))
            if choice == 0:
                break
            elif 1 <= choice <= len(available_tags):
                tag = list(available_tags)[choice - 1]
                filtered_posts = filter.filter_by_tag(tag)
                filter.display_blog_posts(filtered_posts)
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
```
