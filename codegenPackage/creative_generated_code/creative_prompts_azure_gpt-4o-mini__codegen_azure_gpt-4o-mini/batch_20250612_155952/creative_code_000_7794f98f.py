"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maximaseducao.fun
Prompt: Generate a code snippet for a website hosting service that includes error handling for "Page Not Found" scenarios.
Generated: DETERMINISTIC_7794f98fb62240da
Batch ID: 20250612_155952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom handler for 404 errors (Page Not Found).
    
    Args:
        e: The error object.

    Returns:
        A rendered HTML template for the 404 error page.
    """
    return render_template('404.html'), 404

@app.route('/')
def home():
    """
    Home route, renders the main page of the website.
    
    Returns:
        A rendered HTML template for the home page.
    """
    return render_template('home.html')

@app.route('/api/data')
def get_data():
    """
    Example API endpoint that returns sample data.
    
    Returns:
        JSON response containing sample data.
    """
    try:
        data = {'message': 'Welcome to the API!', 'status': 'success'}
        return jsonify(data), 200
    except Exception as e:
        # Log the exception (implement logging as per your logging strategy)
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=False)  # Set debug to True during development only
```

**Note:** Ensure that you have the `404.html` and `home.html` templates created in the appropriate `templates` directory for this code to function correctly.
