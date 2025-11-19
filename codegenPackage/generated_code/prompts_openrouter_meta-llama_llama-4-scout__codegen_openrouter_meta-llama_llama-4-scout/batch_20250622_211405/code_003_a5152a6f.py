"""
Generated Code Metadata:
========================
Original URL: https://daddysoluniversity.com
Prompt: Design a database schema for an e-commerce platform specializing in books, manga, and literary supplies, ensuring efficient storage and retrieval of product information and customer orders.
Generated: DETERMINISTIC_a5152a6fbd545af7
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Create database schema for e-commerce platform
CREATE DATABASE literary_haven;

-- Use the created database
USE literary_haven;

-- Create table for products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT,
    product_type ENUM('book', 'manga', 'literary_supply') NOT NULL,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(100) NOT NULL,
    publisher VARCHAR(100) NOT NULL,
    publication_date DATE,
    price DECIMAL(10, 2) NOT NULL,
    stock_quantity INT NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (product_id)
);

-- Create table for product descriptions
CREATE TABLE product_descriptions (
    product_id INT NOT NULL,
    description TEXT,
    PRIMARY KEY (product_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create table for product images
CREATE TABLE product_images (
    image_id INT AUTO_INCREMENT,
    product_id INT NOT NULL,
    image_url VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (image_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create table for customers
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    address VARCHAR(255),
    city VARCHAR(50),
    state VARCHAR(50),
    zip_code VARCHAR(10),
    country VARCHAR(50),
    phone_number VARCHAR(20),
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (customer_id)
);

-- Create table for orders
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    total_cost DECIMAL(10, 2) NOT NULL,
    status ENUM('pending', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
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
    PRIMARY KEY (order_item_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Create table for payments
CREATE TABLE payments (
    payment_id INT AUTO_INCREMENT,
    order_id INT NOT NULL,
    payment_method ENUM('credit_card', 'paypal', 'bank_transfer') NOT NULL,
    payment_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    amount DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (payment_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

-- Create indexes for efficient querying
CREATE INDEX idx_products_product_type ON products (product_type);
CREATE INDEX idx_products_title ON products (title);
CREATE INDEX idx_orders_customer_id ON orders (customer_id);
CREATE INDEX idx_order_items_order_id ON order_items (order_id);
CREATE INDEX idx_order_items_product_id ON order_items (product_id);
```

```sql
-- Example usage:
-- Insert a new product
INSERT INTO products (product_type, title, author, publisher, publication_date, price, stock_quantity)
VALUES ('book', 'Example Book', 'John Doe', 'Example Publisher', '2022-01-01', 19.99, 10);

-- Insert a new customer
INSERT INTO customers (first_name, last_name, email, password_hash, address, city, state, zip_code, country, phone_number)
VALUES ('Jane', 'Doe', 'jane@example.com', 'password_hash', '123 Main St', 'Anytown', 'CA', '12345', 'USA', '123-456-7890');

-- Place a new order
INSERT INTO orders (customer_id, total_cost)
VALUES (1, 19.99);

-- Add order items to the order
INSERT INTO order_items (order_id, product_id, quantity, unit_price)
VALUES (1, 1, 1, 19.99);

-- Make a payment for the order
INSERT INTO payments (order_id, payment_method, amount)
VALUES (1, 'credit_card', 19.99);
```
