"""
Generated Code Metadata:
========================
Original URL: https://www-magiceden-marketplace-ar5-f.blogspot.com
Prompt: Generate a code snippet for a web application that allows users to search for tires by width, height, and rim size, similar to the functionality described on the GB Truck website.
Generated: DETERMINISTIC_3a1a2b24d5374227
Batch ID: 20250612_163251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tires.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Tire model
class Tire(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    rim_size = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        """Convert Tire object to dictionary for JSON response."""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'rim_size': self.rim_size
        }

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/search_tires', methods=['GET'])
def search_tires():
    """
    Search for tires based on width, height, and rim size.
    Query parameters:
        - width: int
        - height: int
        - rim_size: int
    Returns:
        - JSON list of matching tires or an error message.
    """
    try:
        # Get query parameters
        width = request.args.get('width', type=int)
        height = request.args.get('height', type=int)
        rim_size = request.args.get('rim_size', type=int)

        # Validate input
        if width is None or height is None or rim_size is None:
            return jsonify({'error': 'Missing required parameters'}), 400

        # Query the database for matching tires
        tires = Tire.query.filter_by(width=width, height=height, rim_size=rim_size).all()

        # Convert results to a list of dictionaries
        result = [tire.to_dict() for tire in tires]

        # Return the results as JSON
        return jsonify(result), 200

    except Exception as e:
        # Handle unexpected errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

### Note:
- Ensure you have Flask and Flask-SQLAlchemy installed in your environment. You can install them using pip:
  ```bash
  pip install Flask Flask-SQLAlchemy
  ```
- This code snippet creates a simple web application with a search endpoint for tires. The database is initialized with SQLite, and the application can be expanded with additional features as needed.
