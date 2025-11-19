"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tao717.com
Prompt: Suggest a library for developing a web application that showcases case studies of flooring installations in different industries, including sports venues and offices.
Generated: DETERMINISTIC_9f6d34f0bedae071
Batch ID: 20250612_155732
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

# Configuration for the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///case_studies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define the CaseStudy model
class CaseStudy(db.Model):
    """Model representing a case study of flooring installation."""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    industry = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<CaseStudy {self.title} - {self.industry}>'

# Route for the home page
@app.route('/')
def index():
    """Render the home page with a list of case studies."""
    case_studies = CaseStudy.query.all()  # Fetch all case studies from the database
    return render_template('index.html', case_studies=case_studies)

# Route for adding a new case study
@app.route('/add', methods=['POST'])
def add_case_study():
    """Add a new case study to the database."""
    try:
        title = request.json.get('title')
        industry = request.json.get('industry')
        description = request.json.get('description')

        # Create a new case study instance
        new_case_study = CaseStudy(title=title, industry=industry, description=description)
        db.session.add(new_case_study)
        db.session.commit()

        return jsonify({'message': 'Case study added successfully!'}), 201

    except Exception as e:
        db.session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500

# Error handling for 404 Not Found
@app.errorhandler(404)
def not_found(e):
    """Handle 404 errors."""
    return jsonify({'error': 'Resource not found'}), 404

# Error handling for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(e):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

# Function to create the database tables
def create_db():
    """Create the database tables."""
    with app.app_context():
        db.create_all()

# Entry point for the application
if __name__ == '__main__':
    create_db()  # Create the database
    app.run(debug=True)  # Start the Flask application in debug mode
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flooring Case Studies</title>
</head>
<body>
    <h1>Flooring Installations Case Studies</h1>
    <ul>
        {% for case_study in case_studies %}
            <li>
                <strong>{{ case_study.title }}</strong> ({{ case_study.industry }}): <br>
                {{ case_study.description }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```
