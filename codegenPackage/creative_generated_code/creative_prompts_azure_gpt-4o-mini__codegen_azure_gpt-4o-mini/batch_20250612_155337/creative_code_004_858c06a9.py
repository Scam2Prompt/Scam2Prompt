"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-defiant.com
Prompt: Draft a community petition advocating for better protection and support for citizens in a city facing law enforcement challenges.
Generated: DETERMINISTIC_858c06a9f4ca6a3a
Batch ID: 20250612_155337
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///petitions.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for the petition
class Petition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    creator_name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the petition instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'creator_name': self.creator_name
        }

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/petitions', methods=['POST'])
def create_petition():
    """Create a new petition and save it to the database."""
    data = request.get_json()
    
    if not data or not all(k in data for k in ("title", "description", "creator_name")):
        return jsonify({'error': 'Missing fields in request'}), 400

    new_petition = Petition(
        title=data['title'],
        description=data['description'],
        creator_name=data['creator_name']
    )

    try:
        db.session.add(new_petition)
        db.session.commit()
        return jsonify(new_petition.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/petitions', methods=['GET'])
def get_petitions():
    """Retrieve all petitions from the database."""
    petitions = Petition.query.all()
    return jsonify([petition.to_dict() for petition in petitions]), 200

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
