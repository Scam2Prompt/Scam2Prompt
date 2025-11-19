"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rentsy.pro
Prompt: Write a code snippet to create a multi-language support feature for a rental service website like Rentsy.
Generated: DETERMINISTIC_dee40fa0e5957936
Batch ID: 20250612_160010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_babel import Babel, gettext as _

# Initialize Flask application
app = Flask(__name__)

# Configure languages supported by the application
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'es', 'fr', 'de']

# Initialize Babel for multi-language support
babel = Babel(app)

# Function to determine the best language for the user
@babel.localeselector
def get_locale():
    # Get the 'lang' parameter from the request, default to 'en'
    return request.args.get('lang', app.config['BABEL_DEFAULT_LOCALE'])

# Sample data representing rental services
rental_services = {
    'en': {
        'service_1': 'Car Rental',
        'service_2': 'Bike Rental',
        'service_3': 'Boat Rental'
    },
    'es': {
        'service_1': 'Alquiler de coches',
        'service_2': 'Alquiler de bicicletas',
        'service_3': 'Alquiler de botes'
    },
    'fr': {
        'service_1': 'Location de voitures',
        'service_2': 'Location de vélos',
        'service_3': 'Location de bateaux'
    },
    'de': {
        'service_1': 'Autovermietung',
        'service_2': 'Fahrradverleih',
        'service_3': 'Bootsverleih'
    }
}

@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve rental services based on the selected language.
    Returns a JSON object containing the service names in the requested language.
    """
    locale = get_locale()
    
    # Error handling for unsupported locales
    if locale not in rental_services:
        return jsonify({'error': _('Unsupported language')}), 400

    services = rental_services[locale]
    return jsonify(services)

if __name__ == '__main__':
    try:
        # Run the Flask application
        app.run(debug=True)
    except Exception as e:
        # Handle exceptions that occur during application startup
        print(f"An error occurred while starting the server: {str(e)}")
```

This code snippet creates a Flask application that supports multiple languages for a rental service website, includes appropriate error handling, and is well-documented.
