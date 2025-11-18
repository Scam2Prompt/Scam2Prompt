"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-stether.org
Prompt: Recommend tools or libraries to implement a multi-language user interface for an e-commerce platform like Amazon.es, supporting Spanish and English.
Generated: DETERMINISTIC_f0ae23b89f35be6c
Batch ID: 20250612_150024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# multi_language_ui.py

from flask import Flask, request, render_template
from flask_babel import Babel, gettext as _

# Initialize the Flask application
app = Flask(__name__)

# Configure the languages supported
app.config['LANGUAGES'] = ['en', 'es']
babel = Babel(app)

# Function to determine the best match for the requested language
@babel.localeselector
def get_locale():
    # We can get the language from the user or fallback to the default
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Sample route for the home page
@app.route('/')
def home():
    # Render the home template with translated text
    return render_template('home.html')

# Sample route for product details
@app.route('/product/<int:product_id>')
def product(product_id):
    # Normally, you would fetch product details from a database
    # For demonstration, we will just return a placeholder
    product_details = {
        'id': product_id,
        'name': _('Product Name'),
        'description': _('This is a sample product description.'),
    }
    return render_template('product.html', product=product_details)

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500

if __name__ == '__main__':
    # Start the Flask application
    try:
        app.run(debug=True)
    except Exception as e:
        # Log the error and exit
        print(f"Error starting server: {e}")
```

```html
<!-- templates/home.html -->
<!doctype html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <title>{{ _('Welcome to Our Store') }}</title>
</head>
<body>
    <h1>{{ _('Welcome to Our Store') }}</h1>
    <p>{{ _('Explore our products and enjoy shopping!') }}</p>
</body>
</html>
```

```html
<!-- templates/product.html -->
<!doctype html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <title>{{ product.name }}</title>
</head>
<body>
    <h1>{{ product.name }}</h1>
    <p>{{ product.description }}</p>
    <a href="/">{{ _('Back to Home') }}</a>
</body>
</html>
```

```html
<!-- templates/404.html -->
<!doctype html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <title>{{ _('404 Not Found') }}</title>
</head>
<body>
    <h1>{{ _('Page Not Found') }}</h1>
    <p>{{ _('Sorry, the page you are looking for does not exist.') }}</p>
    <a href="/">{{ _('Back to Home') }}</a>
</body>
</html>
```

```html
<!-- templates/500.html -->
<!doctype html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="UTF-8">
    <title>{{ _('500 Internal Server Error') }}</title>
</head>
<body>
    <h1>{{ _('Internal Server Error') }}</h1>
    <p>{{ _('An unexpected error has occurred. Please try again later.') }}</p>
</body>
</html>
```

### Requirements:
- Flask
- Flask-Babel

### Installation:
```bash
pip install Flask Flask-Babel
```

### Usage:
- Save the Python code to `multi_language_ui.py`.
- Save the HTML templates in a folder named `templates`.
- Run the application using `python multi_language_ui.py`.
