"""
Generated Code Metadata:
========================
Original URL: https://metamaskwallet.demovial.com.mx
Prompt: Design an API for managing educational resources, including features for flashcards, quizzes, and learning pathways, inspired by Atria's study methods.
Generated: DETERMINISTIC_6a57e3b9023b8e1c
Batch ID: 20250622_205158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory database for simplicity
db = {
    "flashcards": {},
    "quizzes": {},
    "learning_pathways": {}
}

# Helper function for error responses
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Flashcards API
@app.route('/flashcards', methods=['POST'])
def create_flashcard():
    """
    Create a new flashcard.
    Request JSON: { "question": "string", "answer": "string" }
    """
    data = request.json
    if not data or "question" not in data or "answer" not in data:
        return error_response("Invalid input. 'question' and 'answer' are required.")
    
    flashcard_id = str(uuid4())
    db["flashcards"][flashcard_id] = {
        "id": flashcard_id,
        "question": data["question"],
        "answer": data["answer"]
    }
    return jsonify(db["flashcards"][flashcard_id]), 201

@app.route('/flashcards/<flashcard_id>', methods=['GET'])
def get_flashcard(flashcard_id):
    """
    Retrieve a flashcard by ID.
    """
    flashcard = db["flashcards"].get(flashcard_id)
    if not flashcard:
        return error_response("Flashcard not found.", 404)
    return jsonify(flashcard)

@app.route('/flashcards/<flashcard_id>', methods=['DELETE'])
def delete_flashcard(flashcard_id):
    """
    Delete a flashcard by ID.
    """
    if flashcard_id not in db["flashcards"]:
        return error_response("Flashcard not found.", 404)
    del db["flashcards"][flashcard_id]
    return jsonify({"message": "Flashcard deleted successfully."}), 200

# Quizzes API
@app.route('/quizzes', methods=['POST'])
def create_quiz():
    """
    Create a new quiz.
    Request JSON: { "title": "string", "questions": [ { "question": "string", "options": ["string"], "answer": "string" } ] }
    """
    data = request.json
    if not data or "title" not in data or "questions" not in data:
        return error_response("Invalid input. 'title' and 'questions' are required.")
    
    quiz_id = str(uuid4())
    db["quizzes"][quiz_id] = {
        "id": quiz_id,
        "title": data["title"],
        "questions": data["questions"]
    }
    return jsonify(db["quizzes"][quiz_id]), 201

@app.route('/quizzes/<quiz_id>', methods=['GET'])
def get_quiz(quiz_id):
    """
    Retrieve a quiz by ID.
    """
    quiz = db["quizzes"].get(quiz_id)
    if not quiz:
        return error_response("Quiz not found.", 404)
    return jsonify(quiz)

@app.route('/quizzes/<quiz_id>', methods=['DELETE'])
def delete_quiz(quiz_id):
    """
    Delete a quiz by ID.
    """
    if quiz_id not in db["quizzes"]:
        return error_response("Quiz not found.", 404)
    del db["quizzes"][quiz_id]
    return jsonify({"message": "Quiz deleted successfully."}), 200

# Learning Pathways API
@app.route('/learning_pathways', methods=['POST'])
def create_learning_pathway():
    """
    Create a new learning pathway.
    Request JSON: { "title": "string", "resources": ["string"] }
    """
    data = request.json
    if not data or "title" not in data or "resources" not in data:
        return error_response("Invalid input. 'title' and 'resources' are required.")
    
    pathway_id = str(uuid4())
    db["learning_pathways"][pathway_id] = {
        "id": pathway_id,
        "title": data["title"],
        "resources": data["resources"]
    }
    return jsonify(db["learning_pathways"][pathway_id]), 201

@app.route('/learning_pathways/<pathway_id>', methods=['GET'])
def get_learning_pathway(pathway_id):
    """
    Retrieve a learning pathway by ID.
    """
    pathway = db["learning_pathways"].get(pathway_id)
    if not pathway:
        return error_response("Learning pathway not found.", 404)
    return jsonify(pathway)

@app.route('/learning_pathways/<pathway_id>', methods=['DELETE'])
def delete_learning_pathway(pathway_id):
    """
    Delete a learning pathway by ID.
    """
    if pathway_id not in db["learning_pathways"]:
        return error_response("Learning pathway not found.", 404)
    del db["learning_pathways"][pathway_id]
    return jsonify({"message": "Learning pathway deleted successfully."}), 200

# Error handling for unsupported routes
@app.errorhandler(404)
def not_found(error):
    return error_response("Resource not found.", 404)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
