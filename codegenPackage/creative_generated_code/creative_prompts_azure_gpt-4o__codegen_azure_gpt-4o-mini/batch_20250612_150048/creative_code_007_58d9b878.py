"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-atomcapital.com
Prompt: Develop a chatbot that answers FAQs about Atom Capital's registration process and educational offerings using NLP libraries.
Generated: DETERMINISTIC_58d9b878eb65e682
Batch ID: 20250612_150048
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
import logging
from flask import Flask, request, jsonify
from flask_cors import CORS
from transformers import pipeline

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Load FAQ data from a JSON file
def load_faq_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        return {}
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {file_path}")
        return {}

# Load FAQ data
faq_data = load_faq_data('faq_data.json')

# Initialize NLP model for question answering
qa_pipeline = pipeline("question-answering")

@app.route('/ask', methods=['POST'])
def ask():
    """Endpoint to receive questions and return answers."""
    try:
        user_input = request.json.get("question", "")
        if not user_input:
            return jsonify({"error": "No question provided."}), 400

        # Generate answer using FAQ data
        answer = find_answer(user_input)

        return jsonify({"question": user_input, "answer": answer}), 200

    except Exception as e:
        logging.error(f"Error processing request: {str(e)}")
        return jsonify({"error": "Internal server error."}), 500

def find_answer(question):
    """Find an answer to a question from the FAQ dataset."""
    try:
        # Check if question matches any FAQ directly
        for entry in faq_data.get('faqs', []):
            if question.lower() in entry['question'].lower():
                return entry['answer']

        # Use NLP model to generate an answer if no direct match found
        context = " ".join([entry['answer'] for entry in faq_data.get('faqs', [])])
        response = qa_pipeline(question=question, context=context)
        return response['answer'] if response['answer'] else "Sorry, I don't have an answer for that."

    except Exception as e:
        logging.error(f"Error finding answer: {str(e)}")
        return "Sorry, I encountered an error while processing your question."

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
```

**Note**: Make sure to create a `faq_data.json` file with the following structure for the code to work properly:

```json
{
    "faqs": [
        {
            "question": "How do I register?",
            "answer": "To register, please visit our website and follow the registration process."
        },
        {
            "question": "What educational offerings do you have?",
            "answer": "We offer various courses including finance, investment strategies, etc."
        }
    ]
}
```
