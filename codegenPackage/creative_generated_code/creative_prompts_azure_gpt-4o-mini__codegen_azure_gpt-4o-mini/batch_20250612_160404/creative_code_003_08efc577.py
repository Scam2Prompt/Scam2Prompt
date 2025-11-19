"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hehnlo.com
Prompt: Develop an API endpoint for handling domain transfer requests, ensuring secure transactions as outlined in the content of hehnlo.com.
Generated: DETERMINISTIC_08efc5777fd1c779
Batch ID: 20250612_160404
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
import logging
import os

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (SQLite for this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///domains.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Domain model for SQLAlchemy
class Domain(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    owner = db.Column(db.String(100), nullable=False)

# Initialize the database
@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/api/domain-transfer', methods=['POST'])
def transfer_domain():
    """
    API endpoint to handle domain transfer requests.
    Expecting JSON with 'domain_name' and 'new_owner'.
    """
    try:
        # Get request data
        data = request.get_json()

        # Validate input
        domain_name = data.get('domain_name')
        new_owner = data.get('new_owner')

        if not domain_name or not new_owner:
            return jsonify({'error': 'Domain name and new owner are required.'}), 400

        # Check if domain exists
        domain = Domain.query.filter_by(name=domain_name).first()
        if not domain:
            return jsonify({'error': 'Domain not found.'}), 404

        # Update domain owner
        domain.owner = new_owner
        db.session.commit()

        return jsonify({'message': f'Domain {domain_name} transferred to {new_owner} successfully.'}), 200

    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error(f"Database error: {str(e)}")
        return jsonify({'error': 'Database error occurred. Please try again later.'}), 500
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred. Please try again later.'}), 500

if __name__ == '__main__':
    # Running the app
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=False)
```
