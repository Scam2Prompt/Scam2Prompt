"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meteora-app-git-sam-racx-294-deploy-ui-for-met-points-wowcats.vercel.app
Prompt: Implement a feature that allows users to create a new pool on the Meteora app, including parameters for multi-token support.
Generated: DETERMINISTIC_ef129c386a1ed65f
Batch ID: 20250612_163950
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# meteora_app.py

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize Flask app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meteora.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Pool model for the database
class Pool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    tokens = db.Column(db.String(500), nullable=False)  # Comma-separated list of tokens
    min_deposit = db.Column(db.Float, nullable=False)
    
    def __repr__(self):
        return f'<Pool {self.name}>'

# Create a schema for validating pool creation input
class PoolSchema(Schema):
    name = fields.Str(required=True)
    tokens = fields.Str(required=True)  # Expecting a comma-separated string
    min_deposit = fields.Float(required=True)

# Create the database and tables
with app.app_context():
    db.create_all()

@app.route('/create_pool', methods=['POST'])
def create_pool():
    """Endpoint to create a new token pool."""
    schema = PoolSchema()
    
    # Validate incoming JSON data
    try:
        data = schema.load(request.json)
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400  # Bad Request if validation fails

    # Check if pool with the same name already exists
    existing_pool = Pool.query.filter_by(name=data['name']).first()
    if existing_pool:
        return jsonify({"error": "Pool with this name already exists."}), 409  # Conflict

    # Create a new pool
    new_pool = Pool(
        name=data['name'],
        tokens=data['tokens'],
        min_deposit=data['min_deposit']
    )

    # Add to the session and commit
    try:
        db.session.add(new_pool)
        db.session.commit()
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({"error": str(e)}), 500  # Internal Server Error

    return jsonify({"message": "Pool created successfully.", "pool_id": new_pool.id}), 201  # Created

if __name__ == '__main__':
    app.run(debug=True)
```
