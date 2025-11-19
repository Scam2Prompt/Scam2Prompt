"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://prgmea.pk
Prompt: How can I create a training program API that aligns with the objectives of the Pakistan Readymade Garments Technical Training Institute (PRGTTI)?
Generated: DETERMINISTIC_a56ca3108c04180a
Batch ID: 20250612_162051
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
from datetime import datetime
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your database credentials)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prgtti_training.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the TrainingProgram model
class TrainingProgram(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in hours
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'duration': self.duration,
            'created_at': self.created_at.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/programs', methods=['POST'])
def create_program():
    """Create a new training program."""
    try:
        data = request.json
        new_program = TrainingProgram(
            title=data['title'],
            description=data['description'],
            duration=data['duration']
        )
        db.session.add(new_program)
        db.session.commit()
        return jsonify(new_program.to_dict()), 201
    except KeyError as e:
        # Handle missing fields
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500

@app.route('/programs', methods=['GET'])
def get_programs():
    """Retrieve a list of all training programs."""
    try:
        programs = TrainingProgram.query.all()
        return jsonify([program.to_dict() for program in programs]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/programs/<int:program_id>', methods=['GET'])
def get_program(program_id):
    """Retrieve a specific training program by ID."""
    try:
        program = TrainingProgram.query.get_or_404(program_id)
        return jsonify(program.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/programs/<int:program_id>', methods=['PUT'])
def update_program(program_id):
    """Update an existing training program."""
    try:
        data = request.json
        program = TrainingProgram.query.get_or_404(program_id)
        program.title = data.get('title', program.title)
        program.description = data.get('description', program.description)
        program.duration = data.get('duration', program.duration)
        db.session.commit()
        return jsonify(program.to_dict()), 200
    except KeyError as e:
        return jsonify({'error': f'Missing field: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/programs/<int:program_id>', methods=['DELETE'])
def delete_program(program_id):
    """Delete a training program."""
    try:
        program = TrainingProgram.query.get_or_404(program_id)
        db.session.delete(program)
        db.session.commit()
        return jsonify({'message': 'Program deleted successfully'}), 204
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', False))
```
