"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xn--grsklippare-m8a.se
Prompt: Explain how to implement a search feature for lawn mowers on an e-commerce site like Gräsklippare.se, highlighting the importance of filtering by type and price.
Generated: DETERMINISTIC_50c9d69f3d50fd32
Batch ID: 20250612_163051
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
from sqlalchemy import create_engine, Column, Integer, String, Float, and_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask app
app = Flask(__name__)

# Database setup
DATABASE_URL = "sqlite:///lawn_mowers.db"  # Example SQLite database
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# Define a model for Lawn Mowers
class LawnMower(Base):
    __tablename__ = 'lawn_mowers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=False)
    price = Column(Float, nullable=False)

# Create the database tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/search', methods=['GET'])
def search_lawn_mowers():
    """
    Search for lawn mowers based on type and price range.
    
    Query Parameters:
    - type: str (optional) - The type of lawn mower to filter by.
    - min_price: float (optional) - The minimum price of the lawn mower.
    - max_price: float (optional) - The maximum price of the lawn mower.
    
    Returns:
    - JSON response containing the list of matching lawn mowers.
    """
    
    # Extract query parameters
    mower_type = request.args.get('type')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)

    # Build the query
    query = session.query(LawnMower)

    if mower_type:
        query = query.filter(LawnMower.type == mower_type)

    if min_price is not None:
        query = query.filter(LawnMower.price >= min_price)

    if max_price is not None:
        query = query.filter(LawnMower.price <= max_price)

    try:
        # Execute the query and retrieve results
        results = query.all()
        # Format results as a list of dictionaries
        lawn_mowers = [{
            'id': mower.id,
            'name': mower.name,
            'type': mower.type,
            'price': mower.price
        } for mower in results]

        return jsonify(lawn_mowers), 200  # Return 200 OK with results
    
    except Exception as e:
        # Handle any errors that occur during query execution
        return jsonify({'error': str(e)}), 500  # Return 500 Internal Server Error

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask application
```
