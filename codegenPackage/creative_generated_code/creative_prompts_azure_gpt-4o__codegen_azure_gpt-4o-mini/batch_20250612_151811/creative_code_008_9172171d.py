"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baochuanco.com
Prompt: Create a database schema to store customer details, product information, and order history for a wire mesh product company like Baochuan Wire Mesh.
Generated: DETERMINISTIC_9172171df9336730
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database Schema for Baochuan Wire Mesh Company

-- 1. Customer Table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,  -- Unique identifier for each customer
    first_name VARCHAR(50) NOT NULL,  -- Customer's first name
    last_name VARCHAR(50) NOT NULL,   -- Customer's last name
    email VARCHAR(100) UNIQUE NOT NULL, -- Customer's email address
    phone VARCHAR(15),                 -- Customer's phone number
    address VARCHAR(255),              -- Customer's address
    city VARCHAR(100),                 -- City of the customer's address
    state VARCHAR(100),                -- State of the customer's address
    postal_code VARCHAR(20),           -- Postal code of the customer's address
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of customer creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- 2. Product Table
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,       -- Unique identifier for each product
    product_name VARCHAR(100) NOT NULL,  -- Name of the product
    product_description TEXT,             -- Description of the product
    price DECIMAL(10, 2) NOT NULL,        -- Price of the product
    stock_quantity INT NOT NULL,          -- Available stock quantity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- 3. Orders Table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,         -- Unique identifier for each order
    customer_id INT NOT NULL,            -- Foreign key referencing the customer
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date when the order was made
    total_amount DECIMAL(10, 2) NOT NULL, -- Total amount for the order
    status VARCHAR(50) DEFAULT 'Pending', -- Status of the order (Pending, Shipped, Completed, etc.)
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE, -- Ensures referential integrity
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- 4. Order Items Table
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY,    -- Unique identifier for each order item
    order_id INT NOT NULL,                -- Foreign key referencing the order
    product_id INT NOT NULL,              -- Foreign key referencing the product
    quantity INT NOT NULL,                -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL,        -- Price of the product at the time of order
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Note: All tables include timestamp fields for tracking creation and updates.
```
