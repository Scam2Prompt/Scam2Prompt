"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: Design a simple web application using Flask that allows users to explore Alghanim Capital's investment services, including private equity, wealth management, and real estate investment, with interactive features.
Generated: DETERMINISTIC_ad4aef61afaee9a2
Batch ID: 20250612_162811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define the investment services offered
investment_services = {
    "private_equity": {
        "title": "Private Equity",
        "description": "Explore opportunities in private equity investments tailored to your needs."
    },
    "wealth_management": {
        "title": "Wealth Management",
        "description": "Comprehensive wealth management solutions to grow and protect your assets."
    },
    "real_estate_investment": {
        "title": "Real Estate Investment",
        "description": "Invest in high-value real estate opportunities with expert guidance."
    }
}

@app.route('/')
def home():
    """
    Home route that displays the main page with links to investment services.
    """
    return render_template('home.html', services=investment_services)

@app.route('/service/<service_name>')
def service_detail(service_name):
    """
    Route to display details of a specific investment service.
    :param service_name: Name of the investment service to display.
    """
    service = investment_services.get(service_name)
    if not service:
        return render_template('404.html'), 404
    return render_template('service_detail.html', service=service)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """
    Route for the contact form. Handles both GET and POST requests.
    """
    if request.method == 'POST':
        # Handle form submission
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Basic validation
        if not name or not email or not message:
            return jsonify({"error": "All fields are required"}), 400

        # In a production app, you would save this data to a database or send an email
        return jsonify({"success": "Thank you for contacting us!"}), 200

    # Render the contact form for GET requests
    return render_template('contact.html')

@app.errorhandler(404)
def page_not_found(e):
    """
    Custom 404 error handler.
    """
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Templates (HTML files)
Below are the HTML templates required for the application. Save them in a `templates` folder.

#### `home.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alghanim Capital</title>
</head>
<body>
    <h1>Welcome to Alghanim Capital</h1>
    <p>Explore our investment services:</p>
    <ul>
        {% for key, service in services.items() %}
        <li><a href="/service/{{ key }}">{{ service.title }}</a></li>
        {% endfor %}
    </ul>
    <a href="/contact">Contact Us</a>
</body>
</html>
```

#### `service_detail.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ service.title }}</title>
</head>
<body>
    <h1>{{ service.title }}</h1>
    <p>{{ service.description }}</p>
    <a href="/">Back to Home</a>
</body>
</html>
```

#### `contact.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST" action="/contact">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea><br>
        <button type="submit">Submit</button>
    </form>
    <a href="/">Back to Home</a>
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
</head>
<body>
    <h1>404 - Page Not Found</h1>
    <p>Sorry, the page you are looking for does not exist.</p>
    <a href="/">Back to Home</a>
</body>
</html>
```
