"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wahedabdelmajed.com
Prompt: Suggest a framework for building a personal website that features articles on philosophical topics, inspired by the content of Dr. Wahed Abdel Majid's official site.
Generated: DETERMINISTIC_8bd005aef80514c0
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Framework: Flask (Python Web Framework)
Description: Flask is lightweight, flexible, and ideal for building personal websites. It supports routing, templates, and easy integration with databases.
Below is an example for a simple personal website structure featuring articles on philosophical topics.
"""

from flask import Flask, render_template, request, abort
import os

# Initialize the Flask application
app = Flask(__name__)

# Sample data: List of philosophical articles
articles = [
    {
        "id": 1,
        "title": "The Nature of Reality",
        "author": "Dr. Wahed Abdel Majid",
        "content": "Reality is a construct that has puzzled philosophers for centuries..."
    },
    {
        "id": 2,
        "title": "Ethics and Morality",
        "author": "Dr. Wahed Abdel Majid",
        "content": "Ethics is the branch of philosophy that involves systematizing, defending, and recommending concepts of right and wrong conduct..."
    },
    {
        "id": 3,
        "title": "Existentialism Explored",
        "author": "Dr. Wahed Abdel Majid",
        "content": "Existentialism emphasizes individual freedom, choice, and responsibility..."
    }
]

# Home route to display the homepage
@app.route("/")
def home():
    """
    Render the homepage.
    """
    return render_template("index.html", articles=articles)

# Route to display a specific article
@app.route("/article/<int:article_id>")
def article(article_id):
    """
    Render a specific article based on the article ID.
    Handles cases where the article ID is invalid.
    """
    # Find the article by ID
    article = next((a for a in articles if a["id"] == article_id), None)
    
    if article is None:
        # Return 404 error if the article is not found
        abort(404)
    
    return render_template("article.html", article=article)

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom error page for 404 errors.
    """
    return render_template("404.html"), 404

# Run the Flask application
if __name__ == "__main__":
    # Set the debug mode based on environment
    app.run(debug=os.getenv("FLASK_DEBUG", "true").lower() == "true")
```

```html
<!-- index.html: Homepage template -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Philosophy Articles</title>
</head>
<body>
    <h1>Welcome to Philosophy Articles</h1>
    <ul>
        <!-- Loop through articles and display links -->
        {% for article in articles %}
        <li>
            <a href="/article/{{ article.id }}">{{ article.title }}</a> by {{ article.author }}
        </li>
        {% endfor %}
    </ul>
</body>
</html>
```

```html
<!-- article.html: Article template -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ article.title }}</title>
</head>
<body>
    <h1>{{ article.title }}</h1>
    <p><strong>Author:</strong> {{ article.author }}</p>
    <p>{{ article.content }}</p>
    <a href="/">Back to homepage</a>
</body>
</html>
```

```html
<!-- 404.html: Custom 404 error page -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="/">Go back to homepage</a>
</body>
</html>
```

### Notes:
1. Save the Python code in a file named `app.py`.
2. Save the HTML files in a folder named `templates`.
3. Run the application by executing `python app.py`.
4. Flask requires the installation of `flask` via `pip install flask`.
