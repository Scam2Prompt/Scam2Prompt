"""
Generated Code Metadata:
========================
Original URL: https://gematria.com
Prompt: Design a database schema to store information about dietary supplements, including product details, ingredients, and scientific research backing their efficacy, using a company like Gematria as a reference.
Generated: DETERMINISTIC_902b4fb84fe3fbfd
Batch ID: 20250622_211011
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for dietary supplements
CREATE DATABASE dietary_supplements;

-- Use the database
USE dietary_supplements;

-- Create table for products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  manufacturer VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for ingredients
CREATE TABLE ingredients (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create many-to-many relationship table for product ingredients
CREATE TABLE product_ingredients (
  product_id INT NOT NULL,
  ingredient_id INT NOT NULL,
  quantity DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, ingredient_id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
  FOREIGN KEY (ingredient_id) REFERENCES ingredients(id) ON DELETE CASCADE
);

-- Create table for scientific research
CREATE TABLE research (
  id INT AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  abstract TEXT,
  publication_date DATE,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create many-to-many relationship table for product research
CREATE TABLE product_research (
  product_id INT NOT NULL,
  research_id INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, research_id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE,
  FOREIGN KEY (research_id) REFERENCES research(id) ON DELETE CASCADE
);

-- Create table for study results
CREATE TABLE study_results (
  id INT AUTO_INCREMENT,
  research_id INT NOT NULL,
  result TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (research_id) REFERENCES research(id) ON DELETE CASCADE
);

-- Create table for dosages
CREATE TABLE dosages (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  recommended_daily_intake DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create table for labels
CREATE TABLE labels (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  label_name VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);
```

```python
# models.py
from sqlalchemy import create_engine, Column, Integer, String, Text, Date, DECIMAL, ForeignKey, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql+pymysql://user:password@localhost/dietary_supplements')
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    manufacturer = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))
    ingredients = relationship('Ingredient', secondary='product_ingredients')
    research = relationship('Research', secondary='product_research')

class Ingredient(Base):
    __tablename__ = 'ingredients'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))
    products = relationship('Product', secondary='product_ingredients')

class Research(Base):
    __tablename__ = 'research'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    abstract = Column(Text)
    publication_date = Column(Date)
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))
    products = relationship('Product', secondary='product_research')

class ProductIngredient(Base):
    __tablename__ = 'product_ingredients'
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    ingredient_id = Column(Integer, ForeignKey('ingredients.id'), primary_key=True)
    quantity = Column(DECIMAL(10, 2))
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))

class ProductResearch(Base):
    __tablename__ = 'product_research'
    product_id = Column(Integer, ForeignKey('products.id'), primary_key=True)
    research_id = Column(Integer, ForeignKey('research.id'), primary_key=True)
    created_at = Column(TIMESTAMP, default=TIMESTAMP('now'))
    updated_at = Column(TIMESTAMP, default=TIMESTAMP('now'), onupdate=TIMESTAMP('now'))

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
```

```python
# crud.py
from models import session, Product, Ingredient, Research

def create_product(name, description, manufacturer):
    try:
        product = Product(name=name, description=description, manufacturer=manufacturer)
        session.add(product)
        session.commit()
        return product
    except Exception as e:
        session.rollback()
        raise e

def create_ingredient(name, description):
    try:
        ingredient = Ingredient(name=name, description=description)
        session.add(ingredient)
        session.commit()
        return ingredient
    except Exception as e:
        session.rollback()
        raise e

def link_product_ingredient(product_id, ingredient_id, quantity):
    try:
        product_ingredient = ProductIngredient(product_id=product_id, ingredient_id=ingredient_id, quantity=quantity)
        session.add(product_ingredient)
        session.commit()
        return product_ingredient
    except Exception as e:
        session.rollback()
        raise e

def create_research(title, abstract, publication_date):
    try:
        research = Research(title=title, abstract=abstract, publication_date=publication_date)
        session.add(research)
        session.commit()
        return research
    except Exception as e:
        session.rollback()
        raise e

def link_product_research(product_id, research_id):
    try:
        product_research = ProductResearch(product_id=product_id, research_id=research_id)
        session.add(product_research)
        session.commit()
        return product_research
    except Exception as e:
        session.rollback()
        raise e
```
