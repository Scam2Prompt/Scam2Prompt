"""
Generated Code Metadata:
========================
Original URL: https://my-store-f9e36a.creator-spring.com
Prompt: Design a database schema for an e-commerce platform selling various products such as EthXY apparel, accessories, and drinkware, including details like product colors and prices.
Generated: DETERMINISTIC_8137f053397316b1
Batch ID: 20250622_204837
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/ethxy-t-shirt.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/ethxy-mug.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/ethxy-phone-case.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/ethxy-hoodie.jpg": {
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
-- Create a database for the e-commerce platform
CREATE DATABASE ecommerce_platform;

-- Use the ecommerce_platform database
USE ecommerce_platform;

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_type ENUM('apparel', 'accessories', 'drinkware') NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create a table for product colors
CREATE TABLE product_colors (
  color_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  color_name VARCHAR(50) NOT NULL,
  color_code VARCHAR(10) NOT NULL,
  PRIMARY KEY (color_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for product prices
CREATE TABLE product_prices (
  price_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  discount DECIMAL(10, 2) DEFAULT 0.00,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (price_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
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

-- Create a table for product variants
CREATE TABLE product_variants (
  variant_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  color_id INT NOT NULL,
  size VARCHAR(20) NOT NULL,
  quantity INT NOT NULL DEFAULT 0,
  PRIMARY KEY (variant_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (color_id) REFERENCES product_colors(color_id) ON DELETE CASCADE
);

-- Create a table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_name VARCHAR(255) NOT NULL,
  customer_email VARCHAR(100) NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total DECIMAL(10, 2) NOT NULL,
  status ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
  PRIMARY KEY (order_id)
);

-- Create a table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  variant_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
  FOREIGN KEY (variant_id) REFERENCES product_variants(variant_id) ON DELETE CASCADE
);

-- Insert sample data into products table
INSERT INTO products (product_name, product_description, product_type)
VALUES 
('EthXY T-Shirt', 'A high-quality EthXY t-shirt', 'apparel'),
('EthXY Hoodie', 'A warm and cozy EthXY hoodie', 'apparel'),
('EthXY Mug', 'A ceramic mug with EthXY design', 'drinkware'),
('EthXY Phone Case', 'A protective phone case with EthXY design', 'accessories');

-- Insert sample data into product_colors table
INSERT INTO product_colors (product_id, color_name, color_code)
VALUES 
(1, 'Black', '#000000'),
(1, 'White', '#FFFFFF'),
(2, 'Grey', '#808080'),
(3, 'Black', '#000000'),
(4, 'White', '#FFFFFF');

-- Insert sample data into product_prices table
INSERT INTO product_prices (product_id, price, discount)
VALUES 
(1, 19.99, 0.00),
(2, 29.99, 10.00),
(3, 14.99, 0.00),
(4, 24.99, 5.00);

-- Insert sample data into product_images table
INSERT INTO product_images (product_id, image_url)
VALUES 
(1, 'https://example.com/ethxy-t-shirt.jpg'),
(2, 'https://example.com/ethxy-hoodie.jpg'),
(3, 'https://example.com/ethxy-mug.jpg'),
(4, 'https://example.com/ethxy-phone-case.jpg');

-- Insert sample data into product_variants table
INSERT INTO product_variants (product_id, color_id, size, quantity)
VALUES 
(1, 1, 'S', 10),
(1, 1, 'M', 15),
(1, 2, 'S', 12),
(2, 3, 'M', 8),
(3, 1, '', 20),
(4, 2, '', 15);
```
