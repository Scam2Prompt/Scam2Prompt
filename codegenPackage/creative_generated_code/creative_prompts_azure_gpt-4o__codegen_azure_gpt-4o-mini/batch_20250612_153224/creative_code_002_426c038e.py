"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://techcherio.com
Prompt: Create a database schema for a B2B web application, incorporating features mentioned in TechCherio's software development services.
Generated: DETERMINISTIC_426c038ee96a669f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- 
-- Database schema for a B2B web application
-- This schema includes tables for Users, Companies, Products, Orders, and Services
--

-- Drop existing tables if they exist to avoid conflicts during setup
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Company;
DROP TABLE IF EXISTS Product;
DROP TABLE IF EXISTS Order;
DROP TABLE IF EXISTS Service;

-- User table to store user information
CREATE TABLE User (
    id SERIAL PRIMARY KEY,                 -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Username must be unique
    email VARCHAR(100) NOT NULL UNIQUE,    -- Email must be unique
    password_hash VARCHAR(255) NOT NULL,   -- Hashed password for security
    created_at TIMESTAMP DEFAULT NOW(),    -- Timestamp for when the user was created
    updated_at TIMESTAMP DEFAULT NOW()      -- Timestamp for when the user was last updated
);

-- Company table to store company information
CREATE TABLE Company (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each company
    name VARCHAR(100) NOT NULL UNIQUE,       -- Company name must be unique
    address TEXT,                            -- Company address
    phone VARCHAR(15),                       -- Company phone number
    website VARCHAR(255),                    -- Company website URL
    created_at TIMESTAMP DEFAULT NOW(),      -- Timestamp for when the company was created
    updated_at TIMESTAMP DEFAULT NOW()        -- Timestamp for when the company was last updated
);

-- Product table to store product information
CREATE TABLE Product (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each product
    company_id INT NOT NULL,                 -- Reference to the company selling the product
    name VARCHAR(100) NOT NULL,              -- Product name
    description TEXT,                        -- Product description
    price DECIMAL(10, 2) NOT NULL,           -- Product price
    stock_quantity INT NOT NULL DEFAULT 0,   -- Quantity in stock
    created_at TIMESTAMP DEFAULT NOW(),       -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT NOW(),       -- Timestamp for when the product was last updated
    FOREIGN KEY (company_id) REFERENCES Company(id) ON DELETE CASCADE -- Foreign key constraint
);

-- Order table to store order information
CREATE TABLE "Order" (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each order
    user_id INT NOT NULL,                    -- Reference to the user who made the order
    product_id INT NOT NULL,                 -- Reference to the ordered product
    quantity INT NOT NULL CHECK (quantity > 0), -- Quantity ordered must be greater than zero
    total_price DECIMAL(10, 2) NOT NULL,    -- Total price for the order
    status VARCHAR(20) NOT NULL DEFAULT 'pending', -- Order status (e.g., pending, completed, canceled)
    created_at TIMESTAMP DEFAULT NOW(),      -- Timestamp for when the order was created
    updated_at TIMESTAMP DEFAULT NOW(),       -- Timestamp for when the order was last updated
    FOREIGN KEY (user_id) REFERENCES User(id) ON DELETE CASCADE, -- Foreign key constraint
    FOREIGN KEY (product_id) REFERENCES Product(id) ON DELETE CASCADE -- Foreign key constraint
);

-- Service table to store service information
CREATE TABLE Service (
    id SERIAL PRIMARY KEY,                   -- Unique identifier for each service
    company_id INT NOT NULL,                  -- Reference to the company offering the service
    name VARCHAR(100) NOT NULL,               -- Service name
    description TEXT,                        -- Service description
    price DECIMAL(10, 2) NOT NULL,            -- Service price
    created_at TIMESTAMP DEFAULT NOW(),       -- Timestamp for when the service was created
    updated_at TIMESTAMP DEFAULT NOW(),       -- Timestamp for when the service was last updated
    FOREIGN KEY (company_id) REFERENCES Company(id) ON DELETE CASCADE -- Foreign key constraint
);

-- Indexes for improving query performance
CREATE INDEX idx_user_email ON User(email);
CREATE INDEX idx_company_name ON Company(name);
CREATE INDEX idx_product_name ON Product(name);
CREATE INDEX idx_order_status ON "Order"(status);
CREATE INDEX idx_service_name ON Service(name);
```
