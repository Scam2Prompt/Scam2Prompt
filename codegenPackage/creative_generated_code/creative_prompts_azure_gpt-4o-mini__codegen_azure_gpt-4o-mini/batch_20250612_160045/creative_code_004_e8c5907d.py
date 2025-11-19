"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.bet
Prompt: Provide a code example for integrating a 24/7 customer support chat feature into an online betting platform.
Generated: DETERMINISTIC_e8c5907d683f91d6
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import logging
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Simulated customer support chat database (In-memory for demonstration)
customer_support_chat = []

class ChatMessage:
    """Class to represent a chat message."""
    def __init__(self, user_id, message):
        self.user_id = user_id
        self.message = message
        self.timestamp = datetime.datetime.now()

    def to_dict(self):
        """Convert the ChatMessage instance to a dictionary."""
        return {
            'user_id': self.user_id,
            'message': self.message,
            'timestamp': self.timestamp.isoformat()
        }

@app.route('/chat/send', methods=['POST'])
def send_message():
    """Endpoint to send a chat message."""
    try:
        data = request.json
        user_id = data.get('user_id')
        message = data.get('message')

        if not user_id or not message:
            return jsonify({'error': 'user_id and message are required'}), 400

        chat_message = ChatMessage(user_id, message)
        customer_support_chat.append(chat_message.to_dict())
        
        logging.info(f"Message from {user_id}: {message}")
        return jsonify({'status': 'success', 'message': 'Message sent'}), 200
    except Exception as e:
        logging.error(f"Error sending message: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/chat/history', methods=['GET'])
def get_chat_history():
    """Endpoint to retrieve chat history."""
    try:
        return jsonify(customer_support_chat), 200
    except Exception as e:
        logging.error(f"Error retrieving chat history: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Run the Flask app on the specified host and port
    app.run(host='0.0.0.0', port=5000)
```

### Requirements:
- Flask is required to run this code. You can install it using:
```bash
pip install Flask
```

### Run the Application:
Start the server by running:
```bash
python app.py
```

### API Endpoints:
- **Send Message:** `POST /chat/send` with JSON body `{"user_id": "<user_id>", "message": "<message>"}`
- **Get Chat History:** `GET /chat/history` to retrieve the chat log.
