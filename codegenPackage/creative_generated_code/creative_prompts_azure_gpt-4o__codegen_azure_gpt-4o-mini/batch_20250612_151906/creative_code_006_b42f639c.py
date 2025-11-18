"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrium.io
Prompt: Generate a REST API structure for a decision control system similar to the one described on Arbitrium's website.
Generated: DETERMINISTIC_b42f639c0961e8d6
Batch ID: 20250612_151906
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
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///decisions.db'  # Use SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Decision model to represent a decision in the database
class Decision(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    outcome = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"<Decision {self.title}>"

# Schema for serializing/validating decision data
class DecisionSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    description = fields.Str()
    outcome = fields.Str(required=True)

# Initialize the schema
decision_schema = DecisionSchema()
decisions_schema = DecisionSchema(many=True)

# Create the database
with app.app_context():
    db.create_all()

# Route to create a new decision
@app.route('/decisions', methods=['POST'])
def create_decision():
    """Create a new decision."""
    try:
        # Validate and deserialize input
        data = decision_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    # Create new decision instance
    new_decision = Decision(**data)

    # Add and commit to the database
    db.session.add(new_decision)
    db.session.commit()
    
    return decision_schema.dump(new_decision), 201

# Route to get all decisions
@app.route('/decisions', methods=['GET'])
def get_decisions():
    """Retrieve all decisions."""
    decisions = Decision.query.all()
    return decisions_schema.dump(decisions), 200

# Route to get a single decision by ID
@app.route('/decisions/<int:id>', methods=['GET'])
def get_decision(id):
    """Retrieve a decision by ID."""
    decision = Decision.query.get(id)
    if decision is None:
        abort(404, description="Decision not found")
    
    return decision_schema.dump(decision), 200

# Route to update a decision by ID
@app.route('/decisions/<int:id>', methods=['PUT'])
def update_decision(id):
    """Update a decision by ID."""
    decision = Decision.query.get(id)
    if decision is None:
        abort(404, description="Decision not found")

    try:
        data = decision_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    # Update decision fields
    decision.title = data.get('title', decision.title)
    decision.description = data.get('description', decision.description)
    decision.outcome = data.get('outcome', decision.outcome)

    # Commit changes to the database
    db.session.commit()
    return decision_schema.dump(decision), 200

# Route to delete a decision by ID
@app.route('/decisions/<int:id>', methods=['DELETE'])
def delete_decision(id):
    """Delete a decision by ID."""
    decision = Decision.query.get(id)
    if decision is None:
        abort(404, description="Decision not found")

    # Remove the decision from the database
    db.session.delete(decision)
    db.session.commit()
    return jsonify({"message": "Decision deleted successfully"}), 204

# Error handler for 404 errors
@app.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return jsonify({"error": str(error)}), 404

# Error handler for 500 errors
@app.errorhandler(Exception)
def internal_error(error):
    """Handle internal server errors."""
    return jsonify({"error": "An internal error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
