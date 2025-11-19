"""
Generated Code Metadata:
========================
Original URL: https://carolcrespo.com.br
Prompt: Develop an API that allows users to receive customized workout routines based on their fitness goals, similar to the personalized training approach of Carol Crespo.
Generated: DETERMINISTIC_8e4bf1d7f4062cb5
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields, ValidationError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workouts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Workout model
class Workout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    goal = db.Column(db.String(50), nullable=False)
    routine = db.Column(db.String(200), nullable=False)

# Create the database
with app.app_context():
    db.create_all()

# Define a schema for input validation
class WorkoutSchema(Schema):
    goal = fields.Str(required=True)
    routine = fields.Str(required=True)

# Initialize the schema
workout_schema = WorkoutSchema()

@app.route('/workout', methods=['POST'])
def create_workout():
    """
    Create a new workout routine based on user goals.
    Expects a JSON payload with 'goal' and 'routine'.
    """
    try:
        # Validate and deserialize input
        data = request.get_json()
        validated_data = workout_schema.load(data)

        # Create a new Workout instance
        new_workout = Workout(goal=validated_data['goal'], routine=validated_data['routine'])
        db.session.add(new_workout)
        db.session.commit()

        return jsonify({"message": "Workout created successfully!", "id": new_workout.id}), 201

    except ValidationError as err:
        return jsonify({"errors": err.messages}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/workout/<int:workout_id>', methods=['GET'])
def get_workout(workout_id):
    """
    Retrieve a workout routine by its ID.
    """
    try:
        workout = Workout.query.get_or_404(workout_id)
        return jsonify({"goal": workout.goal, "routine": workout.routine}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/workouts', methods=['GET'])
def get_all_workouts():
    """
    Retrieve all workout routines.
    """
    try:
        workouts = Workout.query.all()
        result = [{"id": w.id, "goal": w.goal, "routine": w.routine} for w in workouts]
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
