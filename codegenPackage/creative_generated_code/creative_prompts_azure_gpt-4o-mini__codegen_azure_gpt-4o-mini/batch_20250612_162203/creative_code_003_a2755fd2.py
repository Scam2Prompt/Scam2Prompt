"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theneuraluniverse.com
Prompt: Create an API endpoint that allows users to submit their experiences related to neurosurgery, inspired by the content on The Neural Universe.
Generated: DETERMINISTIC_a2755fd275f1657e
Batch ID: 20250612_162203
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
from marshmallow import Schema, fields, ValidationError
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///neurosurgery_experiences.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for user experiences
class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    experience = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Experience {self.id}>'

# Schema for input validation
class ExperienceSchema(Schema):
    user_id = fields.Str(required=True)
    experience = fields.Str(required=True)

# Initialize database
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to submit user experiences
@app.route('/api/experiences', methods=['POST'])
def submit_experience():
    schema = ExperienceSchema()
    try:
        # Validate input data
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400

    # Create a new experience record
    new_experience = Experience(user_id=data['user_id'], experience=data['experience'])
    
    try:
        db.session.add(new_experience)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500

    return jsonify({"message": "Experience submitted successfully!", "id": new_experience.id}), 201

# Error handler for invalid JSON
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
