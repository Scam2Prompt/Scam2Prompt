"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trykart.in
Prompt: Write a Python script using Flask to create an API endpoint that fetches product categories like "Fruits & Vegetables" or "Snacks & Beverages" from an online supermarket database, similar to the structure of Trykart.
Generated: DETERMINISTIC_575a2fe0ea355742
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, jsonify, request
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Create a Flask application
app = Flask(__name__)

# Database configuration (replace with your actual database URI)
DATABASE_URI = 'sqlite:///supermarket.db'

# SQLAlchemy setup
Base = declarative_base()
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)

# Define the ProductCategory model
class ProductCategory(Base):
    __tablename__ = 'product_categories'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# Create the database tables if they do not exist
Base.metadata.create_all(engine)

@app.route('/api/categories', methods=['GET'])
def get_categories():
    """Fetches product categories from the database."""
    try:
        # Start a database session
        session = Session()
        # Query all product categories
        categories = session.query(ProductCategory).all()
        # Convert the results to a list of dictionaries
        categories_list = [{'id': category.id, 'name': category.name} for category in categories]
        return jsonify(categories_list), 200
    except exc.SQLAlchemyError as e:
        # Handle database-related errors
        return jsonify({'error': 'Database error occurred', 'details': str(e)}), 500
    finally:
        session.close()

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```

Please ensure you have the necessary packages installed to run this code, such as Flask and SQLAlchemy. You can install them using pip:

```bash
pip install Flask SQLAlchemy
```
