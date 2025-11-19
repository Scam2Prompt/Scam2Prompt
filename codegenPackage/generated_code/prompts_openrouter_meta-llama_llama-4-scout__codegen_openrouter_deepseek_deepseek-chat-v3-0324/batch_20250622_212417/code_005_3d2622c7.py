"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Design a database schema for an e-commerce platform that manages products, orders, and customers for a business like PureKana or skyMD, with SQL code for data insertion and querying.
Generated: DETERMINISTIC_3d2622c74a47fc95
Batch ID: 20250622_212417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for e-commerce platform

-- Create database
CREATE DATABASE ecommerce_platform;
USE ecommerce_platform;

-- Customers table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    address_line1 VARCHAR(100),
    address_line2 VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    country VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    is_active BOOLEAN DEFAULT TRUE
);

-- Products table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    sku VARCHAR(50) UNIQUE NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    category VARCHAR(50),
    image_url VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Orders table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_amount DECIMAL(10, 2) NOT NULL,
    status ENUM('pending', 'processing', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
    shipping_address TEXT NOT NULL,
    billing_address TEXT NOT NULL,
    payment_method VARCHAR(50) NOT NULL,
    tracking_number VARCHAR(100),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Order items table
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Insert sample data

-- Insert customers
INSERT INTO customers (first_name, last_name, email, password_hash, phone, address_line1, city, state, postal_code, country)
VALUES 
('John', 'Doe', 'john.doe@example.com', '$2a$10$xJwL5J8L6ZJ7V7V7V7V7Ve', '555-123-4567', '123 Main St', 'Los Angeles', 'CA', '90001', 'USA'),
('Jane', 'Smith', 'jane.smith@example.com', '$2a$10$xJwL5J8L6ZJ7V7V7V7V7Ve', '555-987-6543', '456 Oak Ave', 'New York', 'NY', '10001', 'USA');

-- Insert products
INSERT INTO products (name, description, sku, price, stock_quantity, category, image_url)
VALUES 
('CBD Oil 500mg', 'Premium CBD oil tincture', 'CBD-500-OIL', 49.99, 100, 'CBD Oils', '/images/cbd-oil-500.jpg'),
('CBD Gummies 30ct', 'Mixed fruit flavored CBD gummies', 'CBD-GUM-30', 29.99, 200, 'Edibles', '/images/cbd-gummies.jpg'),
('CBD Capsules 25mg', 'Easy-to-swallow CBD capsules', 'CBD-CAP-25', 39.99, 150, 'Capsules', '/images/cbd-capsules.jpg');

-- Insert orders
INSERT INTO orders (customer_id, total_amount, status, shipping_address, billing_address, payment_method)
VALUES 
(1, 79.98, 'processing', '123 Main St, Los Angeles, CA 90001', '123 Main St, Los Angeles, CA 90001', 'credit_card'),
(2, 49.99, 'pending', '456 Oak Ave, New York, NY 10001', '456 Oak Ave, New York, NY 10001', 'paypal');

-- Insert order items
INSERT INTO order_items (order_id, product_id, quantity, unit_price, subtotal)
VALUES 
(1, 1, 1, 49.99, 49.99),
(1, 2, 1, 29.99, 29.99),
(2, 1, 1, 49.99, 49.99);

-- Sample queries

-- Get all active products
SELECT * FROM products WHERE is_active = TRUE;

-- Get orders for a specific customer
SELECT o.order_id, o.order_date, o.total_amount, o.status 
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
WHERE c.email = 'john.doe@example.com';

-- Get order details with product information
SELECT oi.order_item_id, p.name, p.description, oi.quantity, oi.unit_price, oi.subtotal
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
WHERE oi.order_id = 1;

-- Get low stock products
SELECT name, stock_quantity 
FROM products 
WHERE stock_quantity < 10 AND is_active = TRUE;

-- Update product stock after order
UPDATE products 
SET stock_quantity = stock_quantity - 1 
WHERE product_id = 1;

-- Get total sales by product
SELECT p.name, SUM(oi.quantity) as total_quantity, SUM(oi.subtotal) as total_sales
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
GROUP BY p.name
ORDER BY total_sales DESC;
```
