"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://isiv.edu.ar
Prompt: Suggest a Python library for creating a chatbot that can answer questions about ISIV's academic programs, such as "Excel Avanzado" or "Contabilidad Básica."
Generated: DETERMINISTIC_cea31c241065e673
Batch ID: 20250612_154209
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from transformers import pipeline, AutoModelForQuestionAnswering, AutoTokenizer

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model and tokenizer for question answering
model_name = "deepset/roberta-base-squad2"
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Initialize the question-answering pipeline
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

# Sample data representing ISIV's academic programs
academic_programs = {
    "Excel Avanzado": "Excel Avanzado es un curso diseñado para usuarios que ya tienen conocimientos básicos de Excel y desean profundizar en funciones avanzadas, análisis de datos y visualización.",
    "Contabilidad Básica": "Contabilidad Básica proporciona una introducción a los principios de contabilidad, incluyendo el ciclo contable, estados financieros y registros contables."
}

@app.route('/ask', methods=['POST'])
def ask_question():
    """
    Endpoint to answer questions about ISIV's academic programs.
    Expects a JSON object with a "question" key.
    """
    try:
        # Get the question from the request
        data = request.get_json()
        question = data.get('question')

        # Check if the question is provided
        if not question:
            return jsonify({"error": "No question provided"}), 400

        # Prepare context from the academic programs
        context = " ".join(academic_programs.values())

        # Use the pipeline to get an answer to the question
        answer = qa_pipeline(question=question, context=context)

        # Return the answer
        return jsonify({
            "question": question,
            "answer": answer['answer'],
            "score": answer['score']
        }), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True, host='0.0.0.0', port=5000)
```

### Notes:
- Ensure you have the necessary libraries installed:
```bash
pip install Flask transformers
```
- This code snippet creates a simple Flask app with an endpoint to answer questions regarding ISIV's academic programs using a pre-trained question-answering model.
