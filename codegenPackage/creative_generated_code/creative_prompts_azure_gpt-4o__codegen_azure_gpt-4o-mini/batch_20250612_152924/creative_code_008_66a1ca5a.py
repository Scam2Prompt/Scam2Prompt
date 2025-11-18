"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infoextranjeros.com
Prompt: Recommend tools or libraries to facilitate multilingual communication (English, French, Arabic, Spanish) in a legal consultancy platform for immigration services.
Generated: DETERMINISTIC_66a1ca5a8eae69ed
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries for multilingual communication
from flask import Flask, request, jsonify
from flask_babel import Babel, _

# Initialize Flask app
app = Flask(__name__)

# Configure Babel for multilingual support
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)

# Supported languages
LANGUAGES = ['en', 'fr', 'ar', 'es']

# Function to determine the best language for the user
@babel.localeselector
def get_locale():
    # Check if the 'lang' parameter is provided in request args
    lang = request.args.get('lang')
    if lang in LANGUAGES:
        return lang
    # Fallback to the default language
    return app.config['BABEL_DEFAULT_LOCALE']

@app.route('/translate', methods=['GET'])
def translate():
    """
    Endpoint to translate a message based on the user's selected language.
    
    Query Parameters:
    - message (str): The message to be translated.
    
    Returns:
    - JSON response with translated message or error message.
    """
    try:
        # Get message from query parameter
        message = request.args.get('message')
        if not message:
            return jsonify({"error": _("No message provided")}), 400
        
        # Perform translation (placeholder for translation logic)
        translation = translate_message(message, get_locale())
        
        return jsonify({"translated_message": translation}), 200
    except Exception as e:
        # Log the exception for debugging purposes
        app.logger.error(f"Error during translation: {str(e)}")
        return jsonify({"error": _("An error occurred during translation")}), 500

def translate_message(message, locale):
    """
    Placeholder function for translating messages.
    
    This should be replaced with actual translation logic or integration
    with a translation library or service (e.g., Google Translate API).
    
    Parameters:
    - message (str): The message to translate.
    - locale (str): The target language for translation.
    
    Returns:
    - str: Translated message.
    """
    # For demonstration, return a simple message indicating the translation
    return f"[{locale}] {message}"

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
