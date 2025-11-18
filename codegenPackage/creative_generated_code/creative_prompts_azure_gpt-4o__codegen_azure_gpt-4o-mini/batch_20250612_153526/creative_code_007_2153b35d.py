"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kiberahamlets.org
Prompt: Create a chatbot using natural language processing that answers questions about Kibera Hamlets' programs, such as education initiatives ("Somesha") or environmental conservation efforts.
Generated: DETERMINISTIC_2153b35d7ed82cb0
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging
from flask import Flask, request, jsonify
from transformers import pipeline

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the Flask application
app = Flask(__name__)

# Load the NLP model for question answering
try:
    nlp_model = pipeline("question-answering")
except Exception as e:
    logging.error("Failed to load the NLP model: %s", e)
    raise SystemExit("NLP model initialization failed.")

# Define available programs information
programs_info = {
    "Somesha": {
        "description": "Somesha aims to provide quality education to children in Kibera through various initiatives including tutoring and mentorship.",
        "details": [
            "Tutoring sessions are conducted every Saturday.",
            "Mentorship programs connect students with local professionals.",
            "Scholarships are available for eligible students."
        ]
    },
    "Environmental Conservation": {
        "description": "This program focuses on sustainable practices and raising awareness about environmental issues in Kibera.",
        "details": [
            "Community clean-up drives are organized monthly.",
            "Workshops on recycling and waste management are held quarterly.",
            "Tree planting activities engage local youth and families."
        ]
    }
}

# Define a function to answer user questions based on program info
def answer_question(program_name: str, question: str) -> str:
    if program_name in programs_info:
        context = programs_info[program_name]["description"] + ' '.join(programs_info[program_name]["details"])
        answer = nlp_model({"question": question, "context": context})
        return answer['answer']
    else:
        return "I'm sorry, I don't have information on that program."

# Define the chatbot API endpoint
@app.route('/chatbot', methods=['POST'])
def chatbot():
    try:
        # Get the user's input from the request
        user_input = request.json.get('input')
        if not user_input:
            return jsonify({"error": "Input is required."}), 400
        
        # Determine the program name and the question from user input
        if "education" in user_input.lower():
            program_name = "Somesha"
        elif "environment" in user_input.lower():
            program_name = "Environmental Conservation"
        else:
            return jsonify({"response": "Please ask about 'Somesha' or 'Environmental Conservation' programs."}), 200

        # Generate an answer to the user's question
        question = user_input
        response = answer_question(program_name, question)
        
        return jsonify({"response": response}), 200
        
    except Exception as e:
        logging.error("Error processing request: %s", e)
        return jsonify({"error": "An error occurred while processing your request."}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```

Ensure you have the required packages installed, such as `Flask` and `transformers`, to run this code. You can install them using pip:

```bash
pip install Flask transformers
```
