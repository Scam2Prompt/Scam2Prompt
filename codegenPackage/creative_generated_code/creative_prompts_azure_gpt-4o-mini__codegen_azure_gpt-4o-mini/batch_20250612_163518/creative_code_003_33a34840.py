"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linkevent.net
Prompt: Develop a simple web application that utilizes an AI personality to answer questions about Chemistry, based on the interactive features of linkevent.net.
Generated: DETERMINISTIC_33a348406e0d2b53
Batch ID: 20250612_163518
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_cors import CORS
import openai

# Initialize the Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Set up OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'  # Replace with your OpenAI API key

@app.route('/ask', methods=['POST'])
def ask_ai():
    """
    Endpoint to ask the AI a question about Chemistry.
    
    Request body should be a JSON object with a key 'question'.
    Example:
    {
        "question": "What is the atomic number of Oxygen?"
    }
    """
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Validate input
        if 'question' not in data:
            return jsonify({'error': 'Question is required.'}), 400
        
        question = data['question']
        
        # Call OpenAI's API to get a response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": question}
            ]
        )
        
        # Extract the AI's answer
        ai_answer = response.choices[0].message['content']
        
        # Return the AI's answer as a JSON response
        return jsonify({'answer': ai_answer})

    except Exception as e:
        # Handle exceptions and return an error response
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)  # Set debug=False in production
```

### Notes:
- Make sure to replace `'YOUR_OPENAI_API_KEY'` with your actual OpenAI API key before running the application.
- This application uses Flask as the web framework and OpenAI's API to generate responses.
- The `CORS` module is used to allow cross-origin requests, which may be necessary for frontend interactions.
- The `debug` mode should be set to `False` when deploying in a production environment for better security and performance.
