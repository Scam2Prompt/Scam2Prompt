"""
Generated Code Metadata:
========================
Original URL: https://neotokyo.pages.dev
Prompt: Create a FAQ section for a crypto gaming community like Neo Tokyo, addressing common questions about joining, citizens, and the store.
Generated: DETERMINISTIC_8fc0d3524d011a2f
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# FAQ data structure
faq_data = [
    {
        "question": "How do I join the Neo Tokyo community?",
        "answer": "To join Neo Tokyo, you need to participate in the community's recruitment events or purchase a citizen NFT from the marketplace."
    },
    {
        "question": "What is a Neo Tokyo citizen?",
        "answer": "A Neo Tokyo citizen is an NFT that grants membership to the community and access to exclusive events, resources, and opportunities."
    },
    {
        "question": "What can I find in the Neo Tokyo store?",
        "answer": "The Neo Tokyo store offers exclusive merchandise, in-game items, and other collectibles for community members."
    }
]

# Route to get all FAQs
@app.route('/faqs', methods=['GET'])
def get_faqs():
    """
    Endpoint to retrieve all FAQs.
    Returns:
        JSON response containing all FAQs.
    """
    return jsonify({"faqs": faq_data}), 200

# Route to get a specific FAQ by question
@app.route('/faqs/search', methods=['GET'])
def search_faq():
    """
    Endpoint to search for a specific FAQ by question.
    Query Parameters:
        question (str): The question to search for.
    Returns:
        JSON response containing the matching FAQ or an error message.
    """
    question = request.args.get('question', '').strip()
    if not question:
        return jsonify({"error": "Question parameter is required."}), 400

    # Search for the FAQ
    for faq in faq_data:
        if faq["question"].lower() == question.lower():
            return jsonify({"faq": faq}), 200

    return jsonify({"error": "FAQ not found."}), 404

# Error handler for 404 - Not Found
@app.errorhandler(404)
def not_found(error):
    """
    Custom error handler for 404 errors.
    Returns:
        JSON response with error details.
    """
    return jsonify({"error": "Resource not found."}), 404

# Error handler for 500 - Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    """
    Custom error handler for 500 errors.
    Returns:
        JSON response with error details.
    """
    return jsonify({"error": "An internal server error occurred."}), 500

# Main entry point for the application
if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
