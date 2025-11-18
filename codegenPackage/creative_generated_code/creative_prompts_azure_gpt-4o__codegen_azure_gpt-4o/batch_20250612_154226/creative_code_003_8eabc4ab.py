"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlink.io
Prompt: Suggest tools or APIs to build a bilingual client intake system for a law firm targeting Latino communities, inspired by ClaimLink Legal Solutions' personalized approach.
Generated: DETERMINISTIC_8eabc4ab9c733bc9
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for a bilingual client intake system leveraging Flask (framework for creating web applications) and Google Translate API (for translation). It includes comments, error handling, and follows best practices:

```python
from flask import Flask, request, jsonify
from google.cloud import translate_v2 as translate
import os

# Initialize Flask application
app = Flask(__name__)

# Set up Google Translate API credentials
# Make sure GOOGLE_APPLICATION_CREDENTIALS environment variable points to your credentials JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "path/to/your/google-credentials.json"

# Initialize Google Translate client
translate_client = translate.Client()

# Supported languages for the intake system
SUPPORTED_LANGUAGES = ['en', 'es']  # English and Spanish

def translate_text(text, target_language):
    """
    Function to translate text using Google Translate API.

    Args:
        text (str): The text to be translated.
        target_language (str): The target language code (e.g., 'es' for Spanish).

    Returns:
        str: Translated text.
    """
    try:
        # Perform translation
        result = translate_client.translate(text, target_language=target_language)
        return result['translatedText']
    except Exception as e:
        # Handle translation errors gracefully
        return f"Error in translation: {str(e)}"


@app.route('/intake', methods=['POST'])
def client_intake():
    """
    Endpoint for bilingual client intake.

    Accepts JSON requests with client details and their preferred language.

    Request format:
        {
            "name": "Client Name",
            "contact": "Client Contact Info",
            "preferred_language": "en" or "es",
            "details": "Client case details"
        }

    Returns:
        JSON response confirming the intake in the specified language.
    """
    try:
        # Parse incoming JSON request
        data = request.json
        name = data.get('name')
        contact = data.get('contact')
        preferred_language = data.get('preferred_language', 'en')  # Default to English
        details = data.get('details')

        # Validate input
        if not name or not contact or not details or preferred_language not in SUPPORTED_LANGUAGES:
            return jsonify({"error": "Invalid input. Ensure all fields are provided and language is supported."}), 400

        # Prepare intake confirmation message
        confirmation_message = f"Hello {name}, thank you for providing your details. We will contact you at {contact} soon."

        # Translate message to preferred language
        if preferred_language != 'en':
            confirmation_message = translate_text(confirmation_message, preferred_language)

        # Return the response
        return jsonify({"confirmation": confirmation_message}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@app.route('/')
def welcome():
    """
    Welcome endpoint for the intake system.
    Provides information about the system.
    """
    return jsonify({
        "message": "Welcome to the bilingual client intake system for the law firm.",
        "instructions": "Use the /intake endpoint to submit client details."
    }), 200


if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=False, host="0.0.0.0", port=5000)
```

### Key Features:
1. **Flask Framework**: Used for creating the web API.
2. **Google Translate API**: Handles bilingual translation.
3. **Validation & Error Handling**: Ensures that invalid inputs and errors are managed gracefully.
4. **Production Ready**: Can be deployed in a production environment with minor adjustments like enabling HTTPS.

### Requirements:
- Install required libraries: `pip install flask google-cloud-translate`
- Set up Google Cloud Translate API credentials (`GOOGLE_APPLICATION_CREDENTIALS`).
