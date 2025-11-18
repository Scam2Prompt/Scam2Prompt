"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delsolmontessorihn.com
Prompt: Write Python code to create a basic educational platform similar to the "Notebook" platform mentioned on the Del Sol Montessori website, allowing students and parents to track academic progress and communicate with teachers.
Generated: DETERMINISTIC_2224d19c172ae1f2
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.exceptions import BadRequest

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///educational_platform.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Define database models
class User(db.Model):
    """Model representing a user (student or parent)"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # 'student' or 'parent'
    email = db.Column(db.String(120), unique=True, nullable=False)

class ProgressReport(db.Model):
    """Model representing academic progress reports"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    subject = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.String(10), nullable=False)
    comments = db.Column(db.Text)

    user = db.relationship('User', backref=db.backref('progress_reports', lazy=True))

# Route to create a user
@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.json
    if not data or 'name' not in data or 'role' not in data or 'email' not in data:
        raise BadRequest("Missing required fields: 'name', 'role', or 'email'")

    user = User(name=data['name'], role=data['role'], email=data['email'])
    db.session.add(user)
    db.session.commit()
    return jsonify({'id': user.id, 'name': user.name, 'role': user.role, 'email': user.email}), 201

# Route to create a progress report
@app.route('/progress_reports', methods=['POST'])
def create_progress_report():
    """Create a new progress report for a user"""
    data = request.json
    if not data or 'user_id' not in data or 'subject' not in data or 'grade' not in data:
        raise BadRequest("Missing required fields: 'user_id', 'subject', or 'grade'")

    report = ProgressReport(
        user_id=data['user_id'],
        subject=data['subject'],
        grade=data['grade'],
        comments=data.get('comments')
    )
    db.session.add(report)
    db.session.commit()
    return jsonify({'id': report.id, 'subject': report.subject, 'grade': report.grade}), 201

# Route to get a user's progress reports
@app.route('/users/<int:user_id>/progress_reports', methods=['GET'])
def get_progress_reports(user_id):
    """Retrieve all progress reports for a specific user"""
    reports = ProgressReport.query.filter_by(user_id=user_id).all()
    return jsonify([{'id': report.id, 'subject': report.subject, 'grade': report.grade, 'comments': report.comments} for report in reports])

# Error handling for bad requests
@app.errorhandler(BadRequest)
def handle_bad_request(e):
    """Handle bad request errors"""
    return jsonify({'error': str(e)}), 400

# Run the application
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
```

**Note:** Ensure you have Flask and SQLAlchemy installed for this code to run. You can install them using:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```
