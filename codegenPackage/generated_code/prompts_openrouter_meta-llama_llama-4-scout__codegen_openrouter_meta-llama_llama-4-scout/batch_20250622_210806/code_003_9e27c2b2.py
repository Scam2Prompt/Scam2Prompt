"""
Generated Code Metadata:
========================
Original URL: https://icestyle.pl
Prompt: "Design a database schema for storing information about figure skating products, including categories, prices, and product descriptions, inspired by the IceStyle website."
Generated: DETERMINISTIC_9e27c2b214a04e9a
Batch ID: 20250622_210806
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/skate2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/skate1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/skate1-2.jpg": {
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
-- Create a database for figure skating products
CREATE DATABASE figure_skating_products;

-- Use the database
USE figure_skating_products;

-- Create a table for product categories
CREATE TABLE categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Create a table for product images
CREATE TABLE product_images (
  image_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  image_url VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (image_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for product reviews
CREATE TABLE product_reviews (
  review_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  rating TINYINT NOT NULL,
  review_text TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (review_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  CHECK (rating BETWEEN 1 AND 5)
);

-- Create a table for product variants
CREATE TABLE product_variants (
  variant_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  size VARCHAR(50) NOT NULL,
  color VARCHAR(50) NOT NULL,
  quantity INT NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (variant_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Insert sample data into categories table
INSERT INTO categories (category_name, description)
VALUES 
('Skates', 'Figure skating skates for men, women, and children'),
('Apparel', 'Figure skating clothing and accessories'),
('Accessories', 'Figure skating gloves, hats, and bags');

-- Insert sample data into products table
INSERT INTO products (category_id, product_name, description, price)
VALUES 
(1, 'Skate Model 1', 'High-performance figure skating skate', 200.00),
(1, 'Skate Model 2', 'Intermediate figure skating skate', 150.00),
(2, 'Skating Dress', 'Beautiful figure skating dress for competitions', 100.00);

-- Insert sample data into product_images table
INSERT INTO product_images (product_id, image_url)
VALUES 
(1, 'https://example.com/skate1.jpg'),
(1, 'https://example.com/skate1-2.jpg'),
(2, 'https://example.com/skate2.jpg');

-- Insert sample data into product_reviews table
INSERT INTO product_reviews (product_id, rating, review_text)
VALUES 
(1, 5, 'Excellent skate for advanced skaters'),
(1, 4, 'Good skate, but a bit stiff'),
(2, 5, 'Great value for the price');

-- Insert sample data into product_variants table
INSERT INTO product_variants (product_id, size, color, quantity)
VALUES 
(1, '8', 'Black', 5),
(1, '9', 'White', 3),
(2, '10', 'Black', 2);
```
