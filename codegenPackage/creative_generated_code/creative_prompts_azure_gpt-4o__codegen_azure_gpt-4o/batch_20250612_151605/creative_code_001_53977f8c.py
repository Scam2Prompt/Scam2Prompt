"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://runetech0.github.io
Prompt: Generate a code snippet to update a Jekyll-based blog with new content, ensuring compatibility with the Chirpy theme used by Rune Tech.
Generated: DETERMINISTIC_53977f8cdd46b136
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import datetime
import shutil

def create_new_post(title, content, tags=None, category="blog"):
    """
    Creates a new Markdown file for a Jekyll-based blog post, compatible with Chirpy theme.
    Args:
        title (str): Title of the blog post.
        content (str): Content of the blog post.
        tags (list, optional): List of tags for the post. Defaults to None.
        category (str, optional): Category of the post. Defaults to "blog".
    """
    try:
        # Sanitize title for file naming
        sanitized_title = title.lower().replace(" ", "-").replace("'", "").replace('"', "")
        
        # Get current date and time
        today = datetime.datetime.now()
        date_str = today.strftime("%Y-%m-%d")
        time_str = today.strftime("%H:%M:%S")

        # Construct filename and path
        posts_dir = "_posts"
        file_name = f"{date_str}-{sanitized_title}.md"
        file_path = os.path.join(posts_dir, file_name)

        # Ensure posts directory exists
        if not os.path.exists(posts_dir):
            os.makedirs(posts_dir)

        # Build YAML front matter (required by Jekyll and Chirpy)
        yaml_front_matter = f"""---
layout: post
title: "{title}"
date: {date_str} {time_str} +0000
categories: [{category}]
tags: {tags if tags else []}
---
"""

        # Write content to Markdown file
        with open(file_path, "w", encoding="utf-8") as post_file:
            post_file.write(yaml_front_matter + "\n" + content)

        print(f"Post created successfully: {file_path}")

    except Exception as e:
        print(f"Error creating post: {e}")

# Example usage
if __name__ == "__main__":
    post_title = "Understanding Chirpy Theme"
    post_content = """\
The Chirpy theme is a powerful Jekyll-based theme that provides a sleek design and easy integration for tech-focused blogs.
In this post, we explore its features and demonstrate how to set up a blog with Chirpy.
"""
    post_tags = ["chirpy", "jekyll", "themes", "blogging"]
    post_category = "tech"

    create_new_post(post_title, post_content, tags=post_tags, category=post_category)
```
