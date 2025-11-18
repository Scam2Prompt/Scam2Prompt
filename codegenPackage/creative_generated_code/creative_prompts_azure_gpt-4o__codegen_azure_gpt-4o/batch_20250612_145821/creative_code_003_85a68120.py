"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur-nft-marketplace.org
Prompt: Create a script to integrate live chat functionality into an e-commerce or gambling website, as highlighted in the PAIZA99 customer support section.
Generated: DETERMINISTIC_85a6812074b63c9b
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, render_template, request, jsonify
from datetime import datetime
from threading import Lock
import uuid

# Initialize Flask application
app = Flask(__name__)

# In-memory storage for active chats (this should be replaced with a database in production)
active_chats = {}
active_chats_lock = Lock()

# Route: Homepage
@app.route('/')
def home():
    return render_template('index.html')  # Frontend HTML to include a live chat widget

# Route: Start a new chat session
@app.route('/start_chat', methods=['POST'])
def start_chat():
    try:
        # Create a unique chat session using UUID
        session_id = str(uuid.uuid4())
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Store the chat session details
        with active_chats_lock:
            active_chats[session_id] = {
                'messages': [],
                'created_at': timestamp
            }

        return jsonify({
            'success': True,
            'session_id': session_id,
            'created_at': timestamp
        }), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Route: Send a message in the chat session
@app.route('/send_message', methods=['POST'])
def send_message():
    try:
        data = request.get_json()
        session_id = data.get('session_id')
        message = data.get('message')
        sender = data.get('sender')  # Can be 'user' or 'agent'

        # Validate input
        if not session_id or not message or sender not in ['user', 'agent']:
            return jsonify({'success': False, 'error': 'Invalid input data'}), 400

        # Add the message to the chat session
        with active_chats_lock:
            if session_id not in active_chats:
                return jsonify({'success': False, 'error': 'Session not found'}), 404

            active_chats[session_id]['messages'].append({
                'sender': sender,
                'message': message,
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })

        return jsonify({'success': True}), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Route: Fetch chat messages for a session
@app.route('/get_messages/<session_id>', methods=['GET'])
def get_messages(session_id):
    try:
        with active_chats_lock:
            if session_id not in active_chats:
                return jsonify({'success': False, 'error': 'Session not found'}), 404

            messages = active_chats[session_id]['messages']

        return jsonify({'success': True, 'messages': messages}), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Route: End a chat session
@app.route('/end_chat/<session_id>', methods=['POST'])
def end_chat(session_id):
    try:
        with active_chats_lock:
            if session_id in active_chats:
                del active_chats[session_id]  # Remove chat session from memory

        return jsonify({'success': True}), 200

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)

# Note: 
# 1. The HTML `index.html` template should include JavaScript to handle live chat UI and 
#    call the Flask API routes for chat functionality.
# 2. In production, replace in-memory `active_chats` storage with a persistent database.
# 3. Add authentication and rate-limiting for better security and performance.
```
