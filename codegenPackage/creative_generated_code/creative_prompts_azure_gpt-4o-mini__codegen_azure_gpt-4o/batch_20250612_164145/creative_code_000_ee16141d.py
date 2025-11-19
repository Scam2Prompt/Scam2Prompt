"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft.vip-tokyo.jp
Prompt: Generate a code snippet for a web application that allows artists to manage their digital art sales, including features for account creation and product listing as described on VIP Management's website.
Generated: DETERMINISTIC_ee16141d4b31911b
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Initialize the Flask app
app = Flask(__name__)

# Database configuration
DATABASE_URI = 'sqlite:///art_sales.db'  # For production, use a robust database
engine = create_engine(DATABASE_URI, echo=False)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Artist model
class Artist(Base):
    __tablename__ = 'artists'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(100), nullable=False, unique=True)
    password_hash = Column(String(200), nullable=False)
    artworks = relationship('Artwork', back_populates='artist')

# Artwork model
class Artwork(Base):
    __tablename__ = 'artworks'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(String(250), nullable=True)
    price = Column(Float, nullable=False)
    artist_id = Column(Integer, ForeignKey('artists.id'), nullable=False)
    artist = relationship('Artist', back_populates='artworks')

# Create all tables
Base.metadata.create_all(engine)

# Helper function for error response
def error_response(message, status_code=400):
    return jsonify({"error": message}), status_code

# Route for artist account creation
@app.route('/register', methods=['POST'])
def register_artist():
    try:
        data = request.json
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        # Validate input
        if not username or not email or not password:
            return error_response("All fields (username, email, password) are required.")
        
        # Check if the username or email already exists
        if session.query(Artist).filter((Artist.username == username) | (Artist.email == email)).first():
            return error_response("Username or email already exists.")
        
        # Hash the password
        password_hash = generate_password_hash(password)

        # Create artist account
        new_artist = Artist(username=username, email=email, password_hash=password_hash)
        session.add(new_artist)
        session.commit()
        return jsonify({"message": "Artist account created successfully."}), 201
    except Exception as e:
        return error_response(str(e), 500)

# Route for listing a new artwork
@app.route('/artworks', methods=['POST'])
def create_artwork():
    try:
        data = request.json
        artist_id = data.get('artist_id')
        title = data.get('title')
        description = data.get('description')
        price = data.get('price')

        # Validate input
        if not artist_id or not title or not price:
            return error_response("Artist ID, title, and price are required.")
        
        # Ensure price is valid
        try:
            price = float(price)
        except ValueError:
            return error_response("Invalid price format.")

        # Check if the artist exists
        artist = session.query(Artist).filter_by(id=artist_id).first()
        if not artist:
            return error_response("Artist does not exist.")

        # Create artwork listing
        new_artwork = Artwork(title=title, description=description, price=price, artist=artist)
        session.add(new_artwork)
        session.commit()
        return jsonify({"message": "Artwork listed successfully."}), 201
    except Exception as e:
        return error_response(str(e), 500)

# Route for retrieving all artworks for an artist
@app.route('/artists/<int:artist_id>/artworks', methods=['GET'])
def get_artist_artworks(artist_id):
    try:
        # Check if the artist exists
        artist = session.query(Artist).filter_by(id=artist_id).first()
        if not artist:
            return error_response("Artist does not exist.")

        # Fetch all artworks for the artist
        artworks = session.query(Artwork).filter_by(artist_id=artist_id).all()
        artworks_list = [
            {"id": artwork.id, "title": artwork.title, "description": artwork.description, "price": artwork.price}
            for artwork in artworks
        ]
        return jsonify({"artworks": artworks_list}), 200
    except Exception as e:
        return error_response(str(e), 500)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
```
