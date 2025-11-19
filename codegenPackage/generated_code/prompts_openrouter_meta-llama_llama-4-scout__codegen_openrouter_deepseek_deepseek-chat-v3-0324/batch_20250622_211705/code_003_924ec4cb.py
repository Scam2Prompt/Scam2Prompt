"""
Generated Code Metadata:
========================
Original URL: https://promodinamic.com
Prompt: "Design a database schema for storing information about promotional products, printing methods, and customer orders for a company like Promodinamic."
Generated: DETERMINISTIC_924ec4cb061aebf3
Batch ID: 20250622_211705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Promodinamic promotional products management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Products table: stores information about promotional products
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    min_order_quantity INTEGER NOT NULL DEFAULT 1,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (base_price > 0),
    CHECK (min_order_quantity > 0)
);

-- Printing methods table: stores available printing techniques
CREATE TABLE printing_methods (
    method_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT,
    setup_cost DECIMAL(10, 2) NOT NULL DEFAULT 0,
    unit_cost DECIMAL(10, 2) NOT NULL DEFAULT 0,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (setup_cost >= 0),
    CHECK (unit_cost >= 0)
);

-- Customers table: stores customer information
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    contact_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT,
    tax_id TEXT,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%')
);

-- Product printing options: junction table for products and printing methods
CREATE TABLE product_printing_options (
    product_id INTEGER NOT NULL,
    method_id INTEGER NOT NULL,
    additional_cost DECIMAL(10, 2) NOT NULL DEFAULT 0,
    max_colors INTEGER NOT NULL DEFAULT 1,
    min_quantity INTEGER NOT NULL DEFAULT 1,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    PRIMARY KEY (product_id, method_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (method_id) REFERENCES printing_methods(method_id) ON DELETE CASCADE,
    CHECK (additional_cost >= 0),
    CHECK (max_colors > 0),
    CHECK (min_quantity > 0)
);

-- Orders table: stores order headers
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    required_date TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'pending' CHECK (status IN ('pending', 'confirmed', 'production', 'shipped', 'delivered', 'cancelled')),
    notes TEXT,
    total_amount DECIMAL(12, 2) NOT NULL DEFAULT 0,
    tax_amount DECIMAL(12, 2) NOT NULL DEFAULT 0,
    discount_amount DECIMAL(12, 2) NOT NULL DEFAULT 0,
    final_amount DECIMAL(12, 2) NOT NULL DEFAULT 0,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CHECK (total_amount >= 0),
    CHECK (tax_amount >= 0),
    CHECK (discount_amount >= 0),
    CHECK (final_amount >= 0)
);

-- Order items: stores individual items in an order
CREATE TABLE order_items (
    item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    method_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    printing_cost DECIMAL(10, 2) NOT NULL,
    setup_cost DECIMAL(10, 2) NOT NULL,
    item_notes TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    FOREIGN KEY (method_id) REFERENCES printing_methods(method_id),
    CHECK (quantity > 0),
    CHECK (unit_price > 0),
    CHECK (printing_cost >= 0),
    CHECK (setup_cost >= 0)
);

-- Product images: stores images associated with products
CREATE TABLE product_images (
    image_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    image_url TEXT NOT NULL,
    is_primary BOOLEAN NOT NULL DEFAULT FALSE,
    caption TEXT,
    display_order INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE
);

-- Product categories: for organizing products
CREATE TABLE categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    parent_id INTEGER,
    FOREIGN KEY (parent_id) REFERENCES categories(category_id) ON DELETE SET NULL
);

-- Product-category mapping
CREATE TABLE product_categories (
    product_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    PRIMARY KEY (product_id, category_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(category_id) ON DELETE CASCADE
);

-- Triggers for maintaining updated_at timestamps
CREATE TRIGGER update_product_timestamp
AFTER UPDATE ON products
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = NEW.product_id;
END;

CREATE TRIGGER update_printing_method_timestamp
AFTER UPDATE ON printing_methods
BEGIN
    UPDATE printing_methods SET updated_at = CURRENT_TIMESTAMP WHERE method_id = NEW.method_id;
END;

CREATE TRIGGER update_customer_timestamp
AFTER UPDATE ON customers
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = NEW.customer_id;
END;

-- Trigger to calculate order totals when items are added/updated
CREATE TRIGGER update_order_totals
AFTER INSERT OR UPDATE OR DELETE ON order_items
BEGIN
    UPDATE orders 
    SET total_amount = (
        SELECT SUM((unit_price + printing_cost) * quantity + setup_cost)
        FROM order_items
        WHERE order_id = NEW.order_id
    ),
    final_amount = total_amount + tax_amount - discount_amount
    WHERE order_id = NEW.order_id;
END;
```
