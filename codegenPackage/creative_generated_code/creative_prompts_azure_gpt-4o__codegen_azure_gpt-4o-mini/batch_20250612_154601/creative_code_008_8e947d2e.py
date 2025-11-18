"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getabstractus.com
Prompt: Generate code for a collaborative tool that enables joint policy analysis across regions, as described in Abstract's sandboxed environments.
Generated: DETERMINISTIC_8e947d2e06c2b764
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///policy_analysis.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Policy model
class Policy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    region = db.Column(db.String(100), nullable=False)
    policy_name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Policy {self.policy_name} in {self.region}>'

# Create a schema for input validation
class PolicySchema(Schema):
    region = fields.Str(required=True)
    policy_name = fields.Str(required=True)
    description = fields.Str(required=True)

policy_schema = PolicySchema()
policies_schema = PolicySchema(many=True)

# Create the database tables
with app.app_context():
    db.create_all()

# Route to add a new policy
@app.route('/policies', methods=['POST'])
def add_policy():
    try:
        # Validate input data
        data = request.get_json()
        policy_data = policy_schema.load(data)

        # Create a new Policy instance
        new_policy = Policy(**policy_data)
        db.session.add(new_policy)
        db.session.commit()

        return jsonify({"message": "Policy added successfully"}), 201

    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "Policy already exists"}), 409
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get all policies
@app.route('/policies', methods=['GET'])
def get_policies():
    try:
        policies = Policy.query.all()
        return policies_schema.dump(policies), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to get policies by region
@app.route('/policies/region/<string:region>', methods=['GET'])
def get_policies_by_region(region):
    try:
        policies = Policy.query.filter_by(region=region).all()
        return policies_schema.dump(policies), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Route to delete a policy by ID
@app.route('/policies/<int:id>', methods=['DELETE'])
def delete_policy(id):
    try:
        policy = Policy.query.get_or_404(id)
        db.session.delete(policy)
        db.session.commit()
        return jsonify({"message": "Policy deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug to False for production
```
