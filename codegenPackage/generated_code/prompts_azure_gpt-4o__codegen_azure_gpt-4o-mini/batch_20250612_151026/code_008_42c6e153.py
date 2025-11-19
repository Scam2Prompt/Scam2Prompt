"""
Generated Code Metadata:
========================
Original URL: https://virtual5.com.mx
Prompt: Generate code to create a chatbot that provides information about Virtual5's services, including experiential learning, habit creation, and organizational change management.
Generated: DETERMINISTIC_42c6e153193ae0e4
Batch ID: 20250612_151026
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for Virtual5's services
services = {
    "experiential_learning": {
        "description": "Experiential learning focuses on learning through experience and reflection.",
        "benefits": [
            "Enhances critical thinking skills",
            "Promotes active engagement",
            "Encourages collaboration and teamwork"
        ]
    },
    "habit_creation": {
        "description": "Habit creation involves developing new habits to improve personal and professional effectiveness.",
        "benefits": [
            "Increases productivity",
            "Improves time management",
            "Fosters personal growth"
        ]
    },
    "organizational_change_management": {
        "description": "Organizational change management helps organizations navigate and implement change effectively.",
        "benefits": [
            "Minimizes resistance to change",
            "Ensures smooth transitions",
            "Aligns organizational goals with change initiatives"
        ]
    }
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    Chatbot endpoint to provide information about Virtual5's services.
    Expects a JSON payload with a 'query' key.
    """
    try:
        # Get the user's query from the request
        user_query = request.json.get('query', '').lower()

        # Simple keyword-based response generation
        if "experiential learning" in user_query:
            service_info = services["experiential_learning"]
        elif "habit creation" in user_query:
            service_info = services["habit_creation"]
        elif "organizational change management" in user_query:
            service_info = services["organizational_change_management"]
        else:
            return jsonify({"response": "I'm sorry, I don't have information on that topic."}), 400

        # Constructing the response
        response = {
            "service": service_info["description"],
            "benefits": random.choice(service_info["benefits"])  # Randomly select a benefit to share
        }
        return jsonify({"response": response}), 200

    except Exception as e:
        # Log the error (in a real application, use logging framework)
        print(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
```
