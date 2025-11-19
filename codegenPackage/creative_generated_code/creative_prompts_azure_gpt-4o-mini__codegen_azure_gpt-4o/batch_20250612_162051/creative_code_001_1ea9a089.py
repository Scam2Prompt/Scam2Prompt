"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.viviresconvivir.cl
Prompt: How can I create an interactive API that teaches civic education to young students, inspired by the "Vivir es Convivir" initiative from Fundación Patricio Aylwin?
Generated: DETERMINISTIC_1ea9a0893c61bd13
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# civic_education_api.py

from flask import Flask, jsonify, request
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Sample civic education data
civic_lessons = [
    {
        "id": 1,
        "title": "Understanding Democracy",
        "content": "Democracy is a system of government by the whole population or all the eligible members of a state, typically through elected representatives.",
        "quiz": [
            {
                "question": "Who can participate in a democracy?",
                "options": ["Only the president", "Only the elite", "All eligible citizens"],
                "answer": "All eligible citizens"
            }
        ]
    },
    {
        "id": 2,
        "title": "Rights and Responsibilities",
        "content": "As citizens, we have rights such as free speech, and responsibilities like obeying laws and voting in elections.",
        "quiz": [
            {
                "question": "Which of the following is a citizen's responsibility?",
                "options": ["Free speech", "Obeying laws", "Owning property"],
                "answer": "Obeying laws"
            }
        ]
    }
]

# Route to get the list of available civic education lessons
@app.route('/api/lessons', methods=['GET'])
def get_lessons():
    """
    Get a list of all available civic education lessons.
    Returns:
        JSON response with lesson details.
    """
    logging.info("Fetching all civic education lessons.")
    return jsonify(civic_lessons), 200

# Route to get a specific lesson by ID
@app.route('/api/lessons/<int:lesson_id>', methods=['GET'])
def get_lesson(lesson_id):
    """
    Get details of a specific lesson by its ID.
    Args:
        lesson_id (int): ID of the lesson.
    Returns:
        JSON response with lesson details or an error message.
    """
    logging.info(f"Fetching lesson with ID: {lesson_id}")
    lesson = next((lesson for lesson in civic_lessons if lesson['id'] == lesson_id), None)
    if lesson is None:
        logging.error(f"Lesson with ID {lesson_id} not found.")
        return jsonify({"error": "Lesson not found"}), 404
    return jsonify(lesson), 200

# Route to answer a quiz question
@app.route('/api/lessons/<int:lesson_id>/quiz', methods=['POST'])
def answer_quiz(lesson_id):
    """
    Submit an answer to a quiz question for a specific lesson.
    Args:
        lesson_id (int): ID of the lesson.
    Returns:
        JSON response indicating whether the answer is correct or not.
    """
    logging.info(f"Processing quiz answer for lesson ID: {lesson_id}")
    lesson = next((lesson for lesson in civic_lessons if lesson['id'] == lesson_id), None)
    if lesson is None:
        logging.error(f"Lesson with ID {lesson_id} not found.")
        return jsonify({"error": "Lesson not found"}), 404

    data = request.json
    user_answer = data.get("answer")
    question = lesson["quiz"][0]  # Assume one question per lesson for simplicity

    if user_answer is None:
        logging.error("Answer not provided in the request.")
        return jsonify({"error": "Answer is required"}), 400

    is_correct = user_answer == question["answer"]
    logging.info(f"User's answer: {user_answer}, Correct answer: {question['answer']}, Result: {is_correct}")
    return jsonify({"correct": is_correct, "message": "Correct!" if is_correct else "Incorrect, try again."}), 200

# Run the application
if __name__ == '__main__':
    logging.info("Starting Civic Education API.")
    app.run(debug=True)
```

This code sets up a Flask-based API with endpoints to provide civic education lessons and quizzes. It includes error handling, logging, and adheres to best practices for creating reliable and maintainable APIs.
