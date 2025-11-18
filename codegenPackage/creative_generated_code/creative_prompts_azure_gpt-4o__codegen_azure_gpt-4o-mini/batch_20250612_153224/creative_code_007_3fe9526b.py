"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unimeleducacion.org
Prompt: Recommend libraries for creating a chatbot that can answer questions about Unimel Educación courses, such as "Curso Online de Especialización en Función Inspectora del Sistema Educativo."
Generated: DETERMINISTIC_3fe9526bdf9a1f4c
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from flask import Flask, request, jsonify
from transformers import pipeline

# Initialize the Flask application
app = Flask(__name__)

# Load the pre-trained model for question answering
# This assumes you have the 'transformers' library installed and the appropriate model downloaded
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

# Sample course data
courses = {
    "Curso Online de Especialización en Función Inspectora del Sistema Educativo": {
        "description": "This online course provides specialized training for educational inspectors.",
        "duration": "6 months",
        "requirements": "Bachelor's degree in Education or related field."
    },
    # Add more courses as needed
}

@app.route('/ask', methods=['POST'])
def ask_question():
    """
    Handle incoming questions about courses.

    Expects a JSON payload with the following structure:
    {
        "question": "Your question here"
    }
    """
    try:
        # Extract the question from the request
        data = request.get_json()
        question = data.get('question', '')

        if not question:
            return jsonify({"error": "No question provided."}), 400
        
        # Analyze the question to find the relevant course
        response = {}
        for course_name, details in courses.items():
            # Use the QA pipeline to get an answer based on course details
            result = qa_pipeline(question=question, context=details["description"])
            if result['score'] > 0.5:  # Only consider confident answers
                response[course_name] = {
                    "answer": result['answer'],
                    "score": result['score']
                }

        if not response:
            return jsonify({"error": "No relevant information found."}), 404

        return jsonify(response), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Notes:
- Ensure you have the required libraries installed. You can install them using pip:
  ```bash
  pip install flask transformers
  ```
- Adjust the `courses` dictionary to include all relevant courses and their descriptions.
- The application listens for POST requests at `/ask`, expecting a JSON payload containing a question.
- Error handling is included for missing questions and other potential exceptions.
