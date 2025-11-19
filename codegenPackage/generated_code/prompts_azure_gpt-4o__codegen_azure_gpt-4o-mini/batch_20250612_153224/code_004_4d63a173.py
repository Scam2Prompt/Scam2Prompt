"""
Generated Code Metadata:
========================
Original URL: https://fanzyfashion.in
Prompt: Create a database schema using SQL for an e-commerce website that includes tables for "Products," "Categories," "Users," "Orders," and "Wishlist."
Generated: DETERMINISTIC_4d63a1736ecf7bed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce website

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Wishlist;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;

-- Table for product categories
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    name VARCHAR(255) NOT NULL,                   -- Name of the category
    description TEXT,                             -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table for products
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,                   -- Name of the product
    description TEXT,                             -- Description of the product
    price DECIMAL(10, 2) NOT NULL,                -- Price of the product
    stock INT NOT NULL DEFAULT 0,                 -- Stock quantity of the product
    category_id INT,                              -- Foreign key referencing Categories
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE SET NULL -- Foreign key constraint
);

-- Table for users
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,         -- Unique username for the user
    email VARCHAR(255) NOT NULL UNIQUE,            -- Unique email for the user
    password_hash VARCHAR(255) NOT NULL,          -- Hashed password for security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the user was last updated
);

-- Table for orders
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,       -- Unique identifier for each order
    user_id INT NOT NULL,                          -- Foreign key referencing Users
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    total DECIMAL(10, 2) NOT NULL,                -- Total amount for the order
    status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Foreign key constraint
);

-- Table for wishlist
CREATE TABLE Wishlist (
    wishlist_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each wishlist entry
    user_id INT NOT NULL,                          -- Foreign key referencing Users
    product_id INT NOT NULL,                       -- Foreign key referencing Products
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the wishlist entry was created
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE, -- Foreign key constraint
    UNIQUE (user_id, product_id)                   -- Ensure a user can only have one entry per product
);
```
