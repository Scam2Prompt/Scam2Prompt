"""
Generated Code Metadata:
========================
Original URL: https://3becard.com
Prompt: Design a basic database schema for an e-commerce platform focusing on fashion products, inspired by the categories on 3Bee Card.
Generated: DETERMINISTIC_4a98edde49756f15
Batch ID: 20250622_210038
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/womens-t-shirt.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/mens-jeans.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/womens-dress.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/womens-blouse.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/mens-t-shirt.jpg": {
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
CREATE DATABASE fashion_ecommerce;

-- Use the created database
USE fashion_ecommerce;

-- Create a table for product categories
CREATE TABLE categories (
  category_id INT AUTO_INCREMENT,
  category_name VARCHAR(255) NOT NULL,
  category_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (category_id)
);

-- Create a table for product subcategories
CREATE TABLE subcategories (
  subcategory_id INT AUTO_INCREMENT,
  category_id INT NOT NULL,
  subcategory_name VARCHAR(255) NOT NULL,
  subcategory_description TEXT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (subcategory_id),
  FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  subcategory_id INT NOT NULL,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  price DECIMAL(10, 2) NOT NULL,
  stock_quantity INT NOT NULL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id),
  FOREIGN KEY (subcategory_id) REFERENCES subcategories(subcategory_id) ON DELETE CASCADE
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

-- Create a table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255) NOT NULL,
  address VARCHAR(255),
  city VARCHAR(255),
  state VARCHAR(255),
  zip_code VARCHAR(255),
  country VARCHAR(255),
  phone_number VARCHAR(20),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create a table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total DECIMAL(10, 2) NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Create a table for order items
CREATE TABLE order_items (
  order_item_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_item_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
  FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create a table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  payment_method VARCHAR(50) NOT NULL,
  payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  amount DECIMAL(10, 2) NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  PRIMARY KEY (payment_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);
```

```sql
-- Insert sample data into categories table
INSERT INTO categories (category_name, category_description)
VALUES 
('Women', 'Fashion products for women'),
('Men', 'Fashion products for men'),
('Kids', 'Fashion products for kids');

-- Insert sample data into subcategories table
INSERT INTO subcategories (category_id, subcategory_name, subcategory_description)
VALUES 
(1, 'Tops', 'Tops for women'),
(1, 'Dresses', 'Dresses for women'),
(1, 'Bottoms', 'Bottoms for women'),
(2, 'Tops', 'Tops for men'),
(2, 'Bottoms', 'Bottoms for men');

-- Insert sample data into products table
INSERT INTO products (subcategory_id, product_name, product_description, price, stock_quantity)
VALUES 
(1, 'Women''s T-Shirt', 'A basic T-shirt for women', 19.99, 100),
(1, 'Women''s Blouse', 'A stylish blouse for women', 29.99, 50),
(2, 'Women''s Dress', 'A beautiful dress for women', 49.99, 20),
(4, 'Men''s T-Shirt', 'A basic T-shirt for men', 14.99, 150),
(5, 'Men''s Jeans', 'A pair of jeans for men', 39.99, 80);

-- Insert sample data into product_images table
INSERT INTO product_images (product_id, image_url)
VALUES 
(1, 'https://example.com/womens-t-shirt.jpg'),
(2, 'https://example.com/womens-blouse.jpg'),
(3, 'https://example.com/womens-dress.jpg'),
(4, 'https://example.com/mens-t-shirt.jpg'),
(5, 'https://example.com/mens-jeans.jpg');

-- Insert sample data into customers table
INSERT INTO customers (first_name, last_name, email, password_hash, address, city, state, zip_code, country, phone_number)
VALUES 
('John', 'Doe', 'john.doe@example.com', 'password_hash', '123 Main St', 'New York', 'NY', '10001', 'USA', '123-456-7890'),
('Jane', 'Doe', 'jane.doe@example.com', 'password_hash', '456 Park Ave', 'New York', 'NY', '10002', 'USA', '987-654-3210');

-- Insert sample data into orders table
INSERT INTO orders (customer_id, total)
VALUES 
(1, 19.99),
(1, 49.99),
(2, 14.99);

-- Insert sample data into order_items table
INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES 
(1, 1, 1, 19.99),
(2, 3, 1, 49.99),
(3, 4, 1, 14.99);

-- Insert sample data into payments table
INSERT INTO payments (order_id, payment_method, amount)
VALUES 
(1, 'Credit Card', 19.99),
(2, 'PayPal', 49.99),
(3, 'Credit Card', 14.99);
```
