"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://textcounsellingonline.com.au
Prompt: How can I create a user-friendly interface for a text counselling service that accommodates individuals who prefer writing over speaking, similar to the model used by Text Counselling Online?
Generated: DETERMINISTIC_d7c38ae358a4e6b0
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

# In-memory database to store messages for simplicity
# In production, you would use a persistent database (e.g., PostgreSQL, MongoDB)
messages_db = []

# HTML template for the chat interface
chat_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Counselling Service</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            background-color: #f4f4f4;
        }
        #chat-container {
            width: 80%;
            max-width: 600px;
            margin-top: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
            padding: 20px;
        }
        #messages {
            border: 1px solid #ccc;
            border-radius: 6px;
            height: 300px;
            overflow-y: scroll;
            padding: 10px;
            margin-bottom: 10px;
        }
        .message {
            margin-bottom: 10px;
        }
        .message.user {
            text-align: right;
        }
        .message.counsellor {
            text-align: left;
        }
        #input-container {
            display: flex;
        }
        #input-container textarea {
            flex-grow: 1;
            padding: 5px;
            font-size: 14px;
        }
        #input-container button {
            margin-left: 10px;
            padding: 5px 15px;
            font-size: 14px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div id="chat-container">
        <h2>Text Counselling Service</h2>
        <div id="messages"></div>
        <div id="input-container">
            <textarea id="message-input" placeholder="Type your message here..." rows="2"></textarea>
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>
    <script>
        const messagesContainer = document.getElementById('messages');

        // Function to render messages
        function renderMessages(messages) {
            messagesContainer.innerHTML = '';
            messages.forEach(msg => {
                const messageDiv = document.createElement('div');
                messageDiv.className = 'message ' + msg.sender;
                messageDiv.innerText = `[${msg.timestamp}] ${msg.sender}: ${msg.text}`;
                messagesContainer.appendChild(messageDiv);
            });
        }

        // Function to fetch messages from the server
        async function fetchMessages() {
            const response = await fetch('/messages');
            const data = await response.json();
            renderMessages(data);
        }

        // Function to send a new message
        async function sendMessage() {
            const messageInput = document.getElementById('message-input');
            const messageText = messageInput.value.trim();

            if (!messageText) return; // Do not send empty messages

            const response = await fetch('/messages', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ text: messageText })
            });

            if (response.ok) {
                messageInput.value = ''; // Clear the input field
                await fetchMessages(); // Refresh messages
            } else {
                alert('Failed to send message.');
            }
        }

        // Fetch messages initially and set interval to refresh every 5 seconds
        fetchMessages();
        setInterval(fetchMessages, 5000);
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    """
    Renders the chat interface.
    """
    return chat_template

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    """
    GET: Returns all messages.
    POST: Adds a new message to the database.
    """
    if request.method == 'GET':
        return jsonify(messages_db)

    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data or 'text' not in data:
                return jsonify({'error': 'Invalid message format'}), 400

            # Create a new message entry
            message = {
                'sender': 'user',  # In production, this would be determined dynamically
                'text': data['text'],
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            messages_db.append(message)
            return jsonify({'success': True}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    """
    Handles 404 errors.
    """
    return jsonify({'error': 'Not Found'}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    """
    Handles server errors.
    """
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
