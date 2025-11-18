"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adp-magiceden.lojaintegrada.com.br
Prompt: Write code to implement a search functionality for an e-commerce site that allows users to find items like "Apostila PREFEITURA DE BELO JARDIM PE 2025 Professor II Matemática" based on keywords and seller names.
Generated: DETERMINISTIC_b5a0c57546b2d858
Batch ID: 20250612_154946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.exc import SQLAlchemyError

# Setup Flask application
app = Flask(__name__)

# Setup SQLAlchemy
DATABASE_URL = "sqlite:///ecommerce.db"  # Use your preferred database URL
engine = create_engine(DATABASE_URL)
Session = scoped_session(sessionmaker(bind=engine))

# Define a base class for SQLAlchemy models
Base = declarative_base()

# Define a model for the items in the e-commerce database
class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    seller_name = Column(String, nullable=False)

# Create the table (if it doesn't exist)
Base.metadata.create_all(engine)

@app.route('/search', methods=['GET'])
def search_items():
    """
    Search for items based on keywords and seller names.
    
    Query Parameters:
    - query: A string containing keywords to search for in item names and seller names.
    
    Returns:
    - JSON response containing a list of matching items or an error message.
    """
    query = request.args.get('query', '').strip()
    
    if not query:
        return jsonify({'error': 'No search query provided.'}), 400

    session = Session()

    try:
        # Search for items that match the query in name or seller_name
        results = session.query(Item).filter(
            (Item.name.ilike(f'%{query}%')) | 
            (Item.seller_name.ilike(f'%{query}%'))
        ).all()

        # Prepare response data
        items = [{'id': item.id, 'name': item.name, 'seller_name': item.seller_name} for item in results]

        return jsonify({'items': items, 'count': len(items)}), 200
    
    except SQLAlchemyError as e:
        # Handle database errors gracefully
        session.rollback()  # Rollback in case of error
        return jsonify({'error': str(e)}), 500
    
    finally:
        session.close()  # Ensure session is closed
    
if __name__ == '__main__':
    app.run(debug=True)
```

This code snippet provides a fully functional search API for an e-commerce site using Flask and SQLAlchemy. Ensure to set up your database correctly and adjust the `DATABASE_URL` as necessary.
