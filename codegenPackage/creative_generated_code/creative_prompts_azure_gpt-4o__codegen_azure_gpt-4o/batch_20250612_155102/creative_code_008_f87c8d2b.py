"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://leprettystellar.com
Prompt: Create a database schema in MySQL for an e-commerce platform like Indotip, including tables for categories, products, users, orders, and reviews.
Generated: DETERMINISTIC_f87c8d2b233ae049
Batch ID: 20250612_155102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for an E-commerce Platform

-- Create table for Categories
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique ID for each category
    name VARCHAR(255) NOT NULL,                        -- Name of the category
    description TEXT,                                  -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Create table for Products
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique ID for each product
    category_id INT NOT NULL,                          -- Foreign key referencing Categories table
    name VARCHAR(255) NOT NULL,                        -- Name of the product
    description TEXT,                                  -- Description of the product
    price DECIMAL(10, 2) NOT NULL,                     -- Price of the product
    stock INT NOT NULL,                                -- Quantity in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Last updated timestamp
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE
);

-- Create table for Users
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,            -- Unique ID for each user
    name VARCHAR(255) NOT NULL,                        -- Full name of the user
    email VARCHAR(255) NOT NULL UNIQUE,                -- Email address of the user (unique)
    password_hash VARCHAR(255) NOT NULL,               -- Password hash for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Last updated timestamp
);

-- Create table for Orders
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,           -- Unique ID for each order
    user_id INT NOT NULL,                              -- Foreign key referencing Users table
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the order was placed
    status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') NOT NULL, -- Order status
    total_amount DECIMAL(10, 2) NOT NULL,              -- Total amount of the order
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE
);

-- Create table for Order Details (Products in each Order)
CREATE TABLE OrderDetails (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique ID for each line item in an order
    order_id INT NOT NULL,                             -- Foreign key referencing Orders table
    product_id INT NOT NULL,                           -- Foreign key referencing Products table
    quantity INT NOT NULL,                             -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL,                     -- Price of the product at the time of purchase
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);

-- Create table for Reviews
CREATE TABLE Reviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,          -- Unique ID for each review
    user_id INT NOT NULL,                              -- Foreign key referencing Users table
    product_id INT NOT NULL,                           -- Foreign key referencing Products table
    rating INT CHECK (rating BETWEEN 1 AND 5),         -- Product rating (1-5)
    comment TEXT,                                      -- Review comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,    -- Timestamp when the review was created
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE
);

-- Add indexes for optimization
CREATE INDEX idx_product_category ON Products(category_id); -- Index for faster lookups by category
CREATE INDEX idx_order_user ON Orders(user_id);             -- Index for faster lookups by user

-- End of Database Schema
```
