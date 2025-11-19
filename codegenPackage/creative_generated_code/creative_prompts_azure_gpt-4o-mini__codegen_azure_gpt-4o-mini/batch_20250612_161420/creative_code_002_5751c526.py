"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tolaandtola.com
Prompt: Create an API that provides updates on recent legal cases, similar to the news section on Tola and Tola's website, focusing on taxation and super tax issues.
Generated: DETERMINISTIC_5751c52675867627
Batch ID: 20250612_161420
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
from datetime import datetime

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///legal_cases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for legal cases
class LegalCase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    date_updated = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'date_updated': self.date_updated.isoformat()
        }

# Create the database tables
with app.app_context():
    db.create_all()

# Route to get all legal cases
@app.route('/api/cases', methods=['GET'])
def get_cases():
    try:
        cases = LegalCase.query.all()
        return jsonify([case.to_dict() for case in cases]), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to add a new legal case
@app.route('/api/cases', methods=['POST'])
def add_case():
    try:
        data = request.get_json()
        if not data or 'title' not in data or 'description' not in data:
            return jsonify({'error': 'Invalid input data'}), 400

        new_case = LegalCase(title=data['title'], description=data['description'])
        db.session.add(new_case)
        db.session.commit()
        return jsonify(new_case.to_dict()), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update an existing legal case
@app.route('/api/cases/<int:case_id>', methods=['PUT'])
def update_case(case_id):
    try:
        case = LegalCase.query.get(case_id)
        if not case:
            return jsonify({'error': 'Case not found'}), 404
        
        data = request.get_json()
        if 'title' in data:
            case.title = data['title']
        if 'description' in data:
            case.description = data['description']
        
        db.session.commit()
        return jsonify(case.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a legal case
@app.route('/api/cases/<int:case_id>', methods=['DELETE'])
def delete_case(case_id):
    try:
        case = LegalCase.query.get(case_id)
        if not case:
            return jsonify({'error': 'Case not found'}), 404

        db.session.delete(case)
        db.session.commit()
        return jsonify({'message': 'Case deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
