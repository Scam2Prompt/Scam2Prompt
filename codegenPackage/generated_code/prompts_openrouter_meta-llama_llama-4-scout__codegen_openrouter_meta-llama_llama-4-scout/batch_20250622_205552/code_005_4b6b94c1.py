"""
Generated Code Metadata:
========================
Original URL: https://registrations-arcium.hq.net
Prompt: Generate a SQL query to create a database schema for storing product information for Korean cosmetics, including product names, descriptions, and prices.
Generated: DETERMINISTIC_4b6b94c17519f9fe
Batch ID: 20250622_205552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database schema for storing product information for Korean cosmetics

-- Create database
CREATE DATABASE korean_cosmetics;

-- Use the database
USE korean_cosmetics;

-- Create table for product categories
CREATE TABLE product_categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (category_id)
);

-- Create table for product brands
CREATE TABLE product_brands (
  brand_id INT AUTO_INCREMENT,
  brand_name VARCHAR(255) NOT NULL,
  description TEXT,
  PRIMARY KEY (brand_id)
);

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  category_id INT,
  brand_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (category_id) REFERENCES product_categories(category_id),
  FOREIGN KEY (brand_id) REFERENCES product_brands(brand_id)
);

-- Create table for product images
CREATE TABLE product_images (
  image_id INT AUTO_INCREMENT,
  product_id INT,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (image_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create table for product reviews
CREATE TABLE product_reviews (
  review_id INT AUTO_INCREMENT,
  product_id INT,
  rating TINYINT NOT NULL,
  review_text TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (review_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create indexes for foreign keys
CREATE INDEX idx_category_id ON products(category_id);
CREATE INDEX idx_brand_id ON products(brand_id);
CREATE INDEX idx_product_id ON product_images(product_id);
CREATE INDEX idx_product_id_reviews ON product_reviews(product_id);
```
