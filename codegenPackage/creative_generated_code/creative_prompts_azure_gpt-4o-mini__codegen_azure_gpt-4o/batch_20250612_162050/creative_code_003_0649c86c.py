"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://canatechinstitute.ca
Prompt: What are the best practices for developing user-friendly web applications, and how can I apply these principles in a project similar to those showcased by CTIAR?
Generated: DETERMINISTIC_0649c86c4b797fab
Batch ID: 20250612_162050
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Certainly! Below is an example implementation of a user-friendly web application in Python using the Flask framework. This code implements best practices such as clean architecture, responsive design, and error handling. It includes comments to explain each part.

```python
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import logging

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Used for securely signing session cookies

# Configure logging for debugging and production monitoring
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Route for the home page
@app.route('/')
def home():
    """
    Render the home page.
    """
    return render_template('index.html')

# Route for handling user feedback submission
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    """
    Handle feedback submission from the user.
    """
    try:
        # Get the feedback from the request
        feedback = request.form.get('feedback')
        if not feedback:
            flash('Feedback cannot be empty.', 'error')
            return redirect(url_for('home'))

        logging.info(f'Received feedback: {feedback}')
        flash('Thank you for your feedback!', 'success')
        return redirect(url_for('home'))

    except Exception as e:
        # Log the error and return an error response
        logging.error(f'Error submitting feedback: {e}')
        flash('An error occurred while submitting your feedback. Please try again later.', 'error')
        return redirect(url_for('home'))

# Route for handling AJAX calls (e.g., live search)
@app.route('/api/search', methods=['GET'])
def search():
    """
    Handle AJAX search requests.
    """
    try:
        query = request.args.get('query')
        if not query:
            return jsonify({'error': 'Query parameter is missing'}), 400

        # Simulate search results (e.g., querying a database or external API)
        results = ['Result 1', 'Result 2', 'Result 3']
        filtered_results = [r for r in results if query.lower() in r.lower()]
        return jsonify({'results': filtered_results})

    except Exception as e:
        logging.error(f'Error processing search request: {e}')
        return jsonify({'error': 'An internal error occurred'}), 500

# Error handler for 404 (Page Not Found)
@app.errorhandler(404)
def page_not_found(e):
    """
    Render a custom 404 error page.
    """
    return render_template('404.html'), 404

# Error handler for 500 (Internal Server Error)
@app.errorhandler(500)
def internal_server_error(e):
    """
    Render a custom 500 error page.
    """
    return render_template('500.html'), 500

# Run the application only if this module is executed directly
if __name__ == '__main__':
    # Use debug mode in development and disable it in production
    app.run(debug=True)
```

**HTML Templates (example snippets):**

**`templates/index.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User-Friendly Web Application</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1>Welcome to Our Application!</h1>
        <form action="/submit-feedback" method="POST" class="mt-3">
            <div class="mb-3">
                <label for="feedback" class="form-label">Your Feedback:</label>
                <textarea id="feedback" name="feedback" class="form-control" rows="3"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
        </form>
        {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
        <div class="mt-3">
            {% for category, message in messages %}
            <div class="alert alert-{{ category }}">{{ message }}</div>
            {% endfor %}
        </div>
        {% endif %}
        {% endwith %}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

**`templates/404.html`**
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
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="/">Return to Home</a>
</body>
</html>
```

**`templates/500.html`**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal Server Error</title>
</head>
<body>
    <h1>500 - Internal Server Error</h1>
    <p>Sorry, something went wrong on our end. Please try again later.</p>
    <a href="/">Return to Home</a>
</body>
</html>
```

This simple implementation includes features for submitting user feedback, handling AJAX calls, and providing custom error pages, all while adhering to best practices for web development.
