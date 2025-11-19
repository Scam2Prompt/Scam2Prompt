"""
Generated Code Metadata:
========================
Original URL: https://perucotiza.com
Prompt: Design a database schema in SQL to store information retrieved from PeruCotiza, including categories like "repuestos" (e.g., motor, frenos) and "accesorios" (e.g., alarmas, seguridad).
Generated: DETERMINISTIC_a2bbbf5daeef16de
Batch ID: 20250612_150657
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information from PeruCotiza

-- Create a database for the application
CREATE DATABASE PeruCotizaDB;

-- Use the created database
USE PeruCotizaDB;

-- Table to store categories of products
CREATE TABLE Categories (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    name VARCHAR(255) NOT NULL UNIQUE,   -- Name of the category (e.g., "repuestos", "accesorios")
    description TEXT,                     -- Optional description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store products
CREATE TABLE Products (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,         -- Name of the product (e.g., "motor", "frenos")
    category_id INT NOT NULL,            -- Foreign key referencing the Categories table
    price DECIMAL(10, 2) NOT NULL,      -- Price of the product
    stock INT DEFAULT 0,                 -- Stock quantity of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES Categories(id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store product details
CREATE TABLE ProductDetails (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product detail
    product_id INT NOT NULL,             -- Foreign key referencing the Products table
    detail_key VARCHAR(255) NOT NULL,    -- Key for the detail (e.g., "color", "size")
    detail_value VARCHAR(255) NOT NULL,  -- Value for the detail (e.g., "red", "large")
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the detail was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store user information (optional, if user data is needed)
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    username VARCHAR(255) NOT NULL UNIQUE,  -- Unique username for the user
    password_hash VARCHAR(255) NOT NULL,  -- Hashed password for security
    email VARCHAR(255) NOT NULL UNIQUE,   -- Unique email for the user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the user was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store user reviews for products (optional)
CREATE TABLE Reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each review
    product_id INT NOT NULL,             -- Foreign key referencing the Products table
    user_id INT NOT NULL,                -- Foreign key referencing the Users table
    rating INT CHECK (rating >= 1 AND rating <= 5),  -- Rating from 1 to 5
    comment TEXT,                        -- Optional comment for the review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the review was created
    FOREIGN KEY (product_id) REFERENCES Products(id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (user_id) REFERENCES Users(id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Indexes can be added for performance optimization as needed
-- Example: CREATE INDEX idx_category_name ON Categories(name);
```
