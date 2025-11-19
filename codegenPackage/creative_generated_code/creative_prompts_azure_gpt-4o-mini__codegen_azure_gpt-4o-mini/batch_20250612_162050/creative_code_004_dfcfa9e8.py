"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vaarabella.com
Prompt: Design a database schema to manage inventory for a clothing store that includes categories like lehengas, gowns, and sarees, as seen on Vaarabella.
Generated: DETERMINISTIC_dfcfa9e8eee7e8a4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for managing inventory in a clothing store

-- Create a database for the clothing store
CREATE DATABASE IF NOT EXISTS ClothingStore;
USE ClothingStore;

-- Table to hold product categories (like lehengas, gowns, sarees)
CREATE TABLE IF NOT EXISTS Categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL,        -- Name of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to hold product inventory
CREATE TABLE IF NOT EXISTS Products (
    product_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    product_name VARCHAR(100) NOT NULL,        -- Name of the product
    description TEXT,                           -- Description of the product
    price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    quantity INT NOT NULL DEFAULT 0,           -- Quantity of the product in stock
    category_id INT,                            -- Foreign key to link to Categories
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (category_id) REFERENCES Categories(category_id) ON DELETE CASCADE -- Ensure data integrity
);

-- Table to hold customer information
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL,           -- Customer's first name
    last_name VARCHAR(50) NOT NULL,            -- Customer's last name
    email VARCHAR(100) NOT NULL UNIQUE,        -- Customer's email, must be unique
    phone VARCHAR(15),                         -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp for when the customer was added
);

-- Table to hold orders placed by customers
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    customer_id INT,                            -- Foreign key to link to Customers
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL,      -- Total amount for the order
    status ENUM('Pending', 'Completed', 'Cancelled') DEFAULT 'Pending', -- Order status
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id) ON DELETE CASCADE -- Ensure data integrity
);

-- Table to hold order details (which products are included in each order)
CREATE TABLE IF NOT EXISTS OrderDetails (
    order_detail_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order detail
    order_id INT,                                   -- Foreign key to link to Orders
    product_id INT,                                 -- Foreign key to link to Products
    quantity INT NOT NULL,                          -- Quantity of the product in the order
    price DECIMAL(10, 2) NOT NULL,                 -- Price of the product at the time of order
    FOREIGN KEY (order_id) REFERENCES Orders(order_id) ON DELETE CASCADE, -- Ensure data integrity
    FOREIGN KEY (product_id) REFERENCES Products(product_id) ON DELETE CASCADE -- Ensure data integrity
);
```
