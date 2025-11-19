"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://knoxalliance-store.knoxalliance.com
Prompt: Generate a code snippet for an online shop that allows users to search for artists or artwork titles, similar to the functionality described on the Arts & Culture Alliance website.
Generated: DETERMINISTIC_721082b69e3bb7e2
Batch ID: 20250612_160618
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
from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Initialize Flask app
app = Flask(__name__)

# Database setup
DATABASE_URL = "sqlite:///art_shop.db"  # Replace with your production database URL
Base = declarative_base()

# Define the Artwork model
class Artwork(Base):
    __tablename__ = 'artworks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    artist = Column(String(100), nullable=False)  # Artist's name
    title = Column(String(200), nullable=False)  # Artwork title
    description = Column(Text, nullable=True)    # Artwork description

# Create database engine and session
engine = create_engine(DATABASE_URL, echo=False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Route for searching artworks by artist or title
@app.route('/search', methods=['GET'])
def search():
    """
    Search for artworks by artist or title.
    Query parameters:
        artist: Name of the artist (optional)
        title: Title of the artwork (optional)
    Returns:
        JSON response containing the matching artworks.
    """
    try:
        # Get query parameters
        artist_query = request.args.get('artist', '').strip().lower()
        title_query = request.args.get('title', '').strip().lower()
        
        # Build the query based on parameters
        query = session.query(Artwork)
        if artist_query:
            query = query.filter(Artwork.artist.ilike(f"%{artist_query}%"))
        if title_query:
            query = query.filter(Artwork.title.ilike(f"%{title_query}%"))
        
        # Execute the query and fetch results
        results = query.all()

        # Prepare JSON response
        response = [
            {
                "id": artwork.id,
                "artist": artwork.artist,
                "title": artwork.title,
                "description": artwork.description,
            }
            for artwork in results
        ]
        return jsonify({"success": True, "data": response}), 200
    
    except Exception as e:
        # Handle errors gracefully
        return jsonify({"success": False, "error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    # Only for development purposes, use a WSGI server like Gunicorn for production
    app.run(debug=True)
```
