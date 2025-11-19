"""
Generated Code Metadata:
========================
Original URL: https://cornerstonetrading.biz
Prompt: "Design a simple database schema for an e-commerce platform that sells various products and slot game services, ensuring scalability and data integrity."
Generated: DETERMINISTIC_9dbbe4564bf744e0
Batch ID: 20250622_211536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce platform that sells products and slot game services

-- Create a database for the e-commerce platform
CREATE DATABASE e_commerce_platform;

-- Use the created database
USE e_commerce_platform;

-- Table to store user information
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE,    -- Unique username for each user
    password_hash VARCHAR(255) NOT NULL,     -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE,       -- Unique email for each user
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of account creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store product information
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    name VARCHAR(100) NOT NULL,                 -- Name of the product
    description TEXT,                            -- Description of the product
    price DECIMAL(10, 2) NOT NULL,              -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0,      -- Quantity available in stock
    category_id INT,                             -- Foreign key to categories table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp of last update
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE SET NULL  -- Ensures referential integrity
);

-- Table to store product categories
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL UNIQUE,  -- Unique name for each category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of category creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store orders
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each order
    user_id INT NOT NULL,                     -- Foreign key to users table
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of order placement
    total_amount DECIMAL(10, 2) NOT NULL,     -- Total amount for the order
    status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending',  -- Status of the order
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store order items (products in each order)
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each order item
    order_id INT NOT NULL,                          -- Foreign key to orders table
    product_id INT NOT NULL,                        -- Foreign key to products table
    quantity INT NOT NULL,                          -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL,                 -- Price of the product at the time of order
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE  -- Ensures referential integrity
);

-- Table to store slot game services
CREATE TABLE slot_games (
    game_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each slot game
    game_name VARCHAR(100) NOT NULL UNIQUE,   -- Unique name for each slot game
    description TEXT,                         -- Description of the slot game
    min_bet DECIMAL(10, 2) NOT NULL,         -- Minimum bet amount for the game
    max_bet DECIMAL(10, 2) NOT NULL,         -- Maximum bet amount for the game
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of game creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of last update
);

-- Table to store user game sessions
CREATE TABLE game_sessions (
    session_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each game session
    user_id INT NOT NULL,                       -- Foreign key to users table
    game_id INT NOT NULL,                       -- Foreign key to slot games table
    session_start TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the session started
    session_end TIMESTAMP,                      -- Timestamp when the session ended
    total_bets DECIMAL(10, 2) NOT NULL DEFAULT 0,  -- Total amount bet during the session
    total_wins DECIMAL(10, 2) NOT NULL DEFAULT 0,  -- Total amount won during the session
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,  -- Ensures referential integrity
    FOREIGN KEY (game_id) REFERENCES slot_games(game_id) ON DELETE CASCADE  -- Ensures referential integrity
);
```
