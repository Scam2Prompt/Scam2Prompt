"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Develop a chatbot script that can answer FAQs about Swedish family law, business law, and immigration law, using the content from juridiskklinik.se.
Generated: DETERMINISTIC_26ae3138627cefb6
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample FAQs related to Swedish law
FAQ_DATA = {
    "family_law": {
        "What is the legal age for marriage in Sweden?": "The legal age for marriage in Sweden is 18 years.",
        "How does child custody work in Sweden?": "Child custody is decided based on the best interest of the child."
    },
    "business_law": {
        "What are the steps to start a business in Sweden?": "To start a business in Sweden, you need to register your business with the Swedish Companies Registration Office.",
        "What are the tax obligations for businesses in Sweden?": "Businesses in Sweden are required to pay corporate tax, VAT, and potentially other local taxes."
    },
    "immigration_law": {
        "What are the requirements for a work permit in Sweden?": "To obtain a work permit, you must have a job offer from a Swedish employer.",
        "How can I apply for permanent residency in Sweden?": "You can apply for permanent residency after living in Sweden for a specified period on a valid residence permit."
    }
}

def get_faq_response(category, question):
    """
    Retrieve the FAQ response based on the category and question.
    
    Args:
        category (str): The category of law (e.g., family_law, business_law, immigration_law).
        question (str): The question to search for in the FAQ.
    
    Returns:
        str: The answer to the question if found, else a default message.
    """
    # Check if the category exists
    if category not in FAQ_DATA:
        return "I'm sorry, but I don't have information on that category."

    # Check if the question exists in the category
    if question in FAQ_DATA[category]:
        return FAQ_DATA[category][question]
    
    return "I'm sorry, I don't have an answer to that question."

@app.route('/faq', methods=['POST'])
def faq():
    """
    API endpoint to handle FAQ requests.
    
    Expected JSON payload:
    {
        "category": "family_law",
        "question": "What is the legal age for marriage in Sweden?"
    }
    
    Returns:
        JSON response containing the answer to the FAQ.
    """
    try:
        # Parse the incoming JSON request
        data = request.json
        category = data.get('category')
        question = data.get('question')

        # Validate inputs
        if not category or not question:
            return jsonify({"error": "Category and question are required."}), 400

        # Get the response based on the category and question
        answer = get_faq_response(category, question)
        return jsonify({"answer": answer}), 200

    except Exception as e:
        # Log the error for debugging purposes
        app.logger.error(f"Error processing request: {e}")
        return jsonify({"error": "An error occurred while processing your request."}), 500

if __name__ == '__main__':
    # Run the Flask web server
    app.run(debug=True)
```
