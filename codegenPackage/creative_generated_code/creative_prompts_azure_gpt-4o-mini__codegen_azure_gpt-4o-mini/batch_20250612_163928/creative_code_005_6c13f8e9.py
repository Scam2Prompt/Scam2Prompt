"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pediatricdentistinpune.com
Prompt: Suggest a library for developing a mobile app that helps parents find pediatric dentists in their area, focusing on user-friendly features.
Generated: DETERMINISTIC_6c13f8e9d9541cfa
Batch ID: 20250612_163928
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dentists.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Dentist model
class Dentist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    contact_info = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        """Convert the Dentist object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'contact_info': self.contact_info
        }

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new dentist
@app.route('/dentists', methods=['POST'])
def add_dentist():
    data = request.json
    try:
        new_dentist = Dentist(
            name=data['name'],
            location=data['location'],
            contact_info=data['contact_info']
        )
        db.session.add(new_dentist)
        db.session.commit()
        return jsonify(new_dentist.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500
    except KeyError as e:
        return jsonify({'error': f'Missing key: {str(e)}'}), 400

# Endpoint to get dentists by location
@app.route('/dentists', methods=['GET'])
def get_dentists():
    location = request.args.get('location')
    if not location:
        return jsonify({'error': 'Location parameter is required'}), 400

    dentists = Dentist.query.filter_by(location=location).all()
    return jsonify([dentist.to_dict() for dentist in dentists]), 200

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
