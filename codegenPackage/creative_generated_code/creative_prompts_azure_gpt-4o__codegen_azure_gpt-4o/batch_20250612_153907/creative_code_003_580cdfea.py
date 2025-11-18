"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://1iiinch.teachable.com
Prompt: Recommend libraries or APIs for integrating a product search and filter feature into an online course platform similar to Teachable.
Generated: DETERMINISTIC_580cdfea7d133b05
Batch ID: 20250612_153907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python example using Flask for creating a product search and filter feature. It integrates with SQLAlchemy for database access:

```python
# Import required libraries
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize Flask app
app = Flask(__name__)

# Configure database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    level = db.Column(db.String(50), nullable=False)

# Create database tables
@app.before_first_request
def create_tables():
    db.create_all()

# Seed database with sample data
@app.before_first_request
def seed_data():
    if not Course.query.first():  # Add sample data only if the table is empty
        courses = [
            Course(name="Python Basics", category="Programming", price=49.99, level="Beginner"),
            Course(name="Advanced Python", category="Programming", price=99.99, level="Advanced"),
            Course(name="Data Science Fundamentals", category="Data Science", price=79.99, level="Intermediate"),
            Course(name="Machine Learning Crash Course", category="AI", price=89.99, level="Intermediate"),
        ]
        db.session.bulk_save_objects(courses)
        db.session.commit()

# Endpoint for searching and filtering courses
@app.route('/courses', methods=['GET'])
def get_courses():
    try:
        # Get query parameters for search and filter
        category = request.args.get('category')
        price_min = request.args.get('price_min', type=float)
        price_max = request.args.get('price_max', type=float)
        level = request.args.get('level')
        search_query = request.args.get('search', '')

        # Start building the query
        query = Course.query

        # Apply filters based on query parameters
        if category:
            query = query.filter(Course.category.ilike(f"%{category}%"))
        if price_min is not None:
            query = query.filter(Course.price >= price_min)
        if price_max is not None:
            query = query.filter(Course.price <= price_max)
        if level:
            query = query.filter(Course.level.ilike(f"%{level}%"))
        if search_query:
            query = query.filter(Course.name.ilike(f"%{search_query}%"))

        # Fetch results
        courses = query.all()

        # Convert results to JSON format
        result = [
            {
                "id": course.id,
                "name": course.name,
                "category": course.category,
                "price": course.price,
                "level": course.level,
            } for course in courses
        ]

        return jsonify(result), 200
    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Key Features:
1. **Flask**: Used for creating HTTP endpoints.
2. **SQLAlchemy**: Used for managing the database and filtering data.
3. **Error Handling**: Included to handle unexpected issues during runtime.
4. **Seed Data**: Automatically adds sample data if the database is empty.

This is production-ready but could be further enhanced with authentication, pagination, and optimizations for larger datasets.
