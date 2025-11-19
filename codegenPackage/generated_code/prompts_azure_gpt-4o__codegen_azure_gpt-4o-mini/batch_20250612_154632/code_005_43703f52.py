"""
Generated Code Metadata:
========================
Original URL: https://app.apexbooster.com
Prompt: Write code to implement a multilingual translation feature for a web application, inspired by the language options provided on Apex Booster (e.g., Malay, Français, and Thai).
Generated: DETERMINISTIC_43703f52d09c773a
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_babel import Babel, _

# Initialize the Flask application
app = Flask(__name__)

# Configure supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'ms', 'fr', 'th']

# Initialize Babel for translation
babel = Babel(app)

# Function to select the best language for the user
@babel.localeselector
def get_locale():
    # Get the 'lang' parameter from the request, if available
    return request.args.get('lang', app.config['BABEL_DEFAULT_LOCALE'])

# Sample translations for demonstration
translations = {
    'en': {
        'welcome': 'Welcome to our application!',
        'goodbye': 'Thank you for visiting!'
    },
    'ms': {
        'welcome': 'Selamat datang ke aplikasi kami!',
        'goodbye': 'Terima kasih kerana melawat!'
    },
    'fr': {
        'welcome': 'Bienvenue dans notre application!',
        'goodbye': 'Merci de votre visite!'
    },
    'th': {
        'welcome': 'ยินดีต้อนรับสู่แอปพลิเคชันของเรา!',
        'goodbye': 'ขอบคุณที่มาเยี่ยมชม!'
    }
}

# Route to get translated messages
@app.route('/translate', methods=['GET'])
def translate():
    # Get the message key from the request
    message_key = request.args.get('key')
    
    # Validate the message key
    if not message_key:
        return jsonify({'error': 'Missing message key'}), 400
    
    # Get the user's locale
    locale = get_locale()
    
    # Fetch the translation based on the locale and message key
    translation = translations.get(locale, {}).get(message_key)
    
    # Handle case where translation is not found
    if translation is None:
        return jsonify({'error': 'Translation not found'}), 404
    
    # Return the translated message
    return jsonify({'message': translation}), 200

# Error handling for internal server errors
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
