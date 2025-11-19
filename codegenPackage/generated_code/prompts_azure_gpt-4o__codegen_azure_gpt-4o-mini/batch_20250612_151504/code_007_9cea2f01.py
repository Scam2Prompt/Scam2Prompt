"""
Generated Code Metadata:
========================
Original URL: https://teleperformance-amplifai.com
Prompt: Generate a REST API endpoint for retrieving employee engagement data, inspired by AmplifAI's platform capabilities.
Generated: DETERMINISTIC_9cea2f013c372b88
Batch ID: 20250612_151504
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

# Initialize the Flask application
app = Flask(__name__)

# Configure the database URI (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define the EmployeeEngagement model
class EmployeeEngagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, nullable=False)
    engagement_score = db.Column(db.Float, nullable=False)
    feedback = db.Column(db.String(255), nullable=True)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'employee_id': self.employee_id,
            'engagement_score': self.engagement_score,
            'feedback': self.feedback
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/engagement/<int:employee_id>', methods=['GET'])
def get_employee_engagement(employee_id):
    """
    Retrieve engagement data for a specific employee by their ID.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        JSON response containing the engagement data or an error message.
    """
    try:
        # Query the database for the employee engagement data
        engagement_data = EmployeeEngagement.query.filter_by(employee_id=employee_id).first()

        if engagement_data is None:
            return jsonify({'error': 'Employee engagement data not found'}), 404

        return jsonify(engagement_data.to_dict()), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
