"""
Generated Code Metadata:
========================
Original URL: https://matter.com.uy
Prompt: Create an API that facilitates the collection and visualization of organizational data to support decision-making processes, inspired by Matter's data analytics strategies.
Generated: DETERMINISTIC_06244c9ed9dafa7c
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///org_data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the data model for organizational data
class OrgData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<OrgData {self.name}: {self.value}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/data', methods=['POST'])
def add_data():
    """
    Endpoint to add organizational data.
    Expects JSON payload with 'name' and 'value'.
    """
    try:
        data = request.get_json()
        new_data = OrgData(name=data['name'], value=data['value'])
        db.session.add(new_data)
        db.session.commit()
        return jsonify({'message': 'Data added successfully!'}), 201
    except KeyError as e:
        logging.error(f'Missing key: {e}')
        return jsonify({'error': 'Missing key in request data'}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({'error': 'Data integrity error'}), 400
    except Exception as e:
        logging.error(f'Error adding data: {e}')
        return jsonify({'error': 'An error occurred while adding data'}), 500

@app.route('/data', methods=['GET'])
def get_data():
    """
    Endpoint to retrieve all organizational data.
    Returns a JSON array of all data entries.
    """
    try:
        all_data = OrgData.query.all()
        return jsonify([{'id': data.id, 'name': data.name, 'value': data.value} for data in all_data]), 200
    except Exception as e:
        logging.error(f'Error retrieving data: {e}')
        return jsonify({'error': 'An error occurred while retrieving data'}), 500

@app.route('/data/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    """
    Endpoint to delete organizational data by ID.
    """
    try:
        data_to_delete = OrgData.query.get_or_404(data_id)
        db.session.delete(data_to_delete)
        db.session.commit()
        return jsonify({'message': 'Data deleted successfully!'}), 200
    except Exception as e:
        logging.error(f'Error deleting data: {e}')
        return jsonify({'error': 'An error occurred while deleting data'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
