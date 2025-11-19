"""
Generated Code Metadata:
========================
Original URL: https://moinulalam.com
Prompt: Design a database schema for storing information about artworks, exhibitions, and artists, using Moinul Alam's portfolio as a reference.
Generated: DETERMINISTIC_f6905e416918d1d3
Batch ID: 20250622_204958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for artworks, exhibitions, and artists
# Designed with Moinul Alam's portfolio in mind

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Artist(Base):
    """Artist information table"""
    __tablename__ = 'artists'
    
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String(100), nullable=False)
    bio = sa.Column(sa.Text)
    birth_year = sa.Column(sa.Integer)
    nationality = sa.Column(sa.String(50))
    website = sa.Column(sa.String(255))
    email = sa.Column(sa.String(100))
    profile_image = sa.Column(sa.String(255))
    
    artworks = relationship("Artwork", back_populates="artist")
    exhibitions = relationship("Exhibition", secondary="artist_exhibition", back_populates="artists")

class Artwork(Base):
    """Artwork information table"""
    __tablename__ = 'artworks'
    
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(200), nullable=False)
    year = sa.Column(sa.Integer)
    medium = sa.Column(sa.String(100))
    dimensions = sa.Column(sa.String(100))
    description = sa.Column(sa.Text)
    image_url = sa.Column(sa.String(255))
    thumbnail_url = sa.Column(sa.String(255))
    artist_id = sa.Column(sa.Integer, sa.ForeignKey('artists.id'))
    
    artist = relationship("Artist", back_populates="artworks")
    exhibitions = relationship("Exhibition", secondary="artwork_exhibition", back_populates="artworks")

class Exhibition(Base):
    """Exhibition information table"""
    __tablename__ = 'exhibitions'
    
    id = sa.Column(sa.Integer, primary_key=True)
    title = sa.Column(sa.String(200), nullable=False)
    venue = sa.Column(sa.String(200))
    location = sa.Column(sa.String(200))
    start_date = sa.Column(sa.Date)
    end_date = sa.Column(sa.Date)
    description = sa.Column(sa.Text)
    cover_image = sa.Column(sa.String(255))
    
    artworks = relationship("Artwork", secondary="artwork_exhibition", back_populates="exhibitions")
    artists = relationship("Artist", secondary="artist_exhibition", back_populates="exhibitions")

class ArtworkExhibition(Base):
    """Many-to-many relationship between artworks and exhibitions"""
    __tablename__ = 'artwork_exhibition'
    
    artwork_id = sa.Column(sa.Integer, sa.ForeignKey('artworks.id'), primary_key=True)
    exhibition_id = sa.Column(sa.Integer, sa.ForeignKey('exhibitions.id'), primary_key=True)

class ArtistExhibition(Base):
    """Many-to-many relationship between artists and exhibitions"""
    __tablename__ = 'artist_exhibition'
    
    artist_id = sa.Column(sa.Integer, sa.ForeignKey('artists.id'), primary_key=True)
    exhibition_id = sa.Column(sa.Integer, sa.ForeignKey('exhibitions.id'), primary_key=True)

def create_database(engine):
    """Create all tables in the database"""
    Base.metadata.create_all(engine)
```
