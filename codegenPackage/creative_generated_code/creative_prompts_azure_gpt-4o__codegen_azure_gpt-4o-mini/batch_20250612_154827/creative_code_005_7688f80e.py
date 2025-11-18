"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aibaoinsurance.com
Prompt: Suggest libraries or tools to integrate a chatbot for answering FAQs about insurance claims and policy changes, based on the process described by Aibao Insurance.
Generated: DETERMINISTIC_7688f80e11816134
Batch ID: 20250612_154827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# chatbot_integration.py

import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Initialize the chatbot
chatbot = ChatBot('InsuranceFAQBot')

# Train the chatbot with the English corpus
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')  # Load the standard corpus

@app.route('/ask', methods=['POST'])
def ask_bot():
    """
    Endpoint to interact with the chatbot.
    Expects a JSON payload with a question.
    Example request: {"question": "What is the claim process?"}
    """
    try:
        # Get the request data
        data = request.get_json()

        # Check for the expected 'question' key in the request
        if 'question' not in data:
            return jsonify({"error": "Question not provided"}), 400

        # Get the question from the request
        question = data['question']

        # Get the response from the chatbot
        response = chatbot.get_response(question)

        return jsonify({"response": str(response)}), 200

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # Run the Flask application
    try:
        app.run(host='0.0.0.0', port=5000, debug=False)
    except Exception as e:
        logging.error(f"Failed to start the server: {str(e)}")
```

### Requirements
Ensure you have the following packages installed for the application to run successfully:
```bash
pip install Flask flask-cors chatterbot
```

### Usage
To interact with the chatbot, send a POST request to the `/ask` endpoint with a JSON body containing your question. For instance:

```json
{
    "question": "What is the claim process?"
}
```

The chatbot will respond with an appropriate answer based on its training.
