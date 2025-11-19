"""
Generated Code Metadata:
========================
Original URL: https://ramjiacro.com
Prompt: Create a database schema for managing inventory and production data for a textile company specializing in 100% acrylic yarns, including tables for yarn types, machinery details, and customer orders.
Generated: DETERMINISTIC_cef3bce514e7db0c
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```sql
-- Database schema for textile company managing acrylic yarn inventory and production

-- Enable foreign key constraints
PRAGMA foreign_keys = ON;

-- Table for yarn types
CREATE TABLE yarn_types (
    yarn_id INTEGER PRIMARY KEY AUTOINCREMENT,
    yarn_name TEXT NOT NULL,
    yarn_weight TEXT NOT NULL,  -- e.g., DK, Worsted, Bulky
    yarn_color TEXT NOT NULL,
    dye_lot TEXT,
    fiber_content TEXT DEFAULT '100% Acrylic',
    skein_weight_grams INTEGER NOT NULL,
    skein_length_meters INTEGER NOT NULL,
    unit_cost DECIMAL(10, 2) NOT NULL,
    stock_quantity INTEGER NOT NULL DEFAULT 0,
    min_stock_level INTEGER NOT NULL DEFAULT 10,
    date_added DATE DEFAULT CURRENT_DATE,
    last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    CHECK (skein_weight_grams > 0),
    CHECK (skein_length_meters > 0),
    CHECK (unit_cost >= 0),
    CHECK (stock_quantity >= 0),
    CHECK (min_stock_level >= 0)
);

-- Table for machinery
CREATE TABLE machinery (
    machine_id INTEGER PRIMARY KEY AUTOINCREMENT,
    machine_name TEXT NOT NULL,
    machine_type TEXT NOT NULL,  -- e.g., Spinning, Winding, Dyeing
    manufacturer TEXT NOT NULL,
    model_number TEXT,
    serial_number TEXT UNIQUE,
    purchase_date DATE,
    last_maintenance_date DATE,
    next_maintenance_date DATE,
    status TEXT NOT NULL DEFAULT 'Active',  -- Active, Maintenance, Retired
    production_capacity_per_hour DECIMAL(10, 2),
    notes TEXT,
    CHECK (production_capacity_per_hour >= 0)
);

-- Table for production batches
CREATE TABLE production_batches (
    batch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    yarn_id INTEGER NOT NULL,
    machine_id INTEGER NOT NULL,
    batch_size INTEGER NOT NULL,  -- in skeins
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP,
    operator_name TEXT,
    quality_check_passed BOOLEAN DEFAULT FALSE,
    notes TEXT,
    FOREIGN KEY (yarn_id) REFERENCES yarn_types(yarn_id),
    FOREIGN KEY (machine_id) REFERENCES machinery(machine_id),
    CHECK (batch_size > 0),
    CHECK (end_date IS NULL OR end_date >= start_date)
);

-- Table for customers
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_name TEXT NOT NULL,
    contact_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    address_line1 TEXT NOT NULL,
    address_line2 TEXT,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    postal_code TEXT NOT NULL,
    country TEXT NOT NULL DEFAULT 'USA',
    tax_id TEXT,
    date_added DATE DEFAULT CURRENT_DATE,
    notes TEXT,
    UNIQUE (email)
);

-- Table for orders
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    required_date DATE NOT NULL,
    shipped_date DATE,
    status TEXT NOT NULL DEFAULT 'Pending',  -- Pending, Processing, Shipped, Cancelled
    payment_method TEXT NOT NULL,
    payment_status TEXT NOT NULL DEFAULT 'Unpaid',  -- Unpaid, Partial, Paid
    shipping_cost DECIMAL(10, 2) DEFAULT 0,
    tax_amount DECIMAL(10, 2) DEFAULT 0,
    notes TEXT,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CHECK (shipped_date IS NULL OR shipped_date >= order_date),
    CHECK (required_date >= order_date),
    CHECK (shipping_cost >= 0),
    CHECK (tax_amount >= 0)
);

-- Table for order details (line items)
CREATE TABLE order_details (
    order_detail_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    yarn_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    unit_price DECIMAL(10, 2) NOT NULL,
    discount DECIMAL(5, 2) DEFAULT 0,
    FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE,
    FOREIGN KEY (yarn_id) REFERENCES yarn_types(yarn_id),
    CHECK (quantity > 0),
    CHECK (unit_price >= 0),
    CHECK (discount BETWEEN 0 AND 100)
);

-- Table for inventory adjustments
CREATE TABLE inventory_adjustments (
    adjustment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    yarn_id INTEGER NOT NULL,
    adjustment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    quantity_change INTEGER NOT NULL,  -- Positive for additions, negative for deductions
    adjustment_type TEXT NOT NULL,  -- e.g., 'Purchase', 'Sale', 'Damage', 'Adjustment'
    reference_id INTEGER,  -- Could link to order_id or production_batch_id
    reference_type TEXT,   -- e.g., 'Order', 'Production'
    notes TEXT,
    FOREIGN KEY (yarn_id) REFERENCES yarn_types(yarn_id)
);

-- Table for production defects
CREATE TABLE production_defects (
    defect_id INTEGER PRIMARY KEY AUTOINCREMENT,
    batch_id INTEGER NOT NULL,
    defect_type TEXT NOT NULL,  -- e.g., 'Color Mismatch', 'Thickness Variation'
    defect_quantity INTEGER NOT NULL,
    date_reported TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved BOOLEAN DEFAULT FALSE,
    resolution_notes TEXT,
    FOREIGN KEY (batch_id) REFERENCES production_batches(batch_id),
    CHECK (defect_quantity > 0)
);

-- View for current inventory levels
CREATE VIEW current_inventory AS
SELECT 
    y.yarn_id,
    y.yarn_name,
    y.yarn_weight,
    y.yarn_color,
    y.skein_weight_grams,
    y.skein_length_meters,
    y.stock_quantity,
    y.min_stock_level,
    CASE 
        WHEN y.stock_quantity <= y.min_stock_level THEN 'Low Stock'
        WHEN y.stock_quantity = 0 THEN 'Out of Stock'
        ELSE 'In Stock'
    END AS stock_status
FROM yarn_types y;

-- View for order summary
CREATE VIEW order_summary AS
SELECT 
    o.order_id,
    c.company_name,
    o.order_date,
    o.required_date,
    o.status,
    COUNT(od.order_detail_id) AS item_count,
    SUM(od.quantity) AS total_quantity,
    SUM(od.quantity * od.unit_price * (1 - od.discount/100)) AS subtotal,
    o.shipping_cost,
    o.tax_amount,
    (SUM(od.quantity * od.unit_price * (1 - od.discount/100)) + o.shipping_cost + o.tax_amount) AS total_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN order_details od ON o.order_id = od.order_id
GROUP BY o.order_id, c.company_name, o.order_date, o.required_date, o.status, o.shipping_cost, o.tax_amount;
```
