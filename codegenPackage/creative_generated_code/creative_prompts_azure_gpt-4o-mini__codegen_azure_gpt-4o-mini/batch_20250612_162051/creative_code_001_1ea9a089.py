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
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///civic_education.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Question model
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_text = db.Column(db.String(255), nullable=False)
    answer = db.Column(db.String(100), nullable=False)

# Define the schema for validation
class QuestionSchema(Schema):
    question_text = fields.Str(required=True)
    answer = fields.Str(required=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to get all questions
@app.route('/questions', methods=['GET'])
def get_questions():
    """Retrieve all civic education questions."""
    questions = Question.query.all()
    return jsonify([{'id': q.id, 'question_text': q.question_text, 'answer': q.answer} for q in questions])

# Route to add a new question
@app.route('/questions', methods=['POST'])
def add_question():
    """Add a new civic education question."""
    try:
        # Validate and deserialize input
        question_data = QuestionSchema().load(request.json)
        new_question = Question(**question_data)
        db.session.add(new_question)
        db.session.commit()
        return jsonify({'id': new_question.id}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get a specific question by ID
@app.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id):
    """Retrieve a specific question by its ID."""
    question = Question.query.get(question_id)
    if question is None:
        return jsonify({'error': 'Question not found'}), 404
    return jsonify({'id': question.id, 'question_text': question.question_text, 'answer': question.answer})

# Route to update a specific question by ID
@app.route('/questions/<int:question_id>', methods=['PUT'])
def update_question(question_id):
    """Update a specific question by its ID."""
    try:
        question = Question.query.get(question_id)
        if question is None:
            return jsonify({'error': 'Question not found'}), 404

        # Validate and deserialize input
        question_data = QuestionSchema().load(request.json)
        question.question_text = question_data['question_text']
        question.answer = question_data['answer']
        db.session.commit()
        return jsonify({'message': 'Question updated successfully'})
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a specific question by ID
@app.route('/questions/<int:question_id>', methods=['DELETE'])
def delete_question(question_id):
    """Delete a specific question by its ID."""
    question = Question.query.get(question_id)
    if question is None:
        return jsonify({'error': 'Question not found'}), 404
    db.session.delete(question)
    db.session.commit()
    return jsonify({'message': 'Question deleted successfully'})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
