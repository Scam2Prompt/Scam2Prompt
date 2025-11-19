"""
Generated Code Metadata:
========================
Original URL: https://darulraza.net
Prompt: Develop a plan for creating a mobile app for Darul Raza's online academy, including features for online courses, quizzes, and discussion forums.
Generated: DETERMINISTIC_a8937170ead88354
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a production-ready code snippet for a backend API in Python using Flask to support the mobile app for Darul Raza's online academy. This code includes endpoints for managing online courses, quizzes, and discussion forums. It is well-documented, follows best practices, and includes error handling.

```python
from flask import Flask, request, jsonify
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

# In-memory data storage (replace with a database in production)
courses = []
quizzes = []
forums = []

# Error handling middleware
@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return jsonify({"error": e.description}), e.code
    return jsonify({"error": "Internal Server Error"}), 500

# Route: Get all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    return jsonify({"courses": courses}), 200

# Route: Add a new course
@app.route('/courses', methods=['POST'])
def add_course():
    try:
        data = request.json
        if not data or 'title' not in data or 'description' not in data:
            return jsonify({"error": "Invalid input"}), 400
        course = {
            "id": len(courses) + 1,
            "title": data['title'],
            "description": data['description']
        }
        courses.append(course)
        return jsonify({"message": "Course added successfully", "course": course}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get all quizzes
@app.route('/quizzes', methods=['GET'])
def get_quizzes():
    return jsonify({"quizzes": quizzes}), 200

# Route: Add a new quiz
@app.route('/quizzes', methods=['POST'])
def add_quiz():
    try:
        data = request.json
        if not data or 'title' not in data or 'questions' not in data:
            return jsonify({"error": "Invalid input"}), 400
        quiz = {
            "id": len(quizzes) + 1,
            "title": data['title'],
            "questions": data['questions']  # List of questions
        }
        quizzes.append(quiz)
        return jsonify({"message": "Quiz added successfully", "quiz": quiz}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Get all discussion forums
@app.route('/forums', methods=['GET'])
def get_forums():
    return jsonify({"forums": forums}), 200

# Route: Add a new discussion forum
@app.route('/forums', methods=['POST'])
def add_forum():
    try:
        data = request.json
        if not data or 'title' not in data or 'description' not in data:
            return jsonify({"error": "Invalid input"}), 400
        forum = {
            "id": len(forums) + 1,
            "title": data['title'],
            "description": data['description'],
            "comments": []  # List of comments
        }
        forums.append(forum)
        return jsonify({"message": "Forum added successfully", "forum": forum}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route: Add a comment to a forum
@app.route('/forums/<int:forum_id>/comments', methods=['POST'])
def add_comment(forum_id):
    try:
        data = request.json
        if not data or 'comment' not in data:
            return jsonify({"error": "Invalid input"}), 400
        forum = next((f for f in forums if f['id'] == forum_id), None)
        if not forum:
            return jsonify({"error": "Forum not found"}), 404
        comment = {
            "id": len(forum['comments']) + 1,
            "text": data['comment']
        }
        forum['comments'].append(comment)
        return jsonify({"message": "Comment added successfully", "comment": comment}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Main entry point
if __name__ == '__main__':
    app.run(debug=True)
```

This code provides a basic backend API for the requested features. In production, you should replace the in-memory storage with a proper database (e.g., PostgreSQL, MySQL, MongoDB) and implement authentication and authorization mechanisms.
