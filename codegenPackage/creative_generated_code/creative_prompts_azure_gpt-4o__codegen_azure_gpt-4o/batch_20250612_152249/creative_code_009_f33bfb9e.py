"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://askcardiologist.in
Prompt: Create a chatbot using Python that can answer FAQs about cardiac treatments offered by Dr. S. Nagendra Boopathy, including Mitraclip, TAVR/TAVI, and valve therapy.
Generated: DETERMINISTIC_f33bfb9ea203143c
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Import necessary modules for chatbot functionality
from flask import Flask, request, jsonify

# Initialize Flask app for handling HTTP requests
app = Flask(__name__)

# Predefined FAQs and answers about cardiac treatments
faq_data = {
    "mitraclip": (
        "MitraClip is a minimally invasive procedure used to treat mitral regurgitation. "
        "It involves implanting a clip on the mitral valve to restore proper function."
    ),
    "tavr": (
        "Transcatheter Aortic Valve Replacement (TAVR/TAVI) is a procedure to replace a "
        "damaged aortic valve without open-heart surgery."
    ),
    "valve therapy": (
        "Valve therapy refers to treatments for valve diseases, which may include repair, replacement, "
        "or minimally invasive procedures like TAVR and MitraClip."
    ),
}

# Function to respond to user queries
def get_response(user_input):
    """
    Process the user input and return an appropriate response.
    :param user_input: str, the input text from the user.
    :return: str, the chatbot's response.
    """
    user_input = user_input.lower()  # Convert input to lowercase for case-insensitive matching

    # Check if the input matches any available FAQ keywords
    for keyword, answer in faq_data.items():
        if keyword in user_input:
            return answer

    # Default response for unrecognized queries
    return (
        "I'm sorry, I don't have information about that. You can ask me about MitraClip, TAVR/TAVI, or valve therapy."
    )


@app.route("/chat", methods=["POST"])
def chat():
    """
    Endpoint to handle chatbot queries via POST request.
    Expects a JSON payload with a 'message' field.
    """
    try:
        # Extract user message from the request
        user_message = request.json.get("message", "")

        if not user_message:
            # Handle case where message is missing
            return jsonify({"error": "Message field is required"}), 400

        # Generate chatbot response
        bot_response = get_response(user_message)

        # Return response as JSON
        return jsonify({"response": bot_response})
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


@app.route("/", methods=["GET"])
def index():
    """
    Default homepage route for the chatbot service.
    """
    return (
        "Welcome to Dr. S. Nagendra Boopathy's Cardiac Treatments Chatbot. "
        "Use the /chat endpoint to ask questions about MitraClip, TAVR/TAVI, or valve therapy."
    )


if __name__ == "__main__":
    # Run the Flask app on localhost, port 5000
    app.run(host="0.0.0.0", port=5000, debug=False)
```
