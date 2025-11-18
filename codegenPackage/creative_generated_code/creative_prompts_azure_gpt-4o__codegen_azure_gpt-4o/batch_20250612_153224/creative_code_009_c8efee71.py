"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prgmea.pk
Prompt: Build a chatbot using Python and Flask that answers common questions about PRGMEA membership benefits and training programs.
Generated: DETERMINISTIC_c8efee714f8100df
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Predefined responses for common questions
responses = {
    "membership benefits": (
        "PRGMEA membership offers networking opportunities, access to export-related resources, "
        "discounted training programs, and updates on industry news and policies."
    ),
    "training programs": (
        "PRGMEA offers training programs focused on garment manufacturing, export procedures, "
        "quality assurance, and workforce development."
    )
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    Endpoint for the chatbot. Accepts JSON requests with a 'question' key and returns responses.
    """
    try:
        # Get the user input from the JSON request
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({"error": "Invalid input. Please provide a 'question' key in the JSON request."}), 400
        
        question = data['question'].strip().lower()
        
        # Match the question with predefined responses
        if "membership benefits" in question:
            return jsonify({"response": responses["membership benefits"]})
        elif "training programs" in question:
            return jsonify({"response": responses["training programs"]})
        else:
            return jsonify({"response": "I'm sorry, I can only answer questions about PRGMEA membership benefits or training programs."})
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500

@app.route('/')
def home():
    """
    Home endpoint to indicate the service is running.
    """
    return "PRGMEA Chatbot is running. Use the '/chatbot' endpoint to interact."

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=False, host='0.0.0.0', port=5000)
```
