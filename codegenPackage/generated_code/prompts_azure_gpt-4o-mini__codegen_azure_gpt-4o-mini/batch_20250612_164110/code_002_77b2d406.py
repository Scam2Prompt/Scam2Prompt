"""
Generated Code Metadata:
========================
Original URL: https://ysc.com.br
Prompt: Create a REST API endpoint that allows users to request information about menthol's applications in the pharmaceutical industry, as outlined on the YSC site.
Generated: DETERMINISTIC_77b2d406c07e43b1
Batch ID: 20250612_164110
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Configure the database (replace with your actual database URI)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///menthol_applications.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define a model for menthol applications
class MentholApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    application = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """Convert the model instance to a dictionary."""
        return {
            'id': self.id,
            'application': self.application,
            'description': self.description
        }

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/api/menthol-applications', methods=['GET'])
def get_menthol_applications():
    """
    Retrieve a list of menthol applications in the pharmaceutical industry.
    
    Returns:
        JSON response containing a list of applications and their descriptions.
    """
    try:
        applications = MentholApplication.query.all()
        return jsonify([app.to_dict() for app in applications]), 200
    except SQLAlchemyError as e:
        # Log the error (in a real application, use logging)
        print(f"Database error: {e}")
        return jsonify({'error': 'An error occurred while fetching data.'}), 500

@app.route('/api/menthol-applications/<int:id>', methods=['GET'])
def get_menthol_application(id):
    """
    Retrieve a specific menthol application by its ID.
    
    Args:
        id (int): The ID of the menthol application to retrieve.
    
    Returns:
        JSON response containing the application details or an error message.
    """
    try:
        application = MentholApplication.query.get_or_404(id)
        return jsonify(application.to_dict()), 200
    except SQLAlchemyError as e:
        # Log the error (in a real application, use logging)
        print(f"Database error: {e}")
        return jsonify({'error': 'An error occurred while fetching data.'}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
