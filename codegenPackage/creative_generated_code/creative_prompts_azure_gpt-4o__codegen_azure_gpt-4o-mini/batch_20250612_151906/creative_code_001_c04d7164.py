"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blacksprut.shop
Prompt: Generate code to implement a secure search and filtering system for an e-commerce platform, similar to the advanced search panel described on Blacksprut.
Generated: DETERMINISTIC_c04d7164aa0cdd2b
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, Integer, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Initialize Flask application
app = Flask(__name__)

# Database configuration
DATABASE_URI = 'sqlite:///ecommerce.db'  # Update with your database URI
engine = create_engine(DATABASE_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define Product model for the database
class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    description = Column(String)

# Create database tables
Base.metadata.create_all(engine)

@app.route('/search', methods=['GET'])
def search_products():
    """Search for products based on query parameters."""
    session = Session()
    
    # Retrieving search parameters from request
    name = request.args.get('name')
    category = request.args.get('category')
    min_price = request.args.get('min_price', type=int)
    max_price = request.args.get('max_price', type=int)

    # Constructing query based on provided filters
    query = session.query(Product)
    
    if name:
        query = query.filter(Product.name.ilike(f'%{name}%'))  # Case-insensitive search for name
    if category:
        query = query.filter(Product.category == category)  # Exact match for category
    if min_price is not None:
        query = query.filter(Product.price >= min_price)  # Filter for minimum price
    if max_price is not None:
        query = query.filter(Product.price <= max_price)  # Filter for maximum price

    try:
        # Execute the query and fetch results
        products = query.all()
        results = [{
            'id': product.id,
            'name': product.name,
            'category': product.category,
            'price': product.price,
            'description': product.description
        } for product in products]
        
        return jsonify(results), 200  # Return results with a 200 OK status

    except SQLAlchemyError as e:
        session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500  # Return an error message with a 500 Internal Server Error

    finally:
        session.close()  # Ensure the session is closed after query execution

if __name__ == '__main__':
    app.run(debug=True)
```

### Notes
- Ensure you have `Flask` and `SQLAlchemy` installed in your environment.
- Modify the `DATABASE_URI` to connect to your production database.
- This code assumes the existence of a `products` table and is designed to provide a simple, secure search functionality with error handling.
