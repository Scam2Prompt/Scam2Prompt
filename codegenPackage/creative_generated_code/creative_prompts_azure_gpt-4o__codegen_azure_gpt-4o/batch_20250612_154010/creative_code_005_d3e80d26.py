"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colegiodepsicologosoruro.org
Prompt: Recommend an API or library to create interactive capsules for psychological support, similar to the COVID-19 psychological support initiative described on the Colegio de Psicólogos de Oruro website.
Generated: DETERMINISTIC_d3e80d266ca4a7fc
Batch ID: 20250612_154010
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Here's a Python implementation using Flask and OpenAI's GPT model as an interactive capsule for psychological support:

```python
# app.py
# Flask application for creating interactive psychological support capsules using OpenAI's GPT API

from flask import Flask, request, jsonify
import openai
import os

# Initialize the Flask app
app = Flask(__name__)

# Set your OpenAI API key securely
openai.api_key = os.getenv("OPENAI_API_KEY")

# Route for the psychological support capsule
@app.route("/capsule", methods=["POST"])
def psychological_support_capsule():
    """
    Endpoint to interact with the psychological support capsule.
    Accepts JSON input with a 'message' field and returns a response from the AI.
    """
    try:
        # Parse the incoming JSON request
        data = request.get_json()
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"error": "Message field is required"}), 400

        # Generate an AI response using OpenAI GPT
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Choose the GPT model
            messages=[
                {"role": "system", "content": "You are a kind and empathetic psychological support assistant."},
                {"role": "user", "content": user_message}
            ]
        )

        # Extract and return the AI's reply
        ai_message = response["choices"][0]["message"]["content"]
        return jsonify({"response": ai_message}), 200

    except openai.error.OpenAIError as e:
        # Handle errors from OpenAI API
        return jsonify({"error": f"OpenAI API error: {str(e)}"}), 500

    except Exception as e:
        # Handle generic errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

# Run the application
if __name__ == "__main__":
    # Use debug mode only in development, not production
    app.run(host="0.0.0.0", port=5000, debug=True)
```

### Instructions:
1. **Environment Setup**: Install required dependencies using `pip install flask openai`.
2. **Set OpenAI API Key**: Ensure the OpenAI API key is stored securely, e.g., as an environment variable (`OPENAI_API_KEY`).
3. **Run the Server**: Execute the script using `python app.py`, and the application will run on `http://localhost:5000`.
4. **API Request**: To interact with the capsule, send a POST request to `/capsule` with a JSON body containing a `message` field.

### Example Payload:
```json
{
  "message": "I'm feeling anxious about my upcoming exams."
}
```

### Example Response:
```json
{
  "response": "I'm sorry you're feeling this way. Exams can be stressful, but remember to take deep breaths and focus on one step at a time. You've got this!"
}
```
