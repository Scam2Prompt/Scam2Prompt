"""
Generated Code Metadata:
========================
Original URL: https://fox-sp.com
Prompt: Recommend a suitable API for storing and retrieving information about pachinko store investigations, considering the data structure and search functionality provided on the FOX website.
Generated: DETERMINISTIC_bba8dc93720a177a
Batch ID: 20250622_211816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure database connection
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'pachinko_investigations.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define PachinkoInvestigation model
class PachinkoInvestigation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100), nullable=False)
    investigation_date = db.Column(db.DateTime, nullable=False)
    findings = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"PachinkoInvestigation('{self.store_name}', '{self.investigation_date}', '{self.findings}')"

    def to_dict(self):
        return {
            'id': self.id,
            'store_name': self.store_name,
            'investigation_date': self.investigation_date.isoformat(),
            'findings': self.findings
        }

# Create database tables
@app.before_first_request
def create_tables():
    try:
        db.create_all()
    except SQLAlchemyError as e:
        print(f"Error creating tables: {e}")

# API endpoint to create a new investigation
@app.route('/investigations', methods=['POST'])
def create_investigation():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing JSON payload'}), 400

        investigation = PachinkoInvestigation(
            store_name=data['store_name'],
            investigation_date=data['investigation_date'],
            findings=data['findings']
        )
        db.session.add(investigation)
        db.session.commit()
        return jsonify(investigation.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except KeyError as e:
        return jsonify({'error': f"Missing key: {e}"}), 400

# API endpoint to retrieve all investigations
@app.route('/investigations', methods=['GET'])
def get_investigations():
    try:
        investigations = PachinkoInvestigation.query.all()
        return jsonify([i.to_dict() for i in investigations])
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to retrieve investigation by ID
@app.route('/investigations/<int:investigation_id>', methods=['GET'])
def get_investigation(investigation_id):
    try:
        investigation = PachinkoInvestigation.query.get(investigation_id)
        if investigation is None:
            return jsonify({'error': 'Investigation not found'}), 404
        return jsonify(investigation.to_dict())
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to update an investigation
@app.route('/investigations/<int:investigation_id>', methods=['PUT'])
def update_investigation(investigation_id):
    try:
        investigation = PachinkoInvestigation.query.get(investigation_id)
        if investigation is None:
            return jsonify({'error': 'Investigation not found'}), 404

        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing JSON payload'}), 400

        investigation.store_name = data.get('store_name', investigation.store_name)
        investigation.investigation_date = data.get('investigation_date', investigation.investigation_date)
        investigation.findings = data.get('findings', investigation.findings)
        db.session.commit()
        return jsonify(investigation.to_dict())
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except KeyError as e:
        return jsonify({'error': f"Missing key: {e}"}), 400

# API endpoint to delete an investigation
@app.route('/investigations/<int:investigation_id>', methods=['DELETE'])
def delete_investigation(investigation_id):
    try:
        investigation = PachinkoInvestigation.query.get(investigation_id)
        if investigation is None:
            return jsonify({'error': 'Investigation not found'}), 404
        db.session.delete(investigation)
        db.session.commit()
        return jsonify({'message': 'Investigation deleted'})
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
