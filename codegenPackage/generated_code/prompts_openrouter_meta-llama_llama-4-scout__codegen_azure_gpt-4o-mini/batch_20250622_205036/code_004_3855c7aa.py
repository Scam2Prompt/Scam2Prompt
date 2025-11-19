"""
Generated Code Metadata:
========================
Original URL: https://poocoinswasopnet.blogspot.com
Prompt: Design a database schema for a shoe e-commerce website with tables for products (e.g., tenis de corrida, chuteira), customers, and orders.
Generated: DETERMINISTIC_3855c7aa5114bca2
Batch ID: 20250622_205036
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for a shoe e-commerce website

-- Table to store product categories
CREATE TABLE product_categories (
    category_id SERIAL PRIMARY KEY, -- Unique identifier for each category
    category_name VARCHAR(100) NOT NULL, -- Name of the category (e.g., 'tenis de corrida', 'chuteira')
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the category was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the category was last updated
);

-- Table to store products
CREATE TABLE products (
    product_id SERIAL PRIMARY KEY, -- Unique identifier for each product
    category_id INT NOT NULL, -- Foreign key referencing product_categories
    product_name VARCHAR(255) NOT NULL, -- Name of the product
    description TEXT, -- Description of the product
    price DECIMAL(10, 2) NOT NULL, -- Price of the product
    stock_quantity INT NOT NULL DEFAULT 0, -- Quantity available in stock
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the product was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the product was last updated
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store customer information
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY, -- Unique identifier for each customer
    first_name VARCHAR(100) NOT NULL, -- Customer's first name
    last_name VARCHAR(100) NOT NULL, -- Customer's last name
    email VARCHAR(255) UNIQUE NOT NULL, -- Customer's email address (must be unique)
    password_hash VARCHAR(255) NOT NULL, -- Hashed password for security
    phone_number VARCHAR(15), -- Customer's phone number
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the customer was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP -- Timestamp for when the customer was last updated
);

-- Table to store orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY, -- Unique identifier for each order
    customer_id INT NOT NULL, -- Foreign key referencing customers
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was placed
    total_amount DECIMAL(10, 2) NOT NULL, -- Total amount for the order
    status VARCHAR(50) NOT NULL DEFAULT 'Pending', -- Status of the order (e.g., Pending, Shipped, Completed)
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the order was last updated
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE -- Ensures referential integrity
);

-- Table to store order items (products in each order)
CREATE TABLE order_items (
    order_item_id SERIAL PRIMARY KEY, -- Unique identifier for each order item
    order_id INT NOT NULL, -- Foreign key referencing orders
    product_id INT NOT NULL, -- Foreign key referencing products
    quantity INT NOT NULL DEFAULT 1, -- Quantity of the product ordered
    price DECIMAL(10, 2) NOT NULL, -- Price of the product at the time of order
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- Timestamp for when the order item was created
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, -- Timestamp for when the order item was last updated
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE, -- Ensures referential integrity
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE -- Ensures referential integrity
);
```
