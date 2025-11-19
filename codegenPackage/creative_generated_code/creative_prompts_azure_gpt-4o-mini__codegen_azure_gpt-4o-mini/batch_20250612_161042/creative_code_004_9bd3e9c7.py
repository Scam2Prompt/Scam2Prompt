"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mandosecurity.com
Prompt: Create a sample code for a web application that provides 24/7 monitoring and access control features, reflecting the services offered by Mando Security.
Generated: DETERMINISTIC_9bd3e9c723fa3d1f
Batch ID: 20250612_161042
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:5000/api/access`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure the SQLAlchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monitoring_db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Define a model for Access Control Logs
class AccessControlLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    access_time = db.Column(db.DateTime, default=datetime.utcnow)
    action = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<AccessControlLog {self.user_id} {self.access_time} {self.action}>'

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/access', methods=['POST'])
def log_access():
    """Log an access event."""
    data = request.get_json()

    # Validate incoming data
    if not data or 'user_id' not in data or 'action' not in data:
        return jsonify({'error': 'Invalid input data'}), 400

    try:
        new_log = AccessControlLog(user_id=data['user_id'], action=data['action'])
        db.session.add(new_log)
        db.session.commit()
        return jsonify({'message': 'Access logged successfully'}), 201
    except Exception as e:
        logging.error(f"Error logging access: {e}")
        return jsonify({'error': 'Failed to log access'}), 500

@app.route('/api/access', methods=['GET'])
def get_access_logs():
    """Retrieve access logs."""
    try:
        logs = AccessControlLog.query.all()
        return jsonify [{'id': log.id, 'user_id': log.user_id,
                        'access_time': log.access_time.isoformat(),
                        'action': log.action} for log in logs], 200
    except Exception as e:
        logging.error(f"Error retrieving access logs: {e}")
        return jsonify({'error': 'Failed to retrieve access logs'}), 500

@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors."""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    # Start the application
    app.run(host='0.0.0.0', port=5000, debug=True)
```

### Requirements:
- This code requires Flask and Flask-SQLAlchemy to be installed. Use the following command to install:
```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

### Running the Application:
1. Save the above code in a file named `app.py`.
2. Run the application using:
```bash
python app.py
```
3. Access the API at `http://localhost:5000/api/access` for logging and retrieving access events.
