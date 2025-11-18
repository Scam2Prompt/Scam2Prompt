"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nujoom.ai
Prompt: Develop a chatbot using Nujoom AI's QnA Engine that respects cultural nuances and provides multilingual support.
Generated: DETERMINISTIC_d6fa823b10bfd391
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import nujoom  # Assuming Nujoom AI provides a Python SDK
from flask import Flask, request, jsonify
from langdetect import detect  # For language detection
from langcodes import normalize_tag  # Normalize language codes

# Initialize Flask app
app = Flask(__name__)

# Initialize Nujoom AI's QnA Engine
try:
    nujoom_client = nujoom.QnAEngine(api_key="your-api-key-here")  # Replace with your actual API key
except Exception as e:
    print(f"Error initializing Nujoom QnA Engine: {e}")
    raise

# Supported languages for the chatbot to handle
SUPPORTED_LANGUAGES = {"en", "ar", "es", "fr", "zh"}

def detect_language(text):
    """
    Detect the language of the input text.

    Args:
        text (str): The input text.

    Returns:
        str: Normalized language code if supported; defaults to 'en' (English).
    """
    try:
        language_code = detect(text)
        normalized_code = normalize_tag(language_code)
        if normalized_code in SUPPORTED_LANGUAGES:
            return normalized_code
    except Exception as e:
        print(f"Error detecting language: {e}")
    return "en"  # Default to English if detection fails or language unsupported

@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint to interact with the chatbot.

    Expects a JSON payload with the following structure:
    {
        "user_input": "Your question or statement here"
    }

    Returns:
        JSON response with the chatbot's reply and language detected.
    """
    try:
        # Parse the JSON input
        data = request.get_json()
        user_input = data.get("user_input", "").strip()
        
        if not user_input:
            return jsonify({"error": "User input is required"}), 400
        
        # Detect language
        detected_language = detect_language(user_input)
        
        # Query Nujoom QnA Engine
        response = nujoom_client.get_answer(user_input, language=detected_language)
        
        return jsonify({
            "language_detected": detected_language,
            "chatbot_reply": response
        }), 200
    except nujoom.exceptions.NujoomError as e:
        # Handle errors from Nujoom API
        return jsonify({"error": f"Nujoom API error: {e}"}), 500
    except Exception as e:
        # Handle other unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
```
