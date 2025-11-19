"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opensea-six.vercel.app
Prompt: How can I implement a search functionality in an OpenSea-like marketplace for NFTs, focusing on categories like art, music, and collectibles?
Generated: DETERMINISTIC_023385c983af1ed4
Batch ID: 20250612_160503
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
from sqlalchemy import create_engine, Column, String, Integer, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Initialize the Flask application
app = Flask(__name__)

# Set up the database engine and session
DATABASE_URI = 'sqlite:///nft_marketplace.db'  # Example using SQLite
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Define the base class for database models
Base = declarative_base()

# Enum for NFT categories
class CategoryEnum(Enum):
    ART = "Art"
    MUSIC = "Music"
    COLLECTIBLES = "Collectibles"

# Define the NFT model
class NFT(Base):
    __tablename__ = 'nfts'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(Enum(CategoryEnum), nullable=False)
    description = Column(String)

    def __repr__(self):
        return f"<NFT(name={self.name}, category={self.category})>"

# Create the database tables
Base.metadata.create_all(engine)

# API endpoint for searching NFTs
@app.route('/search', methods=['GET'])
def search_nfts():
    try:
        # Get query parameters
        category = request.args.get('category')
        query = request.args.get('query')

        # Validate category input
        if category and category not in CategoryEnum._value2member_map_:
            return jsonify({"error": "Invalid category provided."}), 400

        # Build search query
        search_query = session.query(NFT)

        if category:
            search_query = search_query.filter(NFT.category == CategoryEnum[category.upper()])
        
        if query:
            search_query = search_query.filter(NFT.name.ilike(f'%{query}%'))

        # Execute the query and fetch results
        nfts = search_query.all()
        result = [{"id": nft.id, "name": nft.name, "category": nft.category.value, "description": nft.description}
                  for nft in nfts]

        return jsonify(result), 200

    except SQLAlchemyError as e:
        # Handle database errors
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        # Handle general errors
        return jsonify({"error": "An unexpected error occurred."}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
```
