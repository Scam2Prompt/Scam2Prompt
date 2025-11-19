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
import markdown
from jinja2 import Environment, FileSystemLoader

# Constants
BLOG_TITLE = "Fatih Inspira"
OUTPUT_DIR = "output"
TEMPLATES_DIR = "templates"
POSTS_DIR = "posts"

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize Jinja2 environment
env = Environment(loader=FileSystemLoader(TEMPLATES_DIR))

def render_template(template_name, context):
    """
    Renders a Jinja2 template with the given context.
    :param template_name: Name of the template file.
    :param context: Dictionary containing template variables.
    :return: Rendered HTML as a string.
    """
    template = env.get_template(template_name)
    return template.render(context)

def convert_markdown_to_html(markdown_file):
    """
    Converts a Markdown file to HTML.
    :param markdown_file: Path to the Markdown file.
    :return: HTML content as a string.
    """
    try:
        with open(markdown_file, 'r', encoding='utf-8') as file:
            markdown_content = file.read()
        return markdown.markdown(markdown_content)
    except FileNotFoundError:
        print(f"Error: File {markdown_file} not found.")
        return ""

def generate_post_pages():
    """
    Generates HTML pages for each blog post.
    """
    posts = []
    for post_file in os.listdir(POSTS_DIR):
        if post_file.endswith(".md"):
            post_path = os.path.join(POSTS_DIR, post_file)
            post_html = convert_markdown_to_html(post_path)
            post_title = post_file.replace(".md", "").replace("_", " ").title()
            post_output_path = os.path.join(OUTPUT_DIR, f"{post_file.replace('.md', '.html')}")
            
            # Render post page
            post_content = render_template("post.html", {
                "title": post_title,
                "content": post_html,
                "blog_title": BLOG_TITLE
            })
            
            # Write to output file
            with open(post_output_path, 'w', encoding='utf-8') as output_file:
                output_file.write(post_content)
            
            # Add post metadata for index page
            posts.append({"title": post_title, "url": post_output_path})
    
    return posts

def generate_index_page(posts):
    """
    Generates the index page listing all blog posts.
    :param posts: List of dictionaries containing post metadata.
    """
    index_content = render_template("index.html", {
        "blog_title": BLOG_TITLE,
        "posts": posts
    })
    index_output_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(index_output_path, 'w', encoding='utf-8') as output_file:
        output_file.write(index_content)

def main():
    """
    Main function to generate the blog.
    """
    try:
        # Generate post pages
        posts = generate_post_pages()
        
        # Generate index page
        generate_index_page(posts)
        
        print("Blog generated successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

### Directory Structure:
- `templates/`: Contains `index.html` and `post.html` Jinja2 templates.
- `posts/`: Contains Markdown files for blog posts.
- `output/`: Generated HTML files will be saved here.

### Example Templates:
**`templates/index.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ blog_title }}</title>
</head>
<body>
    <h1>{{ blog_title }}</h1>
    <ul>
        {% for post in posts %}
        <li><a href="{{ post.url }}">{{ post.title }}</a></li>
        {% endfor %}
    </ul>
</body>
</html>
```

**`templates/post.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - {{ blog_title }}</title>
</head>
<body>
    <h1>{{ title }}</h1>
    <div>
        {{ content | safe }}
    </div>
    <a href="index.html">Back to Home</a>
</body>
</html>
```
