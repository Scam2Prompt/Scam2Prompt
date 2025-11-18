"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://epicpinterestfail.com
Prompt: Generate code to filter blog posts by tags such as "Dental," "Surgery," and "Health" and display them in a user-friendly interface.
Generated: DETERMINISTIC_5481b3a3e7ee2ba2
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's the code to filter blog posts by tags and display them in a user-friendly interface using Python and Flask with HTML templates.

### Python (Flask) Code

```python
from flask import Flask, render_template, request

app = Flask(__name__)

# Sample blog post data
BLOG_POSTS = [
    {"title": "Dental Care Tips", "content": "Learn how to take care of your teeth.", "tags": ["Dental", "Health"]},
    {"title": "Surgery Preparation", "content": "Steps to prepare for surgery.", "tags": ["Surgery", "Health"]},
    {"title": "Healthy Eating", "content": "Balanced diet for a healthy life.", "tags": ["Health"]},
    {"title": "Dental Implants", "content": "Everything about dental implants.", "tags": ["Dental"]},
]

@app.route('/')
def home():
    """
    Render the homepage where users can input tags to filter blog posts.
    """
    return render_template("index.html")


@app.route('/filter', methods=['POST'])
def filter_posts():
    """
    Filter blog posts based on user-provided tags.
    """
    try:
        # Get the tags from the form input
        tags = request.form.get('tags')
        if not tags:
            return render_template("index.html", posts=[], error="No tags provided.")

        # Convert comma-separated tags into a list
        filter_tags = [tag.strip() for tag in tags.split(",")]

        # Filter blog posts that match the tags
        filtered_posts = [
            post for post in BLOG_POSTS if any(tag in post["tags"] for tag in filter_tags)
        ]

        # Render the filtered posts
        return render_template("index.html", posts=filtered_posts, error=None)

    except Exception as e:
        # Handle unexpected errors gracefully
        return render_template("index.html", posts=[], error=f"An error occurred: {str(e)}")


if __name__ == '__main__':
    app.run(debug=True)
```

### HTML Template: `templates/index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Filter Blog Posts</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Filter Blog Posts by Tags</h1>
        <form method="POST" action="/filter">
            <label for="tags">Enter Tags (comma-separated):</label><br>
            <input type="text" id="tags" name="tags" placeholder="e.g., Dental, Surgery, Health" required>
            <br><br>
            <button type="submit">Filter</button>
        </form>
        <br>
        {% if error %}
            <p class="error">{{ error }}</p>
        {% endif %}
        {% if posts %}
            <h2>Filtered Blog Posts</h2>
            <ul>
                {% for post in posts %}
                    <li>
                        <h3>{{ post.title }}</h3>
                        <p>{{ post.content }}</p>
                        <strong>Tags:</strong> {{ post.tags | join(", ") }}
                    </li>
                {% endfor %}
            </ul>
        {% else %}
            <p>No blog posts found.</p>
        {% endif %}
    </div>
</body>
</html>
```

### Key Notes:
- The Python script uses Flask as the backend framework.
- The HTML template (`index.html`) displays the filtered blog posts in a user-friendly format.
- Error handling is implemented to manage empty input and unexpected errors.
- Ensure Flask is installed (`pip install flask`) before running the code.
