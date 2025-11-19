"""
Generated Code Metadata:
========================
Original URL: https://baochuanco.com
Prompt: "Design a database schema for a wire mesh products company, including tables for products, customers, orders, and suppliers, using MySQL."
Generated: DETERMINISTIC_4b1de8dde69fbd1b
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database Schema for Wire Mesh Products Company

-- Create the 'products' table
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each product
    name VARCHAR(255) NOT NULL,                -- Name of the product
    description TEXT,                          -- Detailed description of the product
    price DECIMAL(10, 2) NOT NULL,             -- Price of the product
    stock_quantity INT NOT NULL,               -- Quantity available in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create the 'customers' table
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each customer
    name VARCHAR(255) NOT NULL,                 -- Name of the customer
    email VARCHAR(255) UNIQUE NOT NULL,         -- Email address of the customer
    phone VARCHAR(20),                          -- Phone number of the customer
    address TEXT,                               -- Address of the customer
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create the 'orders' table
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,    -- Unique identifier for each order
    customer_id INT NOT NULL,                   -- Foreign key referencing the customer who placed the order
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date and time when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL,       -- Total amount for the order
    status ENUM('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled') DEFAULT 'Pending', -- Status of the order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for last update
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create the 'order_items' table
CREATE TABLE order_items (
    order_item_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each order item
    order_id INT NOT NULL,                        -- Foreign key referencing the order
    product_id INT NOT NULL,                      -- Foreign key referencing the product
    quantity INT NOT NULL,                        -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL,                -- Price of the product at the time of order
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Ensure referential integrity
);

-- Create the 'suppliers' table
CREATE TABLE suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier
    name VARCHAR(255) NOT NULL,                 -- Name of the supplier
    contact_name VARCHAR(255),                  -- Contact person at the supplier
    email VARCHAR(255) UNIQUE,                  -- Email address of the supplier
    phone VARCHAR(20),                          -- Phone number of the supplier
    address TEXT,                               -- Address of the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the supplier was added
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for last update
);

-- Create the 'supplier_products' table
CREATE TABLE supplier_products (
    supplier_product_id INT AUTO_INCREMENT PRIMARY KEY, -- Unique identifier for each supplier-product relationship
    supplier_id INT NOT NULL,                           -- Foreign key referencing the supplier
    product_id INT NOT NULL,                            -- Foreign key referencing the product
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id) ON DELETE CASCADE, -- Ensure referential integrity
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Ensure referential integrity
);
```
