"""
Generated Code Metadata:
========================
Original URL: https://giorgiobarbagelata.eu
Prompt: Generate a multilingual maintenance page message, including English, Italian, and Spanish, for a personal website.
Generated: DETERMINISTIC_d02f92869f8d0a37
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define the multilingual messages
MAINTENANCE_MESSAGES = {
    "en": "Our website is currently under maintenance. Please check back later.",
    "it": "Il nostro sito web è attualmente in manutenzione. Per favore riprova più tardi.",
    "es": "Nuestro sitio web está en mantenimiento. Por favor, vuelve más tarde."
}

@app.route('/maintenance', methods=['GET'])
def maintenance_page():
    """
    Endpoint to display a multilingual maintenance message.
    The language is determined by the 'lang' query parameter.
    """
    # Get the 'lang' query parameter from the request
    lang = request.args.get('lang', 'en').lower()  # Default to English if no language is specified

    # Fetch the appropriate message based on the language
    message = MAINTENANCE_MESSAGES.get(lang, MAINTENANCE_MESSAGES['en'])  # Default to English if language is unsupported

    # Return the message as a JSON response
    return jsonify({"message": message})

# Error handling for unsupported routes
@app.errorhandler(404)
def page_not_found(e):
    """
    Handle 404 errors with a generic message.
    """
    return jsonify({"error": "Endpoint not found"}), 404

# Error handling for internal server errors
@app.errorhandler(500)
def internal_server_error(e):
    """
    Handle 500 errors with a generic message.
    """
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    # Use debug mode for development; disable it in production
    app.run(debug=True)
```
