"""
Generated Code Metadata:
========================
Original URL: https://www.pensar.inf.br
Prompt: "Design a mobile application for managers to access real-time business performance indicators and reports using the Solpen Gerencial tool."
Generated: DETERMINISTIC_f3b6da0e486b3575
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from datetime import datetime

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///business_performance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and marshmallow
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define the BusinessPerformance model
class BusinessPerformance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    indicator_name = db.Column(db.String(100), nullable=False)
    value = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, indicator_name, value):
        self.indicator_name = indicator_name
        self.value = value

# Create a schema for serializing the BusinessPerformance data
class BusinessPerformanceSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = BusinessPerformance

# Initialize the schema
performance_schema = BusinessPerformanceSchema()
performances_schema = BusinessPerformanceSchema(many=True)

# Create the database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Endpoint to add a new business performance indicator
@app.route('/performance', methods=['POST'])
def add_performance():
    try:
        # Get data from the request
        indicator_name = request.json['indicator_name']
        value = request.json['value']

        # Create a new BusinessPerformance instance
        new_performance = BusinessPerformance(indicator_name, value)

        # Add to the session and commit
        db.session.add(new_performance)
        db.session.commit()

        return performance_schema.jsonify(new_performance), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# Endpoint to get all business performance indicators
@app.route('/performance', methods=['GET'])
def get_performances():
    try:
        all_performances = BusinessPerformance.query.all()
        return performances_schema.jsonify(all_performances), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint to get a specific performance indicator by ID
@app.route('/performance/<id>', methods=['GET'])
def get_performance(id):
    try:
        performance = BusinessPerformance.query.get_or_404(id)
        return performance_schema.jsonify(performance), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 404

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Notes:
- This code is a simple Flask application that provides RESTful endpoints for managing business performance indicators.
- It includes error handling for common scenarios such as missing data and database errors.
- The application uses SQLite for simplicity, but it can be easily adapted to other databases.
- Ensure to install the required packages (`Flask`, `Flask-SQLAlchemy`, `Flask-Marshmallow`) before running the application.
