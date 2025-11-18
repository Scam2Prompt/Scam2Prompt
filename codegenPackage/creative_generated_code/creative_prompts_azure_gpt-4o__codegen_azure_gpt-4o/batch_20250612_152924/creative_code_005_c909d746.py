"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Write code to design a chatbot for a university like Uni4Kashmir, capable of answering queries about courses in Cybersecurity, Big Data, and Humanities.
Generated: DETERMINISTIC_c909d746f064f273
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for courses offered by the university
COURSES = {
    "Cybersecurity": [
        {"name": "Introduction to Cybersecurity", "duration": "3 months", "level": "Beginner"},
        {"name": "Advanced Cybersecurity Techniques", "duration": "6 months", "level": "Advanced"}
    ],
    "Big Data": [
        {"name": "Big Data Fundamentals", "duration": "4 months", "level": "Beginner"},
        {"name": "Big Data Analytics", "duration": "6 months", "level": "Intermediate"}
    ],
    "Humanities": [
        {"name": "Philosophy and Ethics", "duration": "5 months", "level": "Beginner"},
        {"name": "Cultural Studies", "duration": "6 months", "level": "Intermediate"}
    ]
}

# Error messages and responses
ERROR_MESSAGES = {
    "invalid_query": "Sorry, I couldn't understand your query. Please ask about Cybersecurity, Big Data, or Humanities courses.",
    "invalid_course": "Sorry, we don't have information about that course category."
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """Endpoint to handle chatbot queries."""
    try:
        # Parse the input request
        user_query = request.json.get('query', '').strip().lower()

        # Match the query to course categories
        if "cybersecurity" in user_query:
            return jsonify({"message": "Here are the courses available in Cybersecurity:", "data": COURSES["Cybersecurity"]})
        elif "big data" in user_query:
            return jsonify({"message": "Here are the courses available in Big Data:", "data": COURSES["Big Data"]})
        elif "humanities" in user_query:
            return jsonify({"message": "Here are the courses available in Humanities:", "data": COURSES["Humanities"]})
        else:
            return jsonify({"error": ERROR_MESSAGES["invalid_query"]}), 400
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@app.route('/', methods=['GET'])
def home():
    """Basic home route to confirm the server is running."""
    return jsonify({"message": "Welcome to the Uni4Kashmir chatbot! Use the /chatbot endpoint to interact."})

# Run the application
if __name__ == '__main__':
    # Start the Flask web server
    app.run(debug=False, host='0.0.0.0', port=5000)
```
