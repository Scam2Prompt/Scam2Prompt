"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Design a database schema to store product information for an e-commerce store selling children's products, including tables for products, categories, and customer reviews.
Generated: DETERMINISTIC_9d397be497cde00a
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- schema.sql

-- Create database for e-commerce store
CREATE DATABASE ecommerce_store;

-- Use ecommerce_store database
USE ecommerce_store;

-- Create table for product categories
CREATE TABLE categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  category_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_price DECIMAL(10, 2) NOT NULL,
  product_image_url VARCHAR(255),
  category_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Create table for customer reviews
CREATE TABLE customer_reviews (
  review_id INT AUTO_INCREMENT,
  product_id INT,
  customer_name VARCHAR(255) NOT NULL,
  review_rating TINYINT NOT NULL,
  review_comment TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (review_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create index on category_id in products table
CREATE INDEX idx_category_id ON products(category_id);

-- Create index on product_id in customer_reviews table
CREATE INDEX idx_product_id ON customer_reviews(product_id);

-- Insert sample data into categories table
INSERT INTO categories (category_name, category_description)
VALUES 
('Toys', 'Toys for kids of all ages'),
('Books', 'Books for kids of all ages'),
('Clothing', 'Clothing for kids of all ages');

-- Insert sample data into products table
INSERT INTO products (product_name, product_description, product_price, product_image_url, category_id)
VALUES 
('Toy Car', 'A red toy car', 19.99, 'toy_car.jpg', 1),
('Kids Book', 'A fun book for kids', 9.99, 'kids_book.jpg', 2),
('Kids T-Shirt', 'A cool t-shirt for kids', 14.99, 'kids_tshirt.jpg', 3);

-- Insert sample data into customer_reviews table
INSERT INTO customer_reviews (product_id, customer_name, review_rating, review_comment)
VALUES 
(1, 'John Doe', 5, 'Great toy!'),
(2, 'Jane Doe', 4, 'Good book, but not perfect'),
(3, 'Bob Smith', 5, 'Comfortable and stylish');
```
