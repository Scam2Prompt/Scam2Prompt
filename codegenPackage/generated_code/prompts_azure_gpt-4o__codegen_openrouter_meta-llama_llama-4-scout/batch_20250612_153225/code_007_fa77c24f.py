"""
Generated Code Metadata:
========================
Original URL: https://tdkco.ir
Prompt: Write a database schema for storing product details, including categories, sizes, and warranty information, based on the diverse product offerings mentioned on the TDKCO website.
Generated: DETERMINISTIC_fa77c24f81ab91a6
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for product information
CREATE DATABASE product_database;

-- Use the product database
USE product_database;

-- Create a table for product categories
CREATE TABLE categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  category_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create a table for product sizes
CREATE TABLE sizes (
  size_id INT AUTO_INCREMENT,
  size_name VARCHAR(50) NOT NULL,
  size_description VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (size_id)
);

-- Create a table for product warranty information
CREATE TABLE warranties (
  warranty_id INT AUTO_INCREMENT,
  warranty_name VARCHAR(255) NOT NULL,
  warranty_description TEXT,
  warranty_duration INT,  -- in months
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (warranty_id)
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  category_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Create a table for product sizes mapping
CREATE TABLE product_sizes (
  product_id INT,
  size_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, size_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (size_id) REFERENCES sizes(size_id) ON DELETE CASCADE
);

-- Create a table for product warranty mapping
CREATE TABLE product_warranties (
  product_id INT,
  warranty_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id, warranty_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (warranty_id) REFERENCES warranties(warranty_id) ON DELETE CASCADE
);

-- Create indexes for faster queries
CREATE INDEX idx_category_id ON products(category_id);
CREATE INDEX idx_product_id ON product_sizes(product_id);
CREATE INDEX idx_size_id ON product_sizes(size_id);
CREATE INDEX idx_product_id_warranty ON product_warranties(product_id);
CREATE INDEX idx_warranty_id ON product_warranties(warranty_id);

-- Example insert statements
INSERT INTO categories (category_name, category_description)
VALUES ('Electronics', 'Electronic devices');

INSERT INTO sizes (size_name, size_description)
VALUES ('Small', 'Small size');

INSERT INTO warranties (warranty_name, warranty_description, warranty_duration)
VALUES ('1 Year', '1 year warranty', 12);

INSERT INTO products (product_name, product_description, category_id)
VALUES ('Smartphone', 'A smartphone', 1);

INSERT INTO product_sizes (product_id, size_id)
VALUES (1, 1);

INSERT INTO product_warranties (product_id, warranty_id)
VALUES (1, 1);
```
