"""
Generated Code Metadata:
========================
Original URL: https://holambraalimentos.com.br
Prompt: "Design a database schema to store information about meat products, suppliers, and customers for a company like Holambra Alimentos."
Generated: DETERMINISTIC_d0586c4a07259832
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Holambra Alimentos meat products management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Create suppliers table
CREATE TABLE suppliers (
    supplier_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    contact_person TEXT,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'Brazil',
    registration_number TEXT UNIQUE NOT NULL,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%'),
    CHECK (LENGTH(phone) >= 10)
);

-- Create product categories table
CREATE TABLE product_categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    description TEXT
);

-- Create meat products table
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    category_id INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    unit_weight DECIMAL(10, 3) NOT NULL, -- in kilograms
    supplier_id INTEGER NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    min_stock_level INTEGER NOT NULL DEFAULT 10,
    active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES product_categories(category_id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    CHECK (unit_price > 0),
    CHECK (unit_weight > 0),
    CHECK (stock_quantity >= 0),
    CHECK (min_stock_level >= 0)
);

-- Create customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'Brazil',
    tax_id TEXT UNIQUE NOT NULL, -- CPF/CNPJ
    customer_type TEXT NOT NULL CHECK (customer_type IN ('individual', 'business')),
    active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%'),
    CHECK (LENGTH(phone) >= 10)
);

-- Create orders table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status TEXT NOT NULL CHECK (status IN ('pending', 'processing', 'shipped', 'delivered', 'cancelled')),
    total_amount DECIMAL(12, 2) NOT NULL,
    payment_method TEXT NOT NULL CHECK (payment_method IN ('credit_card', 'debit_card', 'bank_transfer', 'cash', 'pix')),
    shipping_address TEXT NOT NULL,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CHECK (total_amount > 0)
);

-- Create order items table
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(12, 2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    CHECK (quantity > 0),
    CHECK (unit_price > 0),
    CHECK (subtotal > 0)
);

-- Create inventory movements table
CREATE TABLE inventory_movements (
    movement_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    movement_type TEXT NOT NULL CHECK (movement_type IN ('purchase', 'sale', 'adjustment', 'loss')),
    quantity INTEGER NOT NULL,
    movement_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    reference_id INTEGER, -- Can reference order_id or purchase_id
    notes TEXT,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    CHECK (quantity != 0)
);

-- Create purchase orders table
CREATE TABLE purchase_orders (
    purchase_id INTEGER PRIMARY KEY AUTOINCREMENT,
    supplier_id INTEGER NOT NULL,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    expected_delivery_date TIMESTAMP,
    status TEXT NOT NULL CHECK (status IN ('pending', 'approved', 'received', 'cancelled')),
    total_amount DECIMAL(12, 2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (supplier_id) REFERENCES suppliers(supplier_id),
    CHECK (total_amount > 0)
);

-- Create purchase order items table
CREATE TABLE purchase_order_items (
    purchase_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    purchase_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    subtotal DECIMAL(12, 2) NOT NULL,
    FOREIGN KEY (purchase_id) REFERENCES purchase_orders(purchase_id) ON DELETE CASCADE,
    FOREIGN KEY (product_id) REFERENCES products(product_id),
    CHECK (quantity > 0),
    CHECK (unit_price > 0),
    CHECK (subtotal > 0)
);

-- Create indexes for performance
CREATE INDEX idx_products_supplier ON products(supplier_id);
CREATE INDEX idx_products_category ON products(category_id);
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_order_items_order ON order_items(order_id);
CREATE INDEX idx_order_items_product ON order_items(product_id);
CREATE INDEX idx_inventory_product ON inventory_movements(product_id);
CREATE INDEX idx_purchase_orders_supplier ON purchase_orders(supplier_id);
CREATE INDEX idx_purchase_items_purchase ON purchase_order_items(purchase_id);
CREATE INDEX idx_purchase_items_product ON purchase_order_items(product_id);

-- Create triggers for automatic updates
CREATE TRIGGER update_supplier_timestamp
AFTER UPDATE ON suppliers
FOR EACH ROW
BEGIN
    UPDATE suppliers SET updated_at = CURRENT_TIMESTAMP WHERE supplier_id = OLD.supplier_id;
END;

CREATE TRIGGER update_product_timestamp
AFTER UPDATE ON products
FOR EACH ROW
BEGIN
    UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE product_id = OLD.product_id;
END;

CREATE TRIGGER update_customer_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

-- Trigger to update inventory when order items are inserted
CREATE TRIGGER update_inventory_on_order
AFTER INSERT ON order_items
FOR EACH ROW
BEGIN
    -- Decrease product stock
    UPDATE products SET stock_quantity = stock_quantity - NEW.quantity 
    WHERE product_id = NEW.product_id;
    
    -- Record inventory movement
    INSERT INTO inventory_movements (product_id, movement_type, quantity, reference_id)
    VALUES (NEW.product_id, 'sale', -NEW.quantity, NEW.order_id);
END;

-- Trigger to update inventory when purchase items are inserted
CREATE TRIGGER update_inventory_on_purchase
AFTER INSERT ON purchase_order_items
FOR EACH ROW
BEGIN
    -- Increase product stock
    UPDATE products SET stock_quantity = stock_quantity + NEW.quantity 
    WHERE product_id = NEW.product_id;
    
    -- Record inventory movement
    INSERT INTO inventory_movements (product_id, movement_type, quantity, reference_id)
    VALUES (NEW.product_id, 'purchase', NEW.quantity, NEW.purchase_id);
END;
```
