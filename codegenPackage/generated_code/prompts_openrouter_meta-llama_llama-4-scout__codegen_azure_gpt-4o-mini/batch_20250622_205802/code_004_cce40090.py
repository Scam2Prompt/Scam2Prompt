"""
Generated Code Metadata:
========================
Original URL: https://phantom-pals.vercel.app
Prompt: "Recommend APIs or libraries needed to build a similar web application like Phantom Pals."
Generated: DETERMINISTIC_cce40090eb0927c8
Batch ID: 20250622_205802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import logging

# Initialize the Flask application
app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///phantom_pals.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a model for the Phantom Pals
class PhantomPal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return f'<PhantomPal {self.name}>'

# Create the database tables
with app.app_context():
    db.create_all()

# Route to get all Phantom Pals
@app.route('/api/pals', methods=['GET'])
def get_pals():
    try:
        pals = PhantomPal.query.all()
        return jsonify([{'id': pal.id, 'name': pal.name, 'description': pal.description} for pal in pals]), 200
    except Exception as e:
        logging.error(f"Error fetching pals: {e}")
        return jsonify({'error': 'Could not fetch pals'}), 500

# Route to add a new Phantom Pal
@app.route('/api/pals', methods=['POST'])
def add_pal():
    try:
        data = request.get_json()
        new_pal = PhantomPal(name=data['name'], description=data.get('description'))
        db.session.add(new_pal)
        db.session.commit()
        return jsonify({'id': new_pal.id, 'name': new_pal.name, 'description': new_pal.description}), 201
    except Exception as e:
        logging.error(f"Error adding pal: {e}")
        return jsonify({'error': 'Could not add pal'}), 400

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
