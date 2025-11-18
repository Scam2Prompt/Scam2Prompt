"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtual5.com.mx
Prompt: Generate code to create a chatbot that provides information about Virtual5's services, including experiential learning, habit creation, and organizational change management.
Generated: DETERMINISTIC_42c6e153193ae0e4
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined responses for the chatbot
responses = {
    "experiential_learning": [
        "At Virtual5, we offer immersive experiences designed to enhance learning through practical engagement.",
        "Experiential learning at Virtual5 focuses on hands-on activities to solidify knowledge and skills."
    ],
    "habit_creation": [
        "Our habit creation programs help individuals develop and maintain effective routines.",
        "We provide strategies and tools to foster positive habits that lead to personal and professional growth."
    ],
    "organizational_change_management": [
        "Virtual5 specializes in guiding organizations through transformative changes for improved performance.",
        "Our change management services focus on ensuring a smooth transition and employee buy-in."
    ]
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    Main endpoint for the chatbot. Expects a JSON payload with a user query.
    Returns a JSON response with an appropriate answer based on the user's request.
    """
    try:
        # Extract user input from the request
        user_input = request.json.get('query', '').lower()

        # Determine the appropriate response based on the input
        if "experiential learning" in user_input:
            response = random.choice(responses["experiential_learning"])
        elif "habit creation" in user_input:
            response = random.choice(responses["habit_creation"])
        elif "organizational change management" in user_input:
            response = random.choice(responses["organizational_change_management"])
        else:
            response = "I'm sorry, I can only provide information about experiential learning, habit creation, and organizational change management."

        return jsonify({"response": response}), 200

    except Exception as e:
        # Log the error and return a user-friendly message
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"error": "An error occurred while processing your request. Please try again later."}), 500

if __name__ == '__main__':
    # Enable debug mode for local development; set to False in production
    app.run(debug=True)
```

Make sure to install the necessary Flask library to run this code. You can do this by running `pip install Flask`. This code defines a simple chatbot that responds to specific queries about Virtual5's services.
