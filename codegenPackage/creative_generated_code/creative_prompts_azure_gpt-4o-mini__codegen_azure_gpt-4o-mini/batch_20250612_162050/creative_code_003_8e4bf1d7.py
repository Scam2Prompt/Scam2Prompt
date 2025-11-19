"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolcrespo.com.br
Prompt: Develop an API that allows users to receive customized workout routines based on their fitness goals, similar to the personalized training approach of Carol Crespo.
Generated: DETERMINISTIC_8e4bf1d7f4062cb5
Batch ID: 20250612_162050
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
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
# Configuration for SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workouts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for workouts
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(50), nullable=False)
    routine = db.Column(db.String(500), nullable=False)

# Schema for input validation
class WorkoutSchema(Schema):
    goal = fields.String(required=True)
    routine = fields.String(required=True)

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/workout', methods=['POST'])
def generate_workout():
    """
    Endpoint to generate a customized workout routine based on fitness goals.
    Expects a JSON payload with 'goal' and 'routine'.
    Returns a JSON response with the created workout or an error message.
    """
    # Parse and validate incoming JSON data
    schema = WorkoutSchema()
    try:
        data = schema.load(request.json)  # Validate incoming data
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400
    
    # Create a new Workout instance
    new_workout = Workout(goal=data['goal'], routine=data['routine'])
    
    try:
        db.session.add(new_workout)  # Add to session
        db.session.commit()           # Commit to the database
    except Exception as e:
        db.session.rollback()         # Rollback in case of error
        return jsonify({"error": str(e)}), 500
    
    return jsonify({"id": new_workout.id, "goal": new_workout.goal, "routine": new_workout.routine}), 201

@app.route('/workout/<int:id>', methods=['GET'])
def get_workout(id):
    """
    Endpoint to retrieve a workout routine by its ID.
    Returns the workout details or an error message if not found.
    """
    workout = Workout.query.get(id)
    
    if not workout:
        return jsonify({"error": "Workout not found!"}), 404
    
    return jsonify({
        "id": workout.id,
        "goal": workout.goal,
        "routine": workout.routine
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
```
