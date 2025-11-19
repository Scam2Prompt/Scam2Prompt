"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blocprest.ro
Prompt: Generate a code snippet for a web application that allows users to report technical issues 24/7, inspired by the support services provided by BlocPrest.
Generated: DETERMINISTIC_467fe28417a8b25b
Batch ID: 20250612_155849
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import logging
from datetime import datetime

# Initialize Flask application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///issues.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define the Issue model
class Issue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Issue {self.id} by {self.user_name}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/report_issue', methods=['POST'])
def report_issue():
    """
    Endpoint to report a technical issue.
    Expects JSON data with user_name, email, and description.
    Returns a success message or error details.
    """
    try:
        data = request.get_json()

        # Validate input data
        user_name = data.get('user_name')
        email = data.get('email')
        description = data.get('description')

        if not user_name or not email or not description:
            return jsonify({'error': 'All fields are required.'}), 400

        # Create a new issue and add it to the database
        new_issue = Issue(user_name=user_name, email=email, description=description)
        db.session.add(new_issue)
        db.session.commit()

        logging.info(f"Issue reported by {user_name}: {description}")

        return jsonify({'message': 'Issue reported successfully!'}), 201

    except Exception as e:
        logging.error(f"Error reporting issue: {e}")
        return jsonify({'error': 'An error occurred while reporting the issue.'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
