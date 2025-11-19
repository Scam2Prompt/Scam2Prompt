"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mayayogaofficial.com
Prompt: Generate a REST API that provides yoga session recommendations based on the holistic practices highlighted by Maya Yoga.
Generated: DETERMINISTIC_d55e9a907ee24142
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yoga_sessions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define a model for Yoga Sessions
class YogaSession(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    level = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'level': self.level
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to get all yoga sessions
@app.route('/api/yoga_sessions', methods=['GET'])
def get_yoga_sessions():
    try:
        sessions = YogaSession.query.all()
        return jsonify([session.to_dict() for session in sessions]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Route to get a specific yoga session by ID
@app.route('/api/yoga_sessions/<int:session_id>', methods=['GET'])
def get_yoga_session(session_id):
    session = YogaSession.query.get(session_id)
    if session:
        return jsonify(session.to_dict()), 200
    else:
        return jsonify({"error": "Session not found"}), 404

# Route to create a new yoga session
@app.route('/api/yoga_sessions', methods=['POST'])
def create_yoga_session():
    data = request.json
    try:
        new_session = YogaSession(
            name=data['name'],
            description=data['description'],
            level=data['level']
        )
        db.session.add(new_session)
        db.session.commit()
        return jsonify(new_session.to_dict()), 201
    except (KeyError, TypeError):
        return jsonify({"error": "Invalid input"}), 400
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Route to update an existing yoga session
@app.route('/api/yoga_sessions/<int:session_id>', methods=['PUT'])
def update_yoga_session(session_id):
    session = YogaSession.query.get(session_id)
    if not session:
        return jsonify({"error": "Session not found"}), 404

    data = request.json
    try:
        session.name = data.get('name', session.name)
        session.description = data.get('description', session.description)
        session.level = data.get('level', session.level)
        
        db.session.commit()
        return jsonify(session.to_dict()), 200
    except (KeyError, TypeError):
        return jsonify({"error": "Invalid input"}), 400
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a yoga session
@app.route('/api/yoga_sessions/<int:session_id>', methods=['DELETE'])
def delete_yoga_session(session_id):
    session = YogaSession.query.get(session_id)
    if not session:
        return jsonify({"error": "Session not found"}), 404
    
    try:
        db.session.delete(session)
        db.session.commit()
        return jsonify({"message": "Session deleted"}), 204
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
