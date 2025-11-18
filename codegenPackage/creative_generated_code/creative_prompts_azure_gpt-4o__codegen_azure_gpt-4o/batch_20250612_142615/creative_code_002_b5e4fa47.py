"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbi-apps.teachable.com
Prompt: Recommend libraries or APIs for building an online course platform similar to rabbi-apps, and provide example code for integrating product filters.
Generated: DETERMINISTIC_b5e4fa47427b41e7
Batch ID: 20250612_142615
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
from sqlalchemy.exc import SQLAlchemyError
from flask_cors import CORS

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Configure the database (using SQLite for simplicity)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///courses.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define the Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique identifier for each course
    title = db.Column(db.String(100), nullable=False)  # Course title
    category = db.Column(db.String(50), nullable=False)  # Course category
    price = db.Column(db.Float, nullable=False)  # Course price
    level = db.Column(db.String(20), nullable=False)  # Course difficulty level

# Create database tables
with app.app_context():
    db.create_all()

# API route to fetch filtered courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    try:
        # Extract filter parameters from the query string
        category = request.args.get('category')  # Filter by category
        max_price = request.args.get('max_price', type=float)  # Filter by max price
        level = request.args.get('level')  # Filter by difficulty level

        # Build the query dynamically based on provided filters
        query = Course.query
        if category:
            query = query.filter_by(category=category)
        if max_price is not None:
            query = query.filter(Course.price <= max_price)
        if level:
            query = query.filter_by(level=level)
        
        # Execute the query
        courses = query.all()
        
        # Transform query results into a list of dictionaries for JSON response
        result = [
            {
                "id": course.id,
                "title": course.title,
                "category": course.category,
                "price": course.price,
                "level": course.level,
            }
            for course in courses
        ]
        
        # Return a JSON response with the filtered courses
        return jsonify(result), 200

    except SQLAlchemyError as e:
        # Handle database-related errors
        return jsonify({"error": "Database error occurred.", "message": str(e)}), 500

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "message": str(e)}), 500

# Sample data population route (not intended for production use)
@app.route('/api/populate', methods=['POST'])
def populate_data():
    try:
        # Example data for testing purposes
        example_data = [
            {"title": "Python Basics", "category": "Programming", "price": 19.99, "level": "Beginner"},
            {"title": "Advanced Python", "category": "Programming", "price": 49.99, "level": "Advanced"},
            {"title": "Machine Learning 101", "category": "Data Science", "price": 29.99, "level": "Beginner"},
            {"title": "Deep Learning Mastery", "category": "Data Science", "price": 59.99, "level": "Advanced"},
        ]
        
        # Add example data to the database
        for data in example_data:
            course = Course(**data)
            db.session.add(course)
        
        # Commit changes to the database
        db.session.commit()
        
        return jsonify({"message": "Example data populated successfully."}), 200

    except SQLAlchemyError as e:
        # Handle database-related errors
        return jsonify({"error": "Database error occurred.", "message": str(e)}), 500

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": "An unexpected error occurred.", "message": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```

---

### Recommended Libraries and APIs for Building Online Course Platforms:
1. **Flask**: Lightweight framework for building web applications.
2. **SQLAlchemy**: ORM for managing database interactions.
3. **Flask-CORS**: For handling CORS (Cross-Origin Resource Sharing).
4. **Stripe or PayPal API**: For payment processing.
5. **AWS S3 or Firebase Storage**: For storing course video content.

This code provides an example for integrating product filters (`category`, `price`, `level`) into an online course platform API built with Flask.
