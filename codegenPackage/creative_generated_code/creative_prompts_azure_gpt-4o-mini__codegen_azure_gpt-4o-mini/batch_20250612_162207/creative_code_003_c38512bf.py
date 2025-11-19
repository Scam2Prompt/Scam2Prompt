"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rodi.co.id
Prompt: Develop an API endpoint that allows users to submit their experiences with local welfare programs, akin to the community engagement highlighted by Rodi on his platform.
Generated: DETERMINISTIC_c38512bf9c204c33
Batch ID: 20250612_162207
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
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///welfare_experiences.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Experience(db.Model):
    """Model to represent a user's experience with a local welfare program."""
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    program_name = db.Column(db.String(100), nullable=False)
    experience_text = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the Experience object to a dictionary."""
        return {
            'id': self.id,
            'user_name': self.user_name,
            'program_name': self.program_name,
            'experience_text': self.experience_text
        }


@app.route('/api/experiences', methods=['POST'])
def submit_experience():
    """API endpoint to submit experiences with local welfare programs."""
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid input: JSON data required.'}), 400

    # Validate the input data
    user_name = data.get('user_name')
    program_name = data.get('program_name')
    experience_text = data.get('experience_text')

    if not user_name or not program_name or not experience_text:
        return jsonify({'error': 'Missing required fields: user_name, program_name, experience_text.'}), 400

    # Create a new experience record
    new_experience = Experience(
        user_name=user_name,
        program_name=program_name,
        experience_text=experience_text
    )

    # Save to the database and handle possible errors
    try:
        db.session.add(new_experience)
        db.session.commit()
        return jsonify(new_experience.to_dict()), 201  # 201 Created
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Integrity error: please check your input.'}), 409  # 409 Conflict
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': 'Database error: {}'.format(str(e))}), 500  # 500 Internal Server Error


@app.route('/api/experiences', methods=['GET'])
def get_experiences():
    """API endpoint to retrieve all submitted experiences."""
    experiences = Experience.query.all()
    return jsonify([experience.to_dict() for experience in experiences]), 200  # 200 OK


if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create the database tables
    app.run(debug=True)  # Run the Flask application
```
