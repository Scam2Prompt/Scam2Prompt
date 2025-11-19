"""
Generated Code Metadata:
========================
Original URL: https://wonderplanet.ee
Prompt: Develop an API endpoint that retrieves various entertainment options for events, inspired by the diverse services listed on Wonderplanet.ee, such as face painting and balloon modeling.
Generated: DETERMINISTIC_b8d70cb35d83b5ba
Batch ID: 20250612_160526
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

app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///entertainment.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the EntertainmentOption model
class EntertainmentOption(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category
        }

# Initialize the database (for demonstration purposes)
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/entertainment', methods=['GET'])
def get_entertainment_options():
    """Retrieve a list of entertainment options."""
    try:
        options = EntertainmentOption.query.all()
        return jsonify([option.to_dict() for option in options]), 200
    except SQLAlchemyError as e:
        # Log the error (in a real application, use a logging framework)
        print(f"Database error: {e}")
        return jsonify({'error': 'Could not retrieve entertainment options.'}), 500

@app.route('/api/entertainment', methods=['POST'])
def add_entertainment_option():
    """Add a new entertainment option."""
    data = request.get_json()
    
    if not data or 'name' not in data or 'category' not in data:
        return jsonify({'error': 'Invalid input. Name and category are required.'}), 400

    new_option = EntertainmentOption(
        name=data['name'],
        description=data.get('description'),
        category=data['category']
    )

    try:
        db.session.add(new_option)
        db.session.commit()
        return jsonify(new_option.to_dict()), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        print(f"Database error: {e}")
        return jsonify({'error': 'Could not add entertainment option.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
