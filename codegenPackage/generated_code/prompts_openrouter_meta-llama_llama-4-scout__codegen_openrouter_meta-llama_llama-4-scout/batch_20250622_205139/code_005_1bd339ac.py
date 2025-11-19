"""
Generated Code Metadata:
========================
Original URL: https://metmask.com
Prompt: "Design a database schema for a fishing gear e-commerce platform, including tables for products, prices, and customer information."
Generated: DETERMINISTIC_1bd339acbfb41372
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create a database for the fishing gear e-commerce platform
CREATE DATABASE fishing_gear_ecommerce;

-- Use the database
USE fishing_gear_ecommerce;

-- Create a table for customers
CREATE TABLE customers (
  customer_id INT AUTO_INCREMENT,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  phone_number VARCHAR(20),
  address VARCHAR(255),
  city VARCHAR(100),
  state VARCHAR(100),
  postal_code VARCHAR(20),
  country VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (customer_id)
);

-- Create a table for products
CREATE TABLE products (
  product_id INT AUTO_INCREMENT,
  product_name VARCHAR(255) NOT NULL,
  product_description TEXT,
  product_category VARCHAR(100) NOT NULL,
  product_subcategory VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (product_id)
);

-- Create a table for prices
CREATE TABLE prices (
  price_id INT AUTO_INCREMENT,
  product_id INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  discount DECIMAL(10, 2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (price_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create a table for orders
CREATE TABLE orders (
  order_id INT AUTO_INCREMENT,
  customer_id INT NOT NULL,
  order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  total DECIMAL(10, 2) NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (order_id),
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
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
  FOREIGN KEY (order_id) REFERENCES orders(order_id),
  FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Create a table for payments
CREATE TABLE payments (
  payment_id INT AUTO_INCREMENT,
  order_id INT NOT NULL,
  payment_method VARCHAR(100) NOT NULL,
  payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  amount DECIMAL(10, 2) NOT NULL,
  status VARCHAR(50) NOT NULL DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Create indexes on foreign key columns
CREATE INDEX idx_orders_customer_id ON orders (customer_id);
CREATE INDEX idx_order_items_order_id ON order_items (order_id);
CREATE INDEX idx_order_items_product_id ON order_items (product_id);
CREATE INDEX idx_payments_order_id ON payments (order_id);
CREATE INDEX idx_prices_product_id ON prices (product_id);
```

```sql
-- Insert sample data into the database
INSERT INTO customers (first_name, last_name, email, phone_number, address, city, state, postal_code, country)
VALUES 
('John', 'Doe', 'john.doe@example.com', '123-456-7890', '123 Main St', 'Anytown', 'CA', '12345', 'USA'),
('Jane', 'Doe', 'jane.doe@example.com', '987-654-3210', '456 Elm St', 'Othertown', 'NY', '67890', 'USA');

INSERT INTO products (product_name, product_description, product_category, product_subcategory)
VALUES 
('Fishing Rod', 'A medium action fishing rod', 'Fishing Rods', 'Spinning Rods'),
('Fishing Reel', 'A spinning fishing reel', 'Fishing Reels', 'Spinning Reels'),
('Lure', 'A soft plastic fishing lure', 'Lures', 'Soft Plastics');

INSERT INTO prices (product_id, price, discount)
VALUES 
(1, 99.99, 0.00),
(2, 49.99, 10.00),
(3, 5.99, 0.00);

INSERT INTO orders (customer_id, total)
VALUES 
(1, 100.00),
(2, 50.00);

INSERT INTO order_items (order_id, product_id, quantity, price)
VALUES 
(1, 1, 1, 99.99),
(2, 2, 1, 49.99);

INSERT INTO payments (order_id, payment_method, amount)
VALUES 
(1, 'Credit Card', 100.00),
(2, 'PayPal', 50.00);
```
