"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mail.gtempus.com
Prompt: Generate code for a web application that integrates Grupo de Seguros Tempus's "Programa de Asesor de Seguros Digital," allowing advisors to track their commissions, schedule flexible work hours, and access free training resources.
Generated: DETERMINISTIC_a4051aadbaa39a86
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the Flask application
app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tempus_insurance.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database and migration tools
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Models

class Advisor(db.Model):
    """Model for storing advisor information."""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    commission = db.relationship('Commission', backref='advisor', lazy=True)

class Commission(db.Model):
    """Model for storing commission records."""
    id = db.Column(db.Integer, primary_key=True)
    advisor_id = db.Column(db.Integer, db.ForeignKey('advisor.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False)

class WorkHour(db.Model):
    """Model for storing advisor's work hours."""
    id = db.Column(db.Integer, primary_key=True)
    advisor_id = db.Column(db.Integer, db.ForeignKey('advisor.id'), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)

class TrainingResource(db.Model):
    """Model for storing training resources."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    link = db.Column(db.String(200), nullable=False)

# Routes

@app.route('/')
def index():
    """Render the home page for the application."""
    return render_template('index.html')

@app.route('/advisors', methods=['POST'])
def add_advisor():
    """Endpoint to add a new advisor."""
    try:
        data = request.json
        new_advisor = Advisor(name=data['name'], email=data['email'])
        db.session.add(new_advisor)
        db.session.commit()
        return jsonify({"message": "Advisor added successfully!"}), 201
    except Exception as e:
        logging.error(f"Error adding advisor: {e}")
        return jsonify({"error": "Failed to add advisor"}), 500

@app.route('/commissions', methods=['GET'])
def get_commissions():
    """Endpoint to retrieve commission records of an advisor."""
    advisor_id = request.args.get('advisor_id')
    commissions = Commission.query.filter_by(advisor_id=advisor_id).all()
    return jsonify([{"id": c.id, "amount": c.amount, "date": c.date} for c in commissions]), 200

@app.route('/work_hours', methods=['POST'])
def schedule_work_hours():
    """Endpoint to schedule work hours for an advisor."""
    try:
        data = request.json
        new_hours = WorkHour(advisor_id=data['advisor_id'], 
                             start_time=data['start_time'], 
                             end_time=data['end_time'])
        db.session.add(new_hours)
        db.session.commit()
        return jsonify({"message": "Work hours scheduled successfully!"}), 201
    except Exception as e:
        logging.error(f"Error scheduling work hours: {e}")
        return jsonify({"error": "Failed to schedule work hours"}), 500

@app.route('/training_resources', methods=['GET'])
def get_training_resources():
    """Endpoint to retrieve training resources."""
    resources = TrainingResource.query.all()
    return jsonify([{"id": r.id, "title": r.title, "link": r.link} for r in resources]), 200

# Error handling

@app.errorhandler(404)
def not_found(error):
    """Custom error handler for 404 errors."""
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(error):
    """Custom error handler for server errors."""
    return jsonify({"error": "Internal server error"}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

### Requirements
Make sure you have the following Python packages installed:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

### Note
You will also need to create the corresponding `index.html` file in the `templates` directory to serve the main web page of the application.
