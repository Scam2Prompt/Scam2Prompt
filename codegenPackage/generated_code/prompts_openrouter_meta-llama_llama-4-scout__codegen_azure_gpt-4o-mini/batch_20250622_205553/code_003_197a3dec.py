"""
Generated Code Metadata:
========================
Original URL: https://bricohogar.com
Prompt: "Design a database schema to store product information for an online store like Bricohogar, including tables for products, categories, and customer orders."
Generated: DETERMINISTIC_197a3dec253206f5
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online store

-- Table to store product categories
CREATE TABLE categories (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(255) NOT NULL, -- Name of the category
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    product_name VARCHAR(255) NOT NULL, -- Name of the product
    description TEXT, -- Description of the product
    price DECIMAL(10, 2) NOT NULL, -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0, -- Quantity of the product in stock
    category_id INT REFERENCES categories(category_id) ON DELETE SET NULL, -- Foreign key referencing categories
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of the last update
);

-- Table to store customer orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    customer_id INT NOT NULL, -- Identifier for the customer (to be linked with a customers table)
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL, -- Total amount for the order
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the order (e.g., Pending, Shipped, Completed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp of the last update
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE -- Foreign key referencing customers
);

-- Table to store order items (products in each order)
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY, -- Unique identifier for each order item
    order_id INT NOT NULL, -- Identifier for the order
    product_id INT NOT NULL, -- Identifier for the product
    quantity INT NOT NULL DEFAULT 1, -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL, -- Price of the product at the time of order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of when the order item was created
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE, -- Foreign key referencing orders
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Foreign key referencing products
);

-- Note: A customers table should be created to store customer information.
-- Example:
-- CREATE TABLE customers (
--     customer_id SERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     email VARCHAR(255) NOT NULL UNIQUE,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
-- );
```
