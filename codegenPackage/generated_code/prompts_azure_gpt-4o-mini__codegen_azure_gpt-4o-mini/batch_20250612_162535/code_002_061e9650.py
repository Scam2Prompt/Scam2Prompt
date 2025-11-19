"""
Generated Code Metadata:
========================
Original URL: https://selffeeling.com
Prompt: Create a REST API endpoint that provides guided meditation prompts for self-awareness, based on the Self-Feeling Program's activities.
Generated: DETERMINISTIC_061e96504f7bc2f4
Batch ID: 20250612_162535
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
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meditation_prompts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the MeditationPrompt model
class MeditationPrompt(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    prompt = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {'id': self.id, 'prompt': self.prompt}

# Create the database and the table
with app.app_context():
    db.create_all()

@app.route('/api/prompts', methods=['GET'])
def get_prompts():
    """Retrieve all meditation prompts."""
    try:
        prompts = MeditationPrompt.query.all()
        return jsonify([prompt.to_dict() for prompt in prompts]), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/prompts', methods=['POST'])
def add_prompt():
    """Add a new meditation prompt."""
    data = request.get_json()
    
    if not data or 'prompt' not in data:
        return jsonify({'error': 'Prompt is required'}), 400

    new_prompt = MeditationPrompt(prompt=data['prompt'])
    
    try:
        db.session.add(new_prompt)
        db.session.commit()
        return jsonify(new_prompt.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
