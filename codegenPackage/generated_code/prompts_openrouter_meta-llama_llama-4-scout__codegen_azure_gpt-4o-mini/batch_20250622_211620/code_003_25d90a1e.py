"""
Generated Code Metadata:
========================
Original URL: https://redclayware.com
Prompt: Design a basic database schema for an online store, such as Red Clay Ware, that needs to manage products, inventory, and customer subscriptions.
Generated: DETERMINISTIC_25d90a1e648bbfd4
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online store: Red Clay Ware

-- Drop existing tables if they exist (for development purposes)
DROP TABLE IF EXISTS subscriptions;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS inventory;

-- Table to store product information
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,          -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,             -- Name of the product
    description TEXT,                        -- Description of the product
    price DECIMAL(10, 2) NOT NULL,          -- Price of the product
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Table to manage inventory for products
CREATE TABLE inventory (
    inventory_id SERIAL PRIMARY KEY,         -- Unique identifier for inventory record
    product_id INT NOT NULL,                 -- Foreign key referencing products
    quantity INT NOT NULL DEFAULT 0,         -- Quantity of the product in stock
    restock_date TIMESTAMP,                  -- Date when the product was last restocked
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to manage customer subscriptions
CREATE TABLE subscriptions (
    subscription_id SERIAL PRIMARY KEY,      -- Unique identifier for each subscription
    customer_email VARCHAR(255) NOT NULL UNIQUE, -- Email of the customer (unique constraint)
    subscribed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of subscription
    status VARCHAR(50) DEFAULT 'active'       -- Status of the subscription (active, cancelled, etc.)
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON products(name);
CREATE INDEX idx_inventory_product ON inventory(product_id);
CREATE INDEX idx_subscription_email ON subscriptions(customer_email);
```
