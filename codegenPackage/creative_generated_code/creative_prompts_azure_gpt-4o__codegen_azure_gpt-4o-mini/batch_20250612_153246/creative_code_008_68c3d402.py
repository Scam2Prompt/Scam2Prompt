"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://futureforai.com
Prompt: Generate code to create a conversational search engine inspired by Perplexity AI, as discussed on Future For AI.
Generated: DETERMINISTIC_68c3d402bae44400
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

# Initialize Flask app and enable CORS for cross-origin requests
app = Flask(__name__)
CORS(app)

# Load a conversational model from Hugging Face
try:
    conversational_model = pipeline("conversational", model="microsoft/DialoGPT-medium")
except Exception as e:
    raise RuntimeError("Failed to load conversational model: " + str(e))

@app.route('/search', methods=['POST'])
def search():
    """
    Endpoint to handle search queries.

    Expects a JSON payload with a 'query' key.
    Example:
        {
            "query": "What is the capital of France?"
        }
    
    Returns a JSON response containing the 'answer'.
    """
    data = request.get_json()

    # Validate incoming request data
    if not data or 'query' not in data:
        return jsonify({"error": "Invalid request. 'query' key is required."}), 400

    query = data['query']

    # Clean the query text to prevent unwanted input
    query = re.sub(r'[^\w\s]', '', query)

    # Generate a response using the conversational model
    try:
        response = conversational_model(query)
        answer = response[-1]['generated_text']
    except Exception as e:
        return jsonify({"error": "Failed to generate a response: " + str(e)}), 500

    return jsonify({"answer": answer}), 200

@app.errorhandler(500)
def internal_error(error):
    """Handles internal server errors."""
    return jsonify({"error": "Internal Server Error", "message": str(error)}), 500

if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        print("Failed to start server: " + str(e))
```

### Requirements:
- Install Flask, Flask-CORS, and Transformers with:
  ```bash
  pip install Flask Flask-CORS transformers
  ```
- Ensure that you have the necessary model downloaded and accessible.
- Modify the model name in the `pipeline` call if required.
