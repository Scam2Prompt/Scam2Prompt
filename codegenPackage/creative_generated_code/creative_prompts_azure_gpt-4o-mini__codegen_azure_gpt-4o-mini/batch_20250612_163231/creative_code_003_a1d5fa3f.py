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
from flask import Flask, render_template, request, flash, redirect
import logging

# Initialize the Flask application
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a secure key

# Set up logging to file
logging.basicConfig(filename='app.log', level=logging.INFO)

# Home route
@app.route('/')
def home():
    """Render the home page that showcases services provided by Akash Infotech."""
    return render_template('index.html')

# Tech Support route
@app.route('/tech-support', methods=['GET', 'POST'])
def tech_support():
    """Render the tech support page and handle inquiries from users."""
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Basic error handling
        if not name or not email or not message:
            flash('All fields are required!', 'error')
            return redirect('/tech-support')
        
        # Log the inquiry
        logging.info(f'Tech Support Inquiry - Name: {name}, Email: {email}, Message: {message}')
        flash('Your inquiry has been submitted!', 'success')
        return redirect('/tech-support')

    return render_template('tech_support.html')

# Product Selection route
@app.route('/product-selection')
def product_selection():
    """Render the product selection page for customers."""
    return render_template('product_selection.html')

# Error handler for 404 - Page Not Found
@app.errorhandler(404)
def page_not_found(e):
    """Render a custom 404 page."""
    return render_template('404.html'), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(e):
    """Render a custom 500 page."""
    logging.error(f'Internal Server Error: {e}')
    return render_template('500.html'), 500

# Entry point for the application
if __name__ == '__main__':
    try:
        # Running the Flask app
        app.run(debug=True)  # Set debug=False in production
    except Exception as e:
        logging.error(f'Failed to start the application: {e}')
```

### HTML Templates

#### index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Akash Infotech</title>
</head>
<body>
    <h1>Welcome to Akash Infotech</h1>
    <h2>Our Services</h2>
    <ul>
        <li><a href="/tech-support">Tech Support</a></li>
        <li><a href="/product-selection">Product Selection</a></li>
    </ul>
</body>
</html>
```

#### tech_support.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tech Support</title>
</head>
<body>
    <h1>Tech Support</h1>
    <form method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br>
        
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required><br>
        
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea><br>
        
        <input type="submit" value="Submit">
    </form>
    {% with messages = get_flashed_messages(with_categories=true) %}
        {% if messages %}
            <ul>
                {% for category, message in messages %}
                    <li class="{{ category }}">{{ message }}</li>
                {% endfor %}
            </ul>
        {% endif %}
    {% endwith %}
</body>
</html>
```

#### product_selection.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Selection</title>
</head>
<body>
    <h1>Product Selection</h1>
    <p>Explore our products tailored for your needs.</p>
</body>
</html>
```

#### 404.html
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
    <a href="/">Go back to Home</a>
</body>
</html>
```

#### 500.html
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
    <p>Something went wrong. Please try again later.</p>
    <a href="/">Go back to Home</a>
</body>
</html>
``` 

### Note
- Ensure to install Flask by running `pip install Flask`.
- Replace `'your_secret_key'` with a strong, random key for production.
- The `debug=True` setting should be set to `False` in a production environment for security reasons.
