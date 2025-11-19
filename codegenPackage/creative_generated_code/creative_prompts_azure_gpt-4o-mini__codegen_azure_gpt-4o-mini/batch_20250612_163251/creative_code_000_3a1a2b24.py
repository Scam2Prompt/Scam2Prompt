"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www-magiceden-marketplace-ar5-f.blogspot.com
Prompt: Generate a code snippet for a web application that allows users to search for tires by width, height, and rim size, similar to the functionality described on the GB Truck website.
Generated: DETERMINISTIC_3a1a2b24d5374227
Batch ID: 20250612_163251
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
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask app
app = Flask(__name__)

# Database configuration
DATABASE_URI = 'sqlite:///tires.db'  # SQLite database for demonstration
engine = create_engine(DATABASE_URI)
Base = declarative_base()

# Tire model for the database
class Tire(Base):
    __tablename__ = 'tires'
    id = Column(Integer, primary_key=True)
    width = Column(Integer, nullable=False)
    height = Column(Integer, nullable=False)
    rim_size = Column(Integer, nullable=False)

# Create the database tables
Base.metadata.create_all(engine)

# Create a new session
Session = sessionmaker(bind=engine)

@app.route('/search', methods=['GET'])
def search_tires():
    """
    Search for tires based on width, height, and rim size.
    Query parameters:
    - width (int): Width of the tire
    - height (int): Height of the tire
    - rim_size (int): Size of the rim
    Returns a JSON array of matching tires or an error message.
    """
    # Get search parameters from the request
    width = request.args.get('width', type=int)
    height = request.args.get('height', type=int)
    rim_size = request.args.get('rim_size', type=int)

    # Validate input parameters
    if width is None or height is None or rim_size is None:
        return jsonify({'error': 'All parameters (width, height, rim_size) are required.'}), 400

    # Create a new session to interact with the database
    session = Session()
    try:
        # Query the database for matching tires
        matching_tires = session.query(Tire).filter_by(width=width, height=height, rim_size=rim_size).all()

        # If no tires found, return an empty array
        if not matching_tires:
            return jsonify([]), 200

        # Prepare the response data
        tires_data = [{'id': tire.id, 'width': tire.width, 'height': tire.height, 'rim_size': tire.rim_size} for tire in matching_tires]
        return jsonify(tires_data), 200

    except Exception as e:
        # Handle unexpected errors and return an error message
        return jsonify({'error': str(e)}), 500
    
    finally:
        # Ensure the session is closed
        session.close()

if __name__ == '__main__':
    # Run the app in debug mode for development
    app.run(debug=True)
```
