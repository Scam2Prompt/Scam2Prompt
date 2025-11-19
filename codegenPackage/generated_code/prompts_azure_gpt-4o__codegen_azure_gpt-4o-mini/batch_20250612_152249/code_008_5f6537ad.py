"""
Generated Code Metadata:
========================
Original URL: https://bafybeie3t6miqfcnbmegku6rqykux7ln7q2jug672nhfgveqoixyrzskhq.ipfs.dweb.link
Prompt: Create a chatbot using IntentsGPT to answer user queries about Aperture Finance's features, including liquidity positions, token swaps, and AI-driven strategies.
Generated: DETERMINISTIC_5f6537ad871f84e0
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from flask import Flask, request, jsonify
from intents_gpt import IntentsGPT  # Assuming IntentsGPT is a library for handling intents

# Initialize Flask app
app = Flask(__name__)

# Load environment variables for API keys and configurations
API_KEY = os.getenv('INTENTS_GPT_API_KEY')
if not API_KEY:
    raise ValueError("INTENTS_GPT_API_KEY environment variable not set.")

# Initialize IntentsGPT with the API key
chatbot = IntentsGPT(api_key=API_KEY)

# Define a route for handling user queries
@app.route('/ask', methods=['POST'])
def ask():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Validate input
        if 'query' not in data:
            return jsonify({'error': 'Query not provided'}), 400
        
        user_query = data['query']
        
        # Get the response from IntentsGPT
        response = chatbot.get_response(user_query)
        
        # Return the response as JSON
        return jsonify({'response': response}), 200

    except json.JSONDecodeError:
        return jsonify({'error': 'Invalid JSON format'}), 400
    except Exception as e:
        # Log the exception (in a real application, use a logging framework)
        print(f"Error occurred: {str(e)}")
        return jsonify({'error': 'An error occurred while processing your request'}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Requirements
- Flask
- intents_gpt (hypothetical library)

### Environment Variables
- Set `INTENTS_GPT_API_KEY` in your environment to use the IntentsGPT API.
