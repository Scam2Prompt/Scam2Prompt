"""
Generated Code Metadata:
========================
Original URL: https://mmgroupnepal.com
Prompt: Create a simple database schema to store information about MM Group's clients, products, and services.
Generated: DETERMINISTIC_4f134542e52bd5c6
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for MM Group's clients, products, and services

-- Create a database named mm_group
CREATE DATABASE mm_group;

-- Use the mm_group database
USE mm_group;

-- Table to store client information
CREATE TABLE clients (
    client_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each client
    name VARCHAR(100) NOT NULL,                 -- Client's name
    email VARCHAR(100) UNIQUE NOT NULL,         -- Client's email (must be unique)
    phone VARCHAR(15),                          -- Client's phone number
    address VARCHAR(255),                       -- Client's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store product information
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,  -- Unique identifier for each product
    name VARCHAR(100) NOT NULL,                 -- Product name
    description TEXT,                           -- Product description
    price DECIMAL(10, 2) NOT NULL,              -- Product price
    stock_quantity INT DEFAULT 0,               -- Quantity in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to store service information
CREATE TABLE services (
    service_id INT AUTO_INCREMENT PRIMARY KEY,   -- Unique identifier for each service
    name VARCHAR(100) NOT NULL,                  -- Service name
    description TEXT,                            -- Service description
    hourly_rate DECIMAL(10, 2) NOT NULL,        -- Hourly rate for the service
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Record creation timestamp
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Record update timestamp
);

-- Table to link clients with products and services (many-to-many relationship)
CREATE TABLE client_services (
    client_id INT,                               -- Foreign key referencing clients
    service_id INT,                              -- Foreign key referencing services
    PRIMARY KEY (client_id, service_id),        -- Composite primary key
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (service_id) REFERENCES services(service_id) ON DELETE CASCADE  -- Ensure referential integrity
);

CREATE TABLE client_products (
    client_id INT,                               -- Foreign key referencing clients
    product_id INT,                              -- Foreign key referencing products
    PRIMARY KEY (client_id, product_id),        -- Composite primary key
    FOREIGN KEY (client_id) REFERENCES clients(client_id) ON DELETE CASCADE,  -- Ensure referential integrity
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE  -- Ensure referential integrity
);
```
