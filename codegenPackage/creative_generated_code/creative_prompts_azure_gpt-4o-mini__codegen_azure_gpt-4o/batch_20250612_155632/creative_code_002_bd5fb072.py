"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbie-wall--extension-docs.teachable.com
Prompt: Can you provide code examples for integrating product filters in an online course platform like rabbie-wall--extension-docs's School?
Generated: DETERMINISTIC_bd5fb072dc96f326
Batch ID: 20250612_155632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the code example for integrating product filters in an online course platform using Python with Flask as the backend framework. The example assumes you have a database with course information and want to filter courses based on categories and difficulty levels.

```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, Integer, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask app
app = Flask(__name__)

# Database setup (SQLite for example purposes)
DATABASE_URL = "sqlite:///courses.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define the Course model
class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    difficulty = Column(String, nullable=False)

# Create database tables if not exist
Base.metadata.create_all(engine)

# Sample endpoint to filter courses
@app.route('/filter-courses', methods=['GET'])
def filter_courses():
    try:
        # Fetch query parameters
        category_filter = request.args.get('category')
        difficulty_filter = request.args.get('difficulty')

        # Build query dynamically based on filters
        query = session.query(Course)
        if category_filter:
            query = query.filter(Course.category == category_filter)
        if difficulty_filter:
            query = query.filter(Course.difficulty == difficulty_filter)

        # Execute query and fetch results
        filtered_courses = query.all()

        # Convert results to a JSON-friendly format
        courses_data = [
            {"id": course.id, "name": course.name, "category": course.category, "difficulty": course.difficulty}
            for course in filtered_courses
        ]

        # Return filtered courses as JSON response
        return jsonify(courses_data), 200

    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": str(e)}), 500

# Sample data insertion endpoint (for testing purposes)
@app.route('/add-course', methods=['POST'])
def add_course():
    try:
        # Parse course data from request body
        course_data = request.get_json()
        name = course_data.get("name")
        category = course_data.get("category")
        difficulty = course_data.get("difficulty")

        # Validate input data
        if not name or not category or not difficulty:
            return jsonify({"error": "Missing required fields"}), 400

        # Create new course instance
        new_course = Course(name=name, category=category, difficulty=difficulty)
        session.add(new_course)
        session.commit()

        # Respond with success message
        return jsonify({"message": "Course added successfully"}), 201

    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": str(e)}), 500

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
```

### Setup Instructions
1. Create a virtual environment and install Flask and SQLAlchemy:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install flask sqlalchemy
   ```

2. Run the server and test endpoints using tools such as Postman or curl.

3. Make sure to adapt the database URL (`DATABASE_URL`) and add authentication in the production environment.
