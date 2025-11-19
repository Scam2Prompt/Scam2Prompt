"""
Generated Code Metadata:
========================
Original URL: https://wallstreetpepelive.com
Prompt: "Wall Street Pepe Token FAQs"
Generated: DETERMINISTIC_67df68626da2dcb5
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample FAQs data
faqs = [
    {
        "question": "What is Wall Street Pepe Token?",
        "answer": "Wall Street Pepe Token is a meme-based cryptocurrency that combines the popular Pepe meme with the financial themes of Wall Street."
    },
    {
        "question": "How can I buy Wall Street Pepe Token?",
        "answer": "You can buy Wall Street Pepe Token on various cryptocurrency exchanges that list it. Make sure to do your research before purchasing."
    },
    {
        "question": "Is Wall Street Pepe Token a good investment?",
        "answer": "As with any investment, it's important to do your own research and consider the risks involved. Consult with a financial advisor if needed."
    },
    {
        "question": "Where can I find more information?",
        "answer": "You can find more information on our official website and social media channels."
    }
]

@app.route('/faqs', methods=['GET'])
def get_faqs():
    """
    Endpoint to retrieve the list of FAQs.
    Returns:
        JSON response containing the list of FAQs.
    """
    try:
        return jsonify(faqs), 200
    except Exception as e:
        # Log the error (in a real application, use a logging framework)
        print(f"Error retrieving FAQs: {e}")
        return jsonify({"error": "Unable to retrieve FAQs"}), 500

@app.route('/faqs/<int:faq_id>', methods=['GET'])
def get_faq(faq_id):
    """
    Endpoint to retrieve a specific FAQ by its ID.
    Args:
        faq_id (int): The ID of the FAQ to retrieve.
    Returns:
        JSON response containing the specific FAQ or an error message.
    """
    try:
        if 0 <= faq_id < len(faqs):
            return jsonify(faqs[faq_id]), 200
        else:
            return jsonify({"error": "FAQ not found"}), 404
    except Exception as e:
        # Log the error (in a real application, use a logging framework)
        print(f"Error retrieving FAQ with ID {faq_id}: {e}")
        return jsonify({"error": "Unable to retrieve FAQ"}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True)
```
