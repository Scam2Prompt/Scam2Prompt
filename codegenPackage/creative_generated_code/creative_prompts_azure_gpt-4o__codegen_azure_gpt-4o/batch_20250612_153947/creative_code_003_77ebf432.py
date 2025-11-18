"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://medebooks.shop
Prompt: Write code to build a search functionality for an e-commerce site like medebooks.shop, allowing users to search for medical books and courses by title or category.
Generated: DETERMINISTIC_77ebf432a21b4e14
Batch ID: 20250612_153947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask application
app = Flask(__name__)

# Set up database configuration
DATABASE_URL = "sqlite:///medebooks.db"  # Use SQLite for simplicity; replace with production database
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

# Define the database model for items (books/courses)
class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    category = Column(String, nullable=False)

# Create database tables
Base.metadata.create_all(engine)

# Set up database session
Session = sessionmaker(bind=engine)
session = Session()

# Sample data to populate initially (for testing)
def seed_data():
    items = [
        Item(title="Advanced Medical Practices", category="Books"),
        Item(title="Fundamentals of Anatomy", category="Books"),
        Item(title="Medical Ethics Course", category="Courses"),
        Item(title="Surgical Techniques Course", category="Courses"),
    ]
    session.bulk_save_objects(items)
    session.commit()

# Uncomment the line below to seed the database initially
# seed_data()

# Define the search route
@app.route('/search', methods=['GET'])
def search_items():
    """
    Search for medical books and courses by title or category.
    Query parameters:
    - title: Partial or full title of the item (optional)
    - category: Category of the item (Books or Courses) (optional)
    Returns:
    - JSON response containing the matching items.
    """
    try:
        # Get query parameters
        title_query = request.args.get('title', '').lower()
        category_query = request.args.get('category', '').lower()

        # Build query dynamically based on provided parameters
        query = session.query(Item)

        if title_query:
            query = query.filter(Item.title.ilike(f"%{title_query}%"))  # Case-insensitive search
        if category_query:
            query = query.filter(Item.category.ilike(f"%{category_query}%"))  # Case-insensitive search

        # Execute the query and fetch results
        results = query.all()

        # Format results into JSON-friendly structure
        items = [
            {"id": item.id, "title": item.title, "category": item.category}
            for item in results
        ]

        return jsonify({"success": True, "data": items})

    except Exception as e:
        # Handle any errors gracefully
        return jsonify({"success": False, "error": str(e)}), 500

# Main entry point for the application
if __name__ == '__main__':
    app.run(debug=True)
```
