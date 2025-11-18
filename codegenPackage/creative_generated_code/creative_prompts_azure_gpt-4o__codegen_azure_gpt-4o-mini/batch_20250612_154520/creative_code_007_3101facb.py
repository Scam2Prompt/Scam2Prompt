"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://colatraining.com
Prompt: Develop a chatbot using a Python framework that helps users inquire about plant machinery training courses at CoLa Training Services.
Generated: DETERMINISTIC_3101facb81e95982
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from nltk.chat.util import Chat, reflections

# Initialize app
app = Flask(__name__)

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Enable logging
logging.basicConfig(level=logging.INFO)

# Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.String(50), nullable=False)

    def __init__(self, name, description, duration):
        self.name = name
        self.description = description
        self.duration = duration

# Course schema
class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course

# Initialize database schema
db.create_all()

# Chatbot responses
pairs = [
    ['What courses do you offer?', ['We offer various courses like Forklift Training, Crane Operation, and Heavy Equipment Training.']],
    ['How long does the training take?', ['The duration varies by course, typically ranging from 1 to 5 days.']],
    ['Can I book a course?', ['Yes, you can book a course through our website or contact us directly.']],
    ['Thank you', ['You\'re welcome! If you have any other questions, feel free to ask.']],
]

chatbot = Chat(pairs, reflections)

# API endpoint to get all courses
@app.route('/courses', methods=['GET'])
def get_courses():
    try:
        courses = Course.query.all()
        course_schema = CourseSchema(many=True)
        return jsonify(course_schema.dump(courses)), 200
    except Exception as e:
        logging.error(f"Error fetching courses: {e}")
        return jsonify({"error": "Could not retrieve courses."}), 500

# Chatbot endpoint
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({"error": "No message provided."}), 400

    try:
        response = chatbot.respond(user_input)
        return jsonify({"response": response}), 200
    except Exception as e:
        logging.error(f"Error responding to chat: {e}")
        return jsonify({"error": "Could not process your request."}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
