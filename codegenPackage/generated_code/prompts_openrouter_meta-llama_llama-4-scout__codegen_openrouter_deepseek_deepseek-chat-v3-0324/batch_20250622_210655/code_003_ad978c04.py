"""
Generated Code Metadata:
========================
Original URL: https://thoinayadv.com
Prompt: "Design a database schema for managing orders and services for a company like Quảng cáo Thời Nay that offers custom signage and printing."
Generated: DETERMINISTIC_ad978c041f895966
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for Quang Cao Thoi Nay order management system

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Customers table
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT NOT NULL,
    address TEXT,
    tax_id TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (email LIKE '%@%.%' OR email IS NULL)
);

-- Services table
CREATE TABLE services (
    service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    base_price DECIMAL(10, 2) NOT NULL,
    unit TEXT NOT NULL, -- e.g., 'sqm', 'piece', 'hour'
    estimated_time INTEGER, -- in hours
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Materials table
CREATE TABLE materials (
    material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    unit_price DECIMAL(10, 2) NOT NULL,
    unit TEXT NOT NULL, -- e.g., 'sqm', 'roll', 'kg'
    stock_quantity DECIMAL(10, 2) DEFAULT 0,
    supplier TEXT,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Orders table
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    delivery_date TIMESTAMP,
    status TEXT NOT NULL DEFAULT 'pending', -- pending, in_progress, completed, cancelled
    total_amount DECIMAL(10, 2) NOT NULL DEFAULT 0,
    deposit_amount DECIMAL(10, 2) DEFAULT 0,
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CHECK (status IN ('pending', 'in_progress', 'completed', 'cancelled'))
);

-- Order items table (services)
CREATE TABLE order_services (
    order_service_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    service_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (service_id) REFERENCES services(service_id)
);

-- Order materials table (materials used)
CREATE TABLE order_materials (
    order_material_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    material_id INTEGER NOT NULL,
    quantity DECIMAL(10, 2) NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    notes TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (material_id) REFERENCES materials(material_id)
);

-- Payments table
CREATE TABLE payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    amount DECIMAL(10, 2) NOT NULL,
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    payment_method TEXT NOT NULL, -- cash, bank_transfer, credit_card
    reference TEXT,
    notes TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    CHECK (payment_method IN ('cash', 'bank_transfer', 'credit_card'))
);

-- Design files table
CREATE TABLE design_files (
    file_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    file_name TEXT NOT NULL,
    file_path TEXT NOT NULL,
    file_type TEXT NOT NULL,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    version INTEGER DEFAULT 1,
    notes TEXT,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE
);

-- Triggers for updating timestamps
CREATE TRIGGER update_customer_timestamp
AFTER UPDATE ON customers
FOR EACH ROW
BEGIN
    UPDATE customers SET updated_at = CURRENT_TIMESTAMP WHERE customer_id = OLD.customer_id;
END;

CREATE TRIGGER update_service_timestamp
AFTER UPDATE ON services
FOR EACH ROW
BEGIN
    UPDATE services SET updated_at = CURRENT_TIMESTAMP WHERE service_id = OLD.service_id;
END;

CREATE TRIGGER update_material_timestamp
AFTER UPDATE ON materials
FOR EACH ROW
BEGIN
    UPDATE materials SET updated_at = CURRENT_TIMESTAMP WHERE material_id = OLD.material_id;
END;

CREATE TRIGGER update_order_timestamp
AFTER UPDATE ON orders
FOR EACH ROW
BEGIN
    UPDATE orders SET updated_at = CURRENT_TIMESTAMP WHERE order_id = OLD.order_id;
END;

-- Trigger to update order total when items are added
CREATE TRIGGER update_order_total_after_service_insert
AFTER INSERT ON order_services
FOR EACH ROW
BEGIN
    UPDATE orders 
    SET total_amount = total_amount + (NEW.quantity * NEW.unit_price)
    WHERE order_id = NEW.order_id;
END;

CREATE TRIGGER update_order_total_after_material_insert
AFTER INSERT ON order_materials
FOR EACH ROW
BEGIN
    UPDATE orders 
    SET total_amount = total_amount + (NEW.quantity * NEW.unit_price)
    WHERE order_id = NEW.order_id;
END;

-- Indexes for performance
CREATE INDEX idx_orders_customer ON orders(customer_id);
CREATE INDEX idx_orders_status ON orders(status);
CREATE INDEX idx_order_services_order ON order_services(order_id);
CREATE INDEX idx_order_materials_order ON order_materials(order_id);
CREATE INDEX idx_payments_order ON payments(order_id);
CREATE INDEX idx_design_files_order ON design_files(order_id);
```
