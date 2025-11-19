"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gematria.com
Prompt: Develop a RESTful API endpoint that allows users to retrieve details about hormone and immune support supplements offered by Gematria.
Generated: DETERMINISTIC_bcc6e3f080f398c0
Batch ID: 20250612_162504
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

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///supplements.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Supplement model
class Supplement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the Supplement object to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'description': self.description
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/api/supplements', methods=['GET'])
def get_supplements():
    """Retrieve a list of hormone and immune support supplements."""
    try:
        # Query for supplements of type 'hormone' or 'immune'
        supplements = Supplement.query.filter(Supplement.type.in_(["hormone", "immune"])).all()
        return jsonify([supplement.to_dict() for supplement in supplements]), 200
    except SQLAlchemyError as e:
        # Handle any errors that occur during the database query
        error = str(e.__dict__['orig']) if hasattr(e, '__dict__') else str(e)
        return jsonify({"error": "Database query failed", "details": error}), 500

@app.route('/api/supplements/<int:supplement_id>', methods=['GET'])
def get_supplement(supplement_id):
    """Retrieve details about a specific supplement by ID."""
    try:
        # Query for a specific supplement by ID
        supplement = Supplement.query.get_or_404(supplement_id)
        return jsonify(supplement.to_dict()), 200
    except SQLAlchemyError as e:
        # Handle any errors that occur during the database query
        error = str(e.__dict__['orig']) if hasattr(e, '__dict__') else str(e)
        return jsonify({"error": "Database query failed", "details": error}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

Make sure to install the required packages using:
```bash
pip install Flask Flask-SQLAlchemy
```

This code defines a RESTful API endpoint using Flask that allows users to retrieve details about hormone and immune support supplements. The API includes error handling and proper response codes for different scenarios.
