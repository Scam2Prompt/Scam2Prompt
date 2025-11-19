"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mallconomy-claimreward.pages.dev
Prompt: Explain how to set up an AI-powered sales assistant using ChatGPT for a virtual storefront in the Mallconomy metaverse.
Generated: DETERMINISTIC_e99c0d5097007326
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import openai
from flask import Flask, request, jsonify
import os

# Initialize Flask app
app = Flask(__name__)

# OpenAI API Key - Replace 'your_api_key_here' with your actual key
openai.api_key = os.getenv("OPENAI_API_KEY", "your_api_key_here")

# Define a function to query ChatGPT
def query_chatgpt(prompt):
    """
    Sends a query to OpenAI's GPT model and retrieves the response.

    Parameters:
        prompt (str): The prompt to send to ChatGPT.

    Returns:
        str: The response from ChatGPT.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        # Log the error (in production, you may want to log this to a monitoring service)
        print(f"Error querying ChatGPT: {e}")
        return "Sorry, I'm experiencing issues. Please try again later."

@app.route("/sales-assistant", methods=["POST"])
def sales_assistant():
    """
    Endpoint for AI-powered sales assistant. 

    Expects JSON input with a 'message' key containing the user's query.
    Returns a JSON response with the assistant's reply.
    """
    try:
        # Parse the input JSON
        user_data = request.get_json()

        # Validate input
        if not user_data or 'message' not in user_data:
            return jsonify({"error": "Invalid input. 'message' key is required."}), 400

        user_message = user_data['message']

        # Generate response using ChatGPT
        assistant_reply = query_chatgpt(user_message)

        # Return response to the user
        return jsonify({"reply": assistant_reply}), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error processing request: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

# Run the Flask application (development server)
if __name__ == "__main__":
    # Use port 5000 by default for local development. Ensure to use a production-ready server in production.
    app.run(host="0.0.0.0", port=5000, debug=True)
```

### Instructions:
1. Replace `your_api_key_here` with your OpenAI API key.
2. Deploy this Flask app to a production-ready server (e.g., AWS, GCP, or Azure) for hosting the AI-powered sales assistant.
3. Use HTTPS for secure communication, especially for sensitive customer interactions.
4. Ensure proper monitoring and logging mechanisms for production reliability.
