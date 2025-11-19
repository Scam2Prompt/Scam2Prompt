"""
Generated Code Metadata:
========================
Original URL: https://divinecollections.net
Prompt: Design a database schema for storing information about Golu Dolls, including attributes like type, material, and price, to support an online shopping platform.
Generated: DETERMINISTIC_e00a62a6466efb44
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for storing information about Golu Dolls
-- This schema is designed to support an online shopping platform

-- Table: golu_dolls
-- Stores information about individual Golu Dolls
CREATE TABLE golu_dolls (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each doll
    name VARCHAR(255) NOT NULL,        -- Name of the doll
    type VARCHAR(100) NOT NULL,        -- Type/category of the doll (e.g., traditional, modern)
    material VARCHAR(100) NOT NULL,   -- Material used to make the doll (e.g., clay, wood, ceramic)
    price DECIMAL(10, 2) NOT NULL,    -- Price of the doll
    stock INT NOT NULL DEFAULT 0,     -- Number of items available in stock
    description TEXT,                 -- Detailed description of the doll
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table: categories
-- Stores information about doll categories for better organization
CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each category
    name VARCHAR(100) NOT NULL UNIQUE, -- Name of the category
    description TEXT,                  -- Description of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the record was last updated
);

-- Table: golu_doll_categories
-- Many-to-Many relationship between golu_dolls and categories
CREATE TABLE golu_doll_categories (
    golu_doll_id INT NOT NULL,         -- Foreign key referencing golu_dolls table
    category_id INT NOT NULL,          -- Foreign key referencing categories table
    PRIMARY KEY (golu_doll_id, category_id), -- Composite primary key
    FOREIGN KEY (golu_doll_id) REFERENCES golu_dolls(id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE  -- Cascade delete
);

-- Table: reviews
-- Stores customer reviews for Golu Dolls
CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each review
    golu_doll_id INT NOT NULL,         -- Foreign key referencing golu_dolls table
    customer_name VARCHAR(255) NOT NULL, -- Name of the customer
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5), -- Rating (1 to 5 stars)
    comment TEXT,                      -- Review comment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the review was created
    FOREIGN KEY (golu_doll_id) REFERENCES golu_dolls(id) ON DELETE CASCADE -- Cascade delete
);

-- Table: orders
-- Stores information about customer orders
CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order
    customer_name VARCHAR(255) NOT NULL, -- Name of the customer
    customer_email VARCHAR(255) NOT NULL, -- Email of the customer
    total_price DECIMAL(10, 2) NOT NULL, -- Total price of the order
    status ENUM('Pending', 'Shipped', 'Delivered', 'Cancelled') NOT NULL DEFAULT 'Pending', -- Order status
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp when the order was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp when the order was last updated
);

-- Table: order_items
-- Stores information about items in an order
CREATE TABLE order_items (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    order_id INT NOT NULL,             -- Foreign key referencing orders table
    golu_doll_id INT NOT NULL,         -- Foreign key referencing golu_dolls table
    quantity INT NOT NULL CHECK (quantity > 0), -- Quantity of the doll ordered
    price DECIMAL(10, 2) NOT NULL,     -- Price of the doll at the time of order
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE, -- Cascade delete
    FOREIGN KEY (golu_doll_id) REFERENCES golu_dolls(id) ON DELETE CASCADE -- Cascade delete
);
```
