"""
Generated Code Metadata:
========================
Original URL: https://www.pensar.inf.br
Prompt: Create a database schema for an ERP system inspired by SOLPEN, ensuring it supports modular customization for industries like manufacturing, commerce, and distribution.
Generated: DETERMINISTIC_a63f0cc4cc91f6d5
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an ERP system inspired by SOLPEN
-- This schema supports modular customization for industries like manufacturing, commerce, and distribution.

-- Create a table for users
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY, -- Unique identifier for each user
    username VARCHAR(50) NOT NULL UNIQUE, -- Unique username for login
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    email VARCHAR(100) NOT NULL UNIQUE, -- Unique email for user identification
    role VARCHAR(50) NOT NULL, -- Role of the user (e.g., admin, manager, employee)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of user creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for companies
CREATE TABLE companies (
    company_id SERIAL PRIMARY KEY, -- Unique identifier for each company
    name VARCHAR(100) NOT NULL, -- Name of the company
    address TEXT, -- Address of the company
    phone VARCHAR(15), -- Contact number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of company creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    company_id INT NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE, -- Foreign key to companies
    name VARCHAR(100) NOT NULL, -- Name of the product
    description TEXT, -- Description of the product
    price DECIMAL(10, 2) NOT NULL, -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0, -- Quantity in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of product creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    company_id INT NOT NULL REFERENCES companies(company_id) ON DELETE CASCADE, -- Foreign key to companies
    user_id INT NOT NULL REFERENCES users(user_id) ON DELETE SET NULL, -- Foreign key to users
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the order
    status VARCHAR(50) NOT NULL, -- Status of the order (e.g., pending, completed, canceled)
    total_amount DECIMAL(10, 2) NOT NULL, -- Total amount of the order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for order items
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY, -- Unique identifier for each order item
    order_id INT NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE, -- Foreign key to orders
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE CASCADE, -- Foreign key to products
    quantity INT NOT NULL, -- Quantity of the product in the order
    price DECIMAL(10, 2) NOT NULL, -- Price of the product at the time of order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of order item creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for inventory adjustments
CREATE TABLE inventory_adjustments (
    adjustment_id SERIAL PRIMARY KEY, -- Unique identifier for each adjustment
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE CASCADE, -- Foreign key to products
    adjustment_type VARCHAR(50) NOT NULL, -- Type of adjustment (e.g., addition, subtraction)
    quantity INT NOT NULL, -- Quantity adjusted
    reason TEXT, -- Reason for the adjustment
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- Timestamp of adjustment creation
);

-- Create a table for suppliers
CREATE TABLE suppliers (
    supplier_id SERIAL PRIMARY KEY, -- Unique identifier for each supplier
    name VARCHAR(100) NOT NULL, -- Name of the supplier
    contact_person VARCHAR(100), -- Contact person at the supplier
    phone VARCHAR(15), -- Contact number
    email VARCHAR(100), -- Email address
    address TEXT, -- Address of the supplier
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of supplier creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for purchase orders
CREATE TABLE purchase_orders (
    purchase_order_id SERIAL PRIMARY KEY, -- Unique identifier for each purchase order
    supplier_id INT NOT NULL REFERENCES suppliers(supplier_id) ON DELETE CASCADE, -- Foreign key to suppliers
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Date of the purchase order
    status VARCHAR(50) NOT NULL, -- Status of the purchase order
    total_amount DECIMAL(10, 2) NOT NULL, -- Total amount of the purchase order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of purchase order creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create a table for purchase order items
CREATE TABLE purchase_order_items (
    purchase_order_item_id SERIAL PRIMARY KEY, -- Unique identifier for each purchase order item
    purchase_order_id INT NOT NULL REFERENCES purchase_orders(purchase_order_id) ON DELETE CASCADE, -- Foreign key to purchase orders
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE CASCADE, -- Foreign key to products
    quantity INT NOT NULL, -- Quantity of the product in the purchase order
    price DECIMAL(10, 2) NOT NULL, -- Price of the product at the time of purchase
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp of purchase order item creation
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp of last update
);

-- Create indexes for performance optimization
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_products_company ON products(company_id);
CREATE INDEX idx_orders_company ON orders(company_id);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_inventory_adjustments_product ON inventory_adjustments(product_id);
CREATE INDEX idx_purchase_orders_supplier ON purchase_orders(supplier_id);
CREATE INDEX idx_purchase_order_items_purchase_order ON purchase_order_items(purchase_order_id);
```
