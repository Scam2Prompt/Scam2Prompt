"""
Generated Code Metadata:
========================
Original URL: https://phantomdistro.com
Prompt: Design a simple database schema to store user information, product catalog, and order history for an e-commerce platform selling tobacco and vape products.
Generated: DETERMINISTIC_2293bc7f6c75521d
Batch ID: 20250622_211118
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform selling tobacco and vape products

-- Create a table to store user information
CREATE TABLE Users (
    user_id SERIAL PRIMARY KEY,          -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,    -- Unique email address for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store product catalog
CREATE TABLE Products (
    product_id SERIAL PRIMARY KEY,        -- Unique identifier for each product
    name VARCHAR(100) NOT NULL,           -- Name of the product
    description TEXT,                      -- Description of the product
    price DECIMAL(10, 2) NOT NULL,        -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0, -- Quantity available in stock
    category VARCHAR(50),                  -- Category of the product (e.g., tobacco, vape)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table to store order history
CREATE TABLE Orders (
    order_id SERIAL PRIMARY KEY,           -- Unique identifier for each order
    user_id INT NOT NULL,                  -- Foreign key referencing Users table
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL,  -- Total amount for the order
    status VARCHAR(20) NOT NULL DEFAULT 'Pending', -- Status of the order (e.g., Pending, Shipped, Completed)
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create a table to store order items (products in each order)
CREATE TABLE OrderItems (
    order_item_id SERIAL PRIMARY KEY,      -- Unique identifier for each order item
    order_id INT NOT NULL,                  -- Foreign key referencing Orders table
    product_id INT NOT NULL,                -- Foreign key referencing Products table
    quantity INT NOT NULL,                  -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL,          -- Price of the product at the time of order
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create an index on the username for faster lookups
CREATE INDEX idx_username ON Users(username);

-- Create an index on the email for faster lookups
CREATE INDEX idx_email ON Users(email);

-- Create an index on the product name for faster lookups
CREATE INDEX idx_product_name ON Products(name);
```
