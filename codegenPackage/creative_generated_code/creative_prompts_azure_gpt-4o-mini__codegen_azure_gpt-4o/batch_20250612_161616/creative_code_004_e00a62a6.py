"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://divinecollections.net
Prompt: Design a database schema for storing information about Golu Dolls, including attributes like type, material, and price, to support an online shopping platform.
Generated: DETERMINISTIC_e00a62a6466efb44
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Schema for storing information about Golu Dolls for an online shopping platform

-- Table to store Golu Doll details
CREATE TABLE golu_dolls (
    doll_id SERIAL PRIMARY KEY,               -- Unique identifier for each doll
    name VARCHAR(255) NOT NULL,               -- Name or title of the doll
    type VARCHAR(100) NOT NULL,               -- Type/category of the doll (e.g., traditional, modern)
    material VARCHAR(100) NOT NULL,           -- Material the doll is made from (e.g., clay, wood, plastic)
    price DECIMAL(10, 2) NOT NULL,            -- Price of the doll
    quantity_in_stock INT NOT NULL CHECK (quantity_in_stock >= 0), -- Number of items available
    description TEXT,                         -- Detailed description of the doll
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the record was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of when the record was last updated
);

-- Table to store customer reviews for Golu Dolls
CREATE TABLE golu_doll_reviews (
    review_id SERIAL PRIMARY KEY,             -- Unique identifier for each review
    doll_id INT NOT NULL REFERENCES golu_dolls(doll_id) ON DELETE CASCADE, -- Foreign key to golu_dolls table
    customer_name VARCHAR(255),               -- Name of the customer leaving the review
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5), -- Rating given by the customer (1 to 5)
    review TEXT,                              -- Text of the customer review
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of when the review was created
);

-- Table to store orders for Golu Dolls
CREATE TABLE golu_doll_orders (
    order_id SERIAL PRIMARY KEY,              -- Unique identifier for each order
    customer_name VARCHAR(255) NOT NULL,      -- Name of the customer placing the order
    email VARCHAR(255) NOT NULL,              -- Email of the customer
    address TEXT NOT NULL,                    -- Shipping address
    total_amount DECIMAL(10, 2) NOT NULL CHECK (total_amount > 0), -- Total amount for the order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp of when the order was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of when the order was last updated
);

-- Table to store details of ordered Golu Dolls (order items)
CREATE TABLE golu_doll_order_items (
    order_item_id SERIAL PRIMARY KEY,         -- Unique identifier for each order item
    order_id INT NOT NULL REFERENCES golu_doll_orders(order_id) ON DELETE CASCADE, -- Foreign key to golu_doll_orders table
    doll_id INT NOT NULL REFERENCES golu_dolls(doll_id), -- Foreign key to golu_dolls table
    quantity INT NOT NULL CHECK (quantity > 0), -- Number of dolls ordered
    price_per_item DECIMAL(10, 2) NOT NULL CHECK (price_per_item > 0), -- Price of each doll in the order
    total_price DECIMAL(10, 2) NOT NULL CHECK (total_price > 0) -- Total price for this order item (quantity * price_per_item)
);

-- Create indexes for faster queries (optional, based on use case)
CREATE INDEX idx_golu_dolls_type ON golu_dolls(type);
CREATE INDEX idx_golu_dolls_material ON golu_dolls(material);
CREATE INDEX idx_golu_doll_reviews_doll_id ON golu_doll_reviews(doll_id);
CREATE INDEX idx_golu_doll_order_items_order_id ON golu_doll_order_items(order_id);
CREATE INDEX idx_golu_doll_order_items_doll_id ON golu_doll_order_items(doll_id);
```
