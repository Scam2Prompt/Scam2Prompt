"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mesogia.com
Prompt: Generate code to implement a search functionality for a directory website where users can search for businesses like "Ταπετσαρίες Αυτοκινήτων" by name, category, or city.
Generated: DETERMINISTIC_d9596589c4475b3b
Batch ID: 20250612_151044
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
DATABASE_URL = 'sqlite:///business_directory.db'  # Change this to your production database
Base = declarative_base()

# Define Business model
class Business(Base):
    __tablename__ = 'businesses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    city = Column(String, nullable=False)

# Initialize the database connection
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)  # Create tables if they don't exist
Session = sessionmaker(bind=engine)

# Route for search functionality
@app.route('/search', methods=['GET'])
def search_businesses():
    """
    Endpoint to search for businesses by name, category, or city.
    Query parameters (case-insensitive):
    - name: Name of the business
    - category: Category of the business
    - city: City where the business is located
    """
    try:
        # Extract query parameters
        name = request.args.get('name', '').strip().lower()
        category = request.args.get('category', '').strip().lower()
        city = request.args.get('city', '').strip().lower()

        # Create a new database session
        session = Session()

        # Query businesses based on filters
        query = session.query(Business)
        if name:
            query = query.filter(Business.name.ilike(f'%{name}%'))
        if category:
            query = query.filter(Business.category.ilike(f'%{category}%'))
        if city:
            query = query.filter(Business.city.ilike(f'%{city}%'))

        # Fetch the results
        results = query.all()

        # Format the response
        businesses = [
            {"id": business.id, "name": business.name, "category": business.category, "city": business.city}
            for business in results
        ]

        # Return the results as JSON
        return jsonify({"success": True, "data": businesses}), 200

    except Exception as e:
        # Handle errors and return appropriate response
        return jsonify({"success": False, "error": str(e)}), 500

    finally:
        # Ensure the session is closed
        session.close()

# Main entry point for running the application
if __name__ == '__main__':
    app.run(debug=True)
```
