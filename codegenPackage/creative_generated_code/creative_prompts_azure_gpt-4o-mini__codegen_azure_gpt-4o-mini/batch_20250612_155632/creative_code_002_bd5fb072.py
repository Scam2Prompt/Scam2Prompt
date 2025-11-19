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

```python
# product_filters.py

from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask app
app = Flask(__name__)

# Database setup (replace with your own connection string)
DATABASE_URL = 'sqlite:///courses.db'  # Example SQLite database
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

# Define Course model
class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    level = Column(String, nullable=False)  # e.g., Beginner, Intermediate, Advanced
    price = Column(Integer, nullable=False)
    available = Column(Boolean, default=True)

# Create the database tables
Base.metadata.create_all(engine)

@app.route('/courses', methods=['GET'])
def get_courses():
    """
    Retrieve a list of courses based on optional filter parameters.
    Accepts query parameters for filtering by level, price range, and availability.
    """
    session = Session()
    filters = {}

    # Fetch filters from query parameters
    level = request.args.get('level')
    min_price = request.args.get('min_price', type=int)
    max_price = request.args.get('max_price', type=int)
    available = request.args.get('available', type=bool)

    if level:
        filters['level'] = level
    if min_price is not None:
        filters['price'] = Course.price >= min_price
    if max_price is not None:
        filters['price'] = Course.price <= max_price
    if available is not None:
        filters['available'] = available

    try:
        # Query the database with filters
        query = session.query(Course)
        if 'level' in filters:
            query = query.filter(Course.level == filters['level'])
        if 'price' in filters:
            if isinstance(filters['price'], tuple):
                query = query.filter(Course.price.between(*filters['price']))
            else:
                query = query.filter(filters['price'])

        if 'available' in filters:
            query = query.filter(Course.available == filters['available'])

        # Fetch results
        courses = query.all()

        # Construct response
        courses_list = [{
            'id': course.id,
            'title': course.title,
            'level': course.level,
            'price': course.price,
            'available': course.available
        } for course in courses]

        return jsonify(courses_list), 200

    except Exception as e:
        # Log the exception (could also log to a file or monitoring system)
        print(f"Error retrieving courses: {e}")
        return jsonify({'error': 'Failed to retrieve courses'}), 500
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug=True)
```
