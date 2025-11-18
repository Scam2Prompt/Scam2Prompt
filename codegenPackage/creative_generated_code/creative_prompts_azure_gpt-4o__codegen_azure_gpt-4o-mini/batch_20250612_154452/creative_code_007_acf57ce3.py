"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conferencesglobal.org
Prompt: Develop a chatbot using Python that answers FAQs about abstract submission, registration, invitation letters, duplicate payments, and invoice requests based on the information provided on Conferences Global.
Generated: DETERMINISTIC_acf57ce31b59a6e6
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample FAQ data
faq_data = {
    "abstract_submission": {
        "question": "How can I submit an abstract?",
        "answer": "You can submit your abstract through our online submission portal. Make sure to adhere to the submission guidelines."
    },
    "registration": {
        "question": "How do I register for the conference?",
        "answer": "Registration can be completed online on the registration page of our website."
    },
    "invitation_letters": {
        "question": "Can I request an invitation letter?",
        "answer": "Yes, invitation letters can be requested after successful registration. Please check your email for further instructions."
    },
    "duplicate_payments": {
        "question": "What should I do in case of duplicate payments?",
        "answer": "If you encounter a duplicate payment, please contact our finance team at finance@conferencesglobal.com."
    },
    "invoice_requests": {
        "question": "How can I request an invoice?",
        "answer": "Invoices can be requested through the invoice request form available on our website."
    }
}

@app.route('/chatbot', methods=['POST'])
def chatbot_response():
    """
    Endpoint for the chatbot to process user input and return a relevant answer.
    Expects a JSON payload with 'query' key containing the user question.
    """
    try:
        # Extract user query from the request
        data = request.get_json()

        if not data or 'query' not in data:
            return jsonify({"error": "Invalid input. Please provide a 'query' key."}), 400

        user_query = data['query'].lower()
        
        # Find the best matching FAQ based on the keywords in the query
        response = find_faq_response(user_query)

        if response:
            return jsonify(response), 200
        else:
            return jsonify({"message": "I'm sorry, I don't have an answer for that question."}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500

def find_faq_response(query):
    """
    Finds and returns the relevant FAQ response based on the user's query.
    Uses simple keyword matching to identify the appropriate FAQ.
    """
    for key, value in faq_data.items():
        if key in query:
            return {
                "question": value['question'],
                "answer": value['answer']
            }
    return None

if __name__ == '__main__':
    # Run the Flask app with debug mode off for production
    app.run(host='0.0.0.0', port=5000)
```

### Notes:
- To run this code, Flask must be installed in your environment. You can install it using `pip install Flask`.
- The chatbot API listens for POST requests at the `/chatbot` endpoint and expects a JSON payload with a "query" key.
- Error handling is included to manage invalid input and exceptions during processing.
