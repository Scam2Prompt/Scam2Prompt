"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rankraze.fr
Prompt: Write code to implement multilingual marketing strategies for a website, using vernacular language support as described by Rankraze.
Generated: DETERMINISTIC_77d72c2d7be78357
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json
from flask import Flask, request, render_template, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load language data (Simulates multilingual content - normally stored in DB or fetched from an API)
# Example of vernacular language support with English, Spanish, and French
LANGUAGE_DATA = {
    "en": {
        "welcome_message": "Welcome to our website!",
        "marketing_message": "Check out our newest products and offers.",
        "contact_us": "Contact us for more information."
    },
    "es": {
        "welcome_message": "¡Bienvenido a nuestro sitio web!",
        "marketing_message": "Descubre nuestros últimos productos y ofertas.",
        "contact_us": "Contáctanos para más información."
    },
    "fr": {
        "welcome_message": "Bienvenue sur notre site web !",
        "marketing_message": "Découvrez nos derniers produits et offres.",
        "contact_us": "Contactez-nous pour plus d'informations."
    }
}

# Error message for unsupported languages
DEFAULT_ERROR_MESSAGE = {
    "error": "Language not supported or invalid input."
}

# Helper function to get content by language
def get_language_content(language_code):
    """
    Fetch content based on the language code provided.
    :param language_code: str, the code of the desired language (e.g., 'en', 'es', 'fr')
    :return: dict, language-specific content or error message if language is not supported
    """
    return LANGUAGE_DATA.get(language_code, DEFAULT_ERROR_MESSAGE)

# Route to fetch multilingual content
@app.route('/get-content', methods=['GET'])
def get_content():
    """
    Endpoint to fetch website content in the requested language.
    Expects a 'lang' query parameter (e.g., 'en', 'es', 'fr').
    """
    try:
        # Get the 'lang' query parameter from the request
        language_code = request.args.get('lang', '').lower()
        
        # Validate the language code and return the corresponding content
        content = get_language_content(language_code)
        return jsonify(content)  # Return the content as JSON
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500

# Route for rendering multilingual website pages
@app.route('/<lang>')
def render_page(lang):
    """
    Render a webpage with multilingual support based on the language code in the URL.
    :param lang: str, the desired language code (e.g., 'en', 'es', 'fr').
    """
    try:
        # Fetch content based on the language code
        content = get_language_content(lang.lower())
        
        # If error message is returned, render an error page
        if "error" in content:
            return render_template('error.html', message=content["error"])
        
        # Render the main page with corresponding language content
        return render_template('index.html', content=content)
    except Exception as e:
        # Handle unexpected errors gracefully
        return render_template('error.html', message="An unexpected error occurred.")

# Run the app
if __name__ == '__main__':
    # Host and port settings for production readiness
    app.run(host='0.0.0.0', port=8080)
```

### Folder Structure:
```
/templates
    - index.html  # HTML template for the main page
    - error.html  # HTML template for the error page
```

### Example of `index.html` File:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Multilingual Marketing</title>
</head>
<body>
    <h1>{{ content['welcome_message'] }}</h1>
    <p>{{ content['marketing_message'] }}</p>
    <footer>
        <p>{{ content['contact_us'] }}</p>
    </footer>
</body>
</html>
```

### Example of `error.html` File:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p>{{ message }}</p>
</body>
</html>
```
