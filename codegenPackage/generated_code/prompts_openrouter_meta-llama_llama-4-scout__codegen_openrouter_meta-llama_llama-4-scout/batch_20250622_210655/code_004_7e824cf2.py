"""
Generated Code Metadata:
========================
Original URL: https://saldiana.com.br
Prompt: "Design a database schema to store information about Sal Diana's products, including product lines (e.g., Linha Diana, Linha Apolo), product descriptions, and pricing information."
Generated: DETERMINISTIC_7e824cf291f4a081
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create a database for Sal Diana's products
CREATE DATABASE sal_diana;

-- Use the sal_diana database
USE sal_diana;

-- Create a table for product lines
CREATE TABLE product_lines (
  product_line_id INT AUTO_INCREMENT,
  product_line_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_line_id)
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_line_id INT NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (product_line_id) REFERENCES product_lines(product_line_id) ON DELETE CASCADE
);

-- Create a table for pricing information
CREATE TABLE pricing (
  pricing_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  currency VARCHAR(10) NOT NULL DEFAULT 'BRL',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (pricing_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for product variations (e.g., different sizes, colors)
CREATE TABLE product_variations (
  variation_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  variation_name VARCHAR(255) NOT NULL,
  variation_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (variation_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for variation pricing information
CREATE TABLE variation_pricing (
  variation_pricing_id INT AUTO_INCREMENT,
  variation_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  currency VARCHAR(10) NOT NULL DEFAULT 'BRL',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (variation_pricing_id),
  FOREIGN KEY (variation_id) REFERENCES product_variations(variation_id) ON DELETE CASCADE
);

-- Insert sample data
INSERT INTO product_lines (product_line_name, description)
VALUES
  ('Linha Diana', 'Description for Linha Diana'),
  ('Linha Apolo', 'Description for Linha Apolo');

INSERT INTO products (product_line_id, product_name, product_description)
VALUES
  (1, 'Product 1', 'Description for Product 1'),
  (1, 'Product 2', 'Description for Product 2'),
  (2, 'Product 3', 'Description for Product 3');

INSERT INTO pricing (product_id, price)
VALUES
  (1, 19.99),
  (2, 29.99),
  (3, 39.99);

INSERT INTO product_variations (product_id, variation_name, variation_description)
VALUES
  (1, 'Small', 'Small size'),
  (1, 'Large', 'Large size'),
  (2, 'Red', 'Red color');

INSERT INTO variation_pricing (variation_id, price)
VALUES
  (1, 19.99),
  (2, 24.99),
  (3, 29.99);
```
