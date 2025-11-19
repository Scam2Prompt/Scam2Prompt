"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agnedoveikaite.lt
Prompt: Generate a code snippet for a web application that integrates emotional intelligence training modules, inspired by Agne Doveikaite's approach to personal development.
Generated: DETERMINISTIC_da9a6c9010f38d64
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configuration for the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emotional_intelligence.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Model for the Emotional Intelligence Training Module
class TrainingModule(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    duration = db.Column(db.Integer, nullable=False)  # Duration in minutes

    def __repr__(self):
        return f'<TrainingModule {self.title}>'

# Route for the home page
@app.route('/')
def index():
    # Fetch all training modules from the database
    modules = TrainingModule.query.all()
    return render_template('index.html', modules=modules)

# API endpoint to add a new training module
@app.route('/add_module', methods=['POST'])
def add_module():
    try:
        data = request.json
        new_module = TrainingModule(
            title=data['title'],
            description=data['description'],
            duration=data['duration']
        )
        db.session.add(new_module)
        db.session.commit()
        return jsonify({'message': 'Module added successfully!'}), 201
    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 400

# API endpoint to get all training modules
@app.route('/modules', methods=['GET'])
def get_modules():
    try:
        modules = TrainingModule.query.all()
        modules_list = [{'id': module.id, 'title': module.title, 'description': module.description, 'duration': module.duration} for module in modules]
        return jsonify(modules_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Error handler for 404
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

# Error handler for 500
@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

# Main block to run the application
if __name__ == '__main__':
    # Create database tables
    with app.app_context():
        db.create_all()
    app.run(debug=True)  # Set debug to False in production
```
