"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jiodigital.live
Prompt: Illustrate how to implement an AI chatbot for customer support on a digital downloads store, similar to the support offered by Spec Digital Sales.
Generated: DETERMINISTIC_ea1348d17468ebc9
Batch ID: 20250612_155200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained AI model for conversation
chatbot = pipeline("conversational", model="microsoft/DialoGPT-medium")

@app.route('/chat', methods=['POST'])
def chat():
    """
    Handle chat messages from users.
    
    Expected JSON format:
    {
        "user_id": "string",
        "message": "string"
    }
    
    Returns a JSON response with the chatbot's reply.
    """
    # Error handling
    try:
        # Get the request data
        data = request.get_json()
        user_id = data.get("user_id")
        user_message = data.get("message")

        # Validate the input
        if not user_id or not user_message:
            return jsonify({"error": "Invalid input. 'user_id' and 'message' are required."}), 400

        # Prepare the chatbot input
        conversation = chatbot(user_message)

        # Get the chatbot's response
        bot_response = conversation.generated_responses[-1]

        # Return the response as JSON
        return jsonify({"user_id": user_id, "response": str(bot_response)}), 200

    except json.JSONDecodeError:
        return jsonify({"error": "Invalid JSON format."}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application on the local development server
    app.run(host='0.0.0.0', port=5000)
```

### Requirements:
- Ensure you have Flask and Transformers installed:
```bash
pip install Flask transformers
```

### Usage:
1. Start the Flask application:
   ```bash
   python app.py
   ```
2. Send a POST request to `/chat` with JSON payload:
   ```json
   {
       "user_id": "customer_123",
       "message": "How do I download my purchase?"
   }
   ``` 

3. Receive a JSON response containing the chatbot's reply.
