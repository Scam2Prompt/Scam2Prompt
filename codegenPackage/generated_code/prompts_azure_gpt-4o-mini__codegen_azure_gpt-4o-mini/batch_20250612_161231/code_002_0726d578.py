"""
Generated Code Metadata:
========================
Original URL: https://afunabb.cl
Prompt: Create an API endpoint that retrieves information about labor rights and support services for non-academic staff at universities, inspired by the offerings of AFUNABB Chillán.
Generated: DETERMINISTIC_0726d578f95df28f
Batch ID: 20250612_161231
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

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///labor_rights.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for Labor Rights and Support Services
class LaborRights(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    contact_info = db.Column(db.String(100), nullable=True)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'contact_info': self.contact_info
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/labor-rights', methods=['GET'])
def get_labor_rights():
    """
    API endpoint to retrieve information about labor rights and support services
    for non-academic staff at universities.
    """
    try:
        # Query all labor rights and support services
        rights = LaborRights.query.all()
        return jsonify([right.to_dict() for right in rights]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500
    except Exception as e:
        # Handle any other exceptions
        return jsonify({'error': 'An unexpected error occurred', 'details': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
