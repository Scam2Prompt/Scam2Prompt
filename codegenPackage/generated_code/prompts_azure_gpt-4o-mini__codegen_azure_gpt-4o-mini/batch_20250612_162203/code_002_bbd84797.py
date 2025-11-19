"""
Generated Code Metadata:
========================
Original URL: https://educarcomitan.mx
Prompt: Generate a code snippet for a web application that allows students to track their progress in preparing for admission exams, focusing on features like topic feedback and study resources.
Generated: DETERMINISTIC_bbd84797d0ed4a76
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///study_tracker.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the StudyTopic model
class StudyTopic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    feedback = db.Column(db.Text, nullable=True)
    resources = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<StudyTopic {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to add a new study topic
@app.route('/add_topic', methods=['POST'])
def add_topic():
    try:
        data = request.json
        new_topic = StudyTopic(
            name=data['name'],
            feedback=data.get('feedback'),
            resources=data.get('resources')
        )
        db.session.add(new_topic)
        db.session.commit()
        return jsonify({'message': 'Study topic added successfully!'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to get all study topics
@app.route('/topics', methods=['GET'])
def get_topics():
    try:
        topics = StudyTopic.query.all()
        return jsonify([{
            'id': topic.id,
            'name': topic.name,
            'feedback': topic.feedback,
            'resources': topic.resources,
            'created_at': topic.created_at
        } for topic in topics]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update feedback for a study topic
@app.route('/update_feedback/<int:topic_id>', methods=['PUT'])
def update_feedback(topic_id):
    try:
        data = request.json
        topic = StudyTopic.query.get_or_404(topic_id)
        topic.feedback = data.get('feedback', topic.feedback)
        db.session.commit()
        return jsonify({'message': 'Feedback updated successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Route to delete a study topic
@app.route('/delete_topic/<int:topic_id>', methods=['DELETE'])
def delete_topic(topic_id):
    try:
        topic = StudyTopic.query.get_or_404(topic_id)
        db.session.delete(topic)
        db.session.commit()
        return jsonify({'message': 'Study topic deleted successfully!'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
