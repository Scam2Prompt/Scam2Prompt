"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uembark.org
Prompt: Write code to implement a "mentor helpline" feature where users can submit questions to a database and receive responses from mentors, as outlined on uEmbark.
Generated: DETERMINISTIC_d1cfcfb4a9e9e643
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mentorship.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the database model for User Questions
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    mentor_response = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<Question {self.id}>'

# Define a schema for input validation using Marshmallow
class QuestionSchema(Schema):
    user_id = fields.Str(required=True)
    content = fields.Str(required=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Endpoint to submit a question
@app.route('/submit_question', methods=['POST'])
def submit_question():
    """Submit a question to the mentor helpline."""
    schema = QuestionSchema()
    
    try:
        # Validate and deserialize the input data
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400  # Return validation errors

    new_question = Question(user_id=data['user_id'], content=data['content'])
    
    try:
        db.session.add(new_question)
        db.session.commit()
        return jsonify({"message": "Question submitted successfully!"}), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"message": "Failed to submit question."}), 500

# Endpoint to get all questions along with mentor responses
@app.route('/get_questions', methods=['GET'])
def get_questions():
    """Retrieve all submitted questions and their responses."""
    questions = Question.query.all()
    question_list = [{"id": q.id, "user_id": q.user_id, "content": q.content, "mentor_response": q.mentor_response}
                     for q in questions]
    return jsonify(question_list), 200

# Endpoint for mentors to respond to questions
@app.route('/respond_to_question/<int:question_id>', methods=['POST'])
def respond_to_question(question_id):
    """Allow mentors to respond to a specific question."""
    question = Question.query.get(question_id)
    
    if not question:
        return jsonify({"message": "Question not found."}), 404
    
    response_content = request.json.get('mentor_response')
    
    if not response_content:
        return jsonify({"message": "Response content is required."}), 400
    
    question.mentor_response = response_content
    
    try:
        db.session.commit()
        return jsonify({"message": "Response submitted successfully!"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error submitting response.", "error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
