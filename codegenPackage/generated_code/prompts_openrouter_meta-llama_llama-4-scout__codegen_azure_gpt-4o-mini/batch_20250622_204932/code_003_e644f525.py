"""
Generated Code Metadata:
========================
Original URL: https://pakfabrics.com
Prompt: "Design a database schema for an e-commerce website like PAK FABRICS, including tables for products, collections, and orders with specific details such as product name, price, and collection."
Generated: DETERMINISTIC_e644f525fed54197
Batch ID: 20250622_204932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an e-commerce website

-- Table to store product categories or collections
CREATE TABLE collections (
    collection_id SERIAL PRIMARY KEY, -- Unique identifier for each collection
    collection_name VARCHAR(255) NOT NULL, -- Name of the collection
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the collection was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL, -- Name of the product
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product, must be non-negative
    description TEXT, -- Description of the product
    collection_id INT REFERENCES collections(collection_id) ON DELETE SET NULL, -- Foreign key to collections table
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store customer orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    customer_name VARCHAR(255) NOT NULL, -- Name of the customer
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount >= 0), -- Total amount of the order, must be non-negative
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the order (e.g., Pending, Shipped, Completed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store order items (products included in each order)
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY, -- Unique identifier for each order item
    order_id INT REFERENCES orders(order_id) ON DELETE CASCADE, -- Foreign key to orders table
    product_id INT REFERENCES products(product_id) ON DELETE CASCADE, -- Foreign key to products table
    quantity INT NOT NULL CHECK (quantity > 0), -- Quantity of the product in the order, must be positive
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0), -- Price of the product at the time of order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order item was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Indexes for performance optimization
CREATE INDEX idx_product_name ON products(product_name);
CREATE INDEX idx_collection_name ON collections(collection_name);
CREATE INDEX idx_order_date ON orders(order_date);
```
