"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1iiinch.teachable.com
Prompt: How do I implement product filters for an online course catalog similar to the one on sadm's School?
Generated: DETERMINISTIC_e58d9db8dcfbe55b
Batch ID: 20250612_155723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(50), nullable=False)  # e.g., Beginner, Intermediate, Advanced
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        """Convert course object to dictionary for JSON response."""
        return {
            'id': self.id,
            'title': self.title,
            'category': self.category,
            'level': self.level,
            'price': self.price
        }

# Route to filter courses based on query parameters
@app.route('/api/courses', methods=['GET'])
def get_courses():
    """Retrieve courses with optional filters."""
    try:
        # Get filter parameters from the query string
        category = request.args.get('category')
        level = request.args.get('level')
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)

        # Build the query
        query = Course.query

        if category:
            query = query.filter(Course.category == category)
        if level:
            query = query.filter(Course.level == level)
        if min_price is not None:
            query = query.filter(Course.price >= min_price)
        if max_price is not None:
            query = query.filter(Course.price <= max_price)

        # Execute the query and convert results to a list of dictionaries
        courses = query.all()
        return jsonify([course.to_dict() for course in courses]), 200

    except Exception as e:
        # Handle any unexpected errors and return a 400 response
        return jsonify({'error': str(e)}), 400

# Main entry point
if __name__ == '__main__':
    # Create all tables
    with app.app_context():
        db.create_all()  # Create database tables if they do not exist
    app.run(debug=True)  # Run the application in debug mode (remove in production)
```
