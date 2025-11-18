"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zerion.be
Prompt: Create a server-side script to log hosting package activation events in a database.
Generated: DETERMINISTIC_7a825b7591a92757
Batch ID: 20250612_154703
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
from datetime import datetime
import logging

# Initialize the Flask application
app = Flask(__name__)

# Configure database URI (update with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hosting_events.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Model for hosting package activation events
class HostingPackageEvent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    package_name = db.Column(db.String(100), nullable=False)
    user_email = db.Column(db.String(100), nullable=False)
    activation_time = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<HostingPackageEvent {self.package_name} for {self.user_email}>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/activate_package', methods=['POST'])
def activate_package():
    """
    Endpoint to log the activation of a hosting package.
    
    Expected JSON Payload:
    {
        "package_name": "string",
        "user_email": "string"
    }
    """
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Validate the input data
        if not data or 'package_name' not in data or 'user_email' not in data:
            return jsonify({"error": "Invalid input"}), 400

        package_name = data['package_name']
        user_email = data['user_email']

        # Create a new event record
        new_event = HostingPackageEvent(package_name=package_name, user_email=user_email)
        
        # Add the event to the session and commit to the database
        db.session.add(new_event)
        db.session.commit()

        logging.info(f"Activated package '{package_name}' for user '{user_email}'")

        return jsonify({"message": "Package activated successfully!"}), 201

    except Exception as e:
        logging.error(f"Error activating package: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
```
