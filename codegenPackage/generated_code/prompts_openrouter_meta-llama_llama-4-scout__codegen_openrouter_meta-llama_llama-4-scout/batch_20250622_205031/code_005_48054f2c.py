"""
Generated Code Metadata:
========================
Original URL: https://npaautocare.zouxiaodong.workers.dev
Prompt: Create a data model for storing information about NAPA Auto Care services, including service categories, prices, and descriptions, and suggest a database schema for managing this data.
Generated: DETERMINISTIC_48054f2c3f94d29b
Batch ID: 20250622_205031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for NAPA Auto Care services
CREATE DATABASE napa_auto_care;

-- Use the database
USE napa_auto_care;

-- Create table for service categories
CREATE TABLE service_categories (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create table for services
CREATE TABLE services (
  id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (category_id) REFERENCES service_categories(id) ON DELETE CASCADE
);

-- Create table for service prices history
CREATE TABLE service_prices_history (
  id INT AUTO_INCREMENT,
  service_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  effective_date DATE NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (service_id) REFERENCES services(id) ON DELETE CASCADE
);

-- Create indexes for better query performance
CREATE INDEX idx_services_category_id ON services (category_id);
CREATE INDEX idx_service_prices_history_service_id ON service_prices_history (service_id);
```

```python
# models.py

from typing import Optional
from pydantic import BaseModel
from datetime import datetime

class ServiceCategory(BaseModel):
    id: Optional[int]
    name: str
    description: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class Service(BaseModel):
    id: Optional[int]
    category_id: int
    name: str
    description: Optional[str]
    price: float
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True

class ServicePriceHistory(BaseModel):
    id: Optional[int]
    service_id: int
    price: float
    effective_date: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
```

```python
# database.py

import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self, host: str, database: str, user: str, password: str):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("Connected to database")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def execute_query(self, query: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            self.connection.commit()
            print("Query executed successfully")
        except Error as e:
            print(f"Error executing query: {e}")

    def fetch_data(self, query: str):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error fetching data: {e}")
```

```python
# main.py

from database import Database
from models import ServiceCategory, Service, ServicePriceHistory

def main():
    db = Database("localhost", "napa_auto_care", "root", "password")
    db.connect()

    # Create service category
    query = "INSERT INTO service_categories (name, description) VALUES ('Oil Change', 'Regular oil change service')"
    db.execute_query(query)

    # Create service
    query = "INSERT INTO services (category_id, name, description, price) VALUES (1, 'Synthetic Oil Change', 'Synthetic oil change service', 29.99)"
    db.execute_query(query)

    # Get all service categories
    query = "SELECT * FROM service_categories"
    categories = db.fetch_data(query)
    for category in categories:
        print(ServiceCategory(**dict(zip(["id", "name", "description", "created_at", "updated_at"], category))))

if __name__ == "__main__":
    main()
```
