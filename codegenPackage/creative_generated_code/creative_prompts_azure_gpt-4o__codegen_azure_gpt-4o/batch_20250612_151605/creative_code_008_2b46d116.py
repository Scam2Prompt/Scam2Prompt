"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.hu
Prompt: Create a REST API endpoint to fetch product details from an e-commerce database structured similarly to "Poly-Market.hu," including filtering by category and price range.
Generated: DETERMINISTIC_2b46d11635b06b92
Batch ID: 20250612_151605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, Integer, Float, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask app
app = Flask(__name__)

# Database Configuration
DATABASE_URL = "sqlite:///ecommerce.db"  # Replace with your database connection string
Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine)

# Product Model
class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)

# Ensure the table exists
Base.metadata.create_all(engine)

# REST API Endpoint to fetch product details with filters
@app.route('/products', methods=['GET'])
def fetch_products():
    """
    Endpoint to fetch product details with optional filters for category and price range.
    Query parameters:
        - category (str): Filter products by category.
        - min_price (float): Minimum price range.
        - max_price (float): Maximum price range.
    Returns:
        JSON response containing filtered product details.
    """
    try:
        # Get query parameters
        category = request.args.get('category', None)
        min_price = request.args.get('min_price', None)
        max_price = request.args.get('max_price', None)

        # Start a database session
        session = Session()
        query = session.query(Product)

        # Apply filters
        filters = []
        if category:
            filters.append(Product.category == category)
        if min_price:
            filters.append(Product.price >= float(min_price))
        if max_price:
            filters.append(Product.price <= float(max_price))
        if filters:
            query = query.filter(and_(*filters))

        # Fetch filtered products
        products = query.all()

        # Format the response
        result = [
            {"id": product.id, "name": product.name, "category": product.category, "price": product.price}
            for product in products
        ]

        # Close the session
        session.close()

        # Return JSON response
        return jsonify(result), 200
    except Exception as e:
        # Handle errors and return a proper message
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
