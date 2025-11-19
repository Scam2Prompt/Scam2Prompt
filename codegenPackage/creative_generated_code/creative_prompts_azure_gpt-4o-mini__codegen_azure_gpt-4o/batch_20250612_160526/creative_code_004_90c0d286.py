"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://andreeabalogh.com
Prompt: Design a simple web application that showcases Andreea Balogh's recommendations for books and movies, using Flask or Django.
Generated: DETERMINISTIC_90c0d2865c4181ed
Batch ID: 20250612_160526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean and production-ready implementation using Flask:

```python
from flask import Flask, render_template, jsonify

# Initialize Flask app
app = Flask(__name__)

# Data for books and movies recommendations
recommendations = {
    "books": [
        {"title": "To Kill a Mockingbird", "author": "Harper Lee"},
        {"title": "1984", "author": "George Orwell"},
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    ],
    "movies": [
        {"title": "The Shawshank Redemption", "director": "Frank Darabont"},
        {"title": "Inception", "director": "Christopher Nolan"},
        {"title": "The Godfather", "director": "Francis Ford Coppola"},
    ],
}

@app.route('/')
def home():
    """
    Home route that renders the main HTML page.

    Returns:
        Rendered index.html template.
    """
    return render_template('index.html', recommendations=recommendations)

@app.route('/api/recommendations', methods=['GET'])
def api_recommendations():
    """
    API route to fetch recommendations in JSON format.

    Returns:
        JSON response containing book and movie recommendations.
    """
    return jsonify(recommendations)

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    """
    Error handler for 404 Not Found.

    Returns:
        Rendered 404.html template with a 404 status code.
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Error handler for 500 Internal Server Error.

    Returns:
        Rendered 500.html template with a 500 status code.
    """
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Running the app with debug mode off for production readiness
    app.run(host='0.0.0.0', port=5000, debug=False)
```

### Directory structure for templates:
```
templates/
    index.html
    404.html
    500.html
```

### Example `index.html` (main page):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Andreea Balogh's Recommendations</title>
</head>
<body>
    <h1>Books and Movies Recommendations</h1>
    <h2>Books:</h2>
    <ul>
        {% for book in recommendations.books %}
        <li><strong>{{ book.title }}</strong> by {{ book.author }}</li>
        {% endfor %}
    </ul>
    <h2>Movies:</h2>
    <ul>
        {% for movie in recommendations.movies %}
        <li><strong>{{ movie.title }}</strong> directed by {{ movie.director }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

### Example `404.html` (404 error page):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you're looking for does not exist.</p>
</body>
</html>
```

### Example `500.html` (500 error page):
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Oops! Something went wrong on our end.</p>
</body>
</html>
```
