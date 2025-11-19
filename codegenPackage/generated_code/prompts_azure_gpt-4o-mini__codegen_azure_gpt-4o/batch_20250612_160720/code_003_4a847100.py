"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Create a web application outline that includes sections for Spiritual Therapy and Online Courses as described on the Darul Raza site.
Generated: DETERMINISTIC_4a847100032dfdf1
Batch ID: 20250612_160720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define routes for the web application

@app.route('/')
def home():
    """
    Home page route.
    Displays the main landing page of the web application.
    """
    return render_template('home.html')  # Render the home page template

@app.route('/spiritual-therapy')
def spiritual_therapy():
    """
    Spiritual Therapy page route.
    Displays information and resources related to spiritual therapy.
    """
    return render_template('spiritual_therapy.html')  # Render the spiritual therapy page template

@app.route('/online-courses')
def online_courses():
    """
    Online Courses page route.
    Displays a list of available online courses and their details.
    """
    return render_template('online_courses.html')  # Render the online courses page template

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Contact page route.
    Handles user inquiries via a contact form.
    """
    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Basic validation
        if not name or not email or not message:
            return jsonify({'error': 'All fields are required'}), 400

        # Process the form data (e.g., save to database, send email, etc.)
        # For demonstration, we'll just return a success message
        return jsonify({'success': 'Your message has been received!'}), 200

    return render_template('contact.html')  # Render the contact page template

# Error handling routes
@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error handler.
    Displays a user-friendly message when a page is not found.
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    """
    Custom 500 error handler.
    Displays a user-friendly message when an internal server error occurs.
    """
    return render_template('500.html'), 500

# Main entry point for running the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)  # Set debug=True for development; change to False for production
```

### Notes:
- This code assumes the existence of HTML templates (`home.html`, `spiritual_therapy.html`, `online_courses.html`, `contact.html`, `404.html`, and `500.html`) in a `templates` directory.
- Replace `debug=True` with `debug=False` in production for better security and performance.
- Additional features like database integration, authentication, and styling can be added as needed.
