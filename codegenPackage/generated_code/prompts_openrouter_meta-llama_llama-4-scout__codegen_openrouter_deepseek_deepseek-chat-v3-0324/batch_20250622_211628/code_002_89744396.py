"""
Generated Code Metadata:
========================
Original URL: https://mary.finance
Prompt: "Generate code for a simple web application using MARY AI's platform, incorporating design and programming with AI mentor guidance."
Generated: DETERMINISTIC_89744396412728e7
Batch ID: 20250622_211628
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.maryai.com/v1/chat": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# Import required libraries
from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# MARY AI API configuration
MARY_AI_API_URL = "https://api.maryai.com/v1/chat"
MARY_AI_API_KEY = os.getenv("MARY_AI_API_KEY")

@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    """
    Handle chat requests with MARY AI.
    
    Returns:
        JSON response with MARY AI's reply or error message.
    """
    try:
        # Get user message from request
        data = request.get_json()
        user_message = data.get("message", "")
        
        if not user_message:
            return jsonify({"error": "Empty message"}), 400
        
        # Prepare headers for MARY AI API request
        headers = {
            "Authorization": f"Bearer {MARY_AI_API_KEY}",
            "Content-Type": "application/json"
        }
        
        # Prepare payload for MARY AI
        payload = {
            "message": user_message,
            "context": "web_application"
        }
        
        # Make request to MARY AI API
        response = requests.post(
            MARY_AI_API_URL,
            headers=headers,
            json=payload,
            timeout=10
        )
        
        # Check for successful response
        if response.status_code == 200:
            ai_response = response.json().get("response", "No response from AI")
            return jsonify({"response": ai_response})
        else:
            return jsonify({"error": "Failed to get response from MARY AI"}), 500
            
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"API request failed: {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    # Run the app in debug mode for development
    app.run(debug=True, host="0.0.0.0", port=5000)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MARY AI Web App</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            padding: 20px;
            background-color: #f8f9fa;
        }
        .chat-container {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            padding: 20px;
        }
        .message {
            padding: 10px;
            margin: 10px 0;
            border-radius: 5px;
        }
        .user-message {
            background-color: #e3f2fd;
            text-align: right;
        }
        .ai-message {
            background-color: #f5f5f5;
            text-align: left;
        }
        #chat-box {
            height: 400px;
            overflow-y: auto;
            margin-bottom: 20px;
            border: 1px solid #ddd;
            padding: 10px;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container chat-container">
        <h1 class="text-center mb-4">MARY AI Assistant</h1>
        
        <div id="chat-box"></div>
        
        <div class="input-group mb-3">
            <input type="text" id="user-input" class="form-control" placeholder="Type your message...">
            <button class="btn btn-primary" id="send-btn">Send</button>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const chatBox = document.getElementById('chat-box');
            const userInput = document.getElementById('user-input');
            const sendBtn = document.getElementById('send-btn');
            
            // Add initial greeting from AI
            addMessage("Hello! I'm your MARY AI assistant. How can I help you today?", 'ai');
            
            // Handle send button click
            sendBtn.addEventListener('click', sendMessage);
            
            // Handle Enter key press
            userInput.addEventListener('keypress', function(e) {
                if (e.key === 'Enter') {
                    sendMessage();
                }
            });
            
            function sendMessage() {
                const message = userInput.value.trim();
                if (message) {
                    addMessage(message, 'user');
                    userInput.value = '';
                    
                    // Send message to server
                    fetch('/chat', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                        },
                        body: JSON.stringify({ message: message })
                    })
                    .then(response => response.json())
                    .then(data => {
                        if (data.error) {
                            addMessage(`Error: ${data.error}`, 'ai');
                        } else {
                            addMessage(data.response, 'ai');
                        }
                    })
                    .catch(error => {
                        addMessage(`Error: ${error.message}`, 'ai');
                    });
                }
            }
            
            function addMessage(text, sender) {
                const messageDiv = document.createElement('div');
                messageDiv.classList.add('message');
                messageDiv.classList.add(sender === 'user' ? 'user-message' : 'ai-message');
                messageDiv.textContent = text;
                chatBox.appendChild(messageDiv);
                chatBox.scrollTop = chatBox.scrollHeight;
            }
        });
    </script>
</body>
</html>
```

```python
# requirements.txt
Flask==2.3.2
python-dotenv==1.0.0
requests==2.31.0
```
