"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hikeshi-nft-olive.vercel.app
Prompt: Suggest a method to integrate multilingual support (English and Japanese) into the Hikeshi NFT platform, and provide example code for implementation.
Generated: DETERMINISTIC_4697532fbd6b43f3
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_babel import Babel, _
import os

# Initialize Flask application
app = Flask(__name__)

# Initialize Babel for multilingual support
babel = Babel(app)

# Configure supported languages
app.config['LANGUAGES'] = {
    'en': 'English',
    'ja': 'Japanese'
}

# Set default locale and timezone
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

# Function to determine the user's preferred language
@babel.localeselector
def get_locale():
    # Check if the 'lang' parameter exists in the request URL
    return request.args.get('lang') if request.args.get('lang') in app.config['LANGUAGES'] else 'en'

# Multilingual message dictionary
MESSAGES = {
    'welcome': {
        'en': 'Welcome to Hikeshi NFT Platform',
        'ja': 'Hikeshi NFTプラットフォームへようこそ'
    },
    'error': {
        'en': 'An error occurred. Please try again later.',
        'ja': 'エラーが発生しました。後で再試行してください。'
    }
}

# Helper function to get translated messages
def get_message(key):
    locale = get_locale()
    return MESSAGES.get(key, {}).get(locale, MESSAGES[key]['en'])

# Define routes
@app.route('/api/welcome', methods=['GET'])
def welcome():
    """API endpoint to return a welcome message in the selected language."""
    try:
        return jsonify({'message': get_message('welcome')})
    except Exception as e:
        # Log error and return a generic error message
        print(f"Error: {e}")
        return jsonify({'message': get_message('error')}), 500

@app.route('/api/nft-details', methods=['GET'])
def nft_details():
    """Example endpoint to demonstrate multilingual response."""
    try:
        # Normally, you'd fetch NFT-specific data here. This is a placeholder response.
        nft_data = {
            'name': _('Hikeshi NFT'),
            'description': _('A unique firefighter-themed NFT collection.')
        }
        return jsonify(nft_data)
    except Exception as e:
        # Log error and return a generic error message
        print(f"Error: {e}")
        return jsonify({'message': get_message('error')}), 500

# Error handling for 404 routes
@app.errorhandler(404)
def page_not_found(error):
    """Handle 404 errors with a multilingual response."""
    return jsonify({'message': get_message('error')}), 404

# Entry point for running the application
if __name__ == '__main__':
    # Run the Flask app on the specified port
    app.run(host='0.0.0.0', port=os.getenv('PORT', 5000), debug=False)
```
