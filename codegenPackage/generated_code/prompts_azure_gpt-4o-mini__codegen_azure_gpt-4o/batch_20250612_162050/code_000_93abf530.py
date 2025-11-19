"""
Generated Code Metadata:
========================
Original URL: https://helenhuangauthor.com
Prompt: Generate a code snippet for a web application that showcases a political thriller book, specifically focusing on the themes and characters of "Nuclear Power Nuclear Game" by Helen Huang.
Generated: DETERMINISTIC_93abf530c62fe6ab
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask application to showcase the political thriller book "Nuclear Power Nuclear Game" by Helen Huang

from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Book data
book_data = {
    "title": "Nuclear Power Nuclear Game",
    "author": "Helen Huang",
    "description": (
        "A gripping political thriller that delves into the complex themes of power, "
        "betrayal, and international intrigue. The story revolves around the dangerous "
        "game of nuclear power and the characters caught in its web."
    ),
    "themes": [
        "Political intrigue",
        "Betrayal",
        "International espionage",
        "Nuclear power dynamics"
    ],
    "characters": [
        {"name": "Dr. David Smith", "role": "Nuclear scientist with a dark secret"},
        {"name": "Agent Sarah Johnson", "role": "CIA operative investigating nuclear threats"},
        {"name": "General Viktor Ivanov", "role": "Russian military leader with hidden motives"},
        {"name": "President Michael Carter", "role": "US President navigating political turmoil"}
    ]
}

# Route to render the homepage
@app.route("/")
def home():
    """
    Render the homepage showcasing the book details.
    """
    return render_template("index.html", book=book_data)

# Route to provide book data as JSON
@app.route("/api/book")
def book_api():
    """
    Provide book details as a JSON response.
    """
    return jsonify(book_data)

# Error handling for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a custom message.
    """
    return render_template("404.html"), 404

# Main entry point
if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True)

```

### HTML Templates (to be saved in a `templates` folder):

#### `index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ book.title }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        h1, h2 {
            color: #333;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <h1>{{ book.title }}</h1>
    <h2>By {{ book.author }}</h2>
    <p>{{ book.description }}</p>
    <h3>Themes:</h3>
    <ul>
        {% for theme in book.themes %}
        <li>{{ theme }}</li>
        {% endfor %}
    </ul>
    <h3>Characters:</h3>
    <ul>
        {% for character in book.characters %}
        <li><strong>{{ character.name }}</strong>: {{ character.role }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

#### `404.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            margin: 50px;
        }
        h1 {
            color: #d9534f;
        }
    </style>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="/">Go back to the homepage</a>
</body>
</html>
```
