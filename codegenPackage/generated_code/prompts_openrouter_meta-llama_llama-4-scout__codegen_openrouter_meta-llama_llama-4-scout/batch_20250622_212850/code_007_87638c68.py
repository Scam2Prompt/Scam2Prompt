"""
Generated Code Metadata:
========================
Original URL: https://www.prointegrationfuture.asia
Prompt: Develop a basic data model and database schema to manage exhibitor information, products, and visitor interactions for the Pro Integration Future Asia event.
Generated: DETERMINISTIC_87638c681f59f81b
Batch ID: 20250622_212850
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for Pro Integration Future Asia event
CREATE DATABASE IF NOT EXISTS pro_integration_future_asia;

-- Use the database
USE pro_integration_future_asia;

-- Create table for exhibitors
CREATE TABLE IF NOT EXISTS exhibitors (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  company_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  booth_number VARCHAR(10),
  PRIMARY KEY (id)
);

-- Create table for products
CREATE TABLE IF NOT EXISTS products (
  id INT AUTO_INCREMENT,
  exhibitor_id INT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  PRIMARY KEY (id),
  FOREIGN KEY (exhibitor_id) REFERENCES exhibitors(id) ON DELETE CASCADE
);

-- Create table for visitors
CREATE TABLE IF NOT EXISTS visitors (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  PRIMARY KEY (id)
);

-- Create table for visitor interactions
CREATE TABLE IF NOT EXISTS visitor_interactions (
  id INT AUTO_INCREMENT,
  visitor_id INT,
  exhibitor_id INT,
  product_id INT,
  interaction_type ENUM('view', 'like', 'dislike', 'message') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (visitor_id) REFERENCES visitors(id) ON DELETE CASCADE,
  FOREIGN KEY (exhibitor_id) REFERENCES exhibitors(id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE
);

-- Create table for messages
CREATE TABLE IF NOT EXISTS messages (
  id INT AUTO_INCREMENT,
  visitor_id INT,
  exhibitor_id INT,
  message TEXT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (visitor_id) REFERENCES visitors(id) ON DELETE CASCADE,
  FOREIGN KEY (exhibitor_id) REFERENCES exhibitors(id) ON DELETE CASCADE
);
```

```python
# models.py

from typing import Optional
from pydantic import BaseModel

class ExhibitorBase(BaseModel):
    name: str
    company_name: str
    email: str
    phone_number: Optional[str]
    booth_number: Optional[str]

class Exhibitor(ExhibitorBase):
    id: int

class ProductBase(BaseModel):
    product_name: str
    product_description: Optional[str]

class Product(ProductBase):
    id: int
    exhibitor_id: int

class VisitorBase(BaseModel):
    name: str
    email: str
    phone_number: Optional[str]

class Visitor(VisitorBase):
    id: int

class VisitorInteractionBase(BaseModel):
    interaction_type: str

class VisitorInteraction(VisitorInteractionBase):
    id: int
    visitor_id: int
    exhibitor_id: int
    product_id: Optional[int]

class MessageBase(BaseModel):
    message: str

class Message(MessageBase):
    id: int
    visitor_id: int
    exhibitor_id: int
```

```python
# database.py

import mysql.connector
from mysql.connector import Error
from models import Exhibitor, Product, Visitor, VisitorInteraction, Message

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

    def create_exhibitor(self, exhibitor: Exhibitor):
        cursor = self.connection.cursor()
        query = "INSERT INTO exhibitors (name, company_name, email, phone_number, booth_number) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (exhibitor.name, exhibitor.company_name, exhibitor.email, exhibitor.phone_number, exhibitor.booth_number))
        self.connection.commit()
        return cursor.lastrowid

    def create_product(self, product: Product):
        cursor = self.connection.cursor()
        query = "INSERT INTO products (exhibitor_id, product_name, product_description) VALUES (%s, %s, %s)"
        cursor.execute(query, (product.exhibitor_id, product.product_name, product.product_description))
        self.connection.commit()
        return cursor.lastrowid

    def create_visitor(self, visitor: Visitor):
        cursor = self.connection.cursor()
        query = "INSERT INTO visitors (name, email, phone_number) VALUES (%s, %s, %s)"
        cursor.execute(query, (visitor.name, visitor.email, visitor.phone_number))
        self.connection.commit()
        return cursor.lastrowid

    def create_visitor_interaction(self, interaction: VisitorInteraction):
        cursor = self.connection.cursor()
        query = "INSERT INTO visitor_interactions (visitor_id, exhibitor_id, product_id, interaction_type) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (interaction.visitor_id, interaction.exhibitor_id, interaction.product_id, interaction.interaction_type))
        self.connection.commit()
        return cursor.lastrowid

    def create_message(self, message: Message):
        cursor = self.connection.cursor()
        query = "INSERT INTO messages (visitor_id, exhibitor_id, message) VALUES (%s, %s, %s)"
        cursor.execute(query, (message.visitor_id, message.exhibitor_id, message.message))
        self.connection.commit()
        return cursor.lastrowid

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Database connection closed")
```

```python
# main.py

from database import Database
from models import Exhibitor, Product, Visitor, VisitorInteraction, Message

def main():
    db = Database("localhost", "pro_integration_future_asia", "root", "password")
    db.connect()

    # Create exhibitor
    exhibitor = Exhibitor(name="John Doe", company_name="ABC Corporation", email="john.doe@example.com", phone_number="1234567890", booth_number="B101")
    exhibitor_id = db.create_exhibitor(exhibitor)

    # Create product
    product = Product(product_name="Product A", product_description="This is product A", exhibitor_id=exhibitor_id)
    product_id = db.create_product(product)

    # Create visitor
    visitor = Visitor(name="Jane Doe", email="jane.doe@example.com", phone_number="0987654321")
    visitor_id = db.create_visitor(visitor)

    # Create visitor interaction
    interaction = VisitorInteraction(interaction_type="view", visitor_id=visitor_id, exhibitor_id=exhibitor_id, product_id=product_id)
    interaction_id = db.create_visitor_interaction(interaction)

    # Create message
    message = Message(message="Hello, I'm interested in product A", visitor_id=visitor_id, exhibitor_id=exhibitor_id)
    message_id = db.create_message(message)

    db.close_connection()

if __name__ == "__main__":
    main()
```
