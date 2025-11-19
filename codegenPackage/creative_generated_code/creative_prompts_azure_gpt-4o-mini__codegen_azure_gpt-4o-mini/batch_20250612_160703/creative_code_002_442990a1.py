"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stars-ksa.com
Prompt: Create an API endpoint for a cleaning service platform that retrieves available cleaning packages, similar to the customized solutions offered by Star Cleaning Services.
Generated: DETERMINISTIC_442990a1c0ad3d50
Batch ID: 20250612_160703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cleaning_services.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model for Cleaning Package
class CleaningPackage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(250), nullable=True)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

# Initialize the database and create the cleaning packages table
@app.before_first_request
def create_tables():
    db.create_all()

# API endpoint to retrieve available cleaning packages
@app.route('/api/cleaning-packages', methods=['GET'])
def get_cleaning_packages():
    try:
        packages = CleaningPackage.query.all()
        return jsonify([pkg.to_dict() for pkg in packages]), 200
    except SQLAlchemyError as e:
        # Log the error message for debugging (consider using logging library in production)
        print(f"Database error occurred: {str(e)}")
        return jsonify({'error': 'Unable to fetch cleaning packages at this time.'}), 500

# Main entry point for the application
if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred while starting the application: {str(e)}")
```
