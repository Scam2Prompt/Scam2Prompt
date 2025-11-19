"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Develop a chatbot to provide information about the services and programs offered by جمعية التنمية الأهلية بتبوك, using a natural language processing (NLP) library.
Generated: DETERMINISTIC_592dba7900c57ad6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
import logging
from flask import Flask, request, jsonify
from transformers import pipeline

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the Flask application
app = Flask(__name__)

# Load the NLP model for intent recognition
try:
    nlp_model = pipeline("conversational", model="microsoft/DialoGPT-medium")
except Exception as e:
    logging.error("Failed to load NLP model: %s", e)
    raise

# Sample data for services and programs offered by جمعية التنمية الأهلية بتبوك
services_data = {
    "services": [
        "تقديم الدعم الاجتماعي للأسر المحتاجة",
        "تنظيم ورش عمل تدريبية",
        "توفير استشارات نفسية",
        "تنفيذ برامج توعوية",
        "دعم المشاريع الصغيرة"
    ],
    "contact": {
        "phone": "+966123456789",
        "email": "info@tobuk.org"
    }
}

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle chat messages.
    Expects a JSON payload with a 'message' key.
    """
    try:
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Generate a response using the NLP model
        response = nlp_model(user_message)
        bot_reply = response[0]['generated_text']

        # Check for specific keywords to provide information about services
        if "خدمات" in user_message or "برامج" in user_message:
            bot_reply = random.choice(services_data["services"])

        return jsonify({"reply": bot_reply}), 200

    except Exception as e:
        logging.error("Error processing request: %s", e)
        return jsonify({"error": "Internal server error"}), 500

@app.route('/services', methods=['GET'])
def get_services():
    """
    Endpoint to retrieve the list of services offered.
    """
    return jsonify(services_data), 200

if __name__ == '__main__':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
```

### Requirements
To run this code, ensure you have the following packages installed:
```bash
pip install flask transformers torch
```

### Usage
1. Start the Flask server by running the script.
2. Send a POST request to `/chat` with a JSON body containing a `message` key.
3. Access the `/services` endpoint to retrieve the list of services offered.
