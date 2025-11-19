"""
Generated Code Metadata:
========================
Original URL: https://eigenlab.io
Prompt: What is the purpose of a personal tech blog, and how can it be used to share reflections on technology?
Generated: DETERMINISTIC_1ab165d67b405776
Batch ID: 20250622_212411
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Personal Tech Blog Purpose and Usage
=====================================

This module provides a basic structure for a personal tech blog.
It includes classes for BlogPost and TechBlog, allowing users to create and manage their own tech blog.

Classes:
    BlogPost: Represents a single blog post with title, content, and tags.
    TechBlog: Manages a collection of blog posts and provides methods for adding, removing, and displaying posts.

Functions:
    main: Example usage of the TechBlog class.

"""

class BlogPost:
    """
    Represents a single blog post.

    Attributes:
        title (str): The title of the blog post.
        content (str): The content of the blog post.
        tags (list): A list of tags associated with the blog post.

    """

    def __init__(self, title, content, tags=None):
        """
        Initializes a BlogPost object.

        Args:
            title (str): The title of the blog post.
            content (str): The content of the blog post.
            tags (list, optional): A list of tags. Defaults to None.

        """
        self.title = title
        self.content = content
        self.tags = tags if tags is not None else []

    def __str__(self):
        """
        Returns a string representation of the blog post.

        Returns:
            str: The title and content of the blog post.

        """
        return f"{self.title}\n{self.content}"


class TechBlog:
    """
    Manages a collection of blog posts.

    Attributes:
        posts (list): A list of BlogPost objects.

    """

    def __init__(self):
        """
        Initializes a TechBlog object.

        """
        self.posts = []

    def add_post(self, post):
        """
        Adds a blog post to the collection.

        Args:
            post (BlogPost): The blog post to add.

        """
        self.posts.append(post)

    def remove_post(self, post_title):
        """
        Removes a blog post from the collection by title.

        Args:
            post_title (str): The title of the blog post to remove.

        """
        self.posts = [post for post in self.posts if post.title != post_title]

    def display_posts(self):
        """
        Displays all blog posts in the collection.

        """
        for post in self.posts:
            print(post)
            print("Tags:", post.tags)
            print("------------------------")

    def search_posts_by_tag(self, tag):
        """
        Searches for blog posts by tag.

        Args:
            tag (str): The tag to search for.

        Returns:
            list: A list of blog posts with the specified tag.

        """
        return [post for post in self.posts if tag in post.tags]


def main():
    """
    Example usage of the TechBlog class.

    """
    blog = TechBlog()

    post1 = BlogPost("My First Post", "This is my first blog post.", ["tech", "blog"])
    post2 = BlogPost("My Second Post", "This is my second blog post.", ["tech", "programming"])

    blog.add_post(post1)
    blog.add_post(post2)

    print("All Posts:")
    blog.display_posts()

    print("\nPosts with tag 'tech':")
    tech_posts = blog.search_posts_by_tag("tech")
    for post in tech_posts:
        print(post.title)

    blog.remove_post("My First Post")

    print("\nPosts after removal:")
    blog.display_posts()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", str(e))
```
