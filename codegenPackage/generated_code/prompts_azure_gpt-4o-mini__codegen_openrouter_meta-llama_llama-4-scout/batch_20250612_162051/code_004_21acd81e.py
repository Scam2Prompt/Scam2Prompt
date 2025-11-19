"""
Generated Code Metadata:
========================
Original URL: https://galopinautomobile.fr
Prompt: Design a database schema for managing a collection of luxury vehicles, ensuring it captures essential details like model, condition, and investment value, reflecting the meticulous selection process at Galopin Automobile.
Generated: DETERMINISTIC_21acd81e7c29ac76
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for luxury vehicles
CREATE DATABASE galopin_automobile;

-- Use the database
USE galopin_automobile;

-- Create a table for vehicle manufacturers
CREATE TABLE manufacturers (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for vehicle models
CREATE TABLE models (
  id INT AUTO_INCREMENT,
  manufacturer_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (manufacturer_id) REFERENCES manufacturers(id) ON DELETE CASCADE
);

-- Create a table for vehicle conditions
CREATE TABLE conditions (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for vehicle listings
CREATE TABLE listings (
  id INT AUTO_INCREMENT,
  model_id INT NOT NULL,
  condition_id INT NOT NULL,
  investment_value DECIMAL(10, 2) NOT NULL,
  purchase_price DECIMAL(10, 2) NOT NULL,
  mileage INT NOT NULL,
  year INT NOT NULL,
  vin VARCHAR(17) NOT NULL UNIQUE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (model_id) REFERENCES models(id) ON DELETE CASCADE,
  FOREIGN KEY (condition_id) REFERENCES conditions(id) ON DELETE CASCADE
);

-- Create a table for vehicle features
CREATE TABLE features (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a many-to-many relationship table for listing features
CREATE TABLE listing_features (
  listing_id INT NOT NULL,
  feature_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (listing_id, feature_id),
  FOREIGN KEY (listing_id) REFERENCES listings(id) ON DELETE CASCADE,
  FOREIGN KEY (feature_id) REFERENCES features(id) ON DELETE CASCADE
);

-- Create a table for vehicle images
CREATE TABLE images (
  id INT AUTO_INCREMENT,
  listing_id INT NOT NULL,
  url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (listing_id) REFERENCES listings(id) ON DELETE CASCADE
);

-- Create a table for vehicle history
CREATE TABLE history (
  id INT AUTO_INCREMENT,
  listing_id INT NOT NULL,
  event VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (listing_id) REFERENCES listings(id) ON DELETE CASCADE
);
```

```python
# models.py

from sqlalchemy import create_engine, Column, Integer, String, Text, Decimal, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

engine = create_engine('mysql+pymysql://user:password@localhost/galopin_automobile')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    models = relationship('Model', backref='manufacturer')

class Model(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    manufacturer_id = Column(Integer, ForeignKey('manufacturers.id'), nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    listings = relationship('Listing', backref='model')

class Condition(Base):
    __tablename__ = 'conditions'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    listings = relationship('Listing', backref='condition')

class Listing(Base):
    __tablename__ = 'listings'
    id = Column(Integer, primary_key=True)
    model_id = Column(Integer, ForeignKey('models.id'), nullable=False)
    condition_id = Column(Integer, ForeignKey('conditions.id'), nullable=False)
    investment_value = Column(Decimal(10, 2), nullable=False)
    purchase_price = Column(Decimal(10, 2), nullable=False)
    mileage = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)
    vin = Column(String(17), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    features = relationship('Feature', secondary='listing_features', backref='listings')

class Feature(Base):
    __tablename__ = 'features'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey('listings.id'), nullable=False)
    url = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    listing_id = Column(Integer, ForeignKey('listings.id'), nullable=False)
    event = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)
```
