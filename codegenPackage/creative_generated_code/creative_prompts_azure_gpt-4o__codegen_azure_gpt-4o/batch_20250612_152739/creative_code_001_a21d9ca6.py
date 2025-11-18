"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bismillahgems.com
Prompt: Using the gemstone categories listed on the "Bismillah Gems" website (e.g., Aquamarine, Ruby, Sapphire), write code to create a searchable database of gemstones with attributes like weight, price, and availability.
Generated: DETERMINISTIC_a21d9ca61395180b
Batch ID: 20250612_152739
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
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Set up the Flask application
app = Flask(__name__)

# Database configuration
DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///gemstones.db')  # Default to SQLite if no env variable is set
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# Define the Gemstone model
class Gemstone(Base):
    __tablename__ = 'gemstones'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)  # Gemstone name (e.g., Ruby, Aquamarine)
    weight = Column(Float, nullable=False)  # Weight in carats
    price = Column(Float, nullable=False)  # Price in dollars
    available = Column(Boolean, default=True)  # Availability status

# Create the database tables
Base.metadata.create_all(engine)

# Route to add a new gemstone
@app.route('/add', methods=['POST'])
def add_gemstone():
    """
    Endpoint to add a new gemstone to the database.
    Requires 'name', 'weight', 'price', and 'available' fields in JSON request.
    """
    try:
        data = request.json
        # Validate input data
        if not all(key in data for key in ('name', 'weight', 'price', 'available')):
            return jsonify({'error': 'Missing required fields'}), 400

        gemstone = Gemstone(
            name=data['name'],
            weight=data['weight'],
            price=data['price'],
            available=data['available']
        )
        session = Session()
        session.add(gemstone)
        session.commit()
        session.close()

        return jsonify({'message': 'Gemstone added successfully', 'gemstone': data}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to search gemstones
@app.route('/search', methods=['GET'])
def search_gemstones():
    """
    Endpoint to search for gemstones by name, price, weight, or availability.
    Query parameters:
      - name: Filter by gemstone name
      - min_price: Filter by minimum price
      - max_price: Filter by maximum price
      - min_weight: Filter by minimum weight
      - max_weight: Filter by maximum weight
      - available: Filter by availability (true/false)
    """
    try:
        session = Session()
        query = session.query(Gemstone)

        # Apply filters based on query parameters
        name = request.args.get('name')
        if name:
            query = query.filter(Gemstone.name.ilike(f'%{name}%'))

        min_price = request.args.get('min_price', type=float)
        if min_price is not None:
            query = query.filter(Gemstone.price >= min_price)

        max_price = request.args.get('max_price', type=float)
        if max_price is not None:
            query = query.filter(Gemstone.price <= max_price)

        min_weight = request.args.get('min_weight', type=float)
        if min_weight is not None:
            query = query.filter(Gemstone.weight >= min_weight)

        max_weight = request.args.get('max_weight', type=float)
        if max_weight is not None:
            query = query.filter(Gemstone.weight <= max_weight)

        available = request.args.get('available', type=str)
        if available is not None:
            if available.lower() in ('true', 'false'):
                query = query.filter(Gemstone.available == (available.lower() == 'true'))

        gemstones = query.all()
        session.close()

        # Convert result to JSON-friendly format
        result = [
            {
                'id': g.id,
                'name': g.name,
                'weight': g.weight,
                'price': g.price,
                'available': g.available
            }
            for g in gemstones
        ]

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to update gemstone availability
@app.route('/update/<int:gemstone_id>', methods=['PUT'])
def update_availability(gemstone_id):
    """
    Endpoint to update availability of a gemstone.
    Requires 'available' field in JSON request.
    """
    try:
        data = request.json
        if 'available' not in data:
            return jsonify({'error': 'Missing required field: available'}), 400

        session = Session()
        gemstone = session.query(Gemstone).filter_by(id=gemstone_id).first()

        if not gemstone:
            return jsonify({'error': 'Gemstone not found'}), 404

        gemstone.available = data['available']
        session.commit()
        session.close()

        return jsonify({'message': 'Availability updated successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to delete a gemstone
@app.route('/delete/<int:gemstone_id>', methods=['DELETE'])
def delete_gemstone(gemstone_id):
    """
    Endpoint to delete a gemstone by ID.
    """
    try:
        session = Session()
        gemstone = session.query(Gemstone).filter_by(id=gemstone_id).first()

        if not gemstone:
            return jsonify({'error': 'Gemstone not found'}), 404

        session.delete(gemstone)
        session.commit()
        session.close()

        return jsonify({'message': 'Gemstone deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
