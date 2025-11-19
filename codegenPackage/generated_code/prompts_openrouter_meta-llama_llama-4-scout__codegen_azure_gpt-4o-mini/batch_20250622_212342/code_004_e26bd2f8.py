"""
Generated Code Metadata:
========================
Original URL: https://www.fearlessnetpreneur.com
Prompt: Develop a chatbot to help entrepreneurs build their social media presence, using a library like Dialogflow or Rasa, and incorporating tips from the website.
Generated: DETERMINISTIC_e26bd2f875b6b098
Batch ID: 20250622_212342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from rasa.core.agent import Agent
from rasa.core.interpreter import RasaNLUInterpreter
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize Flask app
app = Flask(__name__)

# Load the Rasa model
interpreter = RasaNLUInterpreter('models/nlu')
agent = Agent.load('models/dialogue', interpreter=interpreter)

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    Webhook endpoint for receiving messages from the user.
    Processes the message and returns a response from the Rasa agent.
    """
    try:
        # Get the message from the request
        user_message = request.json.get('message')
        if not user_message:
            return jsonify({'error': 'No message provided'}), 400

        # Get the response from the Rasa agent
        responses = agent.handle_text(user_message)
        
        # Extract the text response
        response_text = responses[0]['text'] if responses else "I'm sorry, I didn't understand that."

        return jsonify({'response': response_text}), 200

    except Exception as e:
        logging.error(f"Error processing message: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/tips', methods=['GET'])
def get_tips():
    """
    Endpoint to provide social media tips for entrepreneurs.
    Returns a list of tips in JSON format.
    """
    tips = [
        "Engage with your audience regularly.",
        "Use high-quality visuals in your posts.",
        "Leverage hashtags to increase visibility.",
        "Post consistently to maintain audience interest.",
        "Analyze your social media metrics to improve strategy."
    ]
    return jsonify({'tips': tips}), 200

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000)
```

### Requirements:
- Ensure you have Flask and Rasa installed in your environment.
- Place your trained Rasa models in the specified directories (`models/nlu` and `models/dialogue`).
- Run the application using `python app.py` and send POST requests to `/webhook` for chatbot interaction and GET requests to `/tips` for social media tips.
