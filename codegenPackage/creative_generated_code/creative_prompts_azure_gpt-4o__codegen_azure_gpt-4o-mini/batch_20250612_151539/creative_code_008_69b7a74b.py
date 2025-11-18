"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://new.joss-home.com
Prompt: Develop a search functionality for an e-commerce site that allows users to find furniture items based on keywords like "дивани" or "ліжка," similar to the search feature on the Joss Home website.
Generated: DETERMINISTIC_69b7a74ba7c5971e
Batch ID: 20250612_151539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import List, Optional
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, Integer, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Initialize Flask application
app = Flask(__name__)

# Database setup
DATABASE_URL = "sqlite:///furniture.db"  # Use SQLite for simplicity
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = declarative_base()

# Define a Furniture model
class Furniture(Base):
    __tablename__ = 'furniture'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String)

# Create tables if they do not exist
Base.metadata.create_all(engine)

# Create a session factory
SessionFactory = sessionmaker(bind=engine)

@app.route('/search', methods=['GET'])
def search_furniture() -> jsonify:
    """
    Search for furniture items based on a query string.
    Accepts keyword search in the query parameter 'q'.
    
    Returns:
        JSON response containing matched furniture items.
    """
    query: Optional[str] = request.args.get('q')
    
    if not query:
        return jsonify({"error": "No search query provided."}), 400

    try:
        # Create a new session
        with SessionFactory() as session:
            results = session.query(Furniture).filter(
                or_(Furniture.name.ilike(f'%{query}%'), 
                    Furniture.description.ilike(f'%{query}%'))
            ).all()

            # Format results into a list of dictionaries
            items = [{'id': item.id, 'name': item.name, 'description': item.description} for item in results]

            return jsonify({"items": items}), 200
            
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
