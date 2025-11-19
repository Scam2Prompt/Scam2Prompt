"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balajitravelsonline.com
Prompt: Develop an API endpoint that allows users to inquire about Chennai local sightseeing packages with Balaji Tours and Travels.
Generated: DETERMINISTIC_c9b0518212124beb
Batch ID: 20250612_160912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///packages.db'  # Change to your database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Package model
class Package(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert the Package object to a dictionary for JSON serialization."""
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price
        }

@app.route('/api/packages', methods=['GET'])
def get_packages():
    """API endpoint to retrieve all sightseeing packages."""
    try:
        packages = Package.query.all()  # Fetch all packages from the database
        return jsonify([package.to_dict() for package in packages]), 200
    except Exception as e:
        # Log the error (in a real application, you'd use proper logging)
        print(f"Error retrieving packages: {e}")
        abort(500, description="Internal Server Error")

@app.route('/api/packages/<int:package_id>', methods=['GET'])
def get_package(package_id):
    """API endpoint to retrieve a specific sightseeing package by ID."""
    try:
        package = Package.query.get(package_id)  # Fetch package by ID
        if package is None:
            abort(404, description="Package not found")
        return jsonify(package.to_dict()), 200
    except Exception as e:
        print(f"Error retrieving package {package_id}: {e}")
        abort(500, description="Internal Server Error")

if __name__ == '__main__':
    # Create the database tables
    with app.app_context():
        db.create_all()  # Creates the database tables if they do not exist
        
    app.run(debug=True)  # Run the app in debug mode for development
```

This code snippet sets up a Flask API with endpoints to retrieve local sightseeing packages offered by Balaji Tours and Travels. The code follows best practices in Python and Flask, with clear comments for each part of the code. Make sure to adjust the database URI as necessary for your environment.
