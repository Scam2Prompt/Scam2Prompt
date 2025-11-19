"""
Generated Code Metadata:
========================
Original URL: https://azagros.com
Prompt: Create a database schema to store information about grain and fruit production, field mapping, and visit logs, ensuring compatibility with both web and mobile platforms as described on Azagros.
Generated: DETERMINISTIC_47a4a68bb43146a7
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database
CREATE DATABASE azagros_production;

-- Use database
USE azagros_production;

-- Create table for grain production
CREATE TABLE grain_production (
  id INT AUTO_INCREMENT,
  crop_name VARCHAR(255) NOT NULL,
  production_date DATE NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  unit VARCHAR(10) NOT NULL,
  field_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (field_id) REFERENCES fields(id)
);

-- Create table for fruit production
CREATE TABLE fruit_production (
  id INT AUTO_INCREMENT,
  fruit_name VARCHAR(255) NOT NULL,
  production_date DATE NOT NULL,
  quantity DECIMAL(10, 2) NOT NULL,
  unit VARCHAR(10) NOT NULL,
  field_id INT,
  PRIMARY KEY (id),
  FOREIGN KEY (field_id) REFERENCES fields(id)
);

-- Create table for fields
CREATE TABLE fields (
  id INT AUTO_INCREMENT,
  field_name VARCHAR(255) NOT NULL,
  field_type ENUM('grain', 'fruit') NOT NULL,
  location VARCHAR(255) NOT NULL,
  area DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for visit logs
CREATE TABLE visit_logs (
  id INT AUTO_INCREMENT,
  field_id INT NOT NULL,
  visit_date DATE NOT NULL,
  visit_type ENUM('inspection', 'maintenance') NOT NULL,
  notes TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (field_id) REFERENCES fields(id)
);

-- Create table for users
CREATE TABLE users (
  id INT AUTO_INCREMENT,
  username VARCHAR(255) NOT NULL,
  password VARCHAR(255) NOT NULL,
  role ENUM('admin', 'user') NOT NULL,
  PRIMARY KEY (id)
);

-- Create table for user visit logs
CREATE TABLE user_visit_logs (
  id INT AUTO_INCREMENT,
  user_id INT NOT NULL,
  visit_log_id INT NOT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES users(id),
  FOREIGN KEY (visit_log_id) REFERENCES visit_logs(id)
);

-- Indexes for efficient querying
CREATE INDEX idx_grain_production_field_id ON grain_production (field_id);
CREATE INDEX idx_fruit_production_field_id ON fruit_production (field_id);
CREATE INDEX idx_visit_logs_field_id ON visit_logs (field_id);
CREATE INDEX idx_user_visit_logs_user_id ON user_visit_logs (user_id);
CREATE INDEX idx_user_visit_logs_visit_log_id ON user_visit_logs (visit_log_id);
```

```python
# models.py
from sqlalchemy import create_engine, Column, Integer, String, Date, Enum, DECIMAL, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql+pymysql://user:password@localhost/azagros_production')
Base = declarative_base()

class GrainProduction(Base):
    __tablename__ = 'grain_production'
    id = Column(Integer, primary_key=True)
    crop_name = Column(String(255), nullable=False)
    production_date = Column(Date, nullable=False)
    quantity = Column(DECIMAL(10, 2), nullable=False)
    unit = Column(String(10), nullable=False)
    field_id = Column(Integer, ForeignKey('fields.id'))
    field = relationship('Field', backref='grain_productions')

class FruitProduction(Base):
    __tablename__ = 'fruit_production'
    id = Column(Integer, primary_key=True)
    fruit_name = Column(String(255), nullable=False)
    production_date = Column(Date, nullable=False)
    quantity = Column(DECIMAL(10, 2), nullable=False)
    unit = Column(String(10), nullable=False)
    field_id = Column(Integer, ForeignKey('fields.id'))
    field = relationship('Field', backref='fruit_productions')

class Field(Base):
    __tablename__ = 'fields'
    id = Column(Integer, primary_key=True)
    field_name = Column(String(255), nullable=False)
    field_type = Column(Enum('grain', 'fruit'), nullable=False)
    location = Column(String(255), nullable=False)
    area = Column(DECIMAL(10, 2), nullable=False)

class VisitLog(Base):
    __tablename__ = 'visit_logs'
    id = Column(Integer, primary_key=True)
    field_id = Column(Integer, ForeignKey('fields.id'), nullable=False)
    visit_date = Column(Date, nullable=False)
    visit_type = Column(Enum('inspection', 'maintenance'), nullable=False)
    notes = Column(Text)
    field = relationship('Field', backref='visit_logs')

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum('admin', 'user'), nullable=False)

class UserVisitLog(Base):
    __tablename__ = 'user_visit_logs'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    visit_log_id = Column(Integer, ForeignKey('visit_logs.id'), nullable=False)
    user = relationship('User', backref='user_visit_logs')
    visit_log = relationship('VisitLog', backref='user_visit_logs')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
```

```python
# main.py
from models import session, GrainProduction, FruitProduction, Field, VisitLog, User, UserVisitLog

def create_field(field_name, field_type, location, area):
    try:
        field = Field(field_name=field_name, field_type=field_type, location=location, area=area)
        session.add(field)
        session.commit()
        return field
    except Exception as e:
        session.rollback()
        print(f"Error creating field: {e}")

def create_grain_production(crop_name, production_date, quantity, unit, field_id):
    try:
        grain_production = GrainProduction(crop_name=crop_name, production_date=production_date, quantity=quantity, unit=unit, field_id=field_id)
        session.add(grain_production)
        session.commit()
        return grain_production
    except Exception as e:
        session.rollback()
        print(f"Error creating grain production: {e}")

def create_fruit_production(fruit_name, production_date, quantity, unit, field_id):
    try:
        fruit_production = FruitProduction(fruit_name=fruit_name, production_date=production_date, quantity=quantity, unit=unit, field_id=field_id)
        session.add(fruit_production)
        session.commit()
        return fruit_production
    except Exception as e:
        session.rollback()
        print(f"Error creating fruit production: {e}")

def create_visit_log(field_id, visit_date, visit_type, notes):
    try:
        visit_log = VisitLog(field_id=field_id, visit_date=visit_date, visit_type=visit_type, notes=notes)
        session.add(visit_log)
        session.commit()
        return visit_log
    except Exception as e:
        session.rollback()
        print(f"Error creating visit log: {e}")

def main():
    # Example usage
    field = create_field('Field 1', 'grain', 'Location 1', 100.0)
    grain_production = create_grain_production('Crop 1', '2022-01-01', 1000.0, 'kg', field.id)
    fruit_production = create_fruit_production('Fruit 1', '2022-01-01', 500.0, 'kg', field.id)
    visit_log = create_visit_log(field.id, '2022-01-01', 'inspection', 'Notes')

if __name__ == "__main__":
    main()
```
