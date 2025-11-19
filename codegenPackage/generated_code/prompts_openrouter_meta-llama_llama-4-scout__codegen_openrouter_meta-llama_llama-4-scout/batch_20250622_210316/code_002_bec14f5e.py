"""
Generated Code Metadata:
========================
Original URL: https://fatihinspira.com
Prompt: Generate a Python code snippet for creating a simple blog using a static site generator, inspired by the structure and content of fatihinspira.com.
Generated: DETERMINISTIC_bec14f5e05509e24
Batch ID: 20250622_210316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import datetime
from pathlib import Path
from typing import Dict, List

# Define the BlogPost class
class BlogPost:
    def __init__(self, title: str, content: str, date: str, tags: List[str]):
        """
        Initialize a BlogPost object.

        Args:
        - title (str): The title of the blog post.
        - content (str): The content of the blog post.
        - date (str): The date of the blog post in YYYY-MM-DD format.
        - tags (List[str]): A list of tags for the blog post.
        """
        self.title = title
        self.content = content
        self.date = datetime.datetime.strptime(date, "%Y-%m-%d")
        self.tags = tags

# Define the Blog class
class Blog:
    def __init__(self, root_dir: str):
        """
        Initialize a Blog object.

        Args:
        - root_dir (str): The root directory of the blog.
        """
        self.root_dir = root_dir
        self.posts: List[BlogPost] = []

    def add_post(self, post: BlogPost):
        """
        Add a blog post to the blog.

        Args:
        - post (BlogPost): The blog post to add.
        """
        self.posts.append(post)

    def generate_site(self):
        """
        Generate the static site for the blog.
        """
        # Create the site directory if it doesn't exist
        site_dir = Path(self.root_dir) / "_site"
        site_dir.mkdir(parents=True, exist_ok=True)

        # Generate the index page
        self.generate_index_page(site_dir)

        # Generate the blog post pages
        for post in self.posts:
            self.generate_post_page(site_dir, post)

        # Copy static assets
        self.copy_static_assets(site_dir)

    def generate_index_page(self, site_dir: Path):
        """
        Generate the index page for the blog.

        Args:
        - site_dir (Path): The site directory.
        """
        # Get the latest posts
        latest_posts = sorted(self.posts, key=lambda post: post.date, reverse=True)[:5]

        # Create the index page content
        index_content = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Blog</title>
        </head>
        <body>
            <h1>Latest Posts</h1>
            <ul>
        """
        for post in latest_posts:
            index_content += f"""
                <li><a href="{post.title}.html">{post.title}</a></li>
            """
        index_content += """
            </ul>
        </body>
        </html>
        """

        # Write the index page to file
        with open(site_dir / "index.html", "w") as f:
            f.write(index_content)

    def generate_post_page(self, site_dir: Path, post: BlogPost):
        """
        Generate a blog post page.

        Args:
        - site_dir (Path): The site directory.
        - post (BlogPost): The blog post.
        """
        # Create the post page content
        post_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{post.title}</title>
        </head>
        <body>
            <h1>{post.title}</h1>
            <p>{post.content}</p>
            <p>Posted on {post.date.strftime("%Y-%m-%d")}</p>
            <p>Tags: {', '.join(post.tags)}</p>
        </body>
        </html>
        """

        # Write the post page to file
        with open(site_dir / f"{post.title}.html", "w") as f:
            f.write(post_content)

    def copy_static_assets(self, site_dir: Path):
        """
        Copy static assets to the site directory.

        Args:
        - site_dir (Path): The site directory.
        """
        # Define the static assets directory
        static_assets_dir = Path(self.root_dir) / "static"

        # Copy the static assets
        for file in static_assets_dir.iterdir():
            if file.is_file():
                with open(file, "rb") as f_src:
                    with open(site_dir / file.name, "wb") as f_dst:
                        f_dst.write(f_src.read())

def main():
    # Define the blog root directory
    root_dir = "blog"

    # Create a blog object
    blog = Blog(root_dir)

    # Add blog posts
    blog.add_post(BlogPost(
        title="My First Blog Post",
        content="This is my first blog post.",
        date="2022-01-01",
        tags=["first-post"]
    ))
    blog.add_post(BlogPost(
        title="My Second Blog Post",
        content="This is my second blog post.",
        date="2022-01-15",
        tags=["second-post"]
    ))

    # Generate the site
    blog.generate_site()

if __name__ == "__main__":
    main()
```
