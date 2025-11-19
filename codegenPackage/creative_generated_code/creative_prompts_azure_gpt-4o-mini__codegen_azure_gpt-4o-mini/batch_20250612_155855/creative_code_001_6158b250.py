"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cegeduc.org
Prompt: Generate a REST API that allows users to access resources related to biodiversity conservation and urban agriculture initiatives championed by Cegeduc.
Generated: DETERMINISTIC_6158b250ad10e36a
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cegeduc_resources.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for biodiversity conservation and urban agriculture initiatives
class Initiative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the Initiative model to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/initiatives', methods=['GET'])
def get_initiatives():
    """Retrieve a list of all initiatives."""
    initiatives = Initiative.query.all()
    return jsonify([initiative.to_dict() for initiative in initiatives]), 200

@app.route('/initiatives/<int:init_id>', methods=['GET'])
def get_initiative(init_id):
    """Retrieve a specific initiative by ID."""
    initiative = Initiative.query.get_or_404(init_id)
    return jsonify(initiative.to_dict()), 200

@app.route('/initiatives', methods=['POST'])
def create_initiative():
    """Create a new initiative."""
    data = request.get_json()
    if not data or 'title' not in data or 'description' not in data or 'category' not in data:
        abort(400, description="Invalid request data. Must include title, description, and category.")
    
    new_initiative = Initiative(
        title=data['title'],
        description=data['description'],
        category=data['category']
    )
    
    try:
        db.session.add(new_initiative)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        abort(409, description="An initiative with this title already exists.")

    return jsonify(new_initiative.to_dict()), 201


@app.route('/initiatives/<int:init_id>', methods=['PUT'])
def update_initiative(init_id):
    """Update an existing initiative."""
    initiative = Initiative.query.get_or_404(init_id)
    data = request.get_json()

    if not data:
        abort(400, description="Invalid request data.")

    initiative.title = data.get('title', initiative.title)
    initiative.description = data.get('description', initiative.description)
    initiative.category = data.get('category', initiative.category)

    db.session.commit()
    return jsonify(initiative.to_dict()), 200

@app.route('/initiatives/<int:init_id>', methods=['DELETE'])
def delete_initiative(init_id):
    """Delete an existing initiative."""
    initiative = Initiative.query.get_or_404(init_id)
    db.session.delete(initiative)
    db.session.commit()
    return jsonify({"message": "Initiative deleted successfully."}), 204

if __name__ == '__main__':
    app.run(debug=True)
```
