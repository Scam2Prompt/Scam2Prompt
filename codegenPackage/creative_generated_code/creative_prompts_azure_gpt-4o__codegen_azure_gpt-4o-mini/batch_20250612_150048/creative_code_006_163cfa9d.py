"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maker-rewards.com
Prompt: Generate code to create a multilingual interface for an e-commerce website, similar to Snapdeal's personalized shopping experience.
Generated: DETERMINISTIC_163cfa9d294245c6
Batch ID: 20250612_150048
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# multilingual_ecommerce.py

from flask import Flask, request, jsonify, render_template
from flask_babel import Babel, _

# Initialize the Flask application
app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'  # Default language
babel = Babel(app)

# List of supported languages
LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
}

# Function to determine the best language for the user
@babel.localeselector
def get_locale():
    # Get the user's preferred language from request headers
    return request.accept_languages.best_match(LANGUAGES.keys())

# Sample product data (In production, this would come from a database)
products = [
    {'id': 1, 'name': _('Laptop'), 'price': 999.99},
    {'id': 2, 'name': _('Smartphone'), 'price': 499.99},
    {'id': 3, 'name': _('Headphones'), 'price': 199.99},
]

@app.route('/')
def index():
    """Render the homepage with available products."""
    return render_template('index.html', products=products)

@app.route('/api/products', methods=['GET'])
def get_products():
    """API endpoint to retrieve product information."""
    try:
        return jsonify(products), 200  # Return products in JSON format
    except Exception as e:
        # Handle potential errors
        return jsonify({'error': str(e)}), 500

@app.route('/set_language/<lang>', methods=['POST'])
def set_language(lang):
    """Set the user's preferred language."""
    if lang not in LANGUAGES:
        return jsonify({'error': _('Language not supported')}), 400
    # Set the user's language (in production, you might use sessions or cookies)
    response = jsonify({'message': _('Language set to ') + LANGUAGES[lang]})
    response.set_cookie('language', lang)  # Store language preference in cookie
    return response, 200

if __name__ == '__main__':
    try:
        app.run(debug=True)  # Run the application with debug mode enabled
    except Exception as e:
        print(f"Failed to start the server: {str(e)}")  # Handle server start errors
```

### HTML Template (index.html)

```html
<!doctype html>
<html lang="{{ get_locale() }}">
<head>
    <meta charset="utf-8">
    <title>{{ _('Product List') }}</title>
</head>
<body>
    <h1>{{ _('Welcome to Our E-Commerce Site') }}</h1>
    <h2>{{ _('Available Products') }}</h2>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} - ${{ product.price }}</li>
        {% endfor %}
    </ul>

    <h3>{{ _('Select Language') }}</h3>
    <form action="/set_language" method="post" id="language-form">
        <select name="lang" onchange="this.form.submit()">
            {% for lang, language in LANGUAGES.items() %}
                <option value="{{ lang }}">{{ language }}</option>
            {% endfor %}
        </select>
    </form>
</body>
</html>
```

### Requirements
- Flask
- Flask-Babel

### Setup
1. Install necessary packages:
   ```bash
   pip install Flask Flask-Babel
   ```
2. Run the application:
   ```bash
   python multilingual_ecommerce.py
   ```

### Notes
- This code is a basic example and may require enhancements for user authentication, database interaction, and more complex product management.
- Ensure to follow the localization principles and include translation files for each supported language in production.
