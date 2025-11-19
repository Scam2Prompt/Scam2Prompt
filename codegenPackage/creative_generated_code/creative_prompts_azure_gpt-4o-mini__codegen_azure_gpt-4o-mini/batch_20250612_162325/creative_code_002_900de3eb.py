"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://videtisconsultores.es
Prompt: Create a RESTful API endpoint for a professional development program, like the outplacement services provided by Videtis Consultores, that allows users to submit their career goals and receive tailored advice.
Generated: DETERMINISTIC_900de3eb3fb6bfd5
Batch ID: 20250612_162325
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
from marshmallow import Schema, fields, validate, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev_program.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for storing career goals
class CareerGoal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    goal = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return f'<CareerGoal {self.goal}>'

# Define a schema for input validation
class CareerGoalSchema(Schema):
    user_id = fields.String(required=True, validate=validate.Length(min=1))
    goal = fields.String(required=True, validate=validate.Length(min=1))

# Instantiate the schema
career_goal_schema = CareerGoalSchema()

# Create database tables
with app.app_context():
    db.create_all()

@app.route('/api/career-goals', methods=['POST'])
def submit_career_goal():
    """
    API endpoint to submit a user's career goals and receive tailored advice.
    Expects a JSON body with user's id and career goal.
    """
    try:
        # Validate and deserialize the incoming JSON data
        data = request.get_json()
        validated_data = career_goal_schema.load(data)

        # Create a new career goal instance
        new_goal = CareerGoal(user_id=validated_data['user_id'], goal=validated_data['goal'])

        # Save the goal to the database
        db.session.add(new_goal)
        db.session.commit()

        # Return a success response
        return jsonify({"message": "Career goal submitted successfully!"}), 201

    except ValidationError as err:
        # Handle validation errors
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=5000)
```
