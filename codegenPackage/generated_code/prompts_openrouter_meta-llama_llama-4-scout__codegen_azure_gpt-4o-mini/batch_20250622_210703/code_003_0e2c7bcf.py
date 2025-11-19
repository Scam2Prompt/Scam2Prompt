"""
Generated Code Metadata:
========================
Original URL: https://mirrorsshadows.com
Prompt: "Create a code snippet to implement a customer feedback system for a creative studio, with features like FAQs and guest support, similar to Mirrors Shadows."
Generated: DETERMINISTIC_0e2c7bcfd2a16fdb
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.exceptions import NotFound, BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///feedback.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Feedback model
class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __init__(self, name, email, message):
        self.name = name
        self.email = email
        self.message = message

# Feedback schema
class FeedbackSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Feedback

# Initialize the database
with app.app_context():
    db.create_all()

# Route to submit feedback
@app.route('/feedback', methods=['POST'])
def submit_feedback():
    try:
        # Get JSON data from request
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        # Validate input data
        if not name or not email or not message:
            raise BadRequest("Name, email, and message are required.")

        # Create a new feedback entry
        new_feedback = Feedback(name, email, message)
        db.session.add(new_feedback)
        db.session.commit()

        return jsonify({"message": "Feedback submitted successfully!"}), 201

    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An error occurred while submitting feedback."}), 500

# Route to get all feedback
@app.route('/feedback', methods=['GET'])
def get_feedback():
    try:
        feedback_list = Feedback.query.all()
        feedback_schema = FeedbackSchema(many=True)
        return feedback_schema.jsonify(feedback_list), 200

    except Exception as e:
        return jsonify({"error": "An error occurred while retrieving feedback."}), 500

# Route to get FAQs
@app.route('/faqs', methods=['GET'])
def get_faqs():
    faqs = [
        {"question": "What services do you offer?", "answer": "We offer a variety of creative services including design, branding, and marketing."},
        {"question": "How can I contact support?", "answer": "You can contact support via the feedback form or email us directly."},
        {"question": "What is your turnaround time?", "answer": "Our typical turnaround time is 2-4 weeks depending on the project."}
    ]
    return jsonify(faqs), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
