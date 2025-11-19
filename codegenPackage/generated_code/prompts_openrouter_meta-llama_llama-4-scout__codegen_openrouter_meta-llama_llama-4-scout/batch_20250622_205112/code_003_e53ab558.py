"""
Generated Code Metadata:
========================
Original URL: https://opticalize.com
Prompt: Design a simple database schema to store information about eyeglass and sunglass products, including details like frame type, material, and UV protection, inspired by Optic Alizé's product offerings.
Generated: DETERMINISTIC_e53ab55870dcf351
Batch ID: 20250622_205112
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/alize_rectangular_sunglasses.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/alize_wayfarer_eyeglasses.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/alize_aviator_sunglasses.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for eyeglass and sunglass products
CREATE DATABASE optic_alize;

-- Use the optic_alize database
USE optic_alize;

-- Create a table for frame types
CREATE TABLE frame_types (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for materials
CREATE TABLE materials (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for UV protection levels
CREATE TABLE uv_protections (
  id INT AUTO_INCREMENT,
  level VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
);

-- Create a table for eyeglass and sunglass products
CREATE TABLE products (
  id INT AUTO_INCREMENT,
  name VARCHAR(255) NOT NULL,
  frame_type_id INT NOT NULL,
  material_id INT NOT NULL,
  uv_protection_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (frame_type_id) REFERENCES frame_types(id),
  FOREIGN KEY (material_id) REFERENCES materials(id),
  FOREIGN KEY (uv_protection_id) REFERENCES uv_protections(id)
);

-- Create a table for product images
CREATE TABLE product_images (
  id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products(id)
);

-- Insert sample data into frame_types table
INSERT INTO frame_types (name, description)
VALUES
  ('Aviator', 'Classic aviator frame'),
  ('Wayfarer', 'Timeless wayfarer frame'),
  ('Rectangular', 'Modern rectangular frame');

-- Insert sample data into materials table
INSERT INTO materials (name, description)
VALUES
  ('Acetate', 'High-quality acetate material'),
  ('Stainless Steel', 'Durable stainless steel material'),
  ('Titanium', 'Lightweight titanium material');

-- Insert sample data into uv_protections table
INSERT INTO uv_protections (level, description)
VALUES
  ('UV400', 'Blocks 99-100% of UVA and UVB rays'),
  ('UV200', 'Blocks 95-98% of UVA and UVB rays'),
  ('None', 'No UV protection');

-- Insert sample data into products table
INSERT INTO products (name, frame_type_id, material_id, uv_protection_id, price, stock_quantity)
VALUES
  ('Alize Aviator Sunglasses', 1, 1, 1, 99.99, 100),
  ('Alize Wayfarer Eyeglasses', 2, 2, 2, 149.99, 50),
  ('Alize Rectangular Sunglasses', 3, 3, 1, 79.99, 200);

-- Insert sample data into product_images table
INSERT INTO product_images (product_id, image_url)
VALUES
  (1, 'https://example.com/alize_aviator_sunglasses.jpg'),
  (2, 'https://example.com/alize_wayfarer_eyeglasses.jpg'),
  (3, 'https://example.com/alize_rectangular_sunglasses.jpg');
```

```python
# optic_alize.py

import mysql.connector
from mysql.connector import Error

class OpticAlizeDatabase:
    def __init__(self, host, database, user, password):
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
            print("Connected to database successfully")
        except Error as e:
            print(f"Error connecting to database: {e}")

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Disconnected from database successfully")

    def get_products(self):
        try:
            cursor = self.connection.cursor()
            query = """
                SELECT p.id, p.name, ft.name AS frame_type, m.name AS material, up.level AS uv_protection, p.price, p.stock_quantity
                FROM products p
                JOIN frame_types ft ON p.frame_type_id = ft.id
                JOIN materials m ON p.material_id = m.id
                JOIN uv_protections up ON p.uv_protection_id = up.id
            """
            cursor.execute(query)
            products = cursor.fetchall()
            return products
        except Error as e:
            print(f"Error retrieving products: {e}")
            return []

# Example usage
if __name__ == "__main__":
    db = OpticAlizeDatabase('localhost', 'optic_alize', 'username', 'password')
    db.connect()
    products = db.get_products()
    for product in products:
        print(product)
    db.disconnect()
```
