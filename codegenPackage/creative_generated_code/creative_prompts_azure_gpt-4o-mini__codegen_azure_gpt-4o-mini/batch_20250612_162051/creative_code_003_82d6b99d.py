"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drcarloscastillo.com
Prompt: Develop an API endpoint that retrieves information on reconstructive surgery options for ankle injuries, based on the services offered by Dr. Carlos Castillo.
Generated: DETERMINISTIC_82d6b99d9bc82705
Batch ID: 20250612_162051
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///surgery_options.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy database object
db = SQLAlchemy(app)

# Model for storing reconstructive surgery options
class SurgeryOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    recovery_time = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the SurgeryOption object to a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "recovery_time": self.recovery_time
        }

@app.route('/api/surgery-options', methods=['GET'])
def get_surgery_options():
    """
    API endpoint to retrieve all reconstructive surgery options for ankle injuries
    offered by Dr. Carlos Castillo.

    Returns:
        JSON response containing a list of surgery options or an error message.
    """
    try:
        options = SurgeryOption.query.all()
        return jsonify([option.to_dict() for option in options]), 200
    except SQLAlchemyError as e:
        # Log the error (for production, consider using a logging library)
        print(f"Database query error: {str(e)}")
        return jsonify({"error": "Failed to retrieve surgery options."}), 500

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()
        
    # Run the Flask application
    app.run(debug=True)
```

**Note:** To use this code, ensure you have Flask and SQLAlchemy installed in your Python environment. You can install them via pip:

```bash
pip install Flask Flask-SQLAlchemy
``` 

Make sure to create and populate the `surgery_options.db` database with relevant data before making requests to the API.
