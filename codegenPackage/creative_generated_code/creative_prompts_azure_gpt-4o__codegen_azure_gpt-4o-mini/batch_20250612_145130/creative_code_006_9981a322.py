"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo3.cloudwp.dev
Prompt: Create a REST API endpoint to interact with InMotion Central for managing WordPress Playgrounds, including handling expired environments.
Generated: DETERMINISTIC_9981a322c7a61851
Batch ID: 20250612_145130
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
from datetime import datetime, timedelta
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///playgrounds.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for WordPress Playgrounds
class Playground(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)

    def is_expired(self):
        return datetime.utcnow() > self.expires_at

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to create a new playground
@app.route('/api/playgrounds', methods=['POST'])
def create_playground():
    try:
        data = request.json
        name = data.get('name')
        expiration_duration = data.get('expiration_duration', 30)  # Default to 30 days

        # Validate input
        if not name or not isinstance(expiration_duration, int) or expiration_duration <= 0:
            return jsonify({'error': 'Invalid input'}), 400
        
        # Calculate expiration date
        expires_at = datetime.utcnow() + timedelta(days=expiration_duration)
        
        # Create and save the new playground
        new_playground = Playground(name=name, expires_at=expires_at)
        db.session.add(new_playground)
        db.session.commit()

        return jsonify({'id': new_playground.id, 'name': new_playground.name, 'expires_at': new_playground.expires_at}), 201

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to list all playgrounds and their statuses
@app.route('/api/playgrounds', methods=['GET'])
def list_playgrounds():
    try:
        playgrounds = Playground.query.all()
        result = []
        
        for playground in playgrounds:
            result.append({
                'id': playground.id,
                'name': playground.name,
                'created_at': playground.created_at,
                'expires_at': playground.expires_at,
                'is_expired': playground.is_expired()
            })

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Endpoint to delete expired playgrounds
@app.route('/api/playgrounds/cleanup', methods=['DELETE'])
def cleanup_playgrounds():
    try:
        expired_playgrounds = Playground.query.filter(Playground.expires_at < datetime.utcnow()).all()
        for playground in expired_playgrounds:
            db.session.delete(playground)
        db.session.commit()

        return jsonify({'message': f'Deleted {len(expired_playgrounds)} expired playground(s).'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Start the application
if __name__ == '__main__':
    app.run(debug=True)
```
