"""
Generated Code Metadata:
========================
Original URL: https://www.viviresconvivir.cl
Prompt: How can I create an interactive API that teaches civic education to young students, inspired by the "Vivir es Convivir" initiative from Fundación Patricio Aylwin?
Generated: DETERMINISTIC_1ea9a0893c61bd13
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///civic_education.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the model for civic education topics
class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# Create a schema for input validation
class TopicSchema(Schema):
    title = fields.Str(required=True)
    content = fields.Str(required=True)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get all topics
@app.route('/api/topics', methods=['GET'])
def get_topics():
    """Retrieve all civic education topics."""
    topics = Topic.query.all()
    return jsonify([{'id': topic.id, 'title': topic.title, 'content': topic.content} for topic in topics]), 200

# Route to create a new topic
@app.route('/api/topics', methods=['POST'])
def create_topic():
    """Create a new civic education topic."""
    try:
        # Validate and deserialize input
        topic_schema = TopicSchema()
        topic_data = topic_schema.load(request.json)

        # Create a new topic instance
        new_topic = Topic(title=topic_data['title'], content=topic_data['content'])
        db.session.add(new_topic)
        db.session.commit()

        return jsonify({'id': new_topic.id, 'title': new_topic.title, 'content': new_topic.content}), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error creating topic: {e}")
        return jsonify({'error': 'An error occurred while creating the topic.'}), 500

# Route to get a specific topic by ID
@app.route('/api/topics/<int:topic_id>', methods=['GET'])
def get_topic(topic_id):
    """Retrieve a specific civic education topic by ID."""
    topic = Topic.query.get_or_404(topic_id)
    return jsonify({'id': topic.id, 'title': topic.title, 'content': topic.content}), 200

# Route to update a specific topic by ID
@app.route('/api/topics/<int:topic_id>', methods=['PUT'])
def update_topic(topic_id):
    """Update a specific civic education topic by ID."""
    try:
        topic = Topic.query.get_or_404(topic_id)
        topic_schema = TopicSchema()
        topic_data = topic_schema.load(request.json)

        topic.title = topic_data['title']
        topic.content = topic_data['content']
        db.session.commit()

        return jsonify({'id': topic.id, 'title': topic.title, 'content': topic.content}), 200
    except ValidationError as err:
        return jsonify(err.messages), 400
    except Exception as e:
        logging.error(f"Error updating topic: {e}")
        return jsonify({'error': 'An error occurred while updating the topic.'}), 500

# Route to delete a specific topic by ID
@app.route('/api/topics/<int:topic_id>', methods=['DELETE'])
def delete_topic(topic_id):
    """Delete a specific civic education topic by ID."""
    topic = Topic.query.get_or_404(topic_id)
    db.session.delete(topic)
    db.session.commit()
    return jsonify({'message': 'Topic deleted successfully.'}), 204

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
