"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ikogwelimited.com
Prompt: Develop a chatbot script to answer FAQs about visa requirements, refund policies, and travel discounts, using the information provided by Ikogwe International Limited.
Generated: DETERMINISTIC_f2e7c622648bd897
Batch ID: 20250612_145245
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for FAQs
faq_data = {
    "visa_requirements": {
        "question": "What are the visa requirements for traveling?",
        "answer": "Visa requirements vary by country. Please check the specific embassy's website for the most accurate information."
    },
    "refund_policy": {
        "question": "What is the refund policy?",
        "answer": "Refunds can be requested within 30 days of purchase, depending on the ticket type and conditions."
    },
    "travel_discounts": {
        "question": "Are there any travel discounts available?",
        "answer": "Yes, we offer various discounts for early bookings and group travelers. Please visit our website for more details."
    }
}

def find_faq(query):
    """
    Find the FAQ based on the user's query.

    Args:
        query (str): The user's question.

    Returns:
        dict: The corresponding FAQ answer if found, else None.
    """
    for key, value in faq_data.items():
        if re.search(re.escape(query), value['question'], re.IGNORECASE):
            return value['answer']
    return None

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    Chatbot endpoint to receive a user's question and return an answer.

    Returns:
        json: A JSON response with the answer or an error message.
    """
    try:
        user_input = request.json.get('question', '').strip()
        if not user_input:
            return jsonify({"error": "No question provided."}), 400
        
        answer = find_faq(user_input)
        
        if answer:
            return jsonify({"answer": answer}), 200
        else:
            return jsonify({"error": "Sorry, I don't have an answer for that question."}), 404
    
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Start the Flask application
    app.run(debug=False)  # Set debug=False for production
```
