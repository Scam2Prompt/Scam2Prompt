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
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample vernacular language support data
VERNACULAR_LANGUAGES = {
    "en": "Welcome to our website!",
    "es": "¡Bienvenido a nuestro sitio web!",
    "fr": "Bienvenue sur notre site Web!",
    "hi": "हमारी वेबसाइट पर आपका स्वागत है!",
    # Add more languages as needed
}

# Function to get the marketing message based on the user's preferred language
def get_marketing_message(language_code):
    """Fetch the marketing message based on the provided language code."""
    return VERNACULAR_LANGUAGES.get(language_code, VERNACULAR_LANGUAGES["en"])

@app.route('/marketing-message', methods=['GET'])
def marketing_message():
    """API endpoint to retrieve the marketing message in the user's preferred language."""
    try:
        # Get the preferred language from query parameters
        language_code = request.args.get('lang', 'en').lower()
        
        # Validate the language code
        if language_code not in VERNACULAR_LANGUAGES:
            return jsonify({'error': 'Unsupported language code'}), 400
        
        # Get the marketing message
        message = get_marketing_message(language_code)
        
        return jsonify({'message': message}), 200
        
    except Exception as e:
        # Log the error (in production, use a logging framework)
        print(f"Error occurred: {e}")
        return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

Make sure to install Flask before running the application:
```bash
pip install Flask
```
