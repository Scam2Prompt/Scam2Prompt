"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://relivo.se
Prompt: Create a chatbot using a natural language processing library that answers customer questions about Relivo’s ingredients, health benefits, and usage instructions based on the FAQ section.
Generated: DETERMINISTIC_5e28f765cc269746
Batch ID: 20250612_151459
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
from transformers import pipeline

# Load the FAQ data from a JSON file
def load_faq_data(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise Exception("FAQ file not found.")
    except json.JSONDecodeError:
        raise Exception("Error decoding the FAQ file. Ensure it is a valid JSON format.")

# Initialize the Flask application
app = Flask(__name__)

# Load FAQ data
faq_data = load_faq_data('faq.json')

# Initialize the NLP pipeline for question answering
qa_pipeline = pipeline("question-answering")

# Define a function to answer questions based on FAQ content
def answer_question(question):
    # Prepare the context from the FAQ data
    context = " ".join([f"{item['question']} {item['answer']}" for item in faq_data])
    
    # Use the QA pipeline to get an answer
    result = qa_pipeline(question=question, context=context)

    # Check if the answer confidence is above a threshold
    if result['score'] < 0.5:
        return "I'm sorry, I couldn't find a clear answer to your question."
    
    return result['answer']

# Define API route for asking questions
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    
    # Validate incoming data
    if 'question' not in data:
        return jsonify({"error": "No question provided."}), 400

    question = data['question']
    
    # Get the answer from the FAQ data
    try:
        answer = answer_question(question)
        return jsonify({"question": question, "answer": answer}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Sample `faq.json` structure
```json
[
    {
        "question": "What are the ingredients in Relivo?",
        "answer": "Relivo contains a blend of natural ingredients including vitamins, minerals, and herbal extracts."
    },
    {
        "question": "What are the health benefits of Relivo?",
        "answer": "Relivo is known to boost immunity, improve digestion, and enhance overall wellness."
    },
    {
        "question": "How do I use Relivo?",
        "answer": "For best results, take one scoop mixed with water or your favorite beverage daily."
    }
]
```
