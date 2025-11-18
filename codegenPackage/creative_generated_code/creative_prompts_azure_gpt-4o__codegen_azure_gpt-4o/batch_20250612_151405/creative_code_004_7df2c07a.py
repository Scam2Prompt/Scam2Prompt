"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scottytheai-en.web.app
Prompt: Develop a chatbot using OpenAI's GPT API that mimics ScottyChat, providing cryptocurrency market insights and answering questions about $SCOTTY tokens.
Generated: DETERMINISTIC_7df2c07ace5a7782
Batch ID: 20250612_151405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import openai
from flask import Flask, request, jsonify
import os

# Initialize Flask app
app = Flask(__name__)

# OpenAI API key (ensure this is set securely, e.g., using environment variables)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Check if API key is provided
if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not set. Please set it in the environment variables.")

# Define a function to query OpenAI's GPT model
def query_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are ScottyChat, an expert in cryptocurrency markets and $SCOTTY tokens."},
                      {"role": "user", "content": prompt}],
            max_tokens=500,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        # Log and return error message for debugging
        print(f"Error querying GPT: {e}")
        return "I'm sorry, but I encountered an error while processing your request."

# Define Flask route for chatbot interaction
@app.route("/chat", methods=["POST"])
def chat():
    try:
        # Get the user input from the request
        user_input = request.json.get("message", "")
        if not user_input:
            return jsonify({"error": "No message provided"}), 400

        # Query GPT model with user input
        response = query_gpt(user_input)

        # Return GPT's response
        return jsonify({"response": response}), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error in chat endpoint: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

# Start Flask app
if __name__ == "__main__":
    # Ensure the app runs in a production-ready Flask server
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
```

### Notes:
- Set the `OPENAI_API_KEY` environment variable securely (e.g., in a `.env` file or deployment configuration).
- To install dependencies, run: `pip install openai flask`.
- Use a production-ready server like Gunicorn or uWSGI for deployment instead of the Flask development server.
