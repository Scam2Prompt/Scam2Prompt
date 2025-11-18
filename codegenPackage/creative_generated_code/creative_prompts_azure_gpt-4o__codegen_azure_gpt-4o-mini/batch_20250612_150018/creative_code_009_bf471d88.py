"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orangepepe.pages.dev
Prompt: Design a REST API for the ORPE podcast platform that allows users to submit questions or topics for discussion related to meme coins.
Generated: DETERMINISTIC_bf471d88dfa1c2c6
Batch ID: 20250612_150018
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
from flask_migrate import Migrate
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///podcast.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define the Question model
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Question {self.id}: {self.content}>'

# Schema for validating input data
class QuestionSchema(Schema):
    content = fields.String(required=True)

# Initialize the schema
question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to submit a question or topic
@app.route('/api/questions', methods=['POST'])
def submit_question():
    try:
        # Validate and deserialize input data
        data = request.get_json()
        validated_data = question_schema.load(data)

        # Create a new Question instance
        new_question = Question(content=validated_data['content'])

        # Add the question to the database
        db.session.add(new_question)
        db.session.commit()

        # Return a success response
        return jsonify({'message': 'Question submitted successfully!', 'id': new_question.id}), 201
    
    except ValidationError as err:
        # Handle validation errors
        return jsonify({'errors': err.messages}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500

# Endpoint to retrieve all submitted questions
@app.route('/api/questions', methods=['GET'])
def get_questions():
    try:
        # Query all questions from the database
        questions = Question.query.all()

        # Serialize the retrieved questions
        return questions_schema.dump(questions), 200
    
    except Exception as e:
        # Handle exceptions
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
