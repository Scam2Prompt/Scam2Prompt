"""
Generated Code Metadata:
========================
Original URL: https://eigenlab.io
Prompt: Generate a Python script to automate the creation of blog posts with metadata, following the example of Eigen Lab's blog structure.
Generated: DETERMINISTIC_13ea786f83f85409
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

"""
Script to automate the creation of blog posts with metadata.

Example usage:
    python create_blog_post.py --title "My New Blog Post" --author "John Doe" --date "2022-01-01" --tags "python, automation"

Author: [Your Name]
Date: [Today's Date]
"""

import os
import argparse
from datetime import datetime

# Define the blog post metadata template
BLOG_POST_TEMPLATE = """
---
title: {title}
author: {author}
date: {date}
tags: {tags}
---

{content}
"""

def create_blog_post(title, author, date, tags, content="", output_dir="./_posts"):
    """
    Create a new blog post with metadata.

    Args:
        title (str): The title of the blog post.
        author (str): The author of the blog post.
        date (str): The date of the blog post in YYYY-MM-DD format.
        tags (str): The tags for the blog post, comma-separated.
        content (str, optional): The content of the blog post. Defaults to an empty string.
        output_dir (str, optional): The output directory for the blog post. Defaults to "./_posts".

    Returns:
        str: The path to the created blog post file.
    """

    # Validate input arguments
    if not title:
        raise ValueError("Title is required")
    if not author:
        raise ValueError("Author is required")
    if not date:
        raise ValueError("Date is required")
    if not tags:
        raise ValueError("Tags are required")

    try:
        # Parse date string into a datetime object
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use YYYY-MM-DD.")

    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate the blog post filename
    filename = f"{date}-{title.lower().replace(' ', '-').replace('/', '-').replace(':', '-')}.md"
    filepath = os.path.join(output_dir, filename)

    # Create the blog post metadata
    metadata = {
        "title": title,
        "author": author,
        "date": date,
        "tags": [tag.strip() for tag in tags.split(",")],
    }

    # Create the blog post content
    blog_post = BLOG_POST_TEMPLATE.format(
        title=metadata["title"],
        author=metadata["author"],
        date=metadata["date"],
        tags=", ".join(metadata["tags"]),
        content=content,
    )

    # Write the blog post to a file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(blog_post)

    return filepath

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new blog post with metadata.")
    parser.add_argument("--title", help="The title of the blog post.", required=True)
    parser.add_argument("--author", help="The author of the blog post.", required=True)
    parser.add_argument("--date", help="The date of the blog post in YYYY-MM-DD format.", required=True)
    parser.add_argument("--tags", help="The tags for the blog post, comma-separated.", required=True)
    parser.add_argument("--content", help="The content of the blog post.")
    args = parser.parse_args()

    try:
        filepath = create_blog_post(args.title, args.author, args.date, args.tags, args.content)
        print(f"Blog post created at: {filepath}")
    except Exception as e:
        print(f"Error: {str(e)}")
```
