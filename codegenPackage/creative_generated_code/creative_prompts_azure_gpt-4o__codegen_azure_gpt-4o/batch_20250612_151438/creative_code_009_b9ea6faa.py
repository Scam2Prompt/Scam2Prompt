"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milarbrazw.blogspot.com
Prompt: Write code to implement a search functionality for an e-commerce site, allowing users to search for lighting products by name, category, or price range, as demonstrated in the site's "Busque por categorias" feature.
Generated: DETERMINISTIC_b9ea6faa0f57c06e
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, Float, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DATABASE_URL = "sqlite:///ecommerce.db"  # Use appropriate DB URL for your environment
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define the LightingProduct model
class LightingProduct(Base):
    __tablename__ = "lighting_products"
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    price = Column(Float, nullable=False)

# Create the database table if it doesn't exist
Base.metadata.create_all(engine)

@app.route('/search', methods=['GET'])
def search_lighting_products():
    """
    Endpoint to search for lighting products by name, category, or price range.
    Query parameters:
        - name (str): Product name to search for.
        - category (str): Product category to search for.
        - min_price (float): Minimum price for the search.
        - max_price (float): Maximum price for the search.
    Returns:
        - JSON response with the matching products.
    """
    try:
        # Extract query parameters
        name = request.args.get('name', type=str)
        category = request.args.get('category', type=str)
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)
        
        # Open a database session
        session = Session()
        
        # Build the base query
        query = session.query(LightingProduct)
        
        # Apply filters based on query parameters
        if name:
            query = query.filter(LightingProduct.name.ilike(f"%{name}%"))  # Case-insensitive pattern matching
        if category:
            query = query.filter(LightingProduct.category.ilike(f"%{category}%"))
        if min_price is not None:
            query = query.filter(LightingProduct.price >= min_price)
        if max_price is not None:
            query = query.filter(LightingProduct.price <= max_price)
        
        # Execute the query
        results = query.all()
        
        # Format the results as a list of dictionaries
        products = [
            {
                "id": product.id,
                "name": product.name,
                "category": product.category,
                "price": product.price
            }
            for product in results
        ]
        
        # Close the session
        session.close()
        
        # Return the results as JSON
        return jsonify(products=products), 200
    
    except Exception as e:
        # Handle errors gracefully and return a meaningful message
        return jsonify(error=str(e)), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
```
