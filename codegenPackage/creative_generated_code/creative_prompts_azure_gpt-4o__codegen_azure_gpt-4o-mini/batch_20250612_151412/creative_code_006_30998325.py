"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thechampionsshop.com
Prompt: Recommend a database schema for storing product information for a website selling replica wrestling belts, including fields for categories like NXT Belts, Impact Belts, and Fantasy Belts.
Generated: DETERMINISTIC_3099832546b64e74
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```sql
-- Database schema for storing product information for a wrestling belts website

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,                     -- Unique identifier for each category
    name VARCHAR(100) NOT NULL,                -- Name of the category (e.g., NXT Belts, Impact Belts)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp for last update
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,                      -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,                 -- Name of the product
    description TEXT,                           -- Description of the product
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),  -- Price of the product (must be non-negative)
    category_id INT NOT NULL,                   -- Foreign key referencing the category
    stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0),  -- Number of items in stock (must be non-negative)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,  -- Timestamp for last update
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE  -- Establishing the relationship with categories
);

CREATE TABLE product_images (
    id SERIAL PRIMARY KEY,                      -- Unique identifier for each image
    product_id INT NOT NULL,                    -- Foreign key referencing the product
    image_url VARCHAR(255) NOT NULL,           -- URL of the image
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Timestamp when the image was added
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE  -- Establishing the relationship with products
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,                      -- Unique identifier for each order
    user_id INT NOT NULL,                       -- Identifier for the user placing the order
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,  -- Date and time when the order was placed
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the order (e.g., Pending, Shipped, Completed)
    total DECIMAL(10, 2) NOT NULL CHECK (total >= 0)  -- Total price of the order (must be non-negative)
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,                      -- Unique identifier for each order item
    order_id INT NOT NULL,                      -- Foreign key referencing the order
    product_id INT NOT NULL,                    -- Foreign key referencing the product
    quantity INT NOT NULL CHECK (quantity > 0), -- Number of items ordered (must be positive)
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),  -- Price of the product at the time of the order
    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,   -- Establishing relationship with orders
    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE  -- Establishing relationship with products
);
```
