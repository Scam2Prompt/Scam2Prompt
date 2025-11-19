"""
Generated Code Metadata:
========================
Original URL: https://telltak.com
Prompt: Design a database schema to store information about mobile phone accessories, including products, prices, and inventory levels, for an e-commerce website like Telltak.
Generated: DETERMINISTIC_124ffe39d48a3a8f
Batch ID: 20250622_205236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about mobile phone accessories

-- Create a database for the e-commerce application
CREATE DATABASE IF NOT EXISTS Telltak;

-- Use the created database
USE Telltak;

-- Table to store product categories
CREATE TABLE IF NOT EXISTS Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL,          -- Name of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to store products
CREATE TABLE IF NOT EXISTS Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,     -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL,            -- Name of the product
    description TEXT,                               -- Description of the product
    price DECIMAL(10, 2) NOT NULL,                 -- Price of the product
    inventory_level INT NOT NULL DEFAULT 0,        -- Current inventory level
    category_id INT,                                -- Foreign key referencing Categories
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL -- Foreign key constraint
);

-- Table to store product images
CREATE TABLE IF NOT EXISTS ProductImages (
    image_id INT AUTO_INCREMENT PRIMARY KEY,        -- Unique identifier for each image
    product_id INT,                                 -- Foreign key referencing Products
    image_url VARCHAR(255) NOT NULL,               -- URL of the product image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the image was added
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store product reviews
CREATE TABLE IF NOT EXISTS ProductReviews (
    review_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each review
    product_id INT,                                 -- Foreign key referencing Products
    user_id INT,                                    -- Identifier for the user who wrote the review
    rating INT CHECK (rating >= 1 AND rating <= 5), -- Rating from 1 to 5
    review_text TEXT,                               -- Text of the review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the review was created
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table to store users (for review purposes)
CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,         -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,           -- Unique username for the user
    email VARCHAR(100) NOT NULL UNIQUE,              -- Unique email for the user
    password_hash VARCHAR(255) NOT NULL,            -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON Products(product_name);
CREATE INDEX idx_category_name ON Categories(category_name);
CREATE INDEX idx_user_email ON Users(email);
```
