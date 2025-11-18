"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://felixtrujillofalla.com
Prompt: Recommend a library or API for implementing advanced property search filters (e.g., price range, number of bedrooms, bathrooms, parking spaces) as seen on the Félix Trujillo Falla website, and provide example code for integrating it into a web application.
Generated: DETERMINISTIC_7d928da399145b96
Batch ID: 20250612_153224
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
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Database setup
DATABASE_URL = 'sqlite:///properties.db'
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Property model definition
class Property(Base):
    __tablename__ = 'properties'
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    bedrooms = Column(Integer, nullable=False)
    bathrooms = Column(Integer, nullable=False)
    parking_spaces = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"<Property(id={self.id}, price={self.price}, bedrooms={self.bedrooms}, bathrooms={self.bathrooms}, parking_spaces={self.parking_spaces})>"

# Create the database tables
Base.metadata.create_all(engine)

# Initialize Flask app
app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search_properties():
    """
    Search properties based on filters provided in the query parameters.
    Query parameters include price range, number of bedrooms, bathrooms, and parking spaces.
    """
    try:
        # Retrieve query parameters
        min_price = request.args.get('min_price', type=float)
        max_price = request.args.get('max_price', type=float)
        min_bedrooms = request.args.get('min_bedrooms', type=int)
        max_bedrooms = request.args.get('max_bedrooms', type=int)
        min_bathrooms = request.args.get('min_bathrooms', type=int)
        max_bathrooms = request.args.get('max_bathrooms', type=int)
        min_parking_spaces = request.args.get('min_parking_spaces', type=int)
        max_parking_spaces = request.args.get('max_parking_spaces', type=int)

        # Create a session to query the database
        session = Session()
        query = session.query(Property)

        # Apply filters based on provided parameters
        if min_price is not None:
            query = query.filter(Property.price >= min_price)
        if max_price is not None:
            query = query.filter(Property.price <= max_price)
        if min_bedrooms is not None:
            query = query.filter(Property.bedrooms >= min_bedrooms)
        if max_bedrooms is not None:
            query = query.filter(Property.bedrooms <= max_bedrooms)
        if min_bathrooms is not None:
            query = query.filter(Property.bathrooms >= min_bathrooms)
        if max_bathrooms is not None:
            query = query.filter(Property.bathrooms <= max_bathrooms)
        if min_parking_spaces is not None:
            query = query.filter(Property.parking_spaces >= min_parking_spaces)
        if max_parking_spaces is not None:
            query = query.filter(Property.parking_spaces <= max_parking_spaces)

        # Fetch the filtered results
        results = query.all()

        # Convert results to a list of dictionaries for JSON response
        properties = [{"id": p.id, "price": p.price, "bedrooms": p.bedrooms, 
                       "bathrooms": p.bathrooms, "parking_spaces": p.parking_spaces} for p in results]

        return jsonify(properties), 200

    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # Ensure session is closed
        session.close()

if __name__ == '__main__':
    app.run(debug=True)
```
