"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://munshihr.com
Prompt: Suggest tools or libraries for building a large CV database system, inspired by Munshi HR Solutions' "Large CV Bank" feature.
Generated: DETERMINISTIC_3ce3a4a7a3e4e37d
Batch ID: 20250612_151710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
CV Database System: A simple implementation of a CV database using Flask and SQLAlchemy.
This example is inspired by the "Large CV Bank" feature and demonstrates best practices for building a CV database.
"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Configuration for the SQLite database (can be changed to other DBs as needed)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cv_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Model representing a CV in the database
class CV(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), nullable=True)
    skills = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<CV {self.name}>"

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/cv', methods=['POST'])
def add_cv():
    """Endpoint to add a new CV to the database."""
    data = request.json
    try:
        new_cv = CV(
            name=data['name'],
            email=data['email'],
            phone=data.get('phone'),
            skills=data['skills']
        )
        db.session.add(new_cv)
        db.session.commit()
        return jsonify({"message": "CV added successfully!"}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/cv', methods=['GET'])
def get_cvs():
    """Endpoint to retrieve all CVs from the database."""
    try:
        cvs = CV.query.all()
        return jsonify([{'id': cv.id, 'name': cv.name, 'email': cv.email, 'phone': cv.phone, 'skills': cv.skills} for cv in cvs]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cv/<int:cv_id>', methods=['GET'])
def get_cv(cv_id):
    """Endpoint to retrieve a specific CV by ID."""
    try:
        cv = CV.query.get_or_404(cv_id)
        return jsonify({'id': cv.id, 'name': cv.name, 'email': cv.email, 'phone': cv.phone, 'skills': cv.skills}), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

@app.route('/cv/<int:cv_id>', methods=['PUT'])
def update_cv(cv_id):
    """Endpoint to update an existing CV."""
    data = request.json
    try:
        cv = CV.query.get_or_404(cv_id)
        cv.name = data.get('name', cv.name)
        cv.email = data.get('email', cv.email)
        cv.phone = data.get('phone', cv.phone)
        cv.skills = data.get('skills', cv.skills)
        db.session.commit()
        return jsonify({"message": "CV updated successfully!"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@app.route('/cv/<int:cv_id>', methods=['DELETE'])
def delete_cv(cv_id):
    """Endpoint to delete a CV from the database."""
    try:
        cv = CV.query.get_or_404(cv_id)
        db.session.delete(cv)
        db.session.commit()
        return jsonify({"message": "CV deleted successfully!"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
