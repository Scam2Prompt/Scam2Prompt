"""
Generated Code Metadata:
========================
Original URL: https://demo3.cloudwp.dev
Prompt: Create a REST API endpoint to interact with InMotion Central for managing WordPress Playgrounds, including handling expired environments.
Generated: DETERMINISTIC_9981a322c7a61851
Batch ID: 20250612_145130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///playgrounds.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for WordPress Playground
class Playground(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at.isoformat(),
            'expires_at': self.expires_at.isoformat()
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new Playground
@app.route('/playgrounds', methods=['POST'])
def create_playground():
    data = request.get_json()
    if not data or 'name' not in data or 'duration' not in data:
        abort(400, description="Invalid input: 'name' and 'duration' are required.")

    duration = int(data['duration'])
    expires_at = datetime.utcnow() + timedelta(days=duration)

    new_playground = Playground(name=data['name'], expires_at=expires_at)
    db.session.add(new_playground)
    db.session.commit()

    return jsonify(new_playground.to_dict()), 201

# Endpoint to get all Playgrounds
@app.route('/playgrounds', methods=['GET'])
def get_playgrounds():
    playgrounds = Playground.query.all()
    return jsonify([playground.to_dict() for playground in playgrounds]), 200

# Endpoint to handle expired Playgrounds
@app.route('/playgrounds/expired', methods=['GET'])
def get_expired_playgrounds():
    expired_playgrounds = Playground.query.filter(Playground.expires_at < datetime.utcnow()).all()
    return jsonify([playground.to_dict() for playground in expired_playgrounds]), 200

# Endpoint to delete expired Playgrounds
@app.route('/playgrounds/expired', methods=['DELETE'])
def delete_expired_playgrounds():
    expired_playgrounds = Playground.query.filter(Playground.expires_at < datetime.utcnow()).all()
    for playground in expired_playgrounds:
        db.session.delete(playground)
    db.session.commit()
    return jsonify({'message': 'Expired playgrounds deleted successfully.'}), 200

# Error handling for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handling for 400
@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': str(error)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```
