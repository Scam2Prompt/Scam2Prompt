"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehashtagconsultants.com
Prompt: Illustrate how to integrate a training module for call center agents into a management system, referencing the training and development services offered by The Hashtag Consultants.
Generated: DETERMINISTIC_f42d977c16139138
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///call_center_training.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Training model
class Training(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<Training {self.title}>'

# Initialize the database (create tables)
with app.app_context():
    db.create_all()

# Route to create a new training module
@app.route('/training', methods=['POST'])
def create_training():
    """
    Create a new training module for call center agents.
    Expects a JSON payload with 'title' and 'description'.
    """
    try:
        data = request.get_json()
        if not data or 'title' not in data or 'description' not in data:
            return jsonify({"error": "Title and description are required."}), 400

        new_training = Training(title=data['title'], description=data['description'])
        db.session.add(new_training)
        db.session.commit()
        return jsonify({"message": "Training module created successfully.", "id": new_training.id}), 201

    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({"error": str(e)}), 500

# Route to get all training modules
@app.route('/training', methods=['GET'])
def get_training_modules():
    """
    Retrieve all training modules.
    """
    try:
        trainings = Training.query.all()
        return jsonify([{"id": training.id, "title": training.title, "description": training.description} for training in trainings]), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to update a training module
@app.route('/training/<int:id>', methods=['PUT'])
def update_training(id):
    """
    Update an existing training module by ID.
    Expects a JSON payload with 'title' and/or 'description'.
    """
    try:
        data = request.get_json()
        training = Training.query.get_or_404(id)

        if 'title' in data:
            training.title = data['title']
        if 'description' in data:
            training.description = data['description']

        db.session.commit()
        return jsonify({"message": "Training module updated successfully."}), 200

    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({"error": str(e)}), 500

# Route to delete a training module
@app.route('/training/<int:id>', methods=['DELETE'])
def delete_training(id):
    """
    Delete a training module by ID.
    """
    try:
        training = Training.query.get_or_404(id)
        db.session.delete(training)
        db.session.commit()
        return jsonify({"message": "Training module deleted successfully."}), 200

    except Exception as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
