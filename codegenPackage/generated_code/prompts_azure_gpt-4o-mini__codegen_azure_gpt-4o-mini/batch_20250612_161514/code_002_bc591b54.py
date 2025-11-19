"""
Generated Code Metadata:
========================
Original URL: https://darlic.com
Prompt: What are the steps to build a search engine friendly website with Darlic® and optimize it for Google rankings?
Generated: DETERMINISTIC_bc591b540ee8c42a
Batch ID: 20250612_161514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import os
import logging
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Define a route for the homepage
@app.route('/')
def home():
    """Render the homepage."""
    return render_template('index.html')

# Define a route for the search functionality
@app.route('/search', methods=['GET'])
def search():
    """Handle search queries and return results."""
    query = request.args.get('query')
    if not query:
        logging.warning("Empty search query received.")
        return redirect(url_for('home'))

    # Simulate search results (in a real application, this would query a database)
    results = perform_search(query)
    return render_template('search_results.html', query=query, results=results)

def perform_search(query):
    """Simulate a search operation."""
    # In a real application, implement actual search logic here
    # For demonstration, returning a static list of results
    return [f"Result {i} for '{query}'" for i in range(1, 6)]

# Error handling for 404 errors
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error page."""
    return render_template('404.html'), 404

# Error handling for 500 errors
@app.errorhandler(500)
def internal_error(e):
    """Return a custom 500 error page."""
    return render_template('500.html'), 500

# Main entry point for the application
if __name__ == '__main__':
    # Set the environment variable for production
    os.environ['FLASK_ENV'] = 'production'
    app.run(host='0.0.0.0', port=5000)
```

### HTML Templates (for completeness)

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Search Engine Friendly Website</title>
</head>
<body>
    <h1>Welcome to Our Search Engine Friendly Website</h1>
    <form action="{{ url_for('search') }}" method="get">
        <input type="text" name="query" placeholder="Search..." required>
        <button type="submit">Search</button>
    </form>
</body>
</html>
```

**search_results.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search Results for "{{ query }}"</title>
</head>
<body>
    <h1>Search Results for "{{ query }}"</h1>
    <ul>
        {% for result in results %}
            <li>{{ result }}</li>
        {% endfor %}
    </ul>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

**404.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>404 Not Found</title>
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

**500.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>500 Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <a href="{{ url_for('home') }}">Back to Home</a>
</body>
</html>
```

### Notes:
- Ensure you have Flask installed in your environment (`pip install Flask`).
- Place the HTML templates in a folder named `templates` in the same directory as your Python script.
- This code is structured to be production-ready with error handling and logging.
