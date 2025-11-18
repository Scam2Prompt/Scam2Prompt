"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teleperformance-amplifai.com
Prompt: Generate a REST API endpoint for retrieving employee engagement data, inspired by AmplifAI's platform capabilities.
Generated: DETERMINISTIC_9cea2f013c372b88
Batch ID: 20250612_151504
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

app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define an EmployeeEngagement model to represent the data
class EmployeeEngagement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, nullable=False)
    engagement_score = db.Column(db.Float, nullable=False)
    feedback = db.Column(db.String(255))

# Create the database and tables if they don't exist
with app.app_context():
    db.create_all()

@app.route('/api/engagement/<int:employee_id>', methods=['GET'])
def get_employee_engagement(employee_id):
    """
    Retrieve engagement data for a specific employee by their ID.

    :param employee_id: ID of the employee to fetch engagement data for.
    :return: JSON response containing engagement data or an error message.
    """
    try:
        engagement_data = EmployeeEngagement.query.filter_by(employee_id=employee_id).first()
        
        if engagement_data:
            return jsonify({
                'employee_id': engagement_data.employee_id,
                'engagement_score': engagement_data.engagement_score,
                'feedback': engagement_data.feedback
            }), 200
        else:
            return jsonify({'error': 'Employee engagement data not found'}), 404

    except SQLAlchemyError as e:
        # Log the error (not implemented here for simplicity)
        return jsonify({'error': 'An error occurred while fetching data'}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set to False in production
```
