"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://odasloucabrazzz.blogspot.com
Prompt: Develop an API endpoint that provides details about the types of cookware available at Varejão das Louças, including options for restaurants and hotels.
Generated: DETERMINISTIC_34395a76dd3887cd
Batch ID: 20250612_160657
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cookware.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the Cookware model
class Cookware(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    suitable_for = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)

    def to_dict(self):
        """Convert the Cookware model to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'suitable_for': self.suitable_for,
            'description': self.description
        }

# Create the database and the cookware table
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/cookware', methods=['GET'])
def get_cookware():
    """API endpoint to get details about cookware available."""
    try:
        cookware_items = Cookware.query.all()
        return jsonify([item.to_dict() for item in cookware_items]), 200
    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": "Database error occurred", "details": str(e)}), 500

@app.route('/api/cookware', methods=['POST'])
def add_cookware():
    """API endpoint to add new cookware details."""
    data = request.json
    if not data or 'name' not in data or 'type' not in data or 'suitable_for' not in data:
        return jsonify({"error": "Invalid input"}), 400
    
    # Create a new Cookware instance
    new_cookware = Cookware(
        name=data['name'],
        type=data['type'],
        suitable_for=data['suitable_for'],
        description=data.get('description', '')
    )
    
    try:
        db.session.add(new_cookware)
        db.session.commit()
        return jsonify(new_cookware.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Failed to add cookware", "details": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
