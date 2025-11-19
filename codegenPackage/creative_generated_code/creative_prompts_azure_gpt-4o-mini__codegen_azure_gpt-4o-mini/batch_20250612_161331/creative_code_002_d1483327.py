"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://securities-and-exchange-commission.com
Prompt: Create a REST API endpoint that allows users to submit formal notices regarding corporate compliance issues, inspired by the content on the SEC non-official website.
Generated: DETERMINISTIC_d1483327dd02b501
Batch ID: 20250612_161331
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
from sqlalchemy.exc import SQLAlchemyError
import os

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///compliance_notices.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database model for compliance notices
class ComplianceNotice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'submitted_at': self.submitted_at.isoformat()
        }

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/notices', methods=['POST'])
def submit_notice():
    """
    Endpoint to submit a formal notice regarding corporate compliance issues.
    """
    try:
        data = request.get_json()

        # Validate input data
        if not data or 'title' not in data or 'description' not in data:
            return jsonify({'error': 'Invalid input, title and description are required.'}), 400

        # Create a new compliance notice
        new_notice = ComplianceNotice(title=data['title'], description=data['description'])
        db.session.add(new_notice)
        db.session.commit()

        return jsonify(new_notice.to_dict()), 201

    except SQLAlchemyError as e:
        db.session.rollback()  # Rollback the session in case of error
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

@app.route('/api/notices', methods=['GET'])
def get_notices():
    """
    Endpoint to retrieve all submitted compliance notices.
    """
    try:
        notices = ComplianceNotice.query.all()
        return jsonify([notice.to_dict() for notice in notices]), 200

    except SQLAlchemyError as e:
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred: ' + str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=os.environ.get('FLASK_DEBUG', default=False))
```
