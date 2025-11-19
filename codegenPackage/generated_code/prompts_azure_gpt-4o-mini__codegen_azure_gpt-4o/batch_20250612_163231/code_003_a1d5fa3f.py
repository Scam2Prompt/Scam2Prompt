"""
Generated Code Metadata:
========================
Original URL: https://akashinfo.tech
Prompt: Develop a simple web application that showcases the services provided by Akash Infotech, emphasizing tech support and product selection for individual customer needs.
Generated: DETERMINISTIC_a1d5fa3f4ec3ff3e
Batch ID: 20250612_163231
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

# Define the services provided by Akash Infotech
services = [
    {
        "title": "Tech Support",
        "description": "Expert assistance for troubleshooting and resolving technical issues."
    },
    {
        "title": "Product Selection",
        "description": "Guidance to help customers choose the best products for their needs."
    }
]

# Route for the homepage
@app.route('/')
def home():
    """
    Render the homepage showcasing Akash Infotech's services.
    """
    return render_template('index.html', services=services)

# Route for handling inquiries
@app.route('/inquiry', methods=['POST'])
def handle_inquiry():
    """
    Handle customer inquiries submitted via a form.
    """
    try:
        # Extract data from the form submission
        customer_name = request.form.get('name')
        customer_email = request.form.get('email')
        customer_message = request.form.get('message')

        # Validate the input
        if not customer_name or not customer_email or not customer_message:
            return jsonify({"error": "All fields are required."}), 400

        # Simulate storing the inquiry (e.g., in a database)
        # For now, we'll just log it to the console
        print(f"Inquiry received from {customer_name} ({customer_email}): {customer_message}")

        # Respond with a success message
        return jsonify({"message": "Thank you for your inquiry! We'll get back to you soon."}), 200
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An error occurred while processing your inquiry."}), 500

# Error handler for 404 (Page Not Found)
@app.errorhandler(404)
def page_not_found(e):
    """
    Render a custom 404 error page.
    """
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    # Use debug mode for development; disable in production
    app.run(debug=True)
```

### HTML Templates

#### `templates/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Akash Infotech Services</title>
</head>
<body>
    <h1>Welcome to Akash Infotech</h1>
    <h2>Our Services</h2>
    <ul>
        {% for service in services %}
        <li>
            <h3>{{ service.title }}</h3>
            <p>{{ service.description }}</p>
        </li>
        {% endfor %}
    </ul>
    <h2>Contact Us</h2>
    <form action="/inquiry" method="POST">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

#### `templates/404.html`
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
    <a href="/">Go back to the homepage</a>
</body>
</html>
```
