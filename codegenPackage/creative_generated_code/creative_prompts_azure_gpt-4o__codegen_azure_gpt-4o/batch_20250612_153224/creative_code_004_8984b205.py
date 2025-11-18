"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamnhuavietkhanh.com
Prompt: Suggest tools or APIs to integrate a search functionality for Ecoplast furniture models, enabling users to find products like "Giường Nhựa Ecoplast – G010" or "Tủ Bếp Nhựa Ecoplast – TB008."
Generated: DETERMINISTIC_8984b20593fa7547
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Search Functionality for Ecoplast Furniture Models
This script demonstrates how to integrate a search functionality for furniture models from Ecoplast using a Flask API backed by an SQLite database.
"""

from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Flask app initialization
app = Flask(__name__)

# SQLAlchemy setup
DATABASE_URI = 'sqlite:///ecoplast_furniture.db'  # SQLite database URI
engine = create_engine(DATABASE_URI, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Furniture model definition
class Furniture(Base):
    __tablename__ = 'furniture'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    model_number = Column(String, nullable=False)
    description = Column(String)

# Create database tables if they don't exist
Base.metadata.create_all(engine)

# Sample data population (for demonstration purposes)
def populate_sample_data():
    sample_data = [
        Furniture(name="Giường Nhựa Ecoplast", model_number="G010", description="Durable plastic bed model G010"),
        Furniture(name="Tủ Bếp Nhựa Ecoplast", model_number="TB008", description="Stylish plastic kitchen cabinet model TB008")
    ]
    session.bulk_save_objects(sample_data)
    session.commit()

# Populate sample data if the table is empty
if not session.query(Furniture).first():
    populate_sample_data()

# Error message for invalid requests
INVALID_REQUEST_ERROR = {"error": "Invalid search query. Please provide a valid 'query' parameter."}

@app.route('/search', methods=['GET'])
def search_furniture():
    """
    Endpoint to search for Ecoplast furniture models.
    Accepts 'query' as a GET parameter for the search term.
    """
    query = request.args.get('query', None)
    
    # Validate query parameter
    if not query:
        return jsonify(INVALID_REQUEST_ERROR), 400

    # Perform a case-insensitive search in the database
    results = session.query(Furniture).filter(Furniture.name.ilike(f"%{query}%")).all()

    # Format the search results
    response = [{"id": item.id, "name": item.name, "model_number": item.model_number, "description": item.description} for item in results]

    # Return results or inform if no matches are found
    if response:
        return jsonify({"results": response})
    else:
        return jsonify({"message": "No matching furniture models found."}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

Note: Before deploying to production, remove debug mode (`debug=True`) and ensure proper database connection settings are configured.
