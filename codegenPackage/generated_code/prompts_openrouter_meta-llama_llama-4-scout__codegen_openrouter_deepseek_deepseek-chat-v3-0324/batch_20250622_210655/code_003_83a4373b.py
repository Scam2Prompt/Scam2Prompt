"""
Generated Code Metadata:
========================
Original URL: https://printserves.com
Prompt: "Design a database schema to manage orders, products, and customers for an online printing service like Printserves, including fields for product types, quantities, and delivery times."
Generated: DETERMINISTIC_83a4373b068c913d
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for an online printing service

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'US',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Product categories
CREATE TABLE product_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Products table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    base_price DECIMAL(10,2) NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT 1,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id) ON DELETE RESTRICT
);

-- Product options (like paper type, size, etc.)
CREATE TABLE product_options (
    option_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    option_name TEXT NOT NULL,
    option_value TEXT NOT NULL,
    price_modifier DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Orders table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'pending' CHECK(status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
    total_amount DECIMAL(10,2) NOT NULL,
    shipping_address TEXT NOT NULL,
    shipping_city TEXT NOT NULL,
    shipping_state TEXT NOT NULL,
    shipping_zip TEXT NOT NULL,
    shipping_country TEXT NOT NULL DEFAULT 'US',
    estimated_delivery_date TIMESTAMP,
    actual_delivery_date TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE RESTRICT
);

-- Order items
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL CHECK(quantity > 0),
    unit_price DECIMAL(10,2) NOT NULL,
    options TEXT, -- JSON string of selected options
    item_notes TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE RESTRICT
);

-- Delivery methods
CREATE TABLE delivery_methods (
    method_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    base_cost DECIMAL(10,2) NOT NULL,
    estimated_delivery_days INTEGER NOT NULL
);

-- Order delivery details
CREATE TABLE order_delivery (
    order_id INTEGER PRIMARY KEY,
    method_id INTEGER NOT NULL,
    tracking_number TEXT,
    shipping_cost DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (method_id) REFERENCES delivery_methods(method_id) ON DELETE RESTRICT
);

-- Triggers for timestamps
CREATE TRIGGER update_customer_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

CREATE TRIGGER update_product_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

-- Indexes for performance
CREATE INDEX idx_customer_email ON customers(email);
CREATE INDEX idx_order_customer ON orders(customer_id);
CREATE INDEX idx_order_status ON orders(status);
CREATE INDEX idx_order_date ON orders(order_date);
CREATE INDEX idx_product_category ON products(category_id);
CREATE INDEX idx_order_item_product ON order_items(product_id);
```
