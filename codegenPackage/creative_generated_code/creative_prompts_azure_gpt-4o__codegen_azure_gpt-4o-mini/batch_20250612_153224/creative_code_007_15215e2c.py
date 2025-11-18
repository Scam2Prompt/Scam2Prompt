"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aidasdb.org
Prompt: Develop a web application to track the progress of CSR initiatives, such as AIDA's SBI Clinic on Wheels and Swabalambam Silai School, with real-time updates and reports.
Generated: DETERMINISTIC_15215e2cb93c1d27
Batch ID: 20250612_153224
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
from datetime import datetime
import logging

# Initialize Flask application
app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///csr_initiatives.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the CSR Initiative model
class CSRInitiative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    progress_report = db.Column(db.Text, nullable=True)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<CSRInitiative {self.name}>'

# Create the database
@app.before_first_request
def create_tables():
    db.create_all()

# Route to render the main dashboard
@app.route('/')
def index():
    initiatives = CSRInitiative.query.all()
    return render_template('index.html', initiatives=initiatives)

# Route to add a new CSR initiative
@app.route('/add_initiative', methods=['POST'])
def add_initiative():
    try:
        name = request.json.get('name')
        description = request.json.get('description')
        
        if not name:
            raise ValueError("The initiative name is required.")

        new_initiative = CSRInitiative(name=name, description=description)
        db.session.add(new_initiative)
        db.session.commit()
        
        logging.info(f'Added new initiative: {name}')
        return jsonify({"message": "Initiative added successfully!"}), 201
    except Exception as e:
        logging.error(f"Error adding initiative: {str(e)}")
        return jsonify({"error": str(e)}), 400

# Route to update the progress of an initiative
@app.route('/update_progress/<int:id>', methods=['PUT'])
def update_progress(id):
    try:
        initiative = CSRInitiative.query.get_or_404(id)
        progress_report = request.json.get('progress_report')
        
        initiative.progress_report = progress_report
        initiative.updated_at = datetime.utcnow()
        db.session.commit()

        logging.info(f'Updated progress for initiative: {initiative.name}')
        return jsonify({"message": "Progress updated successfully!"}), 200
    except Exception as e:
        logging.error(f"Error updating progress: {str(e)}")
        return jsonify({"error": str(e)}), 400

# Route to get reports of all initiatives
@app.route('/report', methods=['GET'])
def report():
    try:
        initiatives = CSRInitiative.query.all()
        report_data = [
            {"name": initiative.name, "description": initiative.description,
             "progress_report": initiative.progress_report, "updated_at": initiative.updated_at}
            for initiative in initiatives
        ]
        return jsonify(report_data), 200
    except Exception as e:
        logging.error(f"Error fetching reports: {str(e)}")
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

Ensure to create an `index.html` file to render the dashboard and set up the necessary HTML structure for displaying and adding initiatives. Additionally, install Flask and SQLAlchemy using pip:
```bash
pip install Flask SQLAlchemy
```
