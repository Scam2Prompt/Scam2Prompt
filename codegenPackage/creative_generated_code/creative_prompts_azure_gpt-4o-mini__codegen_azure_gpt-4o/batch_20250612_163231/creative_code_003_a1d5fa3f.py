"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://akashinfo.tech
Prompt: Develop a simple web application that showcases the services provided by Akash Infotech, emphasizing tech support and product selection for individual customer needs.
Generated: DETERMINISTIC_a1d5fa3f4ec3ff3e
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define the list of services provided by Akash Infotech
services = [
    {"id": 1, "name": "Tech Support", "description": "Providing expert technical assistance to resolve IT issues."},
    {"id": 2, "name": "Product Selection", "description": "Helping customers choose the best products for their needs."},
    {"id": 3, "name": "Custom Solutions", "description": "Tailored solutions for business and individual IT requirements."},
]

# Route for the home page
@app.route('/')
def home():
    """
    Render the home page of the Akash Infotech web application.
    """
    return render_template('index.html', services=services)

# Route for service details
@app.route('/service/<int:service_id>')
def service_detail(service_id):
    """
    Render the details of a specific service.

    :param service_id: ID of the requested service.
    """
    service = next((s for s in services if s['id'] == service_id), None)
    if service is None:
        return jsonify({"error": "Service not found"}), 404
    return render_template('service_detail.html', service=service)

# Error handler for 404 errors
@app.errorhandler(404)
def page_not_found(error):
    """
    Handle 404 errors with a user-friendly response.
    """
    return render_template('404.html'), 404

# Run the application
if __name__ == '__main__':
    # Ensure debug mode is enabled only for local development
    app.run(debug=True)


# Templates

# index.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Akash Infotech - Services</title>
</head>
<body>
    <h1>Welcome to Akash Infotech</h1>
    <p>We provide a variety of IT services to cater to your needs.</p>
    <h2>Our Services</h2>
    <ul>
        {% for service in services %}
        <li>
            <a href="/service/{{ service.id }}">{{ service.name }}</a>: {{ service.description }}
        </li>
        {% endfor %}
    </ul>
</body>
</html>
"""

# service_detail.html
"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Service Details</title>
</head>
<body>
    <h1>{{ service.name }}</h1>
    <p>{{ service.description }}</p>
    <a href="/">Back to Home</a>
</body>
</html>
"""

# 404.html
"""
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
    <a href="/">Back to Home</a>
</body>
</html>
"""
```
