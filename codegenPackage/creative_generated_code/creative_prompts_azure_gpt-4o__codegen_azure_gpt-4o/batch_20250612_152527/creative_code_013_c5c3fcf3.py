"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gigachadgpt-en.web.app
Prompt: Develop a web application that integrates the GigaChadGPT chatbot API and allows users to interact with it directly from the site.
Generated: DETERMINISTIC_c5c3fcf3705ac807
Batch ID: 20250612_152527
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.gigachadgpt.com/v1/chat`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://127.0.0.1:5000/`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.gigachadgpt.com/v1/chat": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
# Filename: app.py

from flask import Flask, request, jsonify, render_template
import requests

# Initialize Flask application
app = Flask(__name__)

# GigaChadGPT API configuration
GIGACHADGPT_API_URL = "https://api.gigachadgpt.com/v1/chat"  # Replace with the actual API URL
API_KEY = "your_api_key_here"  # Replace with your GigaChadGPT API key

# Define the home route to render the chatbot interface
@app.route('/', methods=['GET'])
def home():
    """
    Render the homepage with chatbot interface.
    """
    return render_template('index.html')

# Define the route to handle user messages and interact with the GigaChadGPT API
@app.route('/send_message', methods=['POST'])
def send_message():
    """
    Handle incoming user messages and fetch responses from GigaChadGPT API.
    """
    try:
        # Extract user message from the request
        user_message = request.json.get('message', '')
        if not user_message:
            return jsonify({"error": "Message cannot be empty"}), 400

        # Prepare the payload for GigaChadGPT API request
        payload = {
            "prompt": user_message,
            "max_tokens": 150,  # Adjust max tokens as needed
            "temperature": 0.7  # Adjust creativity level as needed
        }
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        # Make the API request
        response = requests.post(GIGACHADGPT_API_URL, json=payload, headers=headers)

        # Check for API errors
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch response from GigaChadGPT"}), response.status_code

        # Parse the response from the API
        bot_reply = response.json().get('response', 'Sorry, I could not understand that. Please try again.')

        # Return the chatbot response to the client
        return jsonify({"response": bot_reply})

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the application in debug mode for development purposes
if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- Filename: templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GigaChadGPT Chatbot</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css">
</head>
<body class="bg-light">
    <div class="container mt-5">
        <h1 class="text-center">GigaChadGPT Chatbot</h1>
        <div class="card mt-4">
            <div class="card-body">
                <div id="chatbox">
                    <div id="messages" class="mb-3"></div>
                </div>
                <div class="input-group">
                    <input id="userInput" type="text" class="form-control" placeholder="Type your message..." />
                    <button id="sendButton" class="btn btn-primary">Send</button>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Handle message sending and receiving responses
        document.getElementById('sendButton').addEventListener('click', async () => {
            const userInput = document.getElementById('userInput');
            const message = userInput.value.trim();
            const messagesDiv = document.getElementById('messages');

            if (message) {
                // Add user message to chatbox
                const userMessageDiv = document.createElement('div');
                userMessageDiv.className = 'text-end mb-2';
                userMessageDiv.textContent = `You: ${message}`;
                messagesDiv.appendChild(userMessageDiv);

                // Send message to backend
                try {
                    const response = await fetch('/send_message', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ message })
                    });

                    const data = await response.json();
                    if (response.ok) {
                        // Add bot response to chatbox
                        const botMessageDiv = document.createElement('div');
                        botMessageDiv.className = 'text-start mb-2 text-primary';
                        botMessageDiv.textContent = `Bot: ${data.response}`;
                        messagesDiv.appendChild(botMessageDiv);
                    } else {
                        // Handle error response
                        const errorDiv = document.createElement('div');
                        errorDiv.className = 'text-start mb-2 text-danger';
                        errorDiv.textContent = `Error: ${data.error}`;
                        messagesDiv.appendChild(errorDiv);
                    }
                } catch (error) {
                    // Handle fetch or network errors
                    const errorDiv = document.createElement('div');
                    errorDiv.className = 'text-start mb-2 text-danger';
                    errorDiv.textContent = `Error: ${error.message}`;
                    messagesDiv.appendChild(errorDiv);
                }

                // Clear user input field
                userInput.value = '';
            }
        });
    </script>
</body>
</html>
```

**Instructions**:
1. Replace `your_api_key_here` in the Python code with your actual API key from GigaChadGPT.
2. Replace `https://api.gigachadgpt.com/v1/chat` with the correct endpoint URL for the GigaChadGPT API.
3. Install the required Python packages using `pip install flask requests`.
4. Run the Python app using `python app.py` and open the interface in your browser at `http://127.0.0.1:5000/`.
