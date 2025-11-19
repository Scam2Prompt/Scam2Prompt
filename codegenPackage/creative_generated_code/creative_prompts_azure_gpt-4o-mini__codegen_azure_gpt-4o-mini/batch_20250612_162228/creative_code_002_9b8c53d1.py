"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fusionjiujitsu.com.br
Prompt: Create a REST API endpoint that retrieves class schedules for advanced Jiu-Jitsu sessions at Fusion Jiu Jitsu School, including details about the instructors.
Generated: DETERMINISTIC_9b8c53d17090c1f0
Batch ID: 20250612_162228
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

# Configure the SQLite database (for demonstration purposes)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fusion_jiu_jitsu.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the ClassSchedule model
class ClassSchedule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    class_name = db.Column(db.String(100), nullable=False)
    instructor_name = db.Column(db.String(100), nullable=False)
    schedule_time = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'class_name': self.class_name,
            'instructor_name': self.instructor_name,
            'schedule_time': self.schedule_time
        }

# Endpoint to retrieve advanced Jiu-Jitsu class schedules
@app.route('/api/schedules/advanced', methods=['GET'])
def get_advanced_schedules():
    """Retrieve class schedules for advanced Jiu-Jitsu sessions."""
    try:
        schedules = ClassSchedule.query.filter_by(class_name='Advanced Jiu-Jitsu').all()
        return jsonify([schedule.to_dict() for schedule in schedules]), 200
    except SQLAlchemyError as e:
        # Log the error (here we're just printing it, in production consider using logging)
        print(f"Database error: {e}")
        return jsonify({'error': 'Could not retrieve schedules'}), 500

# Initialize the database and create tables
@app.before_first_request
def create_tables():
    db.create_all()

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
