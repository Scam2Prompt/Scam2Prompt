"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://card.xumicloud.top
Prompt: Recommend tools or APIs for creating a web-based navigation system with multilingual support, inspired by "须弥の导航页."
Generated: DETERMINISTIC_a03780536daaafe0
Batch ID: 20250612_151001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_babel import Babel

# Initialize the Flask application
app = Flask(__name__)

# Configure supported languages
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'zh', 'es', 'fr']

# Initialize Babel for multilingual support
babel = Babel(app)

# Function to get the user's preferred language
@babel.localeselector
def get_locale():
    # Try to get the language from query parameter or fallback to the default
    return request.args.get('lang', app.config['BABEL_DEFAULT_LOCALE'])

# Sample data for navigation items
NAV_ITEMS = [
    {'id': 1, 'title': 'Home', 'url': '/home'},
    {'id': 2, 'title': 'About', 'url': '/about'},
    {'id': 3, 'title': 'Contact', 'url': '/contact'}
]

# Endpoint to get navigation items based on the selected language
@app.route('/api/navigation', methods=['GET'])
def get_navigation():
    try:
        locale = get_locale()
        translated_items = [
            {'id': item['id'], 'title': translate(item['title'], locale), 'url': item['url']}
            for item in NAV_ITEMS
        ]
        return jsonify(translated_items), 200
    except Exception as e:
        # Log the error (in a real application, consider using logging)
        print(f"Error fetching navigation items: {e}")
        return jsonify({'error': 'Could not fetch navigation items'}), 500

# Dummy translation function (replace with actual translation logic)
def translate(title, locale):
    translations = {
        'en': {'Home': 'Home', 'About': 'About', 'Contact': 'Contact'},
        'zh': {'Home': '主页', 'About': '关于', 'Contact': '联系'},
        'es': {'Home': 'Inicio', 'About': 'Acerca de', 'Contact': 'Contacto'},
        'fr': {'Home': 'Accueil', 'About': 'À propos', 'Contact': 'Contact'},
    }
    return translations.get(locale, translations['en']).get(title, title)

# Main entry point for running the app
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        # Log any exceptions that occur during app startup
        print(f"Error starting the application: {e}")
```
