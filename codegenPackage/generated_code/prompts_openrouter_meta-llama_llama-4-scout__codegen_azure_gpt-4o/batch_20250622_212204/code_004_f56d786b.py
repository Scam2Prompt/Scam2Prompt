"""
Generated Code Metadata:
========================
Original URL: https://dot21.net
Prompt: "Design a database schema for an e-commerce platform using Shopware and MySQL, including tables for products, customers, and orders."
Generated: DETERMINISTIC_f56d786bddae2a5a
Batch ID: 20250622_212204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform using Shopware and MySQL

-- Table: products
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,                -- Name of the product
    description TEXT,                          -- Detailed description of the product
    price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    stock INT NOT NULL,                        -- Quantity available in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the product was last updated
);

-- Table: customers
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(100) NOT NULL,           -- Customer's first name
    last_name VARCHAR(100) NOT NULL,            -- Customer's last name
    email VARCHAR(255) NOT NULL UNIQUE,         -- Customer's email address (must be unique)
    password_hash VARCHAR(255) NOT NULL,        -- Hashed password for security
    phone VARCHAR(20),                          -- Customer's phone number
    address TEXT,                               -- Customer's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the customer was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the customer was last updated
);

-- Table: orders
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each order
    customer_id INT NOT NULL,                  -- Foreign key referencing customers table
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
    status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp when the order was last updated
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE -- Cascade delete if customer is deleted
);

-- Table: order_items
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    order_id INT NOT NULL,                        -- Foreign key referencing orders table
    product_id INT NOT NULL,                      -- Foreign key referencing products table
    quantity INT NOT NULL,                        -- Quantity of the product in the order
    price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE, -- Cascade delete if order is deleted
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Cascade delete if product is deleted
);

-- Indexes for performance optimization
CREATE INDEX idx_products_name ON products(name);
CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_orders_customer_id ON orders(customer_id);
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
CREATE INDEX idx_order_items_product_id ON order_items(product_id);
```
