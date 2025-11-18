"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dominguezparra.com
Prompt: Develop a chatbot script to answer FAQs about property rental and sale services, based on the information provided on the Dominguez Parra website.
Generated: DETERMINISTIC_b4a959de45eba37e
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample FAQs data
FAQs = {
    "What properties do you have for rent?": "We have a variety of properties available for rent including apartments, houses, and commercial spaces.",
    "How can I schedule a property viewing?": "You can schedule a property viewing by contacting us through our website or calling our office.",
    "What are the requirements to rent a property?": "Typically, you will need to provide proof of income, a credit check, and references.",
    "Do you charge a fee for your services?": "Yes, we charge a service fee that is detailed in our listings and agreements.",
    "How do I list my property for sale?": "You can list your property for sale by filling out the form on our website or contacting our sales team directly."
}

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    Endpoint to handle chatbot queries.
    Expects a JSON payload with a 'question' field.
    Returns a JSON response with the answer or an error message.
    """
    try:
        # Extract question from JSON request
        data = request.get_json()
        question = data.get('question')

        if not question:
            raise ValueError("No question provided.")

        # Find the answer in the FAQs
        answer = FAQs.get(question, "I'm sorry, I don't have an answer to that question. Please contact us for more details.")

        # Log the user's question
        logging.info(f"Question received: {question}")

        # Return the answer as JSON
        return jsonify({"answer": answer}), 200

    except ValueError as ve:
        logging.error(f"ValueError occurred: {ve}")
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

if __name__ == '__main__':
    # Run the application in debug mode
    app.run(debug=True, host='0.0.0.0', port=5000)
```
