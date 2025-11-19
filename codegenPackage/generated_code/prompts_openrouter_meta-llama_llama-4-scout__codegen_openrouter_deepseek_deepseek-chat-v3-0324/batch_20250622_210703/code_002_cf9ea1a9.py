"""
Generated Code Metadata:
========================
Original URL: https://applestorebali.com
Prompt: Generate a code snippet to implement a chat system, similar to the one on Apple Market Bali's website, using a messaging platform like WhatsApp or a custom solution.
Generated: DETERMINISTIC_cf9ea1a97cad244f
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from flask import Flask, request, jsonify, render_template
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
WHATSAPP_NUMBER = os.getenv('WHATSAPP_NUMBER')
ADMIN_PHONE = os.getenv('ADMIN_PHONE')

# Initialize Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/')
def home():
    """Render the chat interface."""
    return render_template('chat.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    """Handle sending messages via WhatsApp."""
    try:
        data = request.get_json()
        message = data.get('message')
        phone = data.get('phone')
        
        if not message or not phone:
            return jsonify({'error': 'Message and phone number are required'}), 400
        
        # Send message via WhatsApp
        response = client.messages.create(
            body=message,
            from_=f'whatsapp:{WHATSAPP_NUMBER}',
            to=f'whatsapp:{phone}'
        )
        
        return jsonify({
            'status': 'success',
            'message_sid': response.sid
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/receive_message', methods=['POST'])
def receive_message():
    """Handle incoming messages from WhatsApp."""
    try:
        incoming_message = request.values.get('Body', '').strip()
        sender = request.values.get('From', '').strip()
        
        if not incoming_message or not sender:
            return jsonify({'error': 'Invalid request'}), 400
        
        # Forward message to admin
        client.messages.create(
            body=f"New message from {sender}: {incoming_message}",
            from_=f'whatsapp:{WHATSAPP_NUMBER}',
            to=f'whatsapp:{ADMIN_PHONE}'
        )
        
        return jsonify({'status': 'success'}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/chat.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apple Market Bali - Chat</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
        }
        .chat-container {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 20px;
            height: 400px;
            overflow-y: auto;
            margin-bottom: 20px;
        }
        .message {
            margin-bottom: 10px;
            padding: 10px;
            border-radius: 5px;
        }
        .user-message {
            background-color: #e3f2fd;
            text-align: right;
        }
        .response-message {
            background-color: #f1f1f1;
            text-align: left;
        }
        #message-input {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border-radius: 5px;
            border: 1px solid #ddd;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Apple Market Bali - Chat Support</h1>
    <div class="chat-container" id="chat-box">
        <!-- Messages will appear here -->
    </div>
    <input type="text" id="message-input" placeholder="Type your message here...">
    <button onclick="sendMessage()">Send</button>

    <script>
        const phoneNumber = '+6281234567890'; // Replace with your WhatsApp number
        
        function sendMessage() {
            const messageInput = document.getElementById('message-input');
            const message = messageInput.value.trim();
            
            if (!message) {
                alert('Please enter a message');
                return;
            }
            
            // Display user message
            displayMessage(message, 'user-message');
            
            // Send to server
            fetch('/send_message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: message,
                    phone: phoneNumber
                }),
            })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    throw new Error(data.error);
                }
                messageInput.value = '';
            })
            .catch(error => {
                console.error('Error:', error);
                displayMessage('Failed to send message. Please try again.', 'response-message');
            });
        }
        
        function displayMessage(message, className) {
            const chatBox = document.getElementById('chat-box');
            const messageElement = document.createElement('div');
            messageElement.className = `message ${className}`;
            messageElement.textContent = message;
            chatBox.appendChild(messageElement);
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>
</body>
</html>
```

```env
# .env file
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
TWILIO_PHONE_NUMBER=+1234567890
WHATSAPP_NUMBER=+14155238886
ADMIN_PHONE=+6281234567890
```
