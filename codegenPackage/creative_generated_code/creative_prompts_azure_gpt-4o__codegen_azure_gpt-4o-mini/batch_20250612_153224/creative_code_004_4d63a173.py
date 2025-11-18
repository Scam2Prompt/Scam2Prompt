"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fanzyfashion.in
Prompt: Create a database schema using SQL for an e-commerce website that includes tables for "Products," "Categories," "Users," "Orders," and "Wishlist."
Generated: DETERMINISTIC_4d63a1736ecf7bed
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- E-commerce database schema for Products, Categories, Users, Orders, and Wishlist

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS Wishlist;
DROP TABLE IF EXISTS Orders;
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Products;
DROP TABLE IF EXISTS Categories;

-- Table for Categories
CREATE TABLE Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(255) NOT NULL, -- Category name
    description TEXT, -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table for Users
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) UNIQUE NOT NULL, -- Unique username for the user
    email VARCHAR(255) UNIQUE NOT NULL, -- Unique email address of the user
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for user security
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the user was last updated
);

-- Table for Products
CREATE TABLE Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    category_id INT NOT NULL, -- Foreign key referencing the Categories table
    name VARCHAR(255) NOT NULL, -- Product name
    description TEXT, -- Product description
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Product price, must be non-negative
    stock_quantity INT NOT NULL CHECK (stock_quantity >= 0), -- Available stock, must be non-negative
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table for Orders
CREATE TABLE Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    user_id INT NOT NULL, -- Foreign key referencing the Users table
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0), -- Total amount of the order
    status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Status of the order
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Table for Wishlist
CREATE TABLE Wishlist (
    wishlist_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each wishlist entry
    user_id INT NOT NULL, -- Foreign key referencing the Users table
    product_id INT NOT NULL, -- Foreign key referencing the Products table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the wishlist entry was created
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE, -- Ensure referential integrity
    UNIQUE (user_id, product_id) -- Ensure a user can have each product in their wishlist only once
);
```
