"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Develop an API to retrieve technical specifications and applications of Yanmar mini excavators, such as ViO12, ViO17, ViO25, ViO35, and SV100, for use in construction, agriculture, and landscaping projects.
Generated: DETERMINISTIC_35238c1ce06aead0
Batch ID: 20250612_153224
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

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yanmar_excavators.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Excavator model
class Excavator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(50), unique=True, nullable=False)
    specifications = db.Column(db.Text, nullable=False)
    applications = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the Excavator object to a dictionary."""
        return {
            'model': self.model,
            'specifications': self.specifications,
            'applications': self.applications
        }

# Create the database and tables
with app.app_context():
    db.create_all()

# API endpoint to retrieve excavator details by model
@app.route('/excavators/<string:model>', methods=['GET'])
def get_excavator(model):
    """Retrieve technical specifications and applications of a Yanmar mini excavator by model."""
    try:
        excavator = Excavator.query.filter_by(model=model).first()
        if excavator is None:
            return jsonify({'error': 'Excavator not found'}), 404
        return jsonify(excavator.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

# API endpoint to add a new excavator
@app.route('/excavators', methods=['POST'])
def add_excavator():
    """Add a new Yanmar mini excavator to the database."""
    data = request.get_json()
    if not data or 'model' not in data or 'specifications' not in data or 'applications' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    new_excavator = Excavator(
        model=data['model'],
        specifications=data['specifications'],
        applications=data['applications']
    )

    try:
        db.session.add(new_excavator)
        db.session.commit()
        return jsonify(new_excavator.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment.
- Replace the database URI with your actual database connection string if not using SQLite.
- The API includes endpoints to retrieve and add excavator details, with error handling for common issues.
