"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradetoearnoptions.com
Prompt: Suggest libraries or APIs for integrating 24/7 web chat support into an investment platform, similar to the support system described on Tradetoearnoption.
Generated: DETERMINISTIC_6f7680ec7d884e8e
Batch ID: 20250612_154622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to integrate a 24/7 web chat support system into an investment platform.
It uses the ChatGPT API provided by OpenAI and Flask for creating a server to handle chat queries.
Before running, ensure you have installed the necessary libraries: Flask, requests, and OpenAI's Python SDK.
"""

import os
import openai
from flask import Flask, request, jsonify

# Flask app initialization
app = Flask(__name__)

# Set OpenAI API key (replace 'YOUR_API_KEY' with your actual API key)
openai.api_key = os.getenv("OPENAI_API_KEY", "YOUR_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to handle chat messages sent by the client.
    Expects a JSON payload with a 'message' field containing the user's query.
    """
    try:
        # Extract the user's message from the request payload
        user_message = request.json.get("message")
        if not user_message:
            return jsonify({"error": "Message field is required."}), 400

        # Send the user's message to OpenAI's API
        response = openai.ChatCompletion.create(
            model="gpt-4",  # Use GPT-4 model for better quality
            messages=[
                {"role": "system", "content": "You are a helpful and professional support assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        # Parse response from OpenAI
        assistant_response = response.choices[0].message['content']
        return jsonify({"response": assistant_response}), 200

    except openai.error.OpenAIError as e:
        # Handle errors from OpenAI API
        return jsonify({"error": f"OpenAI API error: {str(e)}"}), 500
    except Exception as e:
        # General error handling
        return jsonify({"error": f"Server error: {str(e)}"}), 500

if __name__ == '__main__':
    """
    Entrypoint for the Flask server. Run the app and listen on port 5000.
    """
    app.run(host='0.0.0.0', port=5000)
```

**Required Libraries**:  
Install the necessary Python libraries before running the script:  
```bash
pip install flask openai requests
```

**Notes**:  
- Replace `"YOUR_API_KEY"` with your actual OpenAI API key or set it as an environment variable `OPENAI_API_KEY`.
- You might need to deploy this server on a platform like AWS, Heroku, or Google Cloud for production use.
