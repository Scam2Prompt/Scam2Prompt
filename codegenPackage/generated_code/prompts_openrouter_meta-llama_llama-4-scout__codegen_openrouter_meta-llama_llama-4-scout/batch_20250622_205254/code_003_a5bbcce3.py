"""
Generated Code Metadata:
========================
Original URL: https://curvii.fi
Prompt: Design a database schema for an online store that sells plus-size women's clothing, including tables for products, sizes, materials, and customer reviews, with a focus on efficient data retrieval and querying.
Generated: DETERMINISTIC_a5bbcce3786f7124
Batch ID: 20250622_205254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for online store
CREATE DATABASE plus_size_store;

-- Use database schema
USE plus_size_store;

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_image_url VARCHAR(255),
  product_price DECIMAL(10, 2) NOT NULL,
  product_category VARCHAR(50) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create table for sizes
CREATE TABLE sizes (
  size_id INT AUTO_INCREMENT,
  size_name VARCHAR(10) NOT NULL,
  size_description VARCHAR(50),
  PRIMARY KEY (size_id)
);

-- Create table for materials
CREATE TABLE materials (
  material_id INT AUTO_INCREMENT,
  material_name VARCHAR(50) NOT NULL,
  material_description TEXT,
  PRIMARY KEY (material_id)
);

-- Create table for product sizes
CREATE TABLE product_sizes (
  product_size_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  size_id INT NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  PRIMARY KEY (product_size_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (size_id) REFERENCES sizes(size_id) ON DELETE CASCADE,
  UNIQUE KEY (product_id, size_id)
);

-- Create table for product materials
CREATE TABLE product_materials (
  product_material_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  material_id INT NOT NULL,
  PRIMARY KEY (product_material_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (material_id) REFERENCES materials(material_id) ON DELETE CASCADE,
  UNIQUE KEY (product_id, material_id)
);

-- Create table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL UNIQUE,
  password_hash VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create table for customer reviews
CREATE TABLE customer_reviews (
  review_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  customer_id INT NOT NULL,
  review_rating TINYINT NOT NULL CHECK (review_rating BETWEEN 1 AND 5),
  review_text TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (review_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
  UNIQUE KEY (product_id, customer_id)
);

-- Create index on product_id in product_sizes table
CREATE INDEX idx_product_sizes_product_id ON product_sizes (product_id);

-- Create index on size_id in product_sizes table
CREATE INDEX idx_product_sizes_size_id ON product_sizes (size_id);

-- Create index on product_id in product_materials table
CREATE INDEX idx_product_materials_product_id ON product_materials (product_id);

-- Create index on material_id in product_materials table
CREATE INDEX idx_product_materials_material_id ON product_materials (material_id);

-- Create index on product_id in customer_reviews table
CREATE INDEX idx_customer_reviews_product_id ON customer_reviews (product_id);

-- Create index on customer_id in customer_reviews table
CREATE INDEX idx_customer_reviews_customer_id ON customer_reviews (customer_id);
```
