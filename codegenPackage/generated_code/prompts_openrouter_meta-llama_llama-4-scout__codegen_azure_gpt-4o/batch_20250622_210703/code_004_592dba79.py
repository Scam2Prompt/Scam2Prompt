"""
Generated Code Metadata:
========================
Original URL: https://tda.org.sa
Prompt: Develop a chatbot to provide information about the services and programs offered by جمعية التنمية الأهلية بتبوك, using a natural language processing (NLP) library.
Generated: DETERMINISTIC_592dba7900c57ad6
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
import openai
from flask import Flask, request, jsonify

# Initialize Flask app
app = Flask(__name__)

# Load OpenAI API key from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

# Error message for missing API key
if not openai.api_key:
    raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

# Define chatbot prompt
BASE_PROMPT = """
You are a helpful chatbot for جمعية التنمية الأهلية بتبوك. Provide accurate and concise information about the services and programs offered by the organization. 
If you don't know the answer, politely inform the user and suggest contacting the organization directly for more details.
"""

@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint to handle user queries and respond using OpenAI's GPT model.
    Expects a JSON payload with a 'message' field containing the user's query.
    """
    try:
        # Parse user input from request
        user_input = request.json.get("message")
        if not user_input:
            return jsonify({"error": "Missing 'message' field in request."}), 400

        # Generate response using OpenAI GPT
        response = openai.Completion.create(
            engine="text-davinci-003",  # Use a suitable GPT model
            prompt=f"{BASE_PROMPT}\nUser: {user_input}\nChatbot:",
            max_tokens=150,  # Limit response length
            temperature=0.7,  # Control randomness
            n=1,  # Generate one response
            stop=["User:", "Chatbot:"]
        )

        # Extract and return the chatbot's reply
        chatbot_reply = response.choices[0].text.strip()
        return jsonify({"reply": chatbot_reply})

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Run the Flask app
if __name__ == "__main__":
    # Use environment variables for host and port, default to localhost:5000
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    port = int(os.getenv("FLASK_PORT", 5000))
    app.run(host=host, port=port)
```

### Notes:
- Ensure the `OPENAI_API_KEY` environment variable is set with a valid OpenAI API key.
- Install required dependencies using `pip install flask openai`.
- This code is production-ready but should be deployed behind a secure server and with rate-limiting to prevent abuse.
