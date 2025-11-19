"""
Generated Code Metadata:
========================
Original URL: https://sevalcikolata.com
Prompt: Design a database schema for Seval Çikolata's order management system, including tables for customer information, order details, and product quantities.
Generated: DETERMINISTIC_bc74ec48e1c9875b
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database for Seval Çikolata's order management system
CREATE DATABASE seval_cikolata_oms;

-- Use the created database
USE seval_cikolata_oms;

-- Create table for customers
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (customer_id)
);

-- Create table for products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    product_description TEXT,
    unit_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id)
);

-- Create table for orders
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    total_cost DECIMAL(10, 2) NOT NULL,
    status ENUM('pending', 'shipped', 'delivered', 'cancelled') DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

-- Create table for order items
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (order_item_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create table for product quantities (inventory)
CREATE TABLE product_quantities (
    product_id INT NOT NULL,
    warehouse_id INT NOT NULL,
    quantity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id, warehouse_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create table for warehouses
CREATE TABLE warehouses (
    warehouse_id INT AUTO_INCREMENT,
    warehouse_name VARCHAR(100) NOT NULL,
    address VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (warehouse_id)
);
```

```sql
-- Example usage:

-- Insert a new customer
INSERT INTO customers (first_name, last_name, email, phone_number, address)
VALUES ('John', 'Doe', 'john.doe@example.com', '1234567890', '123 Main St');

-- Insert a new product
INSERT INTO products (product_name, product_description, unit_price)
VALUES ('Chocolate Bar', 'A delicious chocolate bar', 5.99);

-- Insert a new order
INSERT INTO orders (customer_id, total_cost)
VALUES (1, 11.98);

-- Insert order items
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (1, 1, 2, 5.99);

-- Insert a new warehouse
INSERT INTO warehouses (warehouse_name, address)
VALUES ('Main Warehouse', '456 Warehouse St');

-- Insert product quantity
INSERT INTO product_quantities (product_id, warehouse_id, quantity)
VALUES (1, 1, 100);
```
